# Lesson 6 answer key — Make calendars and changing sessions explicit

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

January 15:14:25 UTC; July 15:13:25 UTC. “Next” must mean next eligible trade date under the venue's calendar and applicable session rules. A weekend or holiday can require skipping several dates. Settlement further uses the settlement calendar and instrument cycle; it is not an intraday return horizon.

## A2

Accept an explicitly declared synthetic venue with day 04:00–20:00, reset 20:00–21:00, night 21:00–04:00 and your defined operating weekdays/holiday rules. The exact synthetic policy is free to differ from a real venue, but expected outputs must follow it consistently. Tests should reject an unknown rules version, classify a stipulated halt as unavailable, and avoid treating a pending cancel as an acknowledged reset cancellation. Use timezone-aware instants to avoid ambiguous local fall-back times; if accepting local naive times, require an explicit fold/disambiguation policy.

## A3

Each row needs observed quotes/trades and usable signal receipts for that session, an execution benchmark, sample counts by independent date, same-session baselines, costs, outages and calibration/loss intervals. Daily open/close prices support only an aggregate ordinary-session response target under timing assumptions; they do not supply intraday premarket or overnight returns/fills. Historical ordinary-session observations cannot verify a future schedule. A correct answer leaves unsupported cells blank with an acquisition requirement instead of extrapolated performance.

Repair: compare timestamps around a daylight-time boundary and a holiday. Calendar correctness is not established by checking an ordinary Tuesday.
