# Security posture

What is actually true about this platform's security, stated so that a procurement officer or an agency's technical staff can check it.

## What we do not claim

Omega Point Solutions does not assert CJIS, SOC 2, FedRAMP, or any other certification for Omega Field Command. Controls are described as designed toward the relevant standards. No compliance claim will appear in our material until an independent assessor validates it.

We would rather lose a box on a checklist than put a claim in front of an agency that we cannot substantiate.

## Trust boundaries

1. Internet to API gateway: TLS 1.3, short-lived tokens.
2. API to database: per-request agency binding, row-level security.
3. Application to audit log: append-only, separate credential.
4. Application to integration adapters: typed contracts, permission checked at the edge.
5. Device to local storage: encrypted local storage, attestation field.

## Controls, by asset

### Officer location

| Risk | Control |
|---|---|
| Another agency queries a location | Row-level security, enforced by the database and forced for the table owner |
| A teammate views a location without authority | Scoped, query-time permission evaluation |
| Coordinates land in logs | Audit scrubber removes coordinates before write, including inside nested structures |
| A stale fix is presented as current | Single render path with computed staleness |
| A supervisor force-enables sharing | State machine rejects non-owner transitions into sharing |

### Assistance alerts

| Risk | Control |
|---|---|
| "I never received the alert" | Per-recipient delivery rows plus a timeline |
| A false delivered status | `delivered` requires a transport acknowledgement |
| An alert raised on another officer's behalf | Requester is bound to the authenticated session |
| An alert addressed into another agency | Recipients validated against the caller's own agency roster |

### Audit trail

| Risk | Control |
|---|---|
| An administrator edits history | Immutability enforced by database trigger, with updates and deletes rejected |
| Rows removed between backups | Hash chain breaks on a gap |
| Denied actions go unlogged | Allow, deny, and error are all recorded through one path |
| Sensitive payloads inside audit detail | Scrubber, applied before persistence |

### Identity and sessions

| Risk | Control |
|---|---|
| Credential stuffing | Mandatory multi-factor authentication, account lockout with cooldown, uniform outward errors so accounts cannot be enumerated |
| A stale role in a cached token | No permission caching. Authorization is evaluated per-request |
| A replayed one-time code | Each code is consumed exactly once by an atomic compare-and-set |
| A stolen session token | Only a hash of the token is stored. Revocation and suspension take effect on the next request |
| Secrets exposed by a database compromise | Sensitive fields encrypted at the application layer, bound to their record |

## How the claims are verified

- **Isolation is proven against a real database on every commit.** An automated test applies the production migrations to a live PostgreSQL instance and asserts that one agency cannot read or modify another's records, that a session with no agency bound returns zero rows rather than every row, and that the audit log rejects updates and deletes. The pipeline fails if that proof is skipped rather than passing quietly.
- **Provenance is machine-checked.** A build gate parses every product module and fails on any import outside the standard library, Omega Point packages, and the registered dependencies.
- **The denials are the tests.** The suite asserts failure cases first: cross-agency access, stale rendered as live, non-owner sharing, replayed codes, and unacknowledged delivery reported honestly.

## Data handling

- No real agency, criminal justice, or personal data exists in any Omega Point development environment for this platform. Development seeds describe a fictional training agency.
- No production credentials or endpoints are stored in source control.
- Agency data stays on agency-owned infrastructure or a United States-hosted region of the agency's choosing.

## Responsible disclosure

If you believe you have found a security issue in an Omega Field Command deployment, contact [crose@omegapointsolutions.com](mailto:crose@omegapointsolutions.com). We will acknowledge receipt and work the issue directly. Please do not disclose publicly before we have had a chance to respond.

---

<sub>© 2026 Omega Point Solutions LLC. All rights reserved.</sub>
