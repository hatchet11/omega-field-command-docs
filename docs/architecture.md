# Architecture

How Omega Field Command is put together, and why each load-bearing decision was made that way.

## Design principles

1. **Isolation before features.** Tenant separation and access control were built and proven before any operational data model. Retrofitting isolation onto a shipped product does not work.
2. **Correctness where it affects officer safety.** Location freshness, sharing state, and delivery status are enforced invariants, not display logic.
3. **Accountability is not optional.** Every sensitive action is audited, including the denials.
4. **Own the stack.** No other vendor's product code inside the platform.

## Load-bearing decisions

### Tenant isolation is structural

Row-level security policies keyed to the requesting agency make cross-agency reads impossible at the database layer. The agency is bound to the database session for the life of the request, and PostgreSQL filters every query against it.

The distinction matters. If isolation lives in an application `WHERE` clause, then one forgotten clause in one handler is a cross-agency breach. If isolation lives in the database, the query engine refuses regardless of what the application asks for. Isolation is also forced for the table owner, and the application connects as a least-privilege role that owns nothing.

### Access control is data

Permissions are rows. Roles are named bundles of permissions. Handlers ask an authorization engine whether an actor holds a permission in a scope. There are no role name comparisons anywhere in the code.

Two consequences matter operationally. Revoking a role takes effect on the very next request, because nothing is cached in a token. And an agency can define its own roles without a code change.

### Location is a state machine

One module decides how a location renders. Staleness is computed at presentation time against agency policy, never stored and never trusted from the client. States that mean "not sharing" do not render coordinates. Only the device owner can transition into a sharing state.

Because there is a single render path, there is no second code path that could present a stale fix as current.

### Delivery is never assumed

Assistance alerts move through queued, sending, delivered, seen, and acknowledged states, with one row per intended recipient. `delivered` requires a transport-level acknowledgement. Retries are bounded, and exhausted retries surface to the requesting officer as failed rather than disappearing.

An officer who requested help sees the truth about who received it.

### Audit is a wrapper, not a call

Sensitive handlers are wrapped rather than instrumented by hand, so allow, deny, and error outcomes are all recorded through one path. The trail is append-only at the database layer and hash-chained, so a removed row breaks the chain and is detectable. A scrubber strips coordinates, message content, and credentials before anything is written, because an audit log is not a place for the payload.

### Integrations are contracts

Analysis and intelligence systems sit behind typed contracts. Every call carries the acting user and a stated purpose, and every response returns citations flagged for human review by default. An adapter cannot become a quiet data egress path.

## Mapping

The mapping stack is Omega Point original work built on United States government public domain data:

- Web Mercator projection, tiling, and distance mathematics as a single implementation shared by the geocoder, tile cutter, offline packager, and renderer.
- A reader for United States Census TIGER/Line data.
- A geocoder using the Census Bureau's own address-range interpolation method, with reverse geocoding.
- A vector tile format with GeoJSON export, and offline region packages for degraded coverage.
- A map renderer with no third-party mapping library.

Agencies that already license commercial GIS systems can connect them. The platform never requires one.

## Data protection

- Sensitive fields are encrypted at the application layer with authenticated encryption, so the database never holds the plaintext. Ciphertext is bound to the record it belongs to and cannot be replayed into another row.
- Session tokens are opaque random values. Only a hash is stored, so the token database is not a credential store.
- Password hashing stores its cost parameters per record, so the cost can be raised over time without locking anyone out.
- Key rotation is supported: retired keys stay resolvable for decryption while new writes use the current key.

## Deployment shape

The platform runs behind the agency's TLS-terminating reverse proxy on agency-owned infrastructure or a United States-hosted region of a United States provider. It does not require an outbound connection to a vendor cloud to function.

---

<sub>© 2026 Omega Point Solutions LLC. All rights reserved.</sub>
