# tldraw

**Enforcement shipped September 18, 2025.** MIT in v1, source-available in v2, runtime license keys in SDK 4.0.

---

## Why tldraw is not open source anymore

It happened in two moves, twenty-one months apart. The first was legal. The second was technical. The second is the one that hurt.

**Move one: December 20, 2023.** With the v2 beta, tldraw dropped MIT and adopted a license adapted from Scratch's. The company said it plainly:

> "It's not Open Source in the strictest sense of being under a fully permissive license."

The reason was not defensive. It was a business model choice, stated directly:

> "We want to stay focused on the core product rather than on secondary products or services or upsells."

Read that as: no cloud, no hosting tier, no feature ladder. Sell the component. The rest follows from that one sentence.

**Move two: September 18, 2025, SDK 4.0.** tldraw added enforcement.

> "Fate and capital both demand that tldraw be a sustainable project, so these changes are designed to help us commercialize the SDK without cutting off community adoption."

The license now says the SDK is "only permitted to be used in development environments." You may not "use the Software in Production Environments" without a key. You may not "disable, change, or interfere with the Software's License Key enforcement." And the code enforces itself:

> "The Software includes technical measures to verify License Key validity, detect deployment environments, enforce usage restrictions based on license type, and ensure proper watermark display."

**The insight.** For twenty-one months the SDK behaved like open source and was licensed like it was not. Nothing stopped you shipping it. Most people did. 4.0 closed that gap in a single release, which is why it landed as a rug pull even though the legal terms had barely changed. The rug had been gone since 2023. In 2025 people finally looked down.

Note also that v1 is still MIT and still on GitHub. The thing people remember as open source is real. It is just not the thing anyone would build on today.

## The terms

| Tier | Cost | Condition |
| --- | --- | --- |
| Development | Free | Localhost and internal staging only. No key needed. |
| Trial | Free, 100 days | One per commercial entity. Usage analytics collected during trial. |
| Hobby | Free | Non-commercial. Mandatory "made with tldraw" watermark on canvas. |
| Commercial | $6,000 per team per year | Removes the watermark. Startup pricing on request. |

Keys validate client side and work offline.

## The company

**Founder.** Steve Ruiz, London. Incorporated 2022 out of a canvas side project he had been building in public since 2021. Unusually founder-led: the demos, the API design and the public voice are largely one person's. That is why the community read enforcement as a personal reversal rather than a corporate one.

**Product.** An infinite canvas SDK for React. Shapes, selection, camera, collaboration, undo, export. It is the eighteen months of hard canvas engineering nobody wants to rebuild. tldraw.com is the free flagship whiteboard that proves the SDK and feeds it.

**Business model.** Pure component licensing. A 1990s model applied to a React package. No hosting, no metering, no cloud. Gross margin is close to total. The ceiling is the number of teams in the world building canvas apps.

**Distribution.** Viral demos first, npm second. Make Real, which turned a hand sketch into working code, put tldraw in front of the entire AI tooling audience in a week. After that it is word of mouth and logos as distribution: once Shopify and Autodesk ship on your canvas, the next buyer stops evaluating alternatives. The hobby watermark is the marketing budget.

## Numbers

| Metric | Value |
| --- | --- |
| Total raised | $24.1M across four rounds |
| Rounds | $2.7M seed Nov 2022 (Lux). $2M Nov 2023 (Preston-Werner Ventures). $9.4M Apr 2024. $10M Apr 2025 (Lux, Definition) |
| Commercial license | $6,000 per team per year |
| Trial | 100 days |
| Named customers | Shopify, BlackRock, ClickUp, Autodesk, Google, Replit, Runway |
| Investors | Lux Capital, Amplify Partners, Preston-Werner Ventures, Definition |

## What it cost

This is the cleanest of the four closures in this series. tldraw has no hosting margin to hide revenue in, so licensing is the only line available. 4.0 did not change the deal, it started collecting on it.

The exposure is at the bottom of the funnel. A $6,000 floor with a 100-day clock prices out exactly the indie and seed-stage builders who made Make Real go viral in the first place. Enterprise logos survive that. The next generation of advocates may not.

Excalidraw is still MIT, still free to embed commercially, still unencumbered. That is the substitution risk, and it is the only one that matters.

## Citations

1. tldraw, [License updates for the tldraw SDK](https://tldraw.dev/blog/license-update-for-the-tldraw-sdk), December 20, 2023. Primary. Source of the "not Open Source in the strictest sense" and "stay focused on the core product" quotes.
2. tldraw, [Announcing tldraw SDK 4.0](https://tldraw.dev/blog/tldraw-sdk-4-0), September 18, 2025. Primary. Source of the "fate and capital" quote.
3. [tldraw LICENSE.md](https://github.com/tldraw/tldraw/blob/main/LICENSE.md). Primary. Source of the production environment, key enforcement and watermark clauses.
4. tldraw, [License documentation](https://tldraw.dev/community/license) and [License key docs](https://tldraw.dev/sdk-features/license-key). Primary. Tiers and trial terms.
5. [tldraw v1 LICENSE.md](https://github.com/tldraw/tldraw-v1/blob/main/LICENSE.md). MIT.
6. tldraw, [About the company](https://tldraw.dev/company). Named customers.
7. [Crunchbase, tldraw](https://www.crunchbase.com/organization/tldraw). Funding.
8. [BigGo](https://biggo.com/news/202509190115_tldraw_SDK_4.0_Licensing_Debate), [AlternativeTo](https://alternativeto.net/news/2025/9/tldraw-sdk-4-0-adds-five-new-starter-kits-cli-tool-and-enforces-licensing-changes/). Pricing debate and reaction.

*Compiled August 26, 2026.*
