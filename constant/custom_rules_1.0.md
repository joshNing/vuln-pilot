
# 🔒 Security Vulnerability Handling Rules

## 1. 📊 General Post-Processing by Severity

| Severity Level | Action |
|----------------|--------|
| **High** | File a **bug ticket** (severity: **High**).<br>Send an **email notification** to the responsible team’s **engineering manager** and **security contact**.<br>Mark the issue as **"Security Blocker"** if it's exploitable in production. |
| **Medium** | File a **bug ticket** with **priority: Medium**. Assign to the appropriate team. Notify the security team via internal tracking (no email escalation). |
| **Low** | File a **bug ticket** with **priority: Low**. Add the issue to the **backlog** of the assigned team. No email required. |
| **Informational** | Document the issue in internal wiki or ticketing system as **“informational only”**. No immediate remediation needed unless linked to abuse scenarios. |

---

## 2. 🛠️ Ticket Assignment Rules by Vulnerability Type

| Vulnerability | Action | Assignee Team | Team Email |
|---------------|--------|---------------|------------|
| **SQL Injection** | File bug immediately (High severity). Include proof-of-concept and affected URLs. | Backend / DB Security Team | dbsec@company.com |
| **XML External Entity Injection (XXE)** | File bug (High severity). Verify parser libraries used. | API Platform / Infra Team | infra-sec@company.com |
| **Cross-site Scripting (Reflected)** | File bug (Medium or High depending on impact). Provide sanitization recommendations. | Frontend Security Team | frontend-sec@company.com |
| **Client-side Template Injection** | File bug (High severity). Include details on template engine. | Frontend App Team | frontend-app@company.com |
| **External Service Interaction (HTTP / DNS)** | File bug (Medium). Investigate unintended data leaks. | Network / Logging Team | net-ops@company.com |
| **Vulnerable JavaScript Dependency** | File bug (Medium). Add action to upgrade or patch the vulnerable package. | AppSec / Dependency Management | appsec@company.com |
| **Open Redirection (DOM-based)** | File bug (Medium). Link to browser-specific behaviors. | Frontend Security Team | frontend-sec@company.com |
| **Password Field with Autocomplete Enabled** | File bug (Low). Update frontend form attributes. | UX / Frontend Team | frontend@company.com |
| **Strict Transport Security Not Enforced** | File bug (Low). Apply `Strict-Transport-Security` headers. | Infra / DevOps Team | devops@company.com |
| **Client-side Prototype Pollution** | File bug (High). Identify affected libraries and versions. | Frontend Security Team | frontend-sec@company.com |
| **Input Returned in Response (Reflected)** | File bug (Low or Medium depending on context). | Frontend Dev Team | frontend@company.com |
| **Request URL Override** | File bug (Medium). Review for unsafe `Host` header usage. | API Gateway Team | api-platform@company.com |
| **TLS Cookie Without Secure Flag Set** | File bug (Low). Set `Secure` flag on all session cookies. | Web Platform Team | websec@company.com |
| **Cookie Without HttpOnly Flag Set** | File bug (Low). Add `HttpOnly` attribute to session cookies. | Web Platform Team | websec@company.com |
| **Frameable Response (Clickjacking)** | File bug (Medium). Recommend `X-Frame-Options` or `Content-Security-Policy`. | Frontend or Web Infra Team | websec@company.com |
| **Cacheable HTTPS Response** | File bug (Low). Adjust `Cache-Control` headers. | Web Infrastructure Team | infra-sec@company.com |

---

## 3. 📬 Email Template for High-Severity Alerts

```
Subject: 🔴 [High Severity] Security Vulnerability - [Vulnerability Type] Detected

To: [Team Email], [Engineering Manager Name]  
Cc: security@company.com

A high-severity security issue has been identified during a recent security scan.

Vulnerability Type: SQL Injection  
Affected URL(s): https://ginandjuice.shop/catalog/filter  
Severity: High  
Recommended Action: Immediate triage and patching.

Please acknowledge receipt and provide a remediation ETA within 24 hours.


— Security Engineering Team
```
