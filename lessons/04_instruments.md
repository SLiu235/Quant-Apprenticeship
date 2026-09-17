# Lesson 4 — Translate financial contracts into PnL

Prerequisites: Lessons 1–3. Suggested effort: 5–7 hours, including the lab. Project: 2.

## Units before predictions

A forecast becomes economically meaningful only after specifying the instrument. For q shares bought at P_0 and marked at P_1, cash PnL is q(P_1−P_0) plus received cash distributions minus fees and financing. A short position has q<0 and may incur borrow fees and recall risk. Portfolio return divides PnL by an explicitly chosen capital base; dividing by gross exposure answers a different question from dividing by account equity.

A futures contract is an expiring agreement with a contract-specific multiplier. Its marked variation is contracts × multiplier × price change; notional exposure is not the margin posted. Rolling closes one expiry and opens another, creating two trades and an exposure transition. A concatenated price chart is not a cash ledger.

For an option, expiration payoff and today's price are different objects. A call payoff is max(S−K,0); its profit also subtracts premium. Near a reference state, ΔV≈ΔΔS + ½Γ(ΔS)² + VegaΔσ + ThetaΔt. The approximation is local, and Greek units must specify volatility percentage points versus decimals and calendar versus trading days. Volatility can change option value with unchanged stock price.

For a bond under a small parallel yield move, ΔP/P≈−D_mod Δy + ½Convexity(Δy)². Yield is a decimal here. For FX, state base/quote currency and convert all PnL to account currency at an explicit rate. Equity-only returns do not teach these cashflows automatically.

## Worked examples

Buy 100 shares at $50, sell at $50.20, pay $.50 each side: gross $20, net $19. On $5,000 allocated capital that is 38 bps net. Two hypothetical futures with a $20/point multiplier and a +5-point move make $200 before fees, whatever margin was posted. A call with strike 100 and premium 4 on 100-share units earns $300 at expiration spot 107, ignoring fees and financing.

## Lab procedure

1. Create a typed ledger with instrument ID, multiplier, side, quantity, currency, price, fee and timestamp. Represent deposits separately from trading PnL.
2. Enter the three examples and reconcile cash/exposure independently.
3. Add a split: 100 shares at $50 become 200 at $25 with unchanged economic value. Add a $1/share dividend as a cashflow, with explicit entitlement dates.
4. Read R8's futures-roll and option-pricing introductions. Inspect one actual contract specification before extending beyond hypothetical multipliers. Use R7 to distinguish settlement from mark-to-market economics.

## Assignments

**A1.** Reproduce all three PnLs. Compute the first-order percentage price change for duration 6 and a +25 bp yield move. State why “margin return” is not futures notional return.

**A2.** Implement the equity ledger fixtures including split, dividend, a short sale and fees. Test a $100 deposit so it changes equity but not trading PnL. Submit cash, holdings and equity after each event.

**A3.** Explain why a call's positive stock delta does not determine its one-day PnL and why a rolled futures series may show a jump without a matching trading gain. Relate both to R8.

Mastery check: every reported result has a currency, denominator, holding horizon and cashflow convention.

Check your work with the [answer key](../answers/04_instruments.md). Use the [self-assessment rules](../assessments/MASTERY.md); repair a failed gate before continuing.
