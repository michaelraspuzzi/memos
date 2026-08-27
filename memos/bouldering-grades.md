# A boulder grade is a price, and at the top of the scale half the prices have a sample size of one

**Founder audience: builders of athletic communities, training products and performance data systems. A grade is not a measurement of a rock. It is a price quoted by whoever has climbed the thing, revised by whoever climbs it next, and it carries exactly as much information as the number of independent transactions behind it. That number is usually tiny. The hardest boulder problem in the world, Exodia, was graded 9A+ by one person in November 2025 after more than 200 sessions across four years, and has never been repeated: a global benchmark with a sample size of one.[^8] Climbing spent forty years refining the notation. What actually made grades comparable was not better notation but the LED training board, which standardized the artifact so that the same problem could be attempted in a thousand gyms and the ratings could accumulate. That is the transferable lesson: if your ratings are noisy, fix the thing being rated, not the rating.**

## The position in five facts

- **The scale’s top is almost entirely unverified.** Of roughly fifteen boulders proposed at V17/9A as of late 2025, about seven had been confirmed by a repeat and about eight had not. 2025 was the record year with sixteen V17 ascents in total, worldwide, across all problems.[^1]
- **Verification takes years, and the verifier usually has to rebuild the problem.** *Burden of Dreams*, established by Nalle Hukkataival in October 2016 as the first proposed 9A, went unrepeated until Will Bosi climbed it in April 2023 — six and a half years, fourteen sessions and twenty-four days of work split between the boulder and a **replica** Bosi built to train on.[^2]
- **A single repeat re-prices its neighbours.** After the ascent Bosi observed that if *Burden of Dreams* is solid 9A then *Alphane* is soft 9A. One new observation moved the quoted difficulty of a different problem on another continent.[^2]
- **Where the data is thick enough to model, published grades explain about two-thirds of it.** Fitting a Whole-History Rating model — the method used to rank Go and chess players — to 236,095 logged ascents by 3,000 climbers across 8,917 routes predicted send-or-fail outcomes with about 85% accuracy, but the fitted difficulty ratings correlated with published grades at only R² = 0.640, with substantial overlap between adjacent grades.[^3]
- **The boards solved this by changing the good, not the rating.** On the Aurora LED systems, geometry and hold set are fixed and identical everywhere, every problem is community-graded, the displayed grade is a weighted average of all submitted opinions, the full distribution of opinions is visible, and the grade moves when enough people disagree.[^4] Ratings became useful when the artifact became reproducible.

## What a grade is for

Two notations dominate. The V scale, developed by John Sherman at Hueco Tanks in the 1980s, runs in integers from V0 upward; the Fontainebleau scale, grown out of the forest south of Paris, combines a number with a letter and an optional plus — 6A, 6A+, 6B.[^5][^9] Neither is a unit of anything. Both are labels a local community attaches to a band of expected effort.

The economic function of that label is to allocate attention. A climber has a finite number of sessions and needs to know which problems sit inside a range where effort converts into progress. The grade is the price signal that clears that market: it tells you what a problem will cost you before you spend anything.

Prices work when trades are frequent, observed and comparable. Boulder grades fail all three tests outdoors. A hard problem may see one ascent a decade. The ascent is observed by the ascensionist and perhaps a camera. And no two attempts are comparable, because effective difficulty moves with humidity, skin, temperature, hold wear, height, reach and which sequence the climber found. The UIAA publishes a cross-system comparison table and labels it explicitly approximate; that caveat is not modesty, it is a correct statement about a thin market.[^5]

*Soudain Seul* shows the mechanism plainly. Simon Lorenzi established it in Fontainebleau in 2021 and proposed 9A. Nico Pelorson made the second ascent and proposed 8C+. Camille Coudert made a later ascent and supported 9A. Years on it is still quoted as a slash grade.[^6] Three of the strongest boulderers alive produced a price band, not a price. There is nothing wrong with the climbers or the scale. There are simply not enough transactions.

![Years from first ascent to first independent repeat for three benchmark boulder problems: Burden of Dreams took six and a half years, Soudain Seul was repeated within about two years but downgraded then re-confirmed, and Exodia remains unrepeated since November 2025.](assets/bouldering-grades/price-discovery.svg)
*The interval between a proposed grade and its first independent check is the period during which the number is a single person’s opinion. Roughly eight of fifteen proposed V17s and the sole proposed V18 are currently inside that interval. Sources listed below; V17 counts are from community-maintained lists, not an official register.*

## The measurable part: grades explain about two-thirds of difficulty

Most claims about grade accuracy are anecdotes. One study is not. Dean Scarff applied Whole-History Rating, the Bradley–Terry-based method used to rate game players, to 236,095 ascent records from theCrag covering 8,917 Australian sport routes and 3,000 climbers, treating each attempt as a match between a climber and a route. The model predicted outcomes at roughly 85% accuracy under ten-fold cross-validation. Its fitted difficulty ratings correlated with the published Ewbank grades at R² = 0.640, and adjacent grades overlapped substantially in fitted difficulty.[^3]

Read that carefully, because it cuts both ways. Grades are informative: 85% predictive accuracy from ascent logs alone is high, and the published number carries most of the signal. But roughly a third of the variance in fitted difficulty is not captured by it, and neighbouring grades overlap enough that a single step up the scale is a category, not a unit. That residual third is the product opportunity, and it is large.

Two of the study’s methodological constraints are really product requirements in disguise. Routes needed at least two recorded ascents before the model would move off its prior — no rating without a second observation. And climbers needed both successes *and* failures on record, or reporting bias distorted the fit.[^3] Almost every consumer climbing app logs sends. A product that logs only sends is throwing away the half of the data that makes the estimate unbiased, then wondering why its recommendations are wrong.

## The board fixed the artifact, and the ratings followed

The instructive move in the last decade of climbing was not a new scale. It was the standardized LED board. Fix the panel angle, fix the hold set, fix the coordinates, and a problem set in Seattle is the same problem in Seoul. On the Aurora systems every climb is community-graded, the shown grade is a weighted average of submitted opinions, the distribution of those opinions is visible next to it, and the number moves as votes accumulate.[^4] That is not a better rating algorithm than the guidebook’s. It is the same social process running on an artifact that finally supports repeated, comparable trades.

Bosi’s replica is the same insight arrived at by hand: to check a price, he had to reproduce the good. The boards industrialized that. It also arrived alongside a market big enough to absorb it: the US now has close to 700 commercial climbing gyms generating about $1.1 billion in revenue and growing at roughly 4.7% a year.[^7]

The gym’s own colour circuits are the counter-example worth naming, because founders keep mistaking them for measurement. A commercial gym grades for safety, movement learning, wall turnover and customer experience. One colour may deliberately span several V grades; sets are recalibrated by staff every few weeks. That is inventory management with a difficulty label attached. Publishing a gym colour as a V-grade equivalent, without the gym’s own explicit mapping, converts an operations decision into a false measurement.

## What to build instead of a leaderboard

A product that reduces a climber to their hardest send teaches climbers to avoid slabs, chase soft benchmarks and treat one perfect-conditions day as permanent ability. The alternative is not a more elaborate score. It is keeping the evidence attached to the number.

| Field to store | Why the number is worthless without it |
| --- | --- |
| System, value, modifiers, area, guidebook edition | `V4`, `6A+` and a gym colour are three different objects; a shared integer column silently converts between them |
| Angle, hold type, start position, height | Explains why a grade reads soft or hard for a given body and style |
| Ascent type: flash, send, repeat, ongoing project | Separates route-reading from persistence — different abilities, different training |
| Attempts and sessions, including failures | The only way to get an unbiased difficulty estimate[^3] |
| Conditions and hold state | Effective difficulty moves without the printed grade moving |
| Number of independent ascents and spread of opinion | Distinguishes a priced problem from one person’s guess |

The last row is the one most products omit and the one that carries the most information. A grade with two hundred logged ascents and tight agreement is a price. A grade with one ascent is a quote. Showing both as the same bold number is the core dishonesty of climbing data products, and fixing it costs nothing but a sample-size label.

## Founder playbook

1. **Standardize the artifact before improving the rating.** Ratings converge when the rated thing is reproducible; no amount of statistics rescues a one-of-a-kind object. *Test:* can two users in different cities attempt a provably identical instance of the same problem?
2. **Capture failure, not just success.** Sends-only logging biases every downstream estimate. *Test:* what share of sessions record attempts and non-sends? If it is under half, your difficulty model is fitted on winners.
3. **Ship the denominator with the number.** Display independent ascents and the spread of opinion beside every grade, and mark proposed grades as proposed. *Test:* is there any screen where a grade appears without its sample size?
4. **Never convert silently.** V, Font and gym colours are separate namespaces; the UIAA’s own cross-table is labelled approximate.[^5] *Test:* does any code path write a V-grade into a Font-graded record without a visible approximation flag?
5. **Keep access, landing and safety information out of the score and in first-class fields.** *Test:* can a climber plan a responsible attempt without leaving the product?

The durable rule: **a rating is only as good as the reproducibility of the thing it rates.** Climbing’s scales did not get better; the boulders got copied. Any product that grades performance — athletic, educational or professional — should ask which half of that problem it is actually in, because standardizing the task is usually cheaper than modelling the noise, and it is the only move that makes the ratings accumulate.

## Research notes and sources

[^1]: Community-maintained censuses of V17/9A ascents, including [The Hangboard’s V17 list](https://thehangboard.com/blogs/famous-climbs-around-the-world/v17-9a-boulders) and [Boulderflash](https://boulderflash.com/blog/v17-boulders-and-v18-predictions/), as of late 2025: roughly fifteen proposed V17s, about seven confirmed by repeat, and sixteen V17 ascents recorded in 2025. There is no official register of boulder grades; these lists are compiled from media reports and are approximate. Counts change with each new ascent or downgrade.
[^2]: Lattice Training, [Will Bosi sends *Burden of Dreams* (V17/9A)](https://latticetraining.com/2023/04/19/will-bosi-burden-of-dreams-v17-9a/), and Planetmountain, [Will Bosi repeats *Burden of Dreams* 9A in Finland](https://www.planetmountain.com/en/news/climbing/will-bosi-repeats-burden-of-dreams-9a-in-finland.html), Apr. 2023. Sources for the October 2016 first ascent by Nalle Hukkataival, the April 12, 2023 repeat, fourteen sessions and twenty-four days including replica work, and Bosi’s comparison of *Burden of Dreams* with *Alphane*. Session and day counts are the climber’s own report.
[^3]: Dean Scarff, [*Estimation of Climbing Route Difficulty using Whole-History Rating*](https://ar5iv.labs.arxiv.org/html/2001.05388), arXiv:2001.05388. Primary source for the 236,095 ascents, 3,000 climbers and 8,917 routes drawn from theCrag, the ~85% ten-fold cross-validated prediction accuracy, the R² = 0.640 relationship to published Ewbank grades, the overlap between adjacent grades, and the two-ascent and success-plus-failure requirements. The dataset is Australian outdoor sport climbing, not bouldering; the structural finding about grade variance is applied here by analogy and should be treated as indicative for boulders.
[^4]: Kilter Board, [support and grading documentation](https://kilterboard.io/support). Primary source for community grading, the weighted-average consensus grade, the visible distribution of submitted opinions, and grades that move as opinions accumulate. The page does not state a minimum number of ascents before a grade is treated as established.
[^5]: UIAA, [*The Scales of Difficulty in Climbing*](https://www.theuiaa.org/documents/sport/THE-SCALES-OF-DIFFICULTY-IN-CLIMBING_p1b.pdf). Federation reference for the V and Font systems and the cross-system comparison table, which the UIAA explicitly labels approximate.
[^6]: Planetmountain, [Simon Lorenzi establishes *Soudain Seul* and proposes 9A](https://www.planetmountain.com/en/news/climbing/simon-lorenzi-establishes-soudain-seul-fontainebleau-proposes-9a-boulder.html), and Climbing, [Nico Pelorson makes the second ascent and suggests a downgrade](https://www.climbing.com/news/this-boulder-was-graded-v17-until-it-wasnt/). Sources for the contested grade history and the surviving 8C+/9A slash grade.
[^7]: IBISWorld, [indoor climbing walls industry](https://www.ibisworld.com/united-states/industry/indoor-climbing-walls/4377/), and Climbing Business Journal, [2026 climbing gym market report](https://climbingbusinessjournal.com/building-a-gym-5-insights-from-cbjs-2026-climbing-gym-market-report-and-dashboard/). Sources for approximately 700 US commercial climbing facilities, about $1.1 billion in revenue and roughly 4.7% annual growth. Industry-analyst estimates, not audited figures.
[^8]: Lacrux, [Elias Iagnemma ticks *Exodia*, the world’s first proposed 9A+](https://www.lacrux.com/en/bouldern/The-world's-first-9a--Elias-Iagnemma--ticks-Exodia/), and UKClimbing, [interview with Elias Iagnemma](https://www.ukclimbing.com/articles/features/elias_iagnemma_on_unique_beta_hard_repeats_and_his_9a+_boulder-16756). Sources for the November 2025 first ascent at Rifugio di Barbara, the 200-plus sessions over roughly four years, the proposed 9A+/V18 grade, and its unrepeated status.
[^9]: John Sherman, [*Better Bouldering*](https://www.mountaineersbooks.org/product/9781594851964/), Mountaineers Books. Practitioner reference for the development of the Hueco/V scale in the 1980s.

<footer>Compiled and checked August 27, 2026. Grades change with conditions, access, hold breakage, convention and local consensus, and the V17/V18 counts above will be out of date the next time someone climbs one. Check current local guides and respect area-specific access and safety practices.</footer>
