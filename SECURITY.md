# Security Policy

Omega Point Solutions builds Omega Field Command for law enforcement, where a
security defect is an officer-safety defect. We treat reports accordingly.

## Reporting a vulnerability

If you believe you have found a security issue in an Omega Field Command
deployment, or in anything described in this documentation, contact us directly:

**[crose@omegapointsolutions.com](mailto:crose@omegapointsolutions.com)**

Please include enough detail to reproduce or locate the issue. We will acknowledge
receipt, keep you informed as we work it, and credit you if you would like to be
credited.

Please do not open a public issue for a security report, and please give us a
reasonable window to respond before any public disclosure. We do not operate a
paid bug-bounty program at this time.

## Scope

This repository is documentation only; it does not contain the implementation.
Reports about a running Omega Field Command deployment, or about a claim made in
these documents, are in scope. The proprietary source is maintained privately and
is not distributed here.

## Our posture, stated honestly

We do not claim CJIS, SOC 2, or FedRAMP certification for this platform. Controls
are described as designed toward the relevant standards, and independent
assessment comes before any claim. What we do assert, we prove: tenant isolation
is verified against a live database on every commit, and the provenance of every
dependency is enforced by an automated build gate. See
[docs/security-posture.md](docs/security-posture.md).

---

<sub>© 2026 Omega Point Solutions LLC. All rights reserved.</sub>
