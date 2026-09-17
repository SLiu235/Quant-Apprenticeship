# Lesson 6 — Make calendars and changing sessions explicit

Prerequisites: Lessons 4–5. Suggested effort: 4–6 hours, including the lab. Project: 2.

## Time is a market convention as well as a timestamp

A UTC date, local calendar date, exchange trade date and settlement date can differ. Store them separately. A session classifier should consume a dated venue-rule configuration, holiday calendar, instrument status and timestamp. It should not decide that every weekday minute is tradable. A halt overrides an otherwise open session; partial holidays and auctions need their own handling.

As checked September 11, 2026, Nasdaq's [August 17 announcement](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2026-46) describes a December 6 launch of a 21:00–04:00 ET session, cancellation of remaining orders at 04:00, and next-trading-day assignment for 21:00–midnight trades. This is a dated announcement, not evidence that our historical bars already contain that session. Recheck venue specifications before operational use. The standard U.S. equity settlement cycle is generally T+1; exceptions and cash availability still need an instrument/account-specific contract (R7).

Longer hours change observable states, not just row counts. Liquidity providers, spreads, reference-price freshness, corporate actions and staffing may differ by session. A model trained on daytime observations can face covariate and mechanism shift overnight. Evaluate forecast calibration and execution assumptions by session, with enough independent dates; splitting one short sample into many cells can produce precise-looking nonsense.

## Worked example

In New York, a 09:25 local cutoff is 14:25 UTC in winter and 13:25 UTC in summer. A fixed 14:25 UTC cutoff would be an hour late during daylight time. A synthetic venue gives 21:00–24:00 the next trading date; a Sunday 21:30 trade can belong to Monday under that stipulated rule. Simply adding 24 hours fails around weekends and holidays.

## Lab procedure

1. Make a synthetic calendar fixture with a Monday holiday and a reset interval; label it as a test calendar, not a production exchange calendar.
2. Use `zoneinfo.ZoneInfo('America/New_York')` to convert aware timestamps. Test winter/summer offsets.
3. Implement `session(timestamp, rules_version, calendar)` and `trade_date(...)` as separate functions. Return closed or unknown when rules do not cover the timestamp.
4. Add an order crossing a stipulated reset; require the modeled cancellation event before a new order can be treated as live.
5. Read R6 and R7 for the distinction between trading access and post-trade processing. Record verification date in your rule manifest.

## Assignments

**A1.** Convert January 15, 2026 and July 15, 2026 at 09:25 ET to UTC. Explain why local date plus one is not an exchange trading-date algorithm.

**A2.** Submit calendar tests for weekend, holiday, reset, daylight-time offsets and an instrument halt. Supply explicit expected outputs from your synthetic rule fixture; do not silently call it Nasdaq-certified.

**A3.** Design a three-session validation table: regular, premarket and overnight. Specify minimum evidence to fill each cell and mark which cells the current daily-bar/Reddit pilot cannot support.

Mastery check: you can change a schedule configuration without changing statistical code, and you never manufacture overnight evidence from daily bars.

Check your work with the [answer key](../answers/06_sessions.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
