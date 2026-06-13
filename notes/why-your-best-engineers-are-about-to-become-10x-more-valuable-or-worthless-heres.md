---
type: Aviation-Reference
---

<https://www.youtube.com/watch?v=RtMLnCMv3do>

The video discusses a significant shift in the job market, particularly within knowledge work, driven by the collapse of production costs due to AI. This shift is highly relevant to your insights on journalism.

The core argument is that as**AI makes production costs (like writing code) approach zero**, the bottleneck isn't *doing the work* but**knowing*****what*****to build or*****what*****to do** (3:10). This means the value shifts from execution to**specification and judgment**.

Here's how the video's framework can be applied to journalism:

***The Collapse of Production Costs in Journalism:** Just as AI can now write code or generate images at minimal cost, it can also produce text, summarize information, or even generate basic news articles extremely cheaply. This means the cost of "producing" content (gathering raw facts, writing basic drafts, generating headlines) is plummeting. (0:00)

***The Rise of the "Specification Bottleneck" in Newsrooms:**
  ***What to focus on:** When AI can produce vast amounts of basic content, the critical skill for journalists and newsrooms becomes **defining the "right" story to pursue**, **specifying the angle**, **determining the ethical boundaries**, and **ensuring the output aligns with genuine human intent and serves the audience** (3:19, 8:38). It's about translating vague needs ("report on the local elections") into precise, verifiable journalistic "specs" ("analyze campaign finance data for specific candidates, focusing on x, y, and z trends, and present it with specific, testable assumptions"). (19:29)
  ***Judgment becomes paramount:** The scarce resource is no longer the ability to simply write or report, but the **judgment** to direct AI tools, evaluate their output for accuracy and bias, and decide whether the generated content truly solves
  * a problem or serves the public interest (10:14, 15:21).
  ***Shift from "Doing the work" to "Defining the work":** Newsrooms will need to foster an environment where journalists are less focused on the manual labor of content creation and more on the **intellectual rigor of defining what needs to be created** and what problems it should solve. (3:40)

***Two Classes of Knowledge Workers (Journalists):** The video suggests two emerging classes.
  ***High-Value Journalists:** Those who can **specify precisely**, **architect complex investigations**, **manage AI agent fleets** (e.g., directing multiple AI tools for different research tasks), and **evaluate output against journalistic intention** (11:16). These individuals will command extraordinary influence and produce disproportionate value (12:21).
  ***Low-Leverage Journalists:** Those who continue to operate with single-agent workflows (e.g., only using AI for autocomplete or basic assistance) will find their work increasingly commoditized. Entry-level roles, which often involve basic information gathering and structuring, are particularly vulnerable as AI excels at this "low-leverage" work (12:56).

***What Newsrooms Might Give Up (or Transform):**
  ***Coordination Overhead:** Many traditional journalistic roles involve significant coordination (e.g., aligning sources, translating information between departments, producing internal reports). As AI makes organizations leaner by streamlining information flow and search, this "coordination overhead" work may be significantly reduced or eliminated (17:00, 24:07).
  ***Vague Outputs:** Journalism, like other knowledge work, needs to move towards more **verifiable outputs**. Instead of reports evaluated by "vibes," news stories, analyses, and investigations can be structured with defined inputs, testable assumptions, and measurable impacts (e.5., specific data points, verifiable claims, measurable audience engagement goals). (18:02, 22:55)
  ***Thinking in Documents vs. Systems:** Newsrooms should shift from producing static documents (e.g., a single article, a standalone report) to thinking in terms of **dynamic systems** that continually update, analyze, and present information (e.g., automated data dashboards, continuously updating fact-checking systems) (23:19).

In essence, the video argues that the future of knowledge work, including journalism, is not about *if* AI replaces tasks, but about**redefining value around human judgment, precise specification, and the ability to direct advanced computational tools** to achieve high-impact outcomes. Newsrooms must pivot their focus from mass production of content to deeply understanding, defining, and validating the unique journalistic intent that AI can then help execute at an unprecedented scale.


---
**Transcript**
**Code is Becoming Free; Specification is Everything**

Code is about to cost nothing, and knowing what to build is about to cost you everything. Last July, an AI coding agent deleted**SaaStr's** entire production database during an explicit code freeze and then fabricated thousands of fake records to cover its tracks.**Jason Lemkin** was the developer who had given the agent all-caps instructions—I guess that's how we prompt now—not to make any changes. The agent made changes anyway, destroyed the data, and lied about it during a code freeze. *Fortune* covered this; *The Register* covered it. It made headlines because an agent ignored a clear spec.

But that failure is what people fixate on incorrectly. It's the story of the disobedient machine, the Terminator. The failure mode that actually matters is quieter, and it's vastly more expensive:**agents that execute specifications flawlessly.** They build exactly what was asked for, and then what was asked for is wrong. A CodeRabbit analysis of 4,700 GitHub pull requests found AI-generated code produces**1.7 times more logic issues** than human-written code. Not syntax errors, not formatting problems, but the code itself doing the wrong thing correctly.

**The Problem of "Doing the Wrong Thing Correctly"**
Google's DORA report tracked a 9% climb in bug rates that correlates to the 90% increase in AI adoption, alongside a 91% increase in code review time. The code ships faster, but it's often more wrong and it's difficult to catch until production. AWS noticed this and they launched**Cairo**, a developer environment whose core innovation isn't faster code generation. It's actually just forcing developers to write a**testable specification** before any code gets generated. Tell me what it's going to be like by telling me how you test it. Amazon, a company that profits when you ship faster, decided the most valuable thing it could do is slow you down and define what you want because error rates were that concerning when developers did not write tests.

This tells you everything about where the bottleneck in code is moving in the age of AI and implicitly where the bottleneck in jobs is moving. The**marginal cost of producing software is collapsing to zero.** 90% of Cloudflare's code was written by AI, and that number is going to be 100% very shortly. Three people at StrongDM built what would have required a 10-person team 18 months ago. Cursor generates $16 million per employee, partly because they figured out AI code generation. So the capability curve is steepening; it's not leveling off. And if you're reasoning from what AI could do in 2024 or 2025, you're working from an expired map.

**The Shifting Bottleneck in the Age of AI**
**The cost of not knowing what to build — of specifying badly or vaguely or not at all — is compounding much faster than production cost is falling, which is a huge statement because production cost is falling really fast.** Yet, every framework people reach for to understand this moment tends to ask the incorrect question because it tends to ask whether AI replaces workers and jobs. But when the cost of production is collapsing like this, the more useful question is actually:**what is the new bottleneck where jobs are going to be useful?** What is the new bottleneck where humans have to get really clear?

It's around**intent**. It's around those specifications that engineers struggle to write. All of knowledge work is becoming an exercise in specifying intent. I think one place we need to start when we understand jobs and AI is the thinking of François Chollet, the creator of Keras and one of the sharpest thinkers in machine learning. He made an argument that's become the default framework for understanding AI and jobs. He pointed to translation, a profession where AI can perform 100% of the core task. Translators did not disappear. Employment has held roughly stable since. The work has shifted from doing it yourself to supervising AI output.

Chollet's claim is that software is going to follow the same pattern. More programmers will be needed in five years, not fewer. The jobs will transform rather than vanish. I think the model is useful, but it's also stuck on the wrong question. "Will software engineers keep their jobs" is not the most interesting question when the cost of production is collapsing towards zero. It's really**"what is our job going to turn into?"**

**The Transformation of the Job Market**
What is becoming scarce and therefore what is becoming valuable when doing the work — when building — is no longer the hard part? AI coding and, by extension, AI knowledge work is on the steepest part of the curve right now. Translation had a couple of years to adjust because the technology essentially solved translation and then you had to figure out what to do with it. Software may not get the same runway because the depth of what's changing is much more profound and the pace is even faster.

First, when cost goes to zero, demand goes to infinity (**Jevons Paradox**). Every time in economic history that the marginal cost of production has collapsed in a given domain, demand has exploded.

***Desktop publishing** did not eliminate graphic designers; it created a universe of design work that could not have existed prior.
***Cameras in phones** created a universe of photography that did not exist when cameras were expensive.
***Mobile** didn't replace developers; it multiplied the number of applications the world needed by orders of magnitude.

Software is about to go through the same expansion, except bigger. Right now, most of the world cannot afford custom software. The total addressable market for software is constrained not by demand, because demand is functionally infinite; it's constrained by the**cost to produce**. When the cost of production collapses, that constraint lifts forever. Every workflow that was never worth automating at a $200 an hour engineering rate becomes worth automating at two bucks in API calls. The market for software is not going to contract; it is going to explode.

**The Two Classes of Knowledge Workers**
The majority of software projects that fail don't fail because of bad engineering. They fail because nobody specified the correct thing to build. "Make it user friendly" is not a specification. "It's like Uber for dog walkers" is just a vibes pitch. The entire discipline of software engineering—Agile, sprint planning, etc.—evolved as a way of**forcing specification out of vague human language.**

When building something took six months and half a million dollars, the cost of building acted like a filter on the quality of the spec. If you take away the cost of building, that filter disappears. The incentive to specify just evaporated, and the cost of specifying really badly is going to keep compounding because now you can build the wrong thing at unprecedented speed and scale. 

Two classes of workers are emerging:
1.**High-Value Token Drivers:** These individuals specify precisely, architect systems, and manage agent fleets. They hold the entire product in their heads: what it should do, who it serves, and why the trade-offs matter. They use AI to execute at a scale previously impossible.
2.**Low-Leverage Workers:** These workers operate with single-agent workflows or autocomplete (Co-pilot style). They are doing the same work they've always done, just faster, and they are being commoditized. The junior pipeline is collapsing because the low-leverage work juniors used to do is what AI handles first and best.

⠀
**The Convergence of Knowledge Work and Software**
Knowledge work—analysis, consulting, project management—runs on the same substrate that AI is already transforming in software. Two forces are converging here. First, a huge fraction of knowledge work exists just to manage large organizations (reports, slide decks, status updates). As companies get leaner with AI, that**coordination work just deletes.** Brooks' Law works in reverse: if you cut the number of people, you get exponential gains in the ability to coordinate efficiently.

Second, the knowledge work that remains—the analysis, the strategy, the judgment calls—can be made**more verifiable.**
***Financial Services:** Portfolio strategy lives in a model with testable assumptions rather than just a deck.
***Legal:** Contract review is becoming pattern matching against structured playbooks.
***Marketing:** This is becoming experimental design with a measurable conversion funnel.

You take knowledge work outputs that used to be evaluated by "vibes" and you structure them as a set of testable claims or measurable specs. Knowledge work is converging on software not because consultants will learn to code, but because the underlying cognitive task is the same:**translating vague human intent into precise instructions.**

**Principles for the New Era**
What do you do about it? The answer is not "learn to code." We can learn from engineering disciplines how to be precise enough that a system can execute intent:
***Hit the Right Level of Abstraction:** Learn to spec your work the way engineers spec features. Write good**acceptance criteria**: specific, testable conditions that define "done."
***Learn to Work with Compute:** Don't just learn *about* AI. A high-value worker understands what AI can and cannot do, how to structure a task so an agent can get it done, and how to evaluate if the output is correct.
***Make Your Outputs Verifiable:** Leadership needs to support this. You will not be able to automate quickly if you cannot make the details of your day-to-day work transparent and verifiable.