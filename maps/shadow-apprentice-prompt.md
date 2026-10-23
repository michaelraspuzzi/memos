# The Shadow Apprentice Map prompt

The exact prompts used to build the [Shadow Apprentice Map](https://michaelraspuzzi.github.io/memos/maps/applied-ai-apprentice-map.html) for Anthropic's Applied AI Associate role, with the person's name swapped for a placeholder and typos fixed. Write-up: [Stop Applying, Start Apprenticing](https://michaelsmemos.substack.com/).

## Step 1: give the agent the raw material

```
Transcribe this job description as a markdown file in this folder.
[paste the job description]
```

```
Make a markdown file about [name].
[paste their LinkedIn profile, portfolio link or writing]
```

## Step 2: the map

```
Now, given the role, and given [name] is interested in [their focus], help me make a "shadow apprentice map."

Level 1: fundamentals they should know, from technical (the SDK, the API) to foundational (AI ethics, going through the company's constitution or values).
Level 2: initial projects to work on and ship, and why.
Level 3: one robust project that gets real user feedback.
Level 4: a product that could be a startup.
Level 5: an agent that could win a Nobel Prize.

The goal is that each branch has things relevant to the role, relevant to the company, and relevant to [name].

If you need to, do deep research on the company and its work so you have it as reference files. This should be legit: help them speedrun the role in 24 hours, with great projects to demo and show.

Visual notes:
- Make it an interactive HTML page.
- Put levels across and tracks down (x and y), so each skill is its own card.
- Make the cards toggleable, one open at a time.
- Include citations I can click to check.
- Light mode only.
- Replace the person's real name with a made-up one.
```

## What it set off

Four research agents in parallel (the company's mission and constitution, its developer docs, its science work, and the person's public work): 134 tool calls, about 562,000 tokens, under five minutes. They produced 12,883 words of reference notes, which became 30 cards citing 83 sources.
