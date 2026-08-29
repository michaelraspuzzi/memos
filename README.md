# Closing the Source

Seven memos on open source as a business decision — four companies that closed their code between September 2025 and June 2026, and three that stayed open and are worth more than all four combined — plus ten on credentials and ratings, which are the same problem with a different artifact: who controls the gate, and what the signal is worth once everyone can copy the thing behind it.

**Read on the web: [michaelraspuzzi.github.io/memos](https://michaelraspuzzi.github.io/memos/)**

Compiled August 26, 2026. Ratings memos on chess, tennis and esports added August 29, 2026. Memos on Coursera, Udacity, Michelin stars and rating human performance added August 29, 2026.

---

## Part one: the companies that closed

| Memo | Closed | The move | Read |
| --- | --- | --- | --- |
| **Cal.com** | Apr 14, 2026 | AGPL 3.0 to proprietary. Public repo renamed `cal.diy`, relicensed MIT, stripped of commercial features. | [Markdown](memos/cal-com.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/cal-com.html) |
| **tldraw** | Sep 18, 2025 | MIT to source-available to runtime license keys. Annual, value-based production licensing. | [Markdown](memos/tldraw.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/tldraw.html) |
| **Google, Gemini CLI** | Jun 18, 2026 | Apache 2.0 with 104K stars and 6,000 outside PRs, replaced by a closed Go binary. | [Markdown](memos/gemini-cli.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/gemini-cli.html) |
| **Meta, Llama** | Apr 8, 2026 | Open weights to a proprietary API-only frontier model. | [Markdown](memos/meta-llama.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/meta-llama.html) |

## Part two: the companies that stayed open, and how they make money

| Memo | License | The model | Read |
| --- | --- | --- | --- |
| **ClickHouse** | Apache 2.0 | Give the engine away, sell the operating burden. $250M ARR, $15B valuation. | [Markdown](memos/clickhouse.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/clickhouse.html) |
| **Supabase** | Apache 2.0 | Fully self-hostable, and winning because AI coding tools provision it by default. $10.5B valuation. | [Markdown](memos/supabase.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/supabase.html) |
| **n8n** | Sustainable Use License | Never open source, on purpose, since 2022. No rug to pull. $5.2B valuation. | [Markdown](memos/n8n.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/n8n.html) |

## Part three: credentials, and what a signal is actually worth

| Memo | The question | The finding | Read |
| --- | --- | --- | --- |
| **The bachelor's degree** | Why has a million-credential market not displaced one 800-year-old signal? | The degree sells licensure, not learning. Employers who dropped degree requirements changed fewer than 1 in 700 hires. | [Markdown](memos/bachelors-degree.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/bachelors-degree.html) |
| **Harvard's hybrid master's** | MDE or MS/MBA: Engineering Sciences? | Both cost roughly half a million dollars once forgone salary is counted, and after aid the cheaper-looking one is the more expensive one. | [Markdown](memos/harvard-hybrid-masters.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/harvard-hybrid-masters.html) |
| **Bouldering grades** | Can a community-negotiated rating ever be a measurement? | Only once the rated thing is reproducible. The LED board fixed the artifact; the ratings followed. | [Markdown](memos/bouldering-grades.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/bouldering-grades.html) |
| **Chess ratings** | FIDE owns the only chess number that confers a title. Why is it free? | Because it earns 9% of income from it. FIDE waived €2.2M of rating fees to grow the graph, and sells the licence instead. Chess.com has 600× the users on a rating worth nothing. | [Markdown](memos/chess-elo.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/chess-elo.html) |
| **Tennis rankings** | Why is the ATP ranking worth a five-year Saudi naming deal and the better rating is not? | The ATP ranking scores you zero for not showing up. It is an attendance contract. UTR built the better estimator, lost the official designation in 2023, and now spends $11M a year manufacturing its own matches. | [Markdown](memos/tennis-rankings.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/tennis-rankings.html) |
| **Esports rankings** | What happens when the rules-maker, the rating-keeper and the tournament are one company? | StarCraft II. GSL prize pools fell from $140K a season to a crowdfunded $15K; 402 players earned prize money in 2019 and 30 did in 2025. The only rating still publishing is run by volunteers. | [Markdown](memos/esports-rankings.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/esports-rankings.html) |
| **Coursera** | If you distribute someone else's credential, what do you own? | The traffic. Degrees peaked at 8.3% of revenue at a 100% gross margin, got folded away as a segment in the new CEO's first quarter, and by 2026 Coursera was charging universities a platform fee. | [Markdown](memos/coursera.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/coursera.html) |
| **Udacity** | Can you build a credential employers accept without an accreditor? | No. After twelve years and a sale to Accenture for a reported fraction of the ~$300M raised, the anti-degree company licensed accreditation from a Maltese institution and sells a $3,500 master's. | [Markdown](memos/udacity.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/udacity.html) |
| **Michelin stars** | Who pays for a rating nobody rated can buy, refuse, or appeal? | The territory. Louisiana pays $350,000 a year, Virginia declined at $360,000, and tourism boards nominated the restaurants. In hotels, Michelin now takes the booking too. | [Markdown](memos/michelin-stars.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/michelin-stars.html) |
| **Rating human performance** | What happens to a capability rating when a machine holds a top-200 score? | Codeforces had nothing to refuse. Employers went back to in-person interviews, and the humans who still beat the model get paid ~$95 an hour to train it. | [Markdown](memos/human-performance-ratings.md) / [Web](https://michaelraspuzzi.github.io/memos/memos/human-performance-ratings.html) |

The through-line across the ratings memos: **a score is only a credential if someone who does not need your permission can verify it.** FIDE gives the rating away and sells the title, because the title is the part it can refuse. The ATP sells attendance and calls it merit. Blizzard owns the rules, the rating and the servers, so a StarCraft career converts into nothing the player can carry. In each case the price of the number is set by the door it opens, and the accuracy of the number is set by the density of the match graph — two assets that almost never sit in the same company.

The four memos added on August 29 sharpen the same edge from the supply side. Coursera and Udacity are the two ways to fail at credentials — distribute someone else's and end up owning only the traffic, or issue your own and discover that recognition cannot be manufactured, only rented. Michelin is the one clean solution anybody has found: bill a third party whose interest is that the rating exist and be trusted, never the party being rated. And Codeforces is the new failure mode — a capability rating with nothing attached that it can refuse, saturated by a machine in twenty-four months. Together they give the rule a sharper form: **a rating survives if it certifies membership in a population, and dies if it certifies an ability.**

The through-line with part one: a licence is worth what its issuer can withhold. Open source gives away the artifact and sells the operating burden; a university gives away the lectures and sells admission to practice; a boulder grade is worth nothing until enough people have paid to check it. In all three the asset is the gate, not the thing behind it.

Each memo covers the model, the founding team, the product, distribution, current numbers, and what to take from it. Every claim is cited.

---

## The pattern

**The stated reason is rarely the operative one.** Cal.com said security. tldraw said sustainability. Google said consolidation. Meta said safety. In all four the operative variable is the same: the cost of giving the artifact away exceeded the distribution value of giving it away. That crossover is predictable. It arrives when the product is good enough that people would pay, and the free channel has already delivered most of the users it will ever deliver.

**The real question is whether you have an operating burden to sell.** ClickHouse gives away a petabyte-scale database engine and charges $250M a year for not being paged at 3am. Supabase ships a Docker Compose file that stands up its entire stack and is worth $10.5B. Neither needed a restrictive license, because in both cases the download and the product are different goods. tldraw is a React SDK. Nobody gets paged for a canvas library, so there is nothing to sell but the code, so the license had to do the work. Ask which one you are before you ask what license to use.

**The application layer closes. Infrastructure holds.** Nothing in the database or observability tier closed this year. Redis and Elastic went the other way and re-added AGPLv3. Closures cluster where the code is the product and there is no hosting margin underneath it: a canvas SDK, a scheduling app, a CLI, a model.

**If you will eventually need a restriction, add it on day one.** n8n put its Sustainable Use License in place in March 2022, when the company was small and the reputational cost was cheap. It gave up the words "open source" and kept everything else: 188,000 stars, 1.7 million monthly builders, a $5.2B valuation. Cal.com and tldraw paid the same bill four years later, at a much worse exchange rate.

**The fork is the price, and it usually goes unpaid.** OpenTofu after Terraform, Valkey after Redis, OpenSearch after Elasticsearch. Those only happen when large corporate users are dependent enough to fund a fork. Cal.com and tldraw sit below that threshold, which is exactly why they could close. The absence of a fork is not community approval. It is community indifference plus switching cost.

**A new variable: your buyer may be an agent.** Over 60 percent of new databases on Supabase are now launched by an AI tool rather than a human. When a coding agent picks your default, what wins is being the most legible, most copyable, best documented option available. Closing the source protects nothing there and costs you the channel.

---

## Four questions before you build on someone's open repo

1. **Does the vendor have a hosting margin, or is the code the only asset they can sell?** If the code is the only asset, assume it closes.
2. **Is there a contributor license agreement?** If so, your work can legally become their proprietary product. That is what happened to Gemini CLI's 6,000 contributors.
3. **Does the tool need a vendor-hosted backend to function?** That is the real chokepoint, not the license text. A fork without model access is worthless.
4. **Is the last permissively licensed commit forkable and self-sufficient?** If not, you have a dependency, not an option.

These four would have flagged every closure here in advance.

---

## Baseline: the top open source companies

The 2026 rankings that get cited most (TrueUp's 40 Hottest, Seedtable's 287-company index, Tracxn's sector view) converge on roughly the same ten names. Ranking lists do not track license status, so the third column is the one that matters.

| Company | What it is | License status, Aug 2026 |
| --- | --- | --- |
| Databricks | Lakehouse; Spark, Delta, MLflow | Core Apache 2.0, platform proprietary. Open core. |
| Hugging Face | Model and dataset hub | Apache 2.0 libraries, hosted hub. Open. |
| Mistral AI | Frontier and open-weight models | Apache 2.0 open models plus commercial tier. Open. |
| ClickHouse | Real-time OLAP database | Apache 2.0. Open. [Memo](memos/clickhouse.md) |
| Supabase | Postgres application backend | Apache 2.0. Open. [Memo](memos/supabase.md) |
| n8n | Workflow automation | Fair-code Sustainable Use License. Never OSI approved. [Memo](memos/n8n.md) |
| Grafana Labs | Observability | AGPLv3 since 2021. Still open source. |
| GitLab | DevSecOps platform | MIT community edition plus proprietary EE. Open core. |
| HashiCorp (IBM) | Terraform, Vault, Consul | BUSL 1.1 since Aug 2023. Unchanged after the $6.4B acquisition. |
| Redis and Elastic | Cache and search | Both re-added AGPLv3. Reversals, not defections. |

Most of the top tier has not closed. RedMonk's March 2026 licensing survey found BUSL and SSPL adoption still does not register at statistically significant levels. These closures are loud, not numerous.

### Checked and not closed, despite rumor

Excalidraw is still MIT. PostHog remains MIT with a proprietary enterprise directory. Sentry has been on the Functional Source License since 2023 and did not move. Discourse published an explicit ["we are not going closed source"](https://blog.discourse.org/2026/04/discourse-is-not-going-closed-source/) post in April 2026, in direct response to Cal.com.

**Baseline sources:** [RedMonk, The State of Open Source Licensing in 2026](https://redmonk.com/sogrady/2026/03/25/open-source-licensing-2026/) / [TrueUp Open Source Report](https://www.trueup.io/open-source/reports) / [Seedtable](https://seedtable.com/best-open-source-startups) / [Tracxn](https://tracxn.com/d/sectors/open-source/__86qzqopfw3B9E1ADrcSHQNkYs66EJskfaNi6oSJHuM0/companies)

---

## Formats and build

Every memo exists twice, from one source. The Markdown renders here on GitHub. The HTML is served by GitHub Pages at [michaelraspuzzi.github.io/memos](https://michaelraspuzzi.github.io/memos/), in plain document style, with a **Copy for agents** button and a **Download .md** button at the top of each page.

To change a memo, edit the Markdown in `memos/`, then run `python3 build.py` and push. The HTML is generated, never hand-edited, so the two formats cannot drift.

For new memos and major revisions, use the [Founder Memo skill](.codex/skills/founder-memo/SKILL.md). It defines the narrative standard, research rules, founder-action format, hard quality gates, and 100-point publication rubric.

Confidence is high for Cal.com, tldraw, Gemini CLI, ClickHouse, Supabase and n8n. Medium for Meta, which is flagged in the memo body. Revenue figures sourced from third parties rather than the companies are flagged individually.
