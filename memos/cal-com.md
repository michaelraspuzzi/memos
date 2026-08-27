# Cal.com

**Closed April 14, 2026.** AGPL 3.0 public monorepo to a proprietary private repo. The old repo was renamed `calcom/cal.diy` and relicensed to MIT.

---

## The move

Cal.com spent five years in public. On April 14, 2026 it moved production code into a private repository under a proprietary license.

The public repo did not disappear. It was renamed `calcom/cal.diy` and relicensed from AGPL 3.0 to MIT. That reads like a loosening. It is not. cal.diy keeps the scheduling engine, the app store framework and the booking infrastructure. It drops the commercial features. MIT is cheap to give away once the valuable code is gone.

Two details tell you how much moved. The private repo carries 62 CI workflows; cal.diy carries 53. And cal.diy is now maintained by former interns.

## The stated reason

Security. The argument is that AI can scan a public codebase for exploitable bugs faster than volunteers can patch them. Cal.com cites AI surfacing a 27-year-old BSD kernel vulnerability with working exploits in hours.

> "Open source security always relied on people to find and fix any problems. Now AI attackers are flouting that transparency."
> *Peer Richelsen, co-founder*

> "Open source code is basically like handing out the blueprint to a bank vault. And now there are 100 times more hackers studying the blueprint."
> *Bailey Pumfleet, co-founder*

The company says it hopes to reopen when the threat landscape changes.

## The real reason

Open source was Cal.com's acquisition channel, not its moat. By 2026 the channel had done its job: 32,000+ stars and the top result for "open source Calendly alternative." What it had not done was convert at the scale a $150M valuation implies. Reported ARR was $5.1M in 2024. No Series B has been announced.

The security argument is real but not load bearing. If AI-assisted attackers were the binding constraint, the fix is audits, bounties and a hardened release process, not a private repo. A private repo protects something else: the platform line, where other companies embed Cal's scheduling through an API and pay on usage. That is the only revenue line where owning the code is worth more than distributing it.

## The company

**Founders.** Peer Richelsen and Bailey Pumfleet, co-CEOs. Founded 2020 to 2021 as Calendso. Distribution-native founders: growth came from their own posting cadence plus the repo, not a sales org. Both were the public face of the license decision, which is why the backlash landed on them personally.

**Product.** Scheduling as infrastructure. The visible surface is a Calendly equivalent: booking pages, calendar sync, routing forms, round robin, an app store. The strategic surface is the platform layer, meaning APIs and embeddable components that let other companies ship scheduling without building it.

**Business model.** Four lines. Open core with AGPL self-hosting free. Cloud SaaS per seat, the volume line. Enterprise licenses for self-hosters who cannot accept AGPL. Platform and API deals billed on usage, the highest-leverage line and the one that rewards closing the code.

**Distribution.** The repo was the funnel. Stars and search intent brought developers in, self-hosting converted the serious ones. Behind that: founder-led social, an app store that borrowed distribution from Zoom, Stripe and Google, and infrastructure deals that rent a partner's user base. Closing the repo weakens every one of those except the last.

## Numbers

| Metric | Value |
| --- | --- |
| Total raised | $32.4M across two rounds |
| Rounds | $7.4M seed, Dec 2021. $25M Series A, Apr 2022, led by 776 with Obvious Ventures and OSS Capital |
| Valuation | $150M at the 2022 Series A |
| ARR | $5.1M reported for 2024, up from $1.6M in 2023 |
| GitHub stars | 32,000+ at closure |
| CI workflows | 53 in cal.diy vs 62 in the private repo |
| Series B | None announced as of August 2026 |

> **Confidence note.** The ARR figure is third party (Latka), two years old, and unconfirmed by the company. Treat the current run rate as unknown.

## What it cost

Cal.com traded its cheapest acquisition channel for defensibility on the platform line. That trade pays only if API and embed revenue is already most of the pipeline. If seat revenue still carries the company, they raised the cost of acquiring customers without improving the product.

Two things to watch. Whether cal.diy stays genuinely maintained, because handing it to former interns is not a durable commitment. And whether a credible AGPL fork of the last open commit appears. A fork is the real price of this decision, and nobody has paid it yet.

## Citations

1. Cal.com, [Cal.com Goes Closed Source: Why AI Security Is Forcing Our Decision](https://cal.com/blog/cal-com-goes-closed-source-why), April 14, 2026. Primary.
2. Cal.com, [Going Closed Source: Technical Changes Behind Cal.diy](https://cal.com/blog/cal-diy-open-source-to-closed-source). Primary.
3. [The New Stack](https://thenewstack.io/cal-com-codebase-security-ai/), [It's FOSS](https://itsfoss.com/news/cal-com-goes-proprietary/), [FOSS Force](https://fossforce.com/2026/04/ai-pushes-cal-com-to-shutter-open-and-go-nonfree/), [Slashdot](https://yro.slashdot.org/story/26/04/15/1913213/calcom-is-going-closed-source-because-of-ai), [AlternativeTo](https://alternativeto.net/news/2026/4/cal-com-is-going-closed-source-with-a-major-shift-in-its-license-strategy/). Founder quotes and reaction.
4. [Crunchbase, Cal.com (Calendso)](https://www.crunchbase.com/organization/calendso). Funding.
5. [Latka, Cal.com](https://getlatka.com/companies/calcom). Revenue and valuation.
6. [GitHub, calcom/cal.diy](https://github.com/calcom/cal.diy).

*Compiled August 26, 2026.*
