# 🔒 Vuln-Pilot: AI-Powered Vulnerability Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-purple.svg)](https://openai.com/)

> **VulnPilot** - An intelligent vulnerability management system that automatically processes security scan results and orchestrates remediation workflows using AI agents.

## 🚀 Overview

Vuln-Pilot is an AI-powered vulnerability management system that automatically processes Qualys vulnerability scan reports and takes appropriate actions based on configurable business rules. The system uses OpenAI's GPT-4 and LlamaIndex to intelligently analyze vulnerabilities, determine severity levels, and automatically create Jira tickets and send email notifications to responsible teams.

### ✨ Key Features

- 🤖 **AI-Powered Analysis**: Uses GPT-4 to intelligently process vulnerability scan results
- 📋 **Automated Ticket Creation**: Automatically creates Jira tickets with proper severity and assignment
- 📧 **Smart Email Notifications**: Sends targeted email alerts to responsible teams
- ⚙️ **Configurable Rules Engine**: Customizable business rules for different vulnerability types
- 🔍 **RAG-Powered Queries**: Uses Retrieval-Augmented Generation for context-aware decision making
- 📊 **Severity-Based Workflows**: Different actions based on vulnerability severity levels
- 🎯 **Team Assignment Logic**: Intelligent routing to appropriate teams based on vulnerability type

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Qualys Scan   │───▶│  Vuln-Pilot AI   │───▶│  Jira Tickets   │
│     Results     │    │     Agent        │    │   & Emails      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  Custom Rules    │
                       │    Engine        │
                       └──────────────────┘
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Jira access (for ticket creation)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vuln-pilot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp sample.env .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```env
   OPENAI_API_KEY="your-openai-api-key-here"
   ```

4. **Run the application**
   ```bash
   python index_main.py
   ```

## 📖 Usage

### Basic Usage

The system automatically processes vulnerability scan results and takes actions based on configured rules:

```bash
python index_main.py
```

### Sample Output

```
Parsing nodes: 100%|█████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 709.70it/s]
Generating embeddings: 100%|██████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.09it/s]

--- Jira Ticket ---
Board: Security
Summary: [High Severity] OpenSSH 'Channel' double-free privilege escalation Detected in Web Team

Description:
*Team:* Web Team  
*Vulnerability Type:* OpenSSH 'Channel' double-free privilege escalation  
*Affected URL(s):* 10.0.1.1  
*Severity:* High

A high-severity security vulnerability was identified during a recent scan.

*Recommended Action:*  
Immediate triage, investigation, and remediation are required.

Please provide an estimated time for remediation (ETA) within 24 hours.

— Security Engineering Team

Subject: 🔴 [High Severity] Security Vulnerability - OpenSSH 'Channel' double-free privilege escalation Detected

To: webteam@example.com,  

A high-severity security issue has been identified during a recent security scan.

Vulnerability Type: OpenSSH 'Channel' double-free privilege escalation
Affected URL(s): 10.0.1.1
Severity: High  
Recommended Action: Immediate triage and patching.

Please acknowledge receipt and provide a remediation ETA within 24 hours.

— Security Engineering Team
```

## ⚙️ Configuration

### Custom Rules

The system uses configurable business rules defined in `constant/custom_rules_1.0.md`. These rules determine:

- **Severity-based actions**: Different workflows for severity levels 1-5
- **Team assignments**: Which team handles specific vulnerability types
- **Email templates**: Standardized notification formats
- **Ticket priorities**: Automatic priority assignment based on severity

### Vulnerability Types Supported

| Vulnerability Type | Assigned Team | Action |
|-------------------|---------------|---------|
| SQL Injection | Backend/DB Security | High priority ticket + email |
| XSS (Reflected) | Frontend Security | Medium/High priority ticket |
| XXE | API Platform/Infra | High priority ticket |
| Client-side Template Injection | Frontend App | High priority ticket |
| Vulnerable Dependencies | AppSec | Medium priority ticket |
| And many more... | | |

### Severity Levels

| Level | Action |
|-------|--------|
| **4-5** | File High priority ticket + Send email notification |
| **3** | File Medium priority ticket |
| **2** | File Low priority ticket |
| **1** | No action required |

## 🔧 Customization

### Adding New Vulnerability Types

1. Edit `constant/custom_rules_1.0.md`
2. Add new vulnerability type to the assignment table
3. Specify team assignment and action requirements

### Modifying Email Templates

Update the email template section in `constant/custom_rules_1.0.md` to customize notification formats.

### Extending Actions

Modify `query.py` to add new action types beyond Jira tickets and emails.

## 📁 Project Structure

```
vuln-pilot/
├── index_main.py              # Main application entry point
├── query.py                   # AI agent and tool definitions
├── constant/
│   ├── custom_rules_1.0.md    # Business rules configuration
│   ├── qualys_sample_report.json  # Sample vulnerability data
│   ├── custom_rules/          # Vector store for rules
│   └── scan_results/          # Vector store for scan data
├── openai_rag_agent_w_evals.ipynb  # Development notebook
├── sample.env                 # Environment variables template
└── README.md                  # This file
```

## 🧪 Development

### Jupyter Notebook

For development and experimentation, use the included Jupyter notebook:

```bash
jupyter notebook openai_rag_agent_w_evals.ipynb
```

### Adding New Tools

To add new action tools:

1. Define the function in `query.py`
2. Wrap it as a `FunctionTool`
3. Add it to the `query_engine_tools` list
4. Update the agent context if needed

## 🔒 Security Considerations

- Store API keys securely in environment variables
- Review and validate all automated actions before production use
- Implement proper access controls for Jira and email systems
- Regularly audit custom rules for accuracy and completeness

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built during a hackathon as a proof-of-concept
- Uses OpenAI GPT-4 for intelligent decision making
- Powered by LlamaIndex for RAG capabilities
- Integrates with Jira for ticket management

---

**Note**: This is a demo project created during a hackathon. For production use, additional security reviews, testing, and hardening are recommended. 