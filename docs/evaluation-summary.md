# Evaluation Summary

## Purpose

The evaluation workflow checks whether the shared Request Assessment Core continues to produce expected retrieval and decision behavior after changes to prompts, retrieval, vector storage, or workflow structure.

The evaluation uses a small synthetic regression set rather than claiming production-level model accuracy.

## Test Set

The current baseline contains 6 synthetic automation-request cases covering:

- Customer Support
- Finance
- IT / Operations
- HR
- Sales
- Ambiguous internal process requests

Each case includes expected values for:

- relevant source document
- risk level
- whether human review is required

## Metrics

Two simple pass/fail checks are used:

**Retrieval pass**
- passes when the expected document appears among the retrieved source documents

**Decision pass**
- passes when both the predicted risk level and human-review decision match the expected values

## Initial Result

The first evaluation run passed 4 of 6 cases.

Two failure modes were identified:

1. A low-risk reporting case was incorrectly marked for human review because the model expanded the request with optional AI functionality found in retrieved examples.
2. An ambiguous process request received an incorrect risk classification because the mandatory AI risk policy was not guaranteed to be available through semantic retrieval.

## Changes Made

Two general architectural improvements were introduced:

- The prompt was clarified so the model evaluates only the automation actually requested and does not add optional capabilities from retrieved examples.
- Mandatory AI risk and human-review policy was separated from dynamic semantic retrieval and loaded deterministically for every assessment.

These changes were intentionally general rather than case-specific prompt patches.

## Current Regression Baseline

After the changes, all 6 synthetic cases passed both retrieval and decision checks.

The same 6-case baseline was rerun after:

- migrating from the prototype vector store to Qdrant
- separating knowledge-base indexing from runtime assessment
- extracting the Request Assessment Core into a reusable sub-workflow
- separating operational intake from evaluation

The regression baseline remained 6/6.

## Limitations

This evaluation set is intentionally small and synthetic.

A 6/6 result means the current workflow preserves expected behavior for the current regression cases. It should not be interpreted as production-level reliability or general model accuracy.

A larger production evaluation would require broader datasets, edge cases, retrieval metrics, model-quality metrics, and monitoring over time.