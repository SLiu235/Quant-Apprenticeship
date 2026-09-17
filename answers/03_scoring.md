# Lesson 3 answer key — Score forecasts and quantify dependent evidence

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

NLL = −ln(.5)=.69314718056; Brier=.38. Row mean=(.10−.06)/4=.01; equal-date mean=(.10−.02)/2=.04. Dividing Brier by three defines a scaled score; it is not the stated convention. Fix the convention rather than “correcting” one model's results.

## A2

Reference NLLs: frequency .945665579; market .960576256; public .977373068; graph .986737481. Brier scores respectively .582361958, .595066384, .604963419, .612688607. Each has 139 rows. Accuracy: 65/139, 65/139, 52/139, 56/139 respectively.

Public-minus-market row mean .0167968122; date mean .0146499363 across 52 dates. Bootstrap intervals: b=1 [.0054809274,.0250410328]; b=3 [.0064225027,.0245798988]; b=5 [.0056023510,.0266580692]; b=10 [.0038188209,.0285812485]. Match means within 1e−9. With the specified NumPy RNG and algorithm, intervals should match similarly; another legitimate RNG may differ, but document and compare Monte Carlo variation rather than claiming exact replication.

See `reference/common.py` for one complete implementation after your attempt. Fixtures must detect swapped probability columns even when rows still sum to one.

## A3

Public text worsened the chosen forecast score in this exploratory sample. Frequency is a strong sanity baseline: the market-feature model did not beat it here either. Dates and issuers are dependent; block length approximates dependence and the interval conditions on the observed selected sample and fixed models. It does not incorporate missing observations, model search or archive bias. Tuning now makes these dates development data. A valid next confirmatory evaluation needs independent uninspected observations and a frozen protocol, not a renamed split file.

Repair: if the sign differs, check the subtraction order; if only the headline differs, inspect date weights; if all NLLs are roughly scaled, check logarithm base.
