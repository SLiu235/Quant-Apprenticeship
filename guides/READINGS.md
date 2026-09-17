# Primary reading library

Checked 2026-09-11. These are supplementary sources, not a requirement to read entire books before doing a lab. Each lesson specifies a focus and asks a question whose answer appears in its key. Course explanations and numerical examples are original teaching material. Sources support methods; none establishes profitability for our data.

| ID | Source and focused use |
|---|---|
| R1 | [An Introduction to Statistical Learning, author site](https://www.statlearning.com/) — statistical learning, classification, resampling, regularization and multiple testing; choose the Python edition and chapter titles, since numbering varies across editions. |
| R2 | [scikit-learn: common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — inconsistent preprocessing and data leakage. A pipeline does not itself ensure valid time splits. |
| R3 | [Gu, Kelly & Xiu: Empirical Asset Pricing via Machine Learning](https://www.nber.org/papers/w25398) — prediction problem, economic evaluation and model comparison; inspect how their panel differs from four selected issuers. |
| R4 | [Harvey, Liu & Zhu: …and the Cross-Section of Expected Returns](https://www.nber.org/papers/w20592) — multiple testing and factor discovery. A threshold from a particular study is not a universal approval rule. |
| R5 | [Nasdaq TotalView ITCH 5.0 specification](https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/NQTVITCHSpecification_5.0.pdf) — add, execute, cancel, delete, replace, system events and stock directory messages. Record the retrieved specification version before parsing a feed. |
| R6 | [Nasdaq Equity Trader Alert 2026-46](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2026-46) — dated extended-session announcement; revisit before building any live calendar. |
| R7 | [SEC T+1 investor bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin) — distinguish trade date, settlement and cash availability; identify instrument exceptions instead of assuming all markets share a cycle. |
| R8 | [CME: futures expiration and contract roll](https://www.cmegroup.com/education/courses/introduction-to-futures/understanding-futures-expiration-contract-roll) and [OIC: options pricing](https://www.optionseducation.org/optionsoverview/options-pricing) — contract identity, expiry, payoff versus marked value, intrinsic value and time value. |
| R9 | [Araci: FinBERT](https://arxiv.org/abs/1908.10063) — task, labels and evaluation; sentiment accuracy is not evidence of excess returns. |
| R10 | [Lewis et al.: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) — retrieve/generate architecture. Our as-of restrictions are an additional finance requirement, not a result established by this paper. |
| R11 | [OWASP: LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) — retrieved content as untrusted input, limited tool authority and layered controls. |
| R12 | [Hernán & Robins: Causal Inference, What If](https://miguelhernan.org/whatifbook) — association, exchangeability, confounding and selection; use the freely available author book. |
| R13 | [Ledoit & Wolf: Honey, I Shrunk the Sample Covariance Matrix](https://ledoit.net/honey.pdf) — why sample covariance destabilizes portfolios. Our fixed diagonal shrinkage is a teaching estimator, not the paper's estimated optimal shrinkage. |
| R14 | [Boyd & Vandenberghe: Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) — convex sets, quadratic programs, optimality and duality. |
| R15 | [D4 RL](https://arxiv.org/abs/2004.07219) and [Conservative Q-Learning](https://arxiv.org/abs/2006.04779) — offline coverage and distribution shift; benchmark success is not exchange evidence. |
| R16 | [Ziebart: Maximum Causal Entropy](https://www.cs.cmu.edu/~bziebart/publications/maximum-causal-entropy.html) — sequential stochastic choice and causal entropy. |
| R17 | [Skalse et al.: Identifiability and Generalizability from the Perspective of Inverse Reinforcement Learning](https://proceedings.mlr.press/v202/skalse23a.html) — reward equivalence and what observations identify. |
| R18 | [PyTorch benchmark recipe](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html) — warm-up, synchronization, threads and measurement. No GPU benchmark has been inferred from a CPU run. |

## Contemporary data, and what the course actually has

The local recent pilot uses Yahoo daily bars for four Nasdaq-listed issuers, together with a public Reddit archive for 2025–February 2026. These are vendor bars, not the exchange's order feed. Prices extend into September 2026 locally; the social archive does not. The selected archive, receipt/edit gaps and comment-collection policy limit inference. Read the local [source audit](../../BehaviorIRL/docs/RECENT_DATASETS.md) and [pilot report](../../BehaviorIRL/results/reddit_recent_2026/RECENT_DATA_REPORT.md) before treating “recent” as “representative.”

Optional higher-data paths include [Databento XNAS.ITCH](https://databento.com/datasets/XNAS.ITCH), [Stocktwits Firestream](https://firestream.stocktwits.com/) and [X search documentation](https://docs.x.com/x-api/posts/search/introduction). Access, history, fields and licenses must be checked before acquisition. No subscription, API credentials or entitlement is bundled. Our required labs run from existing local data and explicit simulations. Recent social data has to be independently acquired and audited to make a fresh paired study; a newer price file alone does not refresh a social experiment.
