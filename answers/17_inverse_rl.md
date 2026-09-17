# Lesson 17 answer key — Fit a restricted utility model and test identification

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

TerminalV_H=0 and derivative 0. Given next-step derivatives, differentiateQ to getφ+P dV_next; differentiating log-sum-exp gives the probability-weighted average dV. Subtract and divide by τ for dlogπ. For scale c, induction givesQ'=cQ andV'=cV becauseτ'=cτ; hence(Q'−V')/τ'=(Q−V)/τ. Fixedθ_cost=1 and fixedτ anchor scale within the selected model but do not prove all reward directions are identified.

## A2

Reference held-out NLL fit≈.7688692, generating policy≈.7682670. Gradient maximum absolute error≈7.9e−10 with the given float 64 fixture; joint-scale probability error≈2e−15. Numerical tolerances of 1e−6 and 1e−12 respectively are reasonable across supported hosts. See the saved output for coefficients; parameter error is not zero despite close policy losses.

For frequency, count training active actions with a declared pseudocount, normalize, apply the state's feasibility mask and renormalize. Score only the same held-out active decisions as the IRL comparison. Including completed inventory states where only wait is feasible inflates apparent fit. Do not fit frequencies on held-out actions. Alternative code can earn full credit without matching floating-point optimizer iterates exactly. The final reference also scores 481 held-out active decisions: frequency NLL≈1.083115, behavioral cloning≈.835155 and IRL with training-estimated dynamics≈.824106. The oracle-dynamics IRL result has more information, so its gap must not be attributed solely to architecture.

## A3

Need attributable decisions, action feasibility, remaining mandate/inventory, deadline, usable public information, transition/cost observations and assumptions about unobserved information. Member attribution or daily prices do not supply these fields. Synthetic recovery tests implementation under a favorable known model; real evaluation additionally needs estimated dynamics, misspecification checks, support, unseen episodes/actors and execution relevance. Repair by distinguishing feature observability from theoretical desirability in a table.
