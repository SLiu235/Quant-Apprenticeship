# Lesson 4 answer key — Translate financial contracts into PnL

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Equity: $19 net and 38 bps on $5,000. Futures: $200 before fees. Call: (107−100−4)×100=$300. Bond first-order approximation: −6×.0025=−.015, or −1.5%; convexity is omitted. Futures margin is collateral; its smaller denominator can make a return look large without reducing notional risk.

## A2

Reference ledger equations: cash' = cash − signed_quantity×price×multiplier − fee; holdings' = holdings+signed_quantity; equity=cash +marked holdings. Deposits change cash and a separate contributed-capital account. Trading PnL=equity change−net contributions, with distributions counted once.

Example fixture beginning at $10,000: buy 100 at 50 with $.50 fee → cash 4,999.50, shares 100, marked equity 9,999.50. Split 2:1 → shares 200, price 25, same equity. Receive $1 per current share → cash 5,199.50; a corresponding ex-dividend mark of 24 gives equity 9,999.50, showing the cashflow is not free profit. Deposit 100 → equity 10,099.50 and contribution 100, zero additional trading PnL. Short 10 at 24 with $.50 fee → cash 5,539, net shares 190; specify this as a reduction of the long position, or start a separate flat fixture to test an actual short. In a flat account short 10 at 24 yields cash 10,239.50, shares −10 and equity 9,999.50.

Reject implementations that change share count without adjusting price basis or double-count dividends in both total-return prices and cash. Corporate-action fixtures are stipulated arithmetic, not a historical entitlement engine.

## A3

Option PnL also depends on implied volatility, time decay, rates and nonlinearity. Expiration payoff ignores the price paid. A futures roll crosses different delivery prices and closes/opens actual contracts; a chart splice can introduce a level difference that was never earned by holding one contract. Repair by writing the two separate fills and their contract IDs.
