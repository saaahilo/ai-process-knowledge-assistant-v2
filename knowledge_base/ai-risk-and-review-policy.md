---
document_id: ai-risk-review-policy
title: AI Risk and Review Policy
department: Company-wide
document_type: policy
version: "2.0"
effective_date: 2026-08-01
owner: AI Governance Lead
status: active
---

# AI Risk and Review Policy

## Purpose
This policy defines minimum controls for workflows at Northstar Systems that use generative AI, classification models, extraction models, or other probabilistic AI components to support operational decisions.

The objective is not to prevent AI use. It is to ensure that controls are proportional to the possible impact of an incorrect output.

## Risk Classification
### Low Risk
Low-risk use cases create limited operational impact and are easy to reverse. Examples include drafting internal summaries, suggesting labels for employee review, formatting non-sensitive internal reports, or generating a proposed description for a work item. Low-risk workflows may operate without mandatory case-by-case approval when the output is not used automatically for a consequential decision.

### Medium Risk
Medium-risk use cases can affect operational routing, customer experience, workload prioritization, or internal decisions, but errors can usually be detected and corrected without major harm. Examples include automatically routing customer requests, prioritizing service tickets, suggesting account follow-up actions, or extracting fields used to start an internal process.

Medium-risk workflows should normally include human review for ambiguous or low-confidence cases. Customer-facing automations should initially be piloted with human oversight.

### High Risk
High-risk use cases may create significant financial, legal, employment, security, privacy, or contractual consequences. Examples include automatically approving or rejecting payments, making employment decisions, changing contractual terms, determining customer eligibility, or taking irreversible action based solely on AI output.

High-risk actions must not be executed solely on an AI recommendation. A qualified employee must review the relevant evidence and make the final decision.

## Confidence and Ambiguity
Where the AI system provides a meaningful confidence measure, teams may use it as one signal for escalation. Confidence thresholds must be validated for the specific task before they are used operationally. If no reliable confidence score exists, workflows should use other indicators such as missing fields, conflicting extracted information, unusual input patterns, or explicit model uncertainty.

A model's own statement that it is "confident" is not sufficient evidence of reliability.

## Human Review Requirements
Human review is normally required when the workflow directly affects a customer; has meaningful financial impact; concerns employee or applicant decisions; uses sensitive data; is difficult to reverse; involves ambiguous policy interpretation; conflicts with deterministic business rules; or lacks enough evidence to justify an automated action.

The reviewer must have enough context to understand the proposed action and why the workflow produced it.

## Grounding and Source Use
When an AI workflow relies on internal knowledge, it should provide relevant source material where practical. Retrieved documents are supporting evidence, not proof that a generated answer is correct. Retrieval relevance scores must not be interpreted as factual confidence or probability of correctness.

If available internal knowledge does not support a specific recommendation, the workflow should keep the recommendation general or escalate rather than invent company policy.

## Sensitive Data and Monitoring
Sensitive customer, financial, employee, or contractual data must only be sent to AI services approved for that category. During prototyping, external AI services should use synthetic or approved non-sensitive test data unless an explicit exception exists.

Production workflows should be reviewed periodically for error patterns, inappropriate actions, changing data characteristics, and recurring human overrides. If reviewers frequently reject or correct a recommendation, the process owner should investigate retrieval quality, prompt instructions, model behavior, or changes in the underlying business process.

## Escalation and Suspension
An AI-supported workflow should be paused or restricted when it produces repeated harmful errors, violates a deterministic control, relies on outdated policy information, or behaves materially differently from what was validated during testing.
