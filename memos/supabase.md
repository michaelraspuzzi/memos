# Supabase

**Still open. Apache 2.0, fully self-hostable.** $10.5B valuation, and the distribution channel is now AI agents, not developers.

---

## The model in one line

Give away a backend anyone can self-host, then win because being the default thing an AI coding tool provisions is worth more than being the only thing you can buy.

## How it makes money

Hosted Postgres, sold as a subscription with metered overage. Free at $0, Pro at $25, Team at $599 per organization, Enterprise negotiated. You pay a fixed monthly fee, then meter on compute, storage and egress once you cross the included quota.

The free tier is deliberately shaped, not just small: two active projects, 500 MB of database storage, and projects pause after seven days of inactivity. That last rule is the real conversion mechanism. It is fine for learning and impossible for production.

## Why it can afford to stay open

Two reasons, and the second one is new.

**First, the same operational gap as ClickHouse.** The whole stack self-hosts through a Docker Compose file, and Apache 2.0 permits commercial use with no restriction. It is genuinely allowed. It is also genuinely worse: you inherit backups, connection pooling, upgrades, replication and PITR. The license is not what stops people. The work is.

**Second, and more interesting: the buyer changed.** Database launches on Supabase grew more than 600 percent in the year to June 2026, and over 60 percent of new databases were launched by an AI tool rather than a human. Bolt, Lovable, Cursor, Claude Code and Codex reach for Supabase automatically when a generated app needs a backend.

That flips what the source code is for. When your acquisition channel is a coding agent choosing a default, what protects you is being the easiest thing to wire up correctly on the first try: clean docs, a predictable API, a client library in the model's training data, provisioning that works without a human. Closing the source would do nothing for any of that. Being maximally open, documented and copyable is the moat, because those are the exact properties that make an agent pick you.

Cal.com closed its repo to protect an embed business. Supabase kept its repo open and got embedded by every code generator on the market.

## The company

**Founders.** Paul Copplestone, CEO, and Ant Wilson, CTO. Founded 2020, Y Combinator S20. Distributed from the start.

**Product.** A Postgres development platform. You get a real Postgres database, plus the pieces every app needs anyway: auth, row-level security, object storage, realtime subscriptions, edge functions and an auto-generated API. The positioning was "open source Firebase alternative," which meant the migration path off it was always visible. That was the point.

**Distribution.** Three layers, each larger than the last. Developer word of mouth and a very large GitHub presence. Then a free tier generous enough to build a real prototype on. Then, from 2025, AI code generators provisioning it by default. The third layer is the one that produced the current numbers.

## Numbers

| Metric | Value |
| --- | --- |
| Valuation | $10.5B post-money, Series F, June 2026 |
| Latest round | $500M led by GIC. Stripe invested a second time, Salesforce Ventures joined new |
| Prior round | $100M Series E, October 2025, at $5B, co-led by Accel and Peak XV |
| ARR | ~$170M estimated for 2026, up from ~$70M mid-2025 and ~$30M at end of 2024 |
| Developers | 4M+ |
| Customers | 100,000+ |
| Growth signal | Database launches up 600%+ year over year, 60%+ launched by an AI tool |
| License | Apache 2.0, unchanged |

> **Confidence note.** The ARR figure is a third-party estimate (Latka). The valuation, round composition and growth percentages are company-announced.

## What to take from it

The question is no longer only "can a cloud vendor strip-mine my code." It is "what makes a coding agent choose me by default." Those two questions push in opposite directions. The first argues for restriction. The second argues for the most permissive, most legible, most copyable thing you can ship.

If your users are increasingly agents acting for humans, the second question is the one that pays. Supabase's revenue roughly doubled in twelve months without changing a word of its license.

## Citations

1. Supabase, [Series E announcement](https://supabase.com/blog/supabase-series-e). Primary.
2. [Supabase Raises $500M at $10.5B to Accelerate Lead in Agentic Infrastructure](https://www.prnewswire.com/news-releases/supabase-raises-500m-at-10-5b-to-accelerate-lead-in-agentic-infrastructure-302791787.html), June 2026. Round composition.
3. TechCrunch, [Supabase doubles valuation to $10B in 8 months](https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/), June 5, 2026. Growth figures, AI-tool share of launches.
4. CNBC, [Vibe-coding phenomenon lifts Supabase to $10.5 billion valuation](https://www.cnbc.com/2026/06/04/database-startup-supabase-raises-500-million-10point5-billion-valuation.html), June 4, 2026.
5. [Latka, Supabase](https://getlatka.com/companies/supabase.com). Revenue estimate.
6. [Sacra, Supabase](https://sacra.com/c/supabase/). Business model and pricing mechanics.
7. [supabase/supabase on GitHub](https://github.com/supabase/supabase). Apache 2.0 and the self-host path.

*Compiled August 26, 2026.*
