# Lesson 7 answer key — Build a point-in-time market panel

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

One share×100 becomes two×50: value 100 unchanged. Raw price ratio 50/100−1=−50% is not the holding return. Use consistent adjustment or an explicit split event in the holdings ledger. Total-return prices already embed distributions; adding the same dividend cash again double-counts it.

## A2

The provided snapshot has 394 common dates; Project 3 drops 20 warm-up dates. Per-security coverage should come from files, not inferred from the intersection. Expected locally: ASML/MU/WDC 443 bars starting December 2, 2024; SNDK 394 beginning February 13, 2025; all end September 9, 2026. A first recorded bar is a provider coverage fact, not proof of an IPO date. If your raw fields differ, report the new hashes and investigate rather than forcing these counts.

A complete manifest separates vendor origin from local download location and states that the course has not certified redistribution rights. Hashes identify bytes, not legal rights or truth. Reject conflicting duplicate timestamps; document invalid bars before intersection. Missing history is excluded with a reason, never synthesized as observed data.

## A3

Query a bitemporal security master: eligibility effective at t, mapping valid at t, and information about both available by t. Include listing/delisting, share class, venue, corporate actions and explicit eligibility rules. A current membership list plus historical prices fails. The local four-name archive lacks a full historical universe/security master and delisting outcomes; broader claims require these data and a protocol established before universe selection.

Repair: create a fictional security that delists after a loss. If it vanishes from your report, repair the population query.
