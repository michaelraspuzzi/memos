# Google, Gemini CLI to Antigravity CLI

**Shut down June 18, 2026.** Apache 2.0 TypeScript in public, to a closed Go binary.

---

## The move

Gemini CLI launched June 2025 as an Apache 2.0 terminal coding agent. In twelve months it took 104,000+ GitHub stars and merged 6,000+ pull requests from outside contributors.

In May 2026, at I/O, Google announced the successor: Antigravity CLI. On June 18, 2026 the original stopped serving requests. The successor's public repository contains a changelog, a readme and a GIF. No application code.

Free tier quotas reportedly fell from roughly 1,000 requests a day to about 20. CI pipelines that had pinned the CLI broke on the shutdown date.

## The insight: the license was never the asset

Every one of those 6,000 pull requests was signed under Google's contributor license agreement. That CLA grants Google a perpetual, worldwide, irrevocable right to use the contribution, including inside a proprietary successor.

So two things were true at once. Apache 2.0 told contributors the code they wrote was theirs to keep. The CLA told Google the work was theirs to move. Both held. No rule was broken.

That is the transferable lesson. If you are building on a vendor's open agent, read the CLA before you read the LICENSE file. The license governs the copy you have. The CLA governs where your work can end up.

## The second insight: forking is legal and useless here

The Apache 2.0 code still exists. Anyone can fork it. It does almost nothing without model access, and model access was never open.

The chokepoint was the API key, not the license text. Open sourcing a client for a closed service buys goodwill, not independence. Check whether the tool needs a vendor-hosted backend to function. If it does, the license is decoration.

## The company

**Who owned the decision.** Not a founding team, a product org. Gemini CLI came out of Google's Gemini and developer relations effort. Antigravity is the consolidation of Google's agentic coding surfaces under one enterprise brand. Two competing CLIs, one free and community-shaped and one monetizable, were never both surviving a year in which every lab was rationalizing inference spend.

**Product.** An agentic coding assistant in the terminal. Read the repo, edit files, run commands, call tools, with Gemini as the model. The open TypeScript codebase was the differentiator against closed competitors. Teams forked it, embedded it in CI, wrote custom tools against it. Antigravity delivers the same capability with none of that.

**Business model.** The CLI was never the product. It was free top of funnel for Google AI Pro and Ultra subscriptions, Gemini Code Assist enterprise seats, and Vertex and API token consumption underneath. Open source lowered adoption friction and outsourced integration work to volunteers. Once the funnel had done its job the free tier became a cost center and was cut by roughly 98 percent. Enterprise access was never part of the consumer shutdown.

**Distribution.** npm install, a repo that ranked in every "best AI CLI" roundup, I/O keynote air cover, and a free quota generous enough to become a habit. Contributors were themselves a channel: every merged pull request pulled a maintainer's employer closer to the tool. That is exactly the asset this transition spent.

## Numbers

| Metric | Value |
| --- | --- |
| GitHub stars at retirement | 104,000+ |
| External merged pull requests | 6,000+ |
| Lifespan | 12 months, June 2025 to June 2026 |
| Free daily quota cut | ~98 percent, roughly 1,000 requests to roughly 20 |
| Application code in successor repo | Zero |

## What it cost

Google gained a single monetizable surface and lost the only thing it could not buy: 6,000 developers who had voluntarily made themselves experts in a Google product.

The cost lands on the next team at Google that asks developers to invest in something open. That ask is now more expensive, and the price does not reset quickly.

## Citations

1. TechTimes, [Google Accepted 6,000 Gemini CLI Contributions, Then Closed Tool for Enterprise Only](https://www.techtimes.com/articles/317056/20260523/google-accepted-6000-gemini-cli-contributions-then-closed-tool-enterprise-only.htm), May 23, 2026. Stars, PR count, CLA terms, quota figures, successor repo contents.
2. TechTimes, [Furious Developers Accuse Google of a Gemini CLI Bait-and-Switch](https://www.techtimes.com/articles/317407/20260529/linux-foundation-tool-spotlighted-furious-developers-accuse-sickening-google-gemini-cli.htm), May 29, 2026. Contributor reaction.
3. The Register, [Bye-bye, Gemini CLI](https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/5243605), May 20, 2026. Announcement and shutdown date.
4. TechTimes, [Gemini CLI Shutdown Takes Effect: CI/CD Pipelines Break](https://www.techtimes.com/articles/318660/20260618/gemini-cli-shutdown-takes-effect-ci-cd-pipelines-break-go-based-antigravity-cli-arrives.htm), June 18, 2026. Breakage on shutdown.

*Compiled August 26, 2026.*
