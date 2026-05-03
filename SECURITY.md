# Security Policy

KORA is an early alpha project. Security reports are welcome, but the project does not yet have a formal security response SLA.

## Reporting a security concern

Please do not open a public issue for sensitive security reports.

For now, contact the maintainers directly through the repository owner.

Include enough detail for maintainers to understand and reproduce the concern when possible:

- affected version or commit
- affected command, API, or file
- steps to reproduce
- expected impact
- any suggested mitigation

## What to report

Security concerns may include:

- unexpected model invocation or hidden external calls
- bypass of validation, budgets, or retry limits
- unsafe handling of sensitive input or output
- dependency or packaging vulnerabilities
- behavior that could expose user data or credentials

## Public disclosure

Please give maintainers time to review a sensitive report before publishing details publicly.

Because KORA is currently alpha software, fixes may be handled as regular commits unless a coordinated disclosure process is needed.

## Scope

This policy applies to the public KORA repository and the current alpha CLI, example, telemetry, and packaging surface.
