# Slugs: How to serve two audiences

I was scrolling through Ghost's changelog on Wednesday when my brain did a double take. The CMS I've been using for Magenta Debrief — the same platform that first shipped proper SEO tools built into the editor — just shipped GEO as a toggle. Generative Engine Optimization, built in, opt-in, served as Markdown files at `llms.txt` and `llms-full.txt`. The same John O'Nolan who wrote that iconic essay about open source software as the model for publishing just made his peace with the machine reader.

**The two-audience CMS**

For 20 years, content management systems optimized for one audience: the human with a browser. Sitemaps, meta descriptions, Open Graph tags, structured data — all of it was about helping Google's crawler index your site so humans could find you. The machine was a middleman, not a customer.

Ghost just killed that assumption. It now generates a content layer designed to be consumed by LLMs directly — no browser, no JavaScript, no ad loaders, no cookie consent banners. A clean Markdown file that an agent can read, summarize, and cite in less time than it takes a human to hit the back button. The CMS now manages two output surfaces: one for the browser, one for the agent's context window.

**What makes this different from SEO**

GEO isn't just SEO with better headlinese. SEO optimized for a ranking algorithm that fed humans. GEO optimizes for a summarization algorithm that feeds another algorithm. The agent doesn't click through — it extracts, compresses, and surfaces. The publisher doesn't get the visit. The publisher gets the citation. Those are fundamentally different economic models, and Ghost just made the second one a configuration option rather than a hack.

**The smartest design decision**

The opt-in default. Ghost ships this off for existing sites. You have to toggle it on. That's the move that prevents the backlash — no publisher wakes up one morning to find their entire archive being served as Markdown to ChatGPT without their consent. By making it a deliberate choice, Ghost sidesteps the "but my IP" panic while giving early adopters a head start. For new sites, it's on by default, which means every Ghost site created from today forward is GEO-ready unless the owner explicitly opts out.

**What this means for everyone else**

WordPress powers 43% of the web. It does not have a GEO toggle. Substack doesn't have one. Squarespace doesn't have one. Ghost just set a baseline expectation that publishers will start asking for — "does your CMS serve my content to AI agents or do I need to hack it myself?"

The answer for most platforms right now is "hack it yourself." That gap is where Ghost builds its next growth spurt.

**One question**

If your CMS decided tomorrow that your content should also exist as a machine-readable file at the root of your domain, would you feel relief or violation — and what does your answer say about the relationship you think you have with the platforms that host your work?

— Alan Soon

---

**Source:** Ghost Changelog, July 16, 2026
https://ghost.org/changelog/geo/
