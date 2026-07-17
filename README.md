<div align="center">

<img src="assets/banner.png" alt="Omega Field Command" width="100%">

<br>

[![Status](https://img.shields.io/badge/status-Phase%202%20build-1ea0ff?style=for-the-badge&labelColor=0a1020)](#status)
[![American made](https://img.shields.io/badge/American%20made-by%20construction-d9a441?style=for-the-badge&labelColor=0a1020)](docs/american-made.md)
[![Runtime dependencies](https://img.shields.io/badge/runtime%20dependencies-2-8b8b8b?style=for-the-badge&labelColor=0a1020)](docs/american-made.md)
[![License](https://img.shields.io/badge/license-Proprietary-4a5568?style=for-the-badge&labelColor=0a1020)](LICENSE)

**[Request a pilot](mailto:crose@omegapointsolutions.com?subject=Omega%20Field%20Command%20pilot)**  ·  [Architecture](docs/architecture.md)  ·  [Security posture](docs/security-posture.md)  ·  [American made](docs/american-made.md)

<sub>A product of <b>Omega Point Solutions LLC</b></sub>

</div>

---

## What it does

Field Command answers three questions an agency has to get right, and that ordinary tools get wrong quietly.

- **Where are my officers.** Stale is labeled stale. GPS off renders off. One render path, so nothing can show an old fix as current.
- **Who needs help, now.** One-tap assistance with per-recipient delivery state, acknowledgement, and a mandatory disposition on close.
- **Who actually got the call.** `delivered` is set only on a transport acknowledgement. Exhausted retries surface to the requesting officer as failed, by name.

Built for agencies and multi-agency task forces that need one operating picture without putting their data in a shared cloud tenant they cannot audit.

## Why it is different: evidence, not adjectives

Every vendor says secure. These are the claims we can hand you proof for.

<table>
<tr><td width="50%" valign="top">

**Agencies cannot see each other's data, and it is proven on every commit.**

Isolation is enforced by PostgreSQL row-level security, not by an application `WHERE` clause, so the database refuses even when the application is wrong. An automated test applies the real migrations to a live database and asserts that a cross-agency read returns nothing and an unbound session returns zero rows instead of every row. The build fails if that proof does not run.

</td><td width="50%" valign="top">

**No other vendor's product code ships inside the platform, and a gate enforces it.**

The web framework, authentication, mapping, and geocoder are Omega Point original work on permissively licensed United States foundations. The production build adds exactly two registered dependencies. A build gate parses every module and fails on anything else.

</td></tr>
<tr><td width="50%" valign="top">

**Officer safety is a correctness property, and the failure cases are the tests.**

Staleness, sharing state, and delivery status are enforced invariants, not display logic. The suite asserts the denials first: cross-agency access, stale shown as live, a supervisor force-enabling an officer's sharing, and a replayed one-time code.

</td><td width="50%" valign="top">

**No certification is claimed.**

Controls are described as designed toward the relevant standards. We do not assert CJIS, SOC 2, or FedRAMP until an independent assessor validates it. We would rather lose a checkbox than put a claim in front of an agency that we cannot substantiate.

</td></tr>
</table>

## Capabilities

| Area | Capability |
|---|---|
| **Location** | Owner-controlled sharing, computed staleness, offline map packages |
| **Assistance** | One-tap request, per-recipient delivery state, mandatory disposition |
| **Access control** | Role-based, evaluated per request. Revocation lands on the next request |
| **Multi-agency** | Per-agency isolation at the database layer, scoped grants |
| **Accountability** | Append-only, hash-chained audit. Coordinates scrubbed before write |
| **Mapping** | In-house stack on United States public domain data |
| **Identity** | Mandatory multi-factor authentication, instant revocation, lockout |
| **Integrations** | Typed contracts. Every call carries actor and purpose |

## Architecture

```mermaid
flowchart LR
    C["Officers<br/>mobile and web"] --> E["API edge<br/>MFA, agency binding"]
    E --> A["Application core<br/>location, assistance, mapping"]
    A --> D[("PostgreSQL<br/>per-agency isolation")]
    A -. every decision .-> L[("Audit log<br/>append-only")]
```

Agency data stays on agency-owned infrastructure, or in a United States region of the agency's choosing, behind the agency's own reverse proxy. The platform never needs an outbound connection to a vendor cloud to work.

[Full architecture](docs/architecture.md)  ·  [Security posture](docs/security-posture.md)  ·  [American made](docs/american-made.md)

## Built for

- **Multi-agency task forces** that need one operating picture across departments without a shared tenant nobody controls.
- **Agencies with a compliance office**, who need to answer where data lives and what code is in the stack, in writing, before a review stalls.
- **Operations where accountability is not optional**, because every action, including the denials, is on an append-only record.

## Questions agencies ask

**Is this CJIS compliant?**
No certification is claimed. The platform is designed toward the relevant controls, and the [security posture](docs/security-posture.md) states exactly what we address and what stays the agency's responsibility. Independent assessment comes before any claim.

**Where does our data live?**
On agency-owned infrastructure, or a United States region of your choosing, behind your own reverse proxy. The platform does not require an outbound connection to a vendor cloud to function.

**What does "American made" mean here?**
Every dependency is United States origin, permissively licensed, and recorded in a register that a build gate enforces. The details are in [American made by construction](docs/american-made.md).

**Can it work with our existing GIS or radios?**
The mapping stack is in-house so it never requires a commercial license, and agencies that already run ArcGIS or similar can connect it. Integrations sit behind typed contracts.

**Is the source available?**
The implementation is proprietary and maintained privately. This repository is the public capability and architecture reference.

## Status

Phase 2 build. Identity, authorization, location, assistance, audit, and mapping are implemented and tested. Not yet released for production caseload, and no live agency data is in use.

Pilot slots are open now, and early agencies shape the roadmap.

## Contact

**Omega Point Solutions LLC**
[omegapointsolutions.com](https://omegapointsolutions.com)  ·  [crose@omegapointsolutions.com](mailto:crose@omegapointsolutions.com)

**[Request a pilot](mailto:crose@omegapointsolutions.com?subject=Omega%20Field%20Command%20pilot)** for a technical walkthrough or procurement documentation.

---

<div align="center">
<sub>© 2026 Omega Point Solutions LLC. All rights reserved.<br>
Documentation repository. The implementation is proprietary and maintained privately.</sub>
</div>
