# American made by construction

"No foreign or third party product code in our platform" is easy to say and hard to prove. Here is how Omega Point implements it as something checkable rather than a marketing line.

## The standard, stated precisely

A literal zero is impossible: the interpreter, the database, and the operating system are themselves copyrighted works. So the rule is four verifiable parts.

**1. All application code is Omega Point original work.**
No vendored, copied, or third party derived source. Verified by a build gate that parses every product module and fails on any import outside the standard library, Omega Point packages, and the registered dependencies below.

**2. External foundations are permissively licensed and United States origin.**

| Foundation | License | Origin |
|---|---|---|
| Python | Python Software Foundation License | PSF, a United States 501(c)(3) incorporated in Delaware |
| PostgreSQL | PostgreSQL License (BSD style) | University of California, Berkeley |

Both permit unrestricted commercial use with no copyleft obligation and no per seat cost.

**3. No paid, subscription, or usage metered third party product** sits in any feature path. Where a capability would normally be bought, it is built.

**4. Map and geographic data comes from United States government sources**, public domain by statute (17 U.S.C. 105). Not licensed, not copyrighted, produced in the United States.

## Registered runtime dependencies

The production build adds exactly two dependencies. Both are permissively licensed, both are maintained by United States based projects, and both are recorded here before they were allowed into the build.

| Dependency | License | Origin | Why it is not built in house |
|---|---|---|---|
| `asyncpg` | Apache 2.0 | MagicStack Inc., New York | Speaking the PostgreSQL wire protocol correctly and safely is a security sensitive protocol implementation, not application logic. A hand rolled driver would enlarge the audit surface, not shrink it. |
| `cryptography` | Apache 2.0 or BSD 3 Clause | Python Cryptographic Authority, a United States community project | Authenticated encryption is required for field level encryption. Rolling our own cipher would violate the rule against implementing your own cryptography. This is the audited, FIPS capable standard. |

Adding a third dependency requires a written entry in the provenance register with license, origin, and cost analysis before code review. The build gate enforces the list.

## What was built instead of bought

| Would normally be purchased | Our approach |
|---|---|
| Web framework and validation | Omega Point original framework and validation layer |
| Authentication, multi factor authentication, identity vendor | Built in house: sessions, password hashing, time based one time passwords, lockout |
| Commercial mapping and tiles | In house tile pipeline and renderer over United States government public domain data. Agencies may connect their own licensed GIS systems, but the platform never requires one |
| Commercial geocoding | In house geocoder using the Census Bureau's own address range interpolation method |
| Messaging and alert gateways | In house delivery queue with transport acknowledgement |
| Error and crash reporting services | In house reporting, stored in the agency's own database |

## Why agencies care

- **Supply chain.** Fewer third party components means fewer places for someone else's compromise to become yours.
- **Cost.** No per seat licence stacking underneath the platform.
- **Sovereignty.** Agency data stays on agency chosen infrastructure. The platform does not require an outbound connection to a vendor cloud to function.
- **Procurement.** The provenance register answers the origin and licensing questions that stall reviews, in writing, before they are asked.

## Deployment guidance

- **Operating system:** agency choice. A United States vendor enterprise Linux is recommended for support and validated cryptographic modules. Linux is infrastructure the product runs on, not code linked into it.
- **Hosting:** agency on premises hardware, or United States hosted regions of United States providers.
- **TLS:** terminated at the agency's own reverse proxy.

---

<sub>© 2026 Omega Point Solutions LLC. All rights reserved.</sub>
