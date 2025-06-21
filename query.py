from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.agent import ReActAgent

# File Jira ticket
def file_jira_ticket(
    jira_board: str,
    team_name: str,
    vulnerability_type: str,
    affected_url: str,
    vulnerability_level: str
):

    # sample usage: 
    # file_jira_ticket(
    #     jira_board="SECURITY",
    #     team_name="Backend Services",
    #     vulnerability_type="Cross-Site Scripting (XSS)",
    #     affected_url="https://example.com/search?q=xss",
    #     vulnerability_level="High"
    # )

    summary = f"[{vulnerability_level} Severity] {vulnerability_type} Detected in {team_name}"

    description = f"""*Team:* {team_name}  
*Vulnerability Type:* {vulnerability_type}  
*Affected URL(s):* {affected_url}  
*Severity:* {vulnerability_level}

A {vulnerability_level.lower()}-severity security vulnerability was identified during a recent scan.

*Recommended Action:*  
Immediate triage, investigation, and remediation are required.

Please provide an estimated time for remediation (ETA) within 24 hours.

— Security Engineering Team"""

    print(
        f"--- Jira Ticket ---\nBoard: {jira_board}\nSummary: {summary}\n\nDescription:\n{description}")


# Send an email
def send_security_alert( 
    email: str,
    vulnerability_type: str,
    team_name: str,
    affected_url: str
):
    
    # Sample usage:
    # send_security_alert(
    #     email="team@example.com",
    #     vulnerability_type="SQL Injection",
    #     team_name="Backend Services",
    #     affected_url="https://example.com/api/v1/users"
    # )

    subject = f"🔴 [High Severity] Security Vulnerability - {vulnerability_type} Detected"
    body = f"""Subject: {subject}

To: {email},  

A high-severity security issue has been identified during a recent security scan.

Vulnerability Type: {vulnerability_type}
Affected URL(s): {affected_url}
Severity: High  
Recommended Action: Immediate triage and patching.

Please acknowledge receipt and provide a remediation ETA within 24 hours.

— Security Engineering Team
"""
    print(body)

def query(custom_index, scan_index, llm):
    custom_engine = custom_index.as_query_engine(similarity_top_k=3, llm=llm)
    scan_engine = scan_index.as_query_engine(similarity_top_k=3, llm=llm)

    # Wrap your custom functions as tools with new names
    jira_tool = FunctionTool.from_defaults(
        fn=file_jira_ticket,
        name="vulnerability_file_bug",
        description="File a bug for a security vulnerability. Provide jira_board, team_name, vulnerability_type, affected_url, and vulnerability_level."
    )
    email_tool = FunctionTool.from_defaults(
        fn=send_security_alert,
        name="vulnerability_email",
        description="Send a security alert email. Provide email, vulnerability_type, team_name, and affected_url."
    )

    query_engine_tools = [
        QueryEngineTool(
            query_engine=custom_engine,
            metadata=ToolMetadata(
                name="custom_rules",
                description=(
                    "Provides information about post process of vulnerability scan report. "
                    "Use a detailed plain text question as input to the tool."
                ),
            ),
        ),
        QueryEngineTool(
            query_engine=scan_engine,
            metadata=ToolMetadata(
                name="scanning_results",
                description=(
                    "Provides information about qualys vulnerability reports. "
                    "Use a detailed plain text question as input to the tool."
                ),
            ),
        ),
        jira_tool,
        email_tool,
    ]

    agent = ReActAgent.from_tools(
        query_engine_tools,
        llm=llm,
        verbose=True,
        max_turns=20,
    )

    # Updated context and instructions
    context = (
        "Your role is to process vulnerability scan results and reference custom rules to take actions. "
        "You are not in charge of addressing the vulnerabilities. You have 3 available actions:\n\n"
        "1. not address the case\n"
        "2. email the responsible teams\n"
        "3. file a bug.\n\n"
        "These actions are not exclusive, follow only the custom rules and be explicit which action you took. "
        "You have 2 tools at disposal to act, vulnerability_email and vulnerability_file_bug. "
        "Read first results, what's the next step and take action in plain text. "
        "**After you have taken the appropriate action(s), STOP and do not continue.**"
    )

    response = agent.chat(context)
    print(str(response))
    
def __main__():
    query(custom_index=None, scan_index=None, llm=None)