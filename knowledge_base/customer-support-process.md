---
document_id: customer-support-process
title: Customer Support Intake and Routing Process
department: Customer Support
document_type: process
version: "1.4"
effective_date: 2026-07-10
owner: Head of Customer Support
status: active
---

# Customer Support Intake and Routing Process

## Scope
This process covers new customer support requests submitted through the primary support channels. It begins when a new request enters the intake queue and ends when the request is assigned to an appropriate operational queue or escalated for manual review.

Customer Support owns the business process. IT/Operations supports the technical systems used for intake and routing.

## Current Process
Incoming requests are first reviewed by a support agent. The agent reads the message, identifies the general topic, checks whether it appears urgent, and assigns the ticket to a queue.

Typical queues include Account Access, Billing Questions, Product Configuration, Technical Incident, and General Support. Some requests are straightforward, while others contain incomplete information or overlap multiple topics. Agents may add internal notes when the reason for a routing decision is not obvious.

## Current Pain Points
Manual triage creates repetitive work and adds delay before a specialist starts handling the case. Routing errors are a recurring operational problem. A ticket sent to the wrong queue may be reassigned multiple times before reaching the correct team, increasing response time.

The largest amount of avoidable manual effort comes from common requests that are easy for experienced agents to categorize but still require someone to read and route them. Requests involving account lockout, billing disputes, or possible service outages require more careful handling because they may be urgent or customer-sensitive.

## Automation Opportunity
Customer Support has identified initial routing as a candidate for AI-assisted automation. A suitable pilot may classify incoming request text and recommend a queue. High-confidence, clearly categorized requests may be routed automatically during the pilot if AI Risk and Review Policy requirements are met.

Low-confidence, ambiguous, or multi-topic requests should remain in a manual review queue. The automation should not generate a customer-facing resolution during the initial routing pilot. Its scope is limited to classification and routing support.

## Escalation
Requests that indicate a possible widespread outage should be escalated to the Technical Incident process. Billing disputes above the normal support threshold should be routed to the Billing team for manual review. Requests containing unclear identity, account ownership, or security-related information should not be automatically resolved.

## Quality Monitoring
During a pilot, Customer Support should track routing accuracy, the percentage of cases requiring manual review, and common reasons for correction. The team should review examples of incorrect routing rather than relying only on an overall accuracy number.

If automated routing repeatedly misclassifies a specific request type, that category should be temporarily returned to manual handling while the problem is investigated.

## Ownership
The Head of Customer Support approves changes to queue definitions and triage rules. IT/Operations may maintain the workflow implementation, but should not change routing rules without agreement from Customer Support.
