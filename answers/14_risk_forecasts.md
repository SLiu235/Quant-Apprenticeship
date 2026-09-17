# Lesson 14 answer key — Forecast uncertainty and test calibration

Attempt the assignments before reading. Different code is welcome; the evidence and reasoning must agree.

## A1

Expected loss=logv+m2/v. Derivative(v−m2)/v² changes sign at v=m2>0, giving the minimum. Losses≈−6.824046 and −5.210340. If the target is centered variance with a nonzero mean, use residuals with a valid mean forecast; otherwise the target is the second moment. Converting decimal returns to bps changes numeric QLIKE by a constant under consistent variance scaling, not relative rankings.

## A2

Initialize EWMA from training observations, then v_t=λv_{t−1}+(1−λ)r_{t−1}²; never include r_t. A declaredλ=.94 is acceptable as a teaching choice, not universally optimal. Use the same evaluation dates and variance floor for comparable candidates, report all declared floor sensitivities and show date dependence in uncertainty. At least two bins need count, mean forecast and mean realized square; sparse bins should be labeled unstable.

Recorded reference QLIKE rolling 20≈−5.90865 versus previous-square≈12516.0643. This enormous difference is driven by tiny denominator forecasts. The stronger reference EWMA(.94) comparator gives QLIKE approximately −5.895776; its small difference from rolling 20 needs a paired uncertainty assessment before a superiority claim. A solution that only celebrates the improvement misses the lesson.

## A3

Two equally weighted regimes with forecast second moments 1 and 9 and realized means 2 and 8 have equal aggregate totals 10 but low-risk forecasts understate risk by 100% while high-risk forecasts overstate it. Even correct second moments do not determine tail shape or dependence. Portfolio safety also requires cross-asset covariance, exposure limits, liquidity and execution. Repair by inspecting conditional and tail diagnostics rather than accepting a single aggregate ratio.
