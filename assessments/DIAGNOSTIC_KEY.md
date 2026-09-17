# Entry diagnostic key

1. For L=||Xw−y||²/n, gradient=2Xᵀ(Xw−y)/n. Explain dimensions and why a stationary point is a minimum for this convex objective; rank deficiency can yield multiple minimizers. Refresh R1 linear regression and R14 convexity if this is unfamiliar.
2. E[Y|X=x] is an average over the conditional outcome distribution; one realized Y can differ widely. A useful conditional mean does not eliminate forecast error. Refresh conditional probability/variance and work the binary payoff example in Lesson 1.
3. −ln(.5)=ln 2≈.69314718. Using base 10 changes the unit and will disagree with the course NLL. Lesson 3 gives proper scoring practice.
4. Example: `assert np.isfinite(p).all() and (p >= 0).all() and np.isclose(p.sum(), 1)`. Also verify shape and class order against the label schema. Sum-to-one alone cannot catch a swapped class mapping.
5. A split defines which information can affect fitting, selection and evaluation. A seed controls pseudorandom choices within a specified procedure. Many seeds on one inspected split do not create fresh market outcomes. Lesson 9 develops chronological selection.

If more than two answers are incomplete, spend 4–8 focused hours on the linked primary reading topics and redo the diagnostic with changed numbers. There is no need to repeat a general AI degree before starting the market-specific projects.
