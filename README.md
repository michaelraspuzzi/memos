# Closing the Source

Four companies stopped being open source between September 2025 and June 2026. These are the memos.

Compiled August 26, 2026.

---

## The memos

| Memo | Closed | The move |
| --- | --- | --- |
| **[Cal.com](memos/cal-com.md)** | Apr 14, 2026 | AGPL 3.0 to proprietary. Public repo renamed `cal.diy`, relicensed MIT, stripped of commercial features. |
| **[tldraw](memos/tldraw.md)** | Sep 18, 2025 | MIT to source-available to runtime license keys. $6,000 per team per year. |
| **[Google, Gemini CLI](memos/gemini-cli.md)** | Jun 18, 2026 | Apache 2.0 with 104K stars and 6,000 outside PRs, replaced by a closed Go binary. |
| **[Meta, Llama](memos/meta-llama.md)** | Apr 8, 2026 | Open weights to a proprietary API-only frontier model. |

Each memo covers the move, the real reason, the founding team, product, business model, distribution, current numbers, and what the closure cost. Every claim is cited.

---

## The pattern

**The stated reason is rarely the operative one.** Cal.com said security. tldraw said sustainability. Google said consolidation. Meta said safety. In all four the operative variable is the same: the cost of giving the artifact away exceeded the distribution value of giving it away. That crossover is predictable. It arrives when the product is good enough that people would pay, and the free channel has already delivered most of the users it will ever deliver.

**The application layer closes. Infrastructure holds.** Nothing in the database or observability tier closed this year. Redis and Elastic went the other way and re-added AGPLv3. Closures cluster where the code is the product and there is no hosting margin underneath it: a canvas SDK, a scheduling app, a CLI, a model. If your business has real cloud gross margin, you do not need to close the source. If it does not, you eventually will.

**The fork is the price, and it usually goes unpaid.** OpenTofu after Terraform, Valkey after Redis, OpenSearch after Elasticsearch. Those only happen when large corporate users are dependent enough to fund a fork. Cal.com and tldraw sit below that threshold, which is exactly why they could close. The absence of a fork is not community approval. It is community indifference plus switching cost.

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
| ClickHouse | Real-time OLAP database | Apache 2.0. Open. |
| Supabase | Postgres application backend | Apache 2.0. Open. |
| n8n | Workflow automation | Fair-code Sustainable Use License. Never OSI approved. |
| Grafana Labs | Observability | AGPLv3 since 2021. Still open source. |
| GitLab | DevSecOps platform | MIT community edition plus proprietary EE. Open core. |
| HashiCorp (IBM) | Terraform, Vault, Consul | BUSL 1.1 since Aug 2023. Unchanged after the $6.4B acquisition. |
| Redis and Elastic | Cache and search | Both re-added AGPLv3. Reversals, not defections. |

Most of the top tier has not closed. RedMonk's March 2026 licensing survey found BUSL and SSPL adoption still does not register at statistically significant levels. These closures are loud, not numerous.

### Checked and not closed, despite rumor

Excalidraw is still MIT. Supabase, ClickHouse and Grafana are unchanged. PostHog remains MIT with a proprietary enterprise directory. Sentry has been on the Functional Source License since 2023 and did not move. n8n has been fair-code since inception, so it never was open source in the OSI sense. Discourse published an explicit ["we are not going closed source"](https://blog.discourse.org/2026/04/discourse-is-not-going-closed-source/) post in April 2026, in direct response to Cal.com.

**Baseline sources:** [RedMonk, The State of Open Source Licensing in 2026](https://redmonk.com/sogrady/2026/03/25/open-source-licensing-2026/) / [TrueUp Open Source Report](https://www.trueup.io/open-source/reports) / [Seedtable](https://seedtable.com/best-open-source-startups) / [Tracxn](https://tracxn.com/d/sectors/open-source/__86qzqopfw3B9E1ADrcSHQNkYs66EJskfaNi6oSJHuM0/companies)

---

## Formats

Each memo exists as Markdown (renders here on GitHub) and as HTML with copy-for-agents and download buttons. If GitHub Pages is enabled on this repo, the HTML index is at `index.html`.

Confidence is high for Cal.com, tldraw and Gemini CLI. Medium for Meta, which is flagged in the memo body.
