---
document_id: approved-tools-environments
title: Approved Tools and Environments
department: IT/Operations
document_type: reference
version: "1.5"
effective_date: 2026-05-20
owner: Director of IT Operations
status: active
---

# Approved Tools and Environments

## Purpose
This document describes approved tools and environment expectations for internal automation prototypes and operational workflows at Northstar Systems. Approval of a tool does not mean it is suitable for every data type or production use case.

## Workflow Orchestration
n8n is approved for internal automation prototypes and selected operational workflows maintained by IT/Operations or another approved technical owner. Production workflows should use managed credentials rather than hard-coded secrets. Credentials must not be placed directly in Code nodes, prompts, repository files, or workflow descriptions.

Higher-criticality workflows should document ownership, failure behavior, and major dependencies before production release.

## Work Tracking
Jira is the approved system for implementation tasks, change work, and tracked automation follow-up. Automated Jira issue creation must follow the Jira Governance Standard. Workflows should not invent new labels, statuses, or issue types dynamically.

## Knowledge Sources
Confluence is the preferred internal source for maintained process documentation, operational policies, runbooks, and team knowledge. During early prototypes, local Markdown or text files may be used to simulate the expected document structure. Prototype documents must be clearly identified as synthetic if they are not real company records.

A production knowledge-retrieval workflow should preserve source identifiers and update information where possible so retrieved content can be traced back to its origin.

## AI Services
OpenAI API access may be used for approved prototypes with synthetic or non-sensitive data. Use of external AI services with customer records, financial information, employee information, credentials, or confidential contractual content requires an approved data assessment.

Embedding models may be used for semantic retrieval of approved text sources. The same embedding model should be used for both document indexing and query embedding within one vector index.

## Environments
Teams should distinguish between development/testing and production. Development may use mock systems, synthetic documents, and test projects. Production workflows must use approved accounts, correct credentials, monitored integrations, and business-owner sign-off.

Testing should not create live customer communications, financial transactions, or irreversible updates unless the test is explicitly controlled.

## Data Storage
Automation logs should store operationally useful information without collecting more data than necessary. Vector stores used for internal knowledge retrieval must be appropriate for the sensitivity of indexed documents. A local or in-memory vector store may be used for learning and prototyping, but production knowledge bases should use persistent storage with suitable access control and backup practices.

## Unsupported Practices
The following are not approved: hard-coded API keys; plain-text production passwords; personal unmanaged accounts for production integrations; sending sensitive data to an unapproved AI endpoint; relying on an in-memory vector store for a production knowledge base; or bypassing required human approval because an AI output appears confident.
