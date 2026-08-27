# Cal.com: the open-source advantage was spent before the code closed

**In 2021, Peer Richelsen searched for “Calendly open source” because Calendly could schedule his own calls but could not disappear inside a hiring marketplace with roughly 5,000 users; the missing result became Cal.com, and Bailey Pumfleet says GitHub then delivered the first 500,000 users without a sales team, outbound sales, or growth marketers. In April 2026 the company moved its production code into a private repository, citing one reason: AI had made public code an increasingly useful attack map for sensitive calendar, healthcare, and deal-flow data. By then the open-source advantage had already been spent; the split was the accounting entry, not the transaction.**

## The position in five facts

- **Customers buy coordination logic, not a calendar link.** Cal.com checks availability across calendar providers and time zones, routes a booking to the right person, writes the event back to connected systems, and triggers reminders, CRM updates, payments, or follow-ups. Current annual pricing is free for one individual, $12 per user per month for Teams, $28 for Organizations, and custom for Enterprise.
- **Two buying motions proved different value.** Cal.com says more than 1,200 Deel employees use it across sales, support, and customer success, with a 15% increase in sales close rates. Retell AI embedded Cal.com into voice agents handling more than ten million calls per month and says the integration saves each customer more than two development days. These are vendor-published, unaudited claims.
- **Open source did its work early.** It differentiated Cal.com from Calendly, let marketplaces change the workflow, gave security-conscious buyers deployment control, and turned users into contributors and hires. That momentum raised $32.4 million—a $7.4 million seed in late 2021 and a $25 million Series A in 2022—and grew the repository from about 6,200 GitHub stars at launch to 47,949 by August 2026.
- **The commercial engine left the repository before the license did.** Paid features had diverged from the public core, a sales organization was being built, white-label Platform closed to new customers in January 2026, and commits from Cal.com’s own engineers to the public repository collapsed in March—six weeks before the announcement.
- **Outside contribution was real but modest.** Of the 1,318 public commits in the four months before the split, at most 261—about 20%—came from authors with no visible Cal.com affiliation, across 91 accounts with a median of one commit. After it, external commits fell to 59 from 39 accounts. Current ARR, retention, enterprise win rate, security incidents, and self-hosted-to-paid conversion remain private.

## Cal.com sells the rules around a meeting

The visible product resembles Calendly: a person connects calendars, declares availability, publishes a booking page, and lets another person choose an open time. The economic product begins when a meeting belongs to a system rather than one person.

A sales organization must qualify a lead, read account ownership from Salesforce, select a rep under territory and fairness rules, write the meeting back to the CRM, and trigger follow-ups. A healthcare operator must respect provider geography and privacy. A marketplace must coordinate thousands of users without buying a seat for every participant. These flows cross identities, calendars, time zones, and external applications; failure can lose a lead, deny care, or expose data.

Cal.com replaces that integration and operating burden. Individuals get a free hosted scheduler; Teams pay for shared availability, round robin, routing, and analytics; Organizations add sub-teams, SAML, SCIM, roles, and compliance. Recurring per-user revenue pays Cal.com to operate calendar-provider behavior, identity, routing, data controls, and uptime. That hosted burden is the tollbooth, and it is where the paid surface accumulated.

## Open source got Cal.com into a settled category

Open source began as a product requirement. At Lean Hire, per-seat software did not fit a marketplace whose users booked one another, and pasted Calendly links hid bookings, cancellations, and reschedules from the marketplace. Richelsen needed scheduling he could place inside the product, observe, and change. The public application then did five jobs at once: it made an embeddable, self-hostable product possible; it gave “open-source Calendly alternative” buyers a sharp reason to switch; it compressed diligence, because engineers could inspect the application and regulated operators could self-host before a sales call; it acquired users through GitHub, Product Hunt, and developer search; and it recruited—the core team grew from two to 12 around launch, with many hires drawn from the 76 contributors counted at seed.

Deel and Retell AI show the two motions that adoption produced. Deel buys coordination inside a large organization: routing across sales, support, and customer success, with a claimed lift in close rates. Retell buys infrastructure inside another product: its voice agents inspect availability and manage appointments through Cal.com’s APIs. Consistent revenue operations in the first case, avoided engineering in the second.

Calendly remains the closest comparison because the products now overlap across individual links, round robin, lead routing, CRM integration, SSO, administration, and analytics. Calendly has added a write-capable Scheduling API, enterprise routing, MCP access, an email assistant, a voice-agent booking interface, payments, and meeting automation—plus the stronger brand, a mature sales organization, and a larger installed base.

| Dimension | Cal.com | Calendly | Where the contest now stands |
| --- | --- | --- | --- |
| Annual list price | Free individual; Teams $12/user/month; Organizations $28/user/month; Enterprise custom | Free; Standard $10/seat/month; Teams $16/seat/month; Enterprise starts at $15,000/year for 50 seats | Price alone creates no durable wedge; both package by team and enterprise value. |
| Enterprise product | Routing, workflows, Salesforce, SAML/SCIM, audit logs, analytics, APIs | Routing, managed event types, Salesforce and marketing automation, SAML, domain control, audit logs, implementation support | Feature-by-feature contest on workflow depth, reliability, implementation, and support. |
| Developer control | API v2, embeds, Cal Atoms, unified calendar API, Cal.diy self-hosting | Scheduling API, embeds, webhooks, MCP and integrations | Cal.com keeps a composability edge, but production code is no longer part of the proof. |
| Deployment | Hosted cloud; invitation-only on-prem enterprise; Cal.diy for individuals | Hosted cloud only | Cal.com retains the only self-hosting path in the category, now gated behind sales. |

## The advantage was spent before April 2026

Read the record chronologically and April 14 stops looking like a hinge.

The 2023 Series A memo already identified the limit: acquiring free and self-hosted users was easier than converting them. The company tried consumer SaaS, enterprise contracts, and usage-priced infrastructure under a “Stripe for time” thesis, and the paid surface settled where recurring operational risk lived—organizations, permissions, routing, workflows, analytics, compliance, and support—in code that steadily diverged from the public repository. After the first 500,000 users, Pumfleet began building a go-to-market organization. In January 2026, Cal.com stopped accepting new customers for its fully white-label Platform offer in favor of branded “Continue with Cal.com” OAuth partnerships. Managed enterprise workflow had become the offer.

The commit record makes the sequence visible. Commits to the public repository from Cal.com-affiliated authors ran between 201 and 508 per month from October 2025 through February 2026, then fell to 40 in March. The last public release, v6.2, shipped March 1. Production development had already moved; the April announcement told everyone where it had gone.

By early 2026, each of open source’s original jobs was finished or transferred. Differentiation had been banked as a brand. Distribution had delivered its users and its funding. Contributors had been hired. The embeddable product survived as APIs and Atoms. What remained public was a repository whose development was four-fifths Cal.com payroll. Closure recorded a change that was already two years old, and committed the company to it: enterprise selling and private execution now have to replace what openness still supplied.

## Security supplied the motive; divergence made it cheap

The April 14 announcement gives “one simple reason”: AI can inspect public code for vulnerabilities faster and more cheaply than human attackers could. Pumfleet pointed to healthcare appointments and market-moving deal flow; the application crosses identity, OAuth, billing, credentials, and integrations, and public advisories included critical authentication bypasses in December 2025 and January 2026. There is no second official reason. Pumfleet says Cal.com was profitable, had grown roughly 300% a year, and could have kept making money while open; in a documentary about the decision he rejected forcing payment or preventing free access as motives. Those are company claims, but the available record does not support presenting monetization failure as a disclosed cause.

Both of Cal.com’s claims can be true at once. Security supplied the motive; divergence supplied the low cost. Privatizing a codebase whose commercial features already lived apart—and whose public development was mostly your own payroll—costs little. The same decision in 2023, when the shared repository was the product, the sales proof, and the hiring funnel at once, would have been expensive. The closure is an economic event whatever motivated it.

Private code buys defenders time; it cannot establish security. Public endpoints expose behavior, dependencies disclose vulnerabilities, and Cal.diy still needs patches. The test is whether serious findings, exploit dwell time, and remediation time fall. Discourse chose the opposite answer two days later—staying GPL and using models defensively to find vulnerabilities—but the comparison has limits: a forum platform and a system holding OAuth tokens, calendar contents, payments, and healthcare appointments carry different breach consequences, and Discourse’s path requires mature response and rapid public patching that not every team can fund.

## The MIT relicense says what Cal.com thinks the community edition is worth

On April 15, Cal.com renamed the public monorepo `calcom/cal.diy`, moved production development private, and changed the public license from AGPL 3.0 to MIT. The removed surface maps exactly onto the paid boundary:

| Removed from Cal.diy | Economic role in Cal.com |
| --- | --- |
| Organizations, teams, permissions, and team booking | Creates the per-user collaboration product |
| Routing forms, Salesforce routing, and traces | Connects scheduling to revenue operations |
| Workflows, reminders, triggers, and follow-ups | Automates recurring operational work |
| SAML/SSO, audit logs, analytics, impersonation | Satisfies administration, security, and compliance buyers |
| Instant booking, AI phone, segments, enterprise UI | Expands differentiated application scope |

The license change is the most revealing detail. AGPL is defensive copyleft: its purpose is to stop a competitor from running your code as a service without sharing changes back. Moving Cal.diy to MIT removes that protection entirely—anyone may now take the community edition, close it, and sell it as a hosted product. A company only makes that trade when it no longer believes the public code is competitively dangerous. Stripped of teams, routing, and enterprise administration, Cal.diy is, by Cal.com’s legal judgment, strategically inert: a free individual scheduler maintained by former interns, with a README stating that contributions do not flow into production.

## What the community was measurably worth in 2026

The widely quoted statistic—public commits fell from 1,318 in the four months before the split to 107 in the four months after—mostly measures organizational separation, because the pre-split repository was where Cal.com’s engineers worked. Classifying authors by GitHub profile affiliation, organization membership, and commit email separates the two populations:

![Monthly commits to Cal.com's public repository by author affiliation, October 2025 through August 2026](assets/cal-com/public-repo-commits.svg)
*Commits from Cal.com-affiliated authors collapsed in March 2026, before the announcement; external contributions declined after the split. Authors with no visible Cal.com affiliation are counted as external, so external figures are upper bounds. Counts include merge commits and exclude bots; August runs through August 26. Source: GitHub REST API.*

Employees and affiliates produced 1,023 of the pre-split commits from 23 accounts; external authors produced at most 261 from 91 accounts, 58 of which made exactly one commit. Post-split, external work ran roughly 15 commits per month against 65 before.

Two conclusions follow. The community Cal.com gave up was a long tail of one-off fixes around perhaps a dozen recurring contributors; its greater value was the funnel behind it—contributors who became employees, and inspection that became enterprise trust. And the loss is genuine: external contribution fell by roughly three-quarters once outside work could no longer reach production. By 2026 the community was worth less than in 2022, and Cal.com priced that in before closing.

## The enterprise wedge survives, but only by invitation

The sharpest question the closure raises is whether Cal.com kept its structural differentiator. Self-hosting was the wedge against Calendly for regulated and privacy-sensitive buyers, and Cal.diy cannot supply it: Teams, Organizations, SAML, SCIM, and audit logs are gone from the public code.

It survives in a narrower form. Cal.diy’s README directs commercial buyers to the hosted product “or get invited to on-prem enterprise access” through sales. An enterprise can still run the full Cal.com product on its own infrastructure under a commercial arrangement—something Calendly does not offer at any price. What died is the self-serve path: a hospital’s engineers can no longer clone the production application, audit it, and pilot a deployment before talking to a salesperson. The deployment control that procurement contracts for remains; the cheap diligence that openness provided is gone. Cal.com kept its differentiator but made it sales-mediated, at the moment it must fund a sales motion for the first time.

## Agents add a channel; enterprise workflow remains the product

Cal.com serves agents in two senses: a person can ask a Cal.com agent in Slack, Telegram, email, or a terminal to find, book, or move time, and a developer can give an external agent those actions through API v2, the CLI, a hosted MCP server, and published skills. Cal.com supplies the hard layer beneath the conversation—authenticated calendars, availability, routing, permissions, and reversible writes—and agent-mediated discovery could partially replace the developer distribution GitHub once provided. But Calendly also offers MCP, email assistance, and voice-agent booking, so Cal.com must win on finer permissions, deeper routing, and more reliable writes.

The release record since April—commercial versions 6.4 through 6.8—does not show an agent company. Most work strengthens enterprise coordination (Salesforce routing and traces, SCIM, audit logs, analytics) or expands the meeting lifecycle (Notes, Cal Pay, ticketed events, workflows). The coherent strategy is a scheduling operating system reached through a page, embed, API, or agent; the risk is product sprawl.

## Three outcomes

Cal.com claims more than one million verified users and 20 million bookings but has disclosed no current ARR, retention, win rate, or incident data, so the closure’s verdict sits in one of three futures:

- **Enterprise workflow wins.** Routing, compliance, administration, and support raise contract value and retention, and the new sales team replaces organic acquisition at acceptable cost. Watch enterprise win rate against Calendly, sales cycle, retention, and acquisition cost by source.
- **An agent and developer flywheel emerges.** API-, MCP-, and agent-created bookings grow and send teams into the managed product. Watch successful agent writes, API-created booking share, and paid conversion from developer channels.
- **The surfaces fragment.** Cal.diy becomes a museum, agent interfaces remain demos, adjacent products dilute the roadmap, and Cal.com pays to acquire demand open source once delivered. Watch Cal.diy active installs and releases, free-to-team expansion, and whether marketing spend replaces inbound.

Until those move, rapid private shipping proves nothing about the business.

## What to take from Cal.com

Open source is a depreciating asset with a schedule you can read. Use it when a customer constraint requires source access or deployment control—write that constraint down and count the buyers who cannot adopt without it, as Lean Hire’s marketplace could not. While the community works, measure what it is worth each quarter: external commit share, contributor-to-hire rate, repo-to-revenue conversion. When the commercial product outgrows the public code, decide deliberately between funding one shared core and operating two real products, before payroll gravity decides by drift. If security is the stated reason, publish the metric secrecy must improve: critical findings, exploit dwell time, patch latency. Cal.com closed its code only after the code had stopped carrying the business; the timing is the lesson.

## Sources and research notes

1. Cal.com, [why the company was built open source](https://cal.com/blog/open-source), 2022; [v1 and rebrand](https://cal.com/blog/calendso-rebrands-to-cal-com); and [v2](https://cal.com/blog/cal-v-2-0). Primary sources for the Lean Hire problem, initial open-source rationale, and early team/community figures. Dates on migrated legacy posts are inconsistent; the memo uses the product chronology described in the posts and dated funding releases.
2. Cal.com, [$7.4 million seed announcement](https://cal.com/blog/seed) and [$25 million Series A and v1.5](https://cal.com/blog/cal-v-1-5). Primary sources for the $32.4 million total raised and the App Store/API funding thesis.
3. Cal.com, [Series A memo](https://cal.com/blog/series-a-memo), Apr. 2023. Primary source for the three original monetization motions, acquisition/conversion framing, and “Stripe for time” strategy. Pipeline and virality figures in the memo were forward-looking company claims, not realized results.
4. Cal.com, [current pricing](https://cal.com/pricing), and Calendly, [current pricing](https://calendly.com/pricing), checked Aug. 27, 2026. Primary sources for annual list prices and plan boundaries. Enterprise prices are not directly comparable: Calendly publishes a 50-seat starting price while Cal.com quotes Enterprise individually. Calendly’s product line is hosted only; it publishes no self-hosted or on-premises offering.
5. Cal.com customer materials: [Deel smart routing](https://cal.com/smart-routing) and [Retell AI](https://cal.com/blog/how-retell-ai-saved-thousands-of-hours-of-development-time-with-cal-com). Vendor and customer claims; reported outcomes have not been independently audited.
6. Cal.com, [v6.1](https://cal.com/blog/calcom-v6-1), Jan. 2026; and [Platform FAQ](https://cal.com/docs/platform/faq). Primary sources for the move away from full white-label managed users toward branded OAuth partnerships and the Platform plan’s closure to new customers.
7. Cal.com, [closure announcement](https://cal.com/blog/cal-com-goes-closed-source-why), Apr. 14, 2026; [technical split](https://cal.com/blog/cal-diy-open-source-to-closed-source), Apr. 15; [v6.4](https://cal.com/blog/calcom-v6-4); and [Cal.diy README](https://github.com/calcom/cal.diy/blob/main/README.md). Primary sources for the security rationale, removed features, licenses, maintainers, the one-way contribution boundary, and the README’s direction of commercial buyers to hosted Cal.com “or get invited to on-prem enterprise access” via sales—the basis for the enterprise self-hosting conclusion.
8. Bailey Pumfleet, [closure explanation](https://www.linkedin.com/posts/baileypumfleet_open-source-is-dead-thats-not-a-statement-activity-7450177472979058688-yN0l), [decision documentary](https://www.linkedin.com/posts/baileypumfleet_making-time-documentary-ep02-calcoms-decision-activity-7450984760463704064-kUg7), and [Hacker News discussion](https://news.ycombinator.com/item?id=47780712), Apr. 2026. Founder statements for sensitive-data examples, business performance, and the denial that failed monetization or restricting free access caused the closure. Growth and profitability are unaudited company claims.
9. Bailey Pumfleet, [building a go-to-market team after the first 500,000 users](https://www.linkedin.com/posts/baileypumfleet_we-built-calcom-incs-first-500000-users-activity-7367549308738363392-YI06), 2025; and Linux Foundation/Serena Capital, [Open Source Startups in Europe](https://www.linuxfoundation.org/hubfs/Research%20Reports/lfr_serena_capital_report_082225b.pdf?hsLang=en), 2025. Primary founder statement for the no-sales acquisition claim and a research interview for openness as a sales aid in compliance, privacy, and extensibility.
10. GitHub, [Cal.diy security advisories](https://github.com/calcom/cal.diy/security/advisories). Primary repository record for disclosed critical vulnerabilities before the change. An advisory list is not a complete incident history.
11. Discourse, [Discourse is not going closed source](https://blog.discourse.org/2026/04/discourse-is-not-going-closed-source/), Apr. 16, 2026. Primary comparator for the alternative choice to keep an application public and use AI defensively.
12. Cal.com, [Cal.com versus Calendly APIs](https://cal.com/blog/calendly-api-vs-cal-com-api), Aug. 2026; and Calendly, [product announcements](https://calendly.com/blog). Vendor sources for current API, MCP, assistant, voice-agent, automation, and enterprise capabilities. Each company’s competitive framing is treated as marketing, not independent evaluation.
13. Cal.com, [Agents](https://cal.com/agents), [agent documentation](https://cal.com/docs/agents), and [hosted MCP server](https://cal.com/docs/mcp-server). Primary sources for Slack, Telegram, email, CLI, skills, API actions, OAuth, and MCP access.
14. Cal.com, [2026 engineering plan](https://cal.com/blog/engineering-in-2026-and-beyond), [v6.3](https://cal.com/blog/calcom-v6-3), [v6.5](https://cal.com/blog/calcom-v6-5), [v6.6](https://cal.com/blog/calcom-v6-6), [v6.7](https://cal.com/blog/calcom-v6-7), and [v6.8](https://cal.com/blog/calcom-v6-8). Primary sources for the pre-split organization, agent launch, current user and booking claims, and monthly commercial shipping through August.
15. GitHub REST API, [repository](https://api.github.com/repos/calcom/cal.diy), [commit history](https://api.github.com/repos/calcom/cal.diy/commits), and [releases](https://api.github.com/repos/calcom/cal.diy/releases), checked Aug. 27, 2026. Commit counts include merge commits; equal four-month windows are Dec. 14, 2025–Apr. 13, 2026 and Apr. 14–Aug. 13, 2026. Author affiliation was classified as Cal.com-affiliated when a commit author’s GitHub profile declares the calcom organization or Cal.com employment (current or during the window), the account is a public calcom organization member, or commits carry a cal.com or founder-domain email; bot accounts were excluded. Authors with no visible affiliation are counted as external, so external totals are upper bounds—an unlabeled employee or intern would inflate them.
16. Cal.com, [current customer directory](https://cal.com/customers) and [About](https://cal.com/about). Primary sources for company-reported user scale. The figures are not independently audited.

*Compiled and checked August 27, 2026. Cal.com has not disclosed current revenue, ARR, revenue mix, paid customer count, retention, security incident rate, or a post-Series A financing. Third-party estimates were excluded from the argument because they conflict and are not company-confirmed.*
