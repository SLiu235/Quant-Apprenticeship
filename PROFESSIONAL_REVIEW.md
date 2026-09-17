# Professional review and revision — September 14, 2026

This reviews the apprenticeship, not the learner. No learner work has been assessed. The judgments below are a synthesis of the supplied code/materials and public research-role descriptions, not a claim of employment at or privileged knowledge of any firm.

## Judgment

The original package is a useful builder foundation. It is not yet enough to develop an exceptional independent quant researcher. It emphasizes completing a safe, small system; professional research also requires discovering an economically meaningful question, acquiring defensible evidence, deciding what to abandon, and earning a place in a portfolio. Adding more model names would not close that gap.

My earlier description of the pack as complete was too broad. The files and worked reference were complete for their teaching scope. The evidence needed for a professional research apprenticeship was not. The revised [professional track](PROFESSIONAL_TRACK.md) now defines that work explicitly and connects it to executable labs.

## Specific shortcomings and changes

| Previous weakness | What a strong researcher should demonstrate | Revision |
|---|---|---|
| A supplied signal and clean dataset remove most problem discovery | Originate a question, explain the market mechanism and why a tradable discrepancy might persist | Studio 1: edge thesis, competing explanations, data diligence and research priority |
| Four selected issuers and inspected outcomes are too narrow for general claims | Separate replication, development, prospective evidence and population limits | Studio 2: real-data replication followed by an original extension and untouched-data plan |
| Statistical discipline is largely prose | Account for failed ideas, prompts, features and selection; lock choices before examining evaluation | Transactional experiment book, trial budgets, immutable contracts/results and evaluation exposure state |
| “Keep it simple” can become an excuse to avoid deep ML | Train, diagnose and modify models; demonstrate when nonlinearity or representation learning earns its cost | Real-data five-model lab, feature ablation, train-only normalization, validation checkpoints and future-label mutation test |
| AI research support is represented by lexical retrieval alone | Evaluate extraction semantics, abstention, historical model availability, cost, latency and permissions | Structured-output evaluation harness and Studio 5; live-model experiments remain explicitly separate |
| Forecast quality is not connected tightly enough to deployed inventory | Explain horizon alignment and what each dollar of P&L comes from | Overnight/intraday/execution decomposition, independently reconciled against ledger P&L |
| Only one portfolio rule and one capital scale | Compare credible alternatives under shared costs and limits; investigate size and liquidity | Cash/equal-weight/signal comparisons over two capital scales and three cost settings |
| Passing tests risks becoming the definition of readiness | Know which economic assumptions the tests do not establish | Six evidence-producing studios, investment committee memo and limited prospective paper protocol |
| Communication is mostly a final memo | Defend an idea, respond to skeptical replication and hand off work | Research agenda, reviewer handoff, counter-thesis and decision-reversal records |
| Many specialties, little explicit depth | Develop a primary specialty plus the interfaces needed to work with PMs, traders and engineers | A depth requirement within a self-selected market problem; no obligation to master every asset class first |

## Concrete implementation findings

The execution replay checked quote freshness by comparing a quote timestamp with itself. That could never expose a stale or future quote. It now compares against the scheduled execution clock and validates snapshots even when no orders are sent. A regression test supplies a future-stamped quote.

The quote lookup silently collapsed duplicate symbol/date observations. It now rejects duplicate quotes and missing/duplicate forecast symbols. The execution cost function now rejects nonfinite terminal and decision benchmarks instead of allowing an invalid opportunity-cost result downstream.

The forecast target remains intraday while the example carries inventory overnight. Rather than hiding that difference, the new report explicitly separates overnight P&L, intraday market P&L and execution cost. This still does not attribute all intraday P&L to skill, and final inventory is still marked rather than liquidated. Studio 4 requires alignment or an explicit holding-policy explanation, plus an executable exit study before an investability claim.

## What public evidence supports

Citadel's Data Strategies Group description includes independently developing hypotheses, evaluating alternative data, finding new questions and sources, and translating work into investment decisions. This supports a stronger emphasis on research ownership and data discovery. It is not evidence that every quant role has identical requirements. [Citadel DSG role](https://www.citadel.com/careers/details/quantitative-researcher-data-strategies-group/).

Jane Street describes work spanning neural-network research, changing distributions, trading feedback, training infrastructure and collaboration among researchers, engineers and traders. This supports teaching serious model work and systems understanding together; it does not make low-latency infrastructure or deep learning mandatory for every horizon. [Jane Street machine learning](https://www.janestreet.com/join-jane-street/machine-learning/).

Two Sigma describes a research process linking hypotheses, datasets, models, experimentation and collaboration. I infer that independent scientific practice is a better organizing principle for this apprenticeship than collecting frameworks or software tools. [Two Sigma careers](https://www.twosigma.com/careers/).

The DatedGPT research paper studies temporally bounded pretraining as a response to financial lookahead risk in language models. Its proposal illustrates why historical model provenance deserves its own investigation; it does not prove that any particular current model is clean. The revised AI evaluation records unknown availability explicitly. [DatedGPT paper](https://arxiv.org/abs/2603.11838).

## What still must be earned

The new code does not create a proprietary dataset, original market insight, independently replicated alpha or a prospective track record. It does not run a live LLM or a broker, and its cost model is stipulated. The experiment book cannot stop someone editing its database, viewing files outside the API or hiding trials. The model comparison uses a selected, already inspected panel. Block intervals are conditional descriptive calculations, not a multiple-testing correction.

These limits are why the professional track asks for independently produced evidence. Its success criterion is the ability to find, test, reject or develop ideas and own their consequences. Completing the supplied examples alone does not establish that ability.
