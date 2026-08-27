# ClickHouse

**Still open. Apache 2.0, no restrictions.** $250M ARR, $15B valuation, and not one line of the license touched.

---

## The model in one line

Give the engine away under the most permissive license available, then sell the thing that is hard to operate.

## How it makes money

ClickHouse Cloud, priced on consumption. You pay for compute units actually used and storage held, not for seats and not for a subscription tier that ignores your workload. Tiers are Basic, Scale and Enterprise. There is a second line in managed connectors (ClickPipes, for Kafka, S3 and similar), which is the same idea applied to the plumbing around the database.

The open source database has no commercial restriction on it at all. You can run it, resell it, build a competing managed service on it. Apache 2.0 means Apache 2.0.

## Why it can afford to stay open

Because the download and the product are different goods.

ClickHouse gives away the hardest engineering in the company, the columnar engine, and keeps the business anyway. That works because the engine is not where the cost sits. Running it is. Operating a petabyte-scale analytics database means capacity planning, replication, upgrades, backups, tiered storage and being paged at 3am. A team can have the binary for free and still rationally pay to never touch any of that.

That gap is the entire business. It is also the test for whether you need to close your source. tldraw is a React SDK. Nobody gets paged for a canvas library, so there is no operational gap, so there is nothing to sell but the code itself. ClickHouse has a gap measured in headcount. The license never had to do the work.

Second thing worth noticing: ClickHouse did not have to build its community. The project started inside Yandex in 2016 and was already widely used before the company existed. The company was formed in 2021 around adoption that had already happened. Buying that distribution afterward would have cost more than the Series D.

## The company

**Founders.** Alexey Milovidov, who wrote ClickHouse at Yandex and is CTO. Aaron Katz, CEO, from Elastic. Yury Izrailevsky, president of product and technology, from Netflix. Incorporated 2021, five years after the code.

**Product.** A real-time OLAP database. Analytical queries over very large tables, returned fast enough to sit behind an interactive dashboard. The 2026 expansion is into observability and AI workloads, bought rather than built: HyperDX, Langfuse and LibreChat were all acquired.

**Distribution.** Benchmarks and word of mouth among data engineers, an Apache 2.0 repo anyone can adopt without a procurement conversation, then land and expand. Developers start free, hit the operational wall, move the workload to Cloud. The named customer list is its own channel: Anthropic, Tesla, OpenAI, Meta, Mercado Libre.

## Numbers

| Metric | Value |
| --- | --- |
| ARR | $250M annualized as of May 2026, roughly tripled year over year. Third-party estimate of $350M by August 2026 |
| Valuation | $15B, Series D, January 2026 |
| Latest round | $400M led by Dragoneer, with Bessemer, GIC, Index, Khosla, Lightspeed, T. Rowe Price, WCM |
| Total raised | Over $1B |
| Customers | 4,000 as of May 2026, up from 3,000 in January |
| Named customers | Anthropic, Tesla, OpenAI, Meta, Mercado Libre |
| License | Apache 2.0, unchanged |
| Next step | Targeting an IPO within a few years |

> **Confidence note.** The $250M figure is company-reported via TechCrunch and dated May 2026. The $350M August figure is a Sacra estimate, not company-confirmed. Treat the trajectory as solid and the current exact number as approximate.

## What to take from it

If your product has a real operating burden, open source is free distribution with no downside. Publish everything. The people who will self-host were never going to pay you, and the people who will pay you are buying relief from work, not access to code.

Ask honestly which one you are. Most application-layer companies want ClickHouse's outcome and have tldraw's cost structure.

## Citations

1. TechCrunch, [ClickHouse triples annualized revenue to $250M, charting a path toward an IPO](https://techcrunch.com/2026/05/27/clickhouse-triples-annualized-revenue-to-250m-charting-a-path-toward-an-ipo/), May 27, 2026. ARR, customer count, IPO intent.
2. Bloomberg, [ClickHouse Lands $15 Billion Valuation in AI Database Race](https://www.bloomberg.com/news/articles/2026-01-16/clickhouse-lands-15-billion-valuation-in-ai-database-race), January 16, 2026.
3. [ClickHouse secures $400m in Series D led by Dragoneer](https://finance.yahoo.com/news/clickhouse-secures-400m-series-d-123835366.html). Round composition.
4. [Sacra, ClickHouse](https://sacra.com/c/clickhouse/). Pricing mechanics, revenue estimates, named customers, acquisitions.
5. [ClickHouse on GitHub](https://github.com/ClickHouse/ClickHouse). Apache 2.0.

*Compiled August 26, 2026.*
