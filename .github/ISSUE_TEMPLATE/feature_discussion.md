---
name: Feature discussion
about: Discuss a possible feature before implementation
title: "Feature discussion: "
labels: enhancement
assignees: ""
---

## Problem or use case

What problem would this solve?

## Proposed direction

Describe the smallest useful version of the idea.

## KORA relevance

- How does this preserve deterministic-first execution?
- Can it reduce unnecessary inference, improve validation, clarify telemetry, or improve contributor onboarding?
- Does it affect benchmark evidence or public claims?

## Public surface impact

Would this add or change CLI commands, examples, task schema, telemetry output, or documented behavior?

Public surface expansion should be discussed before implementation.

## Deterministic-first check

Can any part of this be handled deterministically before model inference?

## Verification idea

How could this be tested or smoke-checked?

## Notes

Add links or prior discussion if relevant.

Do not include sensitive vulnerability details here. Use [SECURITY.md](../../SECURITY.md) for security reports.
