---
type: Note
---

<https://www.youtube.com/watch?v=w-cmMcMZoZ4>

Jensen Huang interviews Mark Zuckerberg at SIGGRAPH 2024. They discuss Meta's AI work, including PyTorch and LLAMA models. Zuckerberg explains Meta's open-source philosophy and vision for AI assistants and agents. They talk about Meta's smart glasses and AR/VR plans. Huang praises Zuckerberg's leadership and Meta's AI progress. They discuss the rapid impact of generative AI across industries. The interview ends with a lighthearted jacket swap between the two CEOs.

Based on the interview, some key predictions and visions discussed include:

1. AI assistants and agents becoming more prevalent, with users able to create their own customized AI agents for different purposes.

2. AI models becoming more diverse and specialized rather than just one large general model, with companies creating tailored AIs for specific functions.

3. Smart glasses and AR/VR technology advancing, with a range of products at different price points emerging:

 - Displayless AI glasses at around $300 becoming a mass-market product

 - Full holographic AR glasses in stylish frames coming in the near future

 - VR/MR headsets serving as more immersive workstations or gaming devices

4. Open ecosystems becoming dominant in the next generation of computing platforms, similar to how Windows dominated PCs.

5. AI dramatically impacting and transforming various industries, enterprises, and scientific fields.

6. AI assistants evolving to handle more complex, multi-step tasks over longer timeframes rather than just turn-based interactions.

7. Video understanding and segmentation AI models enabling new applications in areas like content creation, industrial monitoring, and scientific research.

8. AI becoming integrated into more aspects of daily life and work, amplifying human capabilities and productivity.

"It's one of the big questions that's going to be in the future to what extent are people just using the kind of the bigger, more sophisticated models versus just training their own models for the uses that they have." — Zuckerberg


Ladies and gentlemen, I have a very special guest, but could I ask everybody to sit down?

We're about to get started.

My next guest, I am so impressed by this person.

Three reasons.

First reason is there are only a handful of entrepreneurs, founders that started a company that literally touched the lives of billions of people around the world, as part of the social fabric, invented services, and a state-of-the-art computing company.

Two, very few entrepreneurs, founders founded the company and led it to over a trillion dollars of value.

And three, a college dropout.

All three things simultaneously true.

Ladies and gentlemen, please help me welcome Mark Zuckerberg.

Mark, welcome to your first SIGGRAPH.

Hi.

Can you believe this?

One of the pioneers of computing, a driver of modern computing, and I had to invite him to SIGGRAPH.

So anyways, Mark's it down.

It's great to have you here.

Welcome.

Thanks for flying down.

Yeah, that would be fun.

I hear you've been going for like five hours already or something.

Well, yeah, sure.

This is SIGGRAPH, you know, these 90% PhDs.

And so the thing that's really great about SIGGRAPH, as you know, this is the show of computer graphics, image processing, artificial intelligence, and robotics combined.

And some of the companies that over the years have demonstrated and revealed amazing things here from Disney, Pixar, Adobe, Epic Games, and of course, you know, Nvidia, we've done a lot of work here.

This year, we introduced 20 papers at the intersection of artificial intelligence and simulation.

So we're using artificial intelligence to do help simulation be way larger scale, way faster, for example, differentiable physics.

We're using simulation to create simulation environments for synthetic data generation for artificial intelligence.

And so these two areas are really coming together, really proud of the work that we've done here.

At Meta, you guys have done amazing AI work.

I mean, one of the things that I find amusing is when the press writes about how Meta's jumped into AI this last couple of years.

As if, you know, the work that Fair has done, remember, we all use PyTorch, that comes out of Meta.

The work that you do in computer vision, the work in language models, real-time translation, groundbreaking work.

I guess my first question for you is, how do you see the advances of generative AI, AdMetta today, and how do you apply it to either enhance your operations or introduce new capabilities that you're offering?

Yeah, so a lot to unpack there.

First of all, really happy to be here.

Meta has done a lot of work and has been at SIGGRAPH for eight years.

I mean, it's, you know, we're newbs compared to you guys.

And I think it was back in 2018.

You're dressed right, but this is my hood.

I just -- No, it's -- I mean, well, thank you for welcoming me to your hood.

And I think it was back in 2018, we showed some of the early hand-tracking work for our VR and mixed reality headsets.

I think we've talked a bunch about the progress that we're making on codec avatars, the photorealistic avatars that we want to be able to drive from consumer headsets, which we're getting closer and closer to, so pretty excited about that, and also a lot of the display systems work that we've done.

Some of the future prototypes and research for getting the mixed reality headsets to be able to be really thin, but with just pretty advanced optical stacks and display systems, the integrated system.

And that's been stuff that we've typically shown here first.

So excited to be here this year.

Not just talking about the metaverse stuff, but also all the AI pieces, which, as you said, we started FAIR, the AI research center back then it was Facebook.

Now, meta, before we started Reality Labs, and we've been at this for a while.

The -- you know, all of the stuff around Gen AI, it's an interesting revolution.

And I think that it's going to end up making, I think, all of the different products that we do, you know, different in interesting ways.

I mean, I kind of go through -- you can look at the big product lines that we have already, so things like the, you know, feed and recommendation systems and Instagram and Facebook.

And we've kind of been on this journey where that's gone from just being about connecting with your friends, and ranking was always important because even when you were just, you know, following friends, you know, if someone did something really important, like your cousin had a baby or something, like you want that at the top, you'd be pretty angry at us if we, you know, was buried somewhere down in your feed.

So the ranking was important, but now, over the last few years, it's gotten to a point where more of that stuff is just different public content that's out there.

The recommendation systems are super important because now, instead of just a few hundred or thousand potential candidate posts from friends, there's millions of pieces of content, and that turns into, like, a really interesting recommendation problem.

And with generative AI, I think we're going to quickly move into this zone where not only is the majority of the content that you see today on Instagram, you know, just recommended to you from kind of stuff that's out there in the world that matches your interests and whether or not you follow the people, I think in the future a lot of this stuff is going to be created with these tools, too.

Some of that is going to be creators using the tools to create new content.

Some of it, I think, eventually is going to be content that's either created on the fly for you or kind of pulled together and synthesized through different things that are out there.

So that's just one example of how kind of the core part of what we're doing is just going to evolve, and it's been evolving for 20 years already, but I think that's going to happen.

Well, a few people realized that one of the largest computing systems the world has ever conceived of is a recommender system.

Yeah, I mean, it's this whole, yeah, it's this whole different path, right?

It's not quite the kind of gen AI hotness that people talk about, but I think it's like, as, I mean, it's all the transformer architectures, and it's a similar thing of just building up more and more general models.

And betting unstructured data into features?

Yeah, I mean, one of the big things that just drives quality improvements is, you know, it used to be that you'd have a different model for each type of content, right?

So a recent example is, you know, we had one model for ranking and recommending reels and another model for ranking and recommending more long-form videos, and then, you know, take some product work to basically make it so that the system can display, you know, anything in line, but, you know, the more you kind of just create more general recommendation models that can span everything, it just gets better and better.

So, I mean, part of it, I think, is just like economics and liquidity of content, and the broader of a pool that you can pull from, you're just not having these weird inefficiencies of pulling from different pools, but, yeah, I mean, as the models get bigger and more general, that gets better and better.

So I kind of dream of one day, like you can almost imagine all of Facebook or Instagram being, you know, like a single AI model that has unified all these different content types and systems together that actually have different objectives over different timeframes, right, because some of it is just showing you, you know, what's the interesting content that you're going to be, that you want to see today.

But some of it is helping you build out your network over the long-term, right, people you may know, or accounts you might want to follow.

And these multimodal models tend to be much better at recognizing patterns, weak signals and such.

And so one of the things that people, you know, it's so interesting that AI has been so deep in your company, you've been building GPU infrastructure, running these large recommender systems for a long time.

Now you're -- >> We'll slow on it, actually, getting to GPUs.

>> Yeah, I was trying to be nice.

>> I know.

Well, you know, too nice.

>> I was trying to be nice, you know.

>> You're my guest.

>> Backstage, before I came on here, you were talking about like owning your mistakes or something, right?

So.

>> You don't have to volunteer it out of the blue.

>> I think this one has been well-tried.

>> Yeah.

>> It's like I got -- >> But as soon as you got into it -- >> Why?

>> As soon as you got into it, you got into it strong.

Let's just put -- there you go.

>> That's how we roll.

>> Now, the thing that's really cool about Jarrant of AI is these days, when I use WhatsApp, I feel like I'm collaborating with WhatsApp.

I love "imagine."

I'm sitting here typing, and it's generating the images as I'm going.

>> Yeah.

>> I go back and I change my words at generating other images.

>> Yeah.

>> You know, and so the one that old Chinese guy enjoying a glass of whiskey at sundown with three dogs, golden retriever, golden doodle, and a Bernie's mountain dog.

And it generates a pretty good, real-time picture.

>> Yeah, we're getting there.

>> That's me.

>> Every month.

>> Yeah, yeah.

>> And now you could actually load my picture in there.

>> Yeah.

>> And I should be me.

>> Yeah, that's as of last week.

>> Yeah.

>> I'm super excited about that.

>> Now, imagine me.

I'm spending a lot of time with my daughters, imagining them as mermaids and things over the last week.

It's been a lot of fun.

>> Yeah.

>> That's the other half of it.

A lot of the Jann AI stuff is going to -- on the one hand, it's, I think, going to just be this big upgrade for all of the workflows and products that we've had for a long time.

But on the other hand, there's going to be all these completely new things that can now get created.

So meta-AI, you know, the idea of having, you know, just an AI assistant that can help you with different tasks.

And in our world, it's going to be, you know, very creatively oriented, like you're saying.

But, I mean, they're very general.

So, I mean, you don't need to just constrain it to that.

It'll be able to answer any question.

Over time, I think, you know, when we move from, like, the llama 3 class of models to llama 4 and beyond, it's, um, it's going to, I think, feel less like a chatbot where it's like, you give it a prompt and it just responds, then you give the prompt and it responds.

And it's just, like, back and forth.

I think it's going to pretty quickly evolve to you give it an intent, and it actually can go away on multiple timeframes.

And I mean, it probably should acknowledge that you gave it an intent up front.

But, I mean, some of the stuff, I think, will end up, you know, spin up, you know, compute jobs that take, you know, weeks or months or something and then just come back to you when, like, something happens in the world.

And I think that that's going to be really powerful.

So, I mean, today's AI, as you know, is kind of turn-based.

You say something, it says something back to you.

But obviously, when we think, when we're given a mission or we're giving a problem, you know, we'll contemplate multiple options or maybe we come up with a, you know, a tree of options, a decision tree, and we walk down to the decision tree simulating in our mind, you know, what are the different outcomes of each decision that we could potentially make.

And so we, we're doing planning.

And so in the future, AI's will kind of do the same.

One of the things that I was super excited about when you talked about your vision of Creator AI, I just think that's a home run idea, frankly.

Tell everybody about the Creator AI and AI studio that's going to enable you to do that.

Yeah, so we actually, I mean, this is something that we're, you know, we've talked about it a bit, but we're rolling it out a lot wider today.

You know, a lot of our vision is that I don't think that there's just going to be like one AI model.

Right, I mean, this is something that some of the other companies in the industry, they're like, you know, it's like they're building like one central agent and, and yeah, we'll have the med AI assistant that you can use, but a lot of our vision is that we want to empower all the people who use our products to basically create agents for themselves.

So whether that's, you know, all the many, many millions of creators that are on the platform or, you know, hundreds of millions of small businesses.

We eventually want to just be able to pull in all your content and very quickly stand up a business agent and be able to interact with your customers and, you know, do sales and customer support and all that.

So the one that we're, that we're just starting to roll out more now is we call it AI studio and it basically is a set of tools that eventually is going to make it so that every creator can build sort of an AI version of themselves as sort of an agent or an assistant that their community can interact with.

There's kind of a fundamental issue here where there's, there's just not enough hours in the day, right?

It's like if you're, if you're a creator, you want to engage more with your community, but you're constrained on time.

And similarly, your community wants to engage with you, but it's tough.

I mean, there's just, there's a limited time to do that.

So the next best thing is, is allowing people to basically create these artifacts, right?

It's, it's sort of, it's an agent, but it's, you train it to kind of on your material to represent you in the way that you want.

I think it, it's, it's a very kind of creative endeavor, almost like a, like a piece of art or content that you're putting out there.

And, no, it's, it's going to be very clear that it's not engaging with the creator themselves, but I think it'll be another interesting way, just like how creators put out content on, on these social systems to be able to have agents that do that.

Similarly, I think that there's going to be a thing where people basically create their own agents for all different kinds of uses.

Some will be sort of customized utility, things that they're trying to get done that they want to kind of fine tune and, and train agent for.

Some of them will be entertainment.

And some of the things that people create are just funny, you know, in, in just kind of silly in different ways or, or kind of have a funny attitude about things that, you know, we probably couldn't, we probably wouldn't build into meta AI as an assistant, but I think people, people are kind of pretty interested to see and interact with.

And then one of the interesting use cases that we're seeing is people kind of using these agents for support.

This was one thing that, that was a little bit surprising to me is one of the top use cases for meta AI already is people basically using it to role play difficult social situations that they're going to be in.

So whether it's a professional situation, it's like, all right, I want to ask my manager, like, how do I get a promotion or raise, or I'm having this fight with my friend, or I'm having this difficult situation with my girlfriend, like how, like, how can this conversation go?

And basically having a, like a completely judgment free zone where you can basically role play that and see how the conversation will go and get feedback on it.

But a lot of people, they don't just want to interact with the same kind of agent, whether it's meta AI or chat, pt or whatever it is that everyone else is using, they want to kind of create their own thing.

So that's, that's roughly where we're going with AI studio, but it's all part of this bigger, I guess, view that we have that there shouldn't just be kind of one big AI that people interact with.

We just think that the world will be better and more interesting if there's a diversity of these different things.

I just think it's so cool that if you're an artist and you have a style, you could take your style, all of your body of work, you could fine tune one of your models, and now this becomes an AI model that you can come and you could prompt it, you could ask me to, you know, create something along the lines of the art style that I have, and you might even give me a piece of art as a drawing, a sketch, as an inspiration, and I can generate something for you.

And you come to my, come to my, you know, come to my bot for that, come to my AI for that.

It could be, it could be a, every single, every single restaurant, every single website will probably in the future have these AIs.

Yeah, I mean, I kind of think that in the future, just like every business has, you know, an email address and a website and a social media account or several.

I think in the future, every business is going to have an AI agent that interfaces with their customers.

Some of these things I think have been pretty hard to do historically.

Like, if you think about any company, it's like you probably have customer support is just a separate organization from sales, and that's not really how you'd want it to work as CEO.

It's just that, okay, they're kind of different skills, you're building up these.

I'm your customer support, just to-- What's up?

You are?

Yeah, well, apparently, I am.

I mean, I remember Mark needs something.

As CEO, you-- I can't tell whether his chatbot or-- Yeah, just my chatbot just hasn't here.

No, well, I guess that's kind of-- yeah, when you're CEO, you have to do all the stuff.

But I mean, then, when you build the abstraction into your organization, a lot of times, like the, you know, in general, the organizations are separate because they're kind of optimized for different things, but I think, like, the platonic ideal of this would be that it's kind of one thing, right?

Because, you know, as a customer, you don't really care, you know, you don't want to, like, have a different route when you're trying to buy something versus if you're having an issue with something that you bought.

You just want to have a place that you can go and get your questions answered and be able to engage with the business in different ways.

I think that that applies for creators to-- I think that the kind of personal consumer side of this is going to be-- And all of that engagement with your customers, especially if they're complaints, is going to make your company better.

Yeah, totally.

The fact that it's all engagement with this AI is going to capture the institutional knowledge and how to-- and all of that can go into analytics, which improves the AI and so on and so forth.

Yeah.

So the business version of this is that, I think, has a little more integration and we're still in a pretty early alpha with that.

But the AI studio, making it so people can kind of create their UGC agents and different things and getting started on this flywheel of having creators create them, I'm pretty excited about that.

So can I use AI studio to fine-tune with my images, my collection of images?

Yeah, we're going to get there.

Okay.

And then I could give it, load it, all the things that I've written, so use it as MyRag.

Yeah, yeah, basically.

Okay.

And then every time I come back to it, it loads up its memory again, so it remembers where it left off last time.

And we carry on our conversation as nothing ever happened.

Yeah, and look, I mean, like any product, it'll get better over time.

The tools for training, it will get better.

It's not just about what you want it to say.

I mean, I think generally creators and businesses have topics that they want to stay away from too.

So just getting better at all this stuff.

I think the platonic version of this is not just text.

You almost want to just be able to, and this is sort of an intersection with some of the codec avatar work that we're doing over time.

You want to basically be able to have almost like a video chat with the agent.

I think we'll get there over time.

I don't think that this stuff is that far off, but the flywheel is spinning really quickly.

So it's exciting.

There is a lot of new stuff to build.

And I think even if the progress on the foundation models kind of stopped now, which I don't think it will, I think we'd have like five years of product innovation for the industry to basically figure out how to most effectively use all the stuff that's gotten built so far.

But I actually just think the kind of foundation models and the progress on the fundamental research is accelerating.

So that it's a pre-wild time.

Your vision, you kind of made this happen.

Thank you.

In the last conversation, thank you.

(Applause) Yeah.

CEOs, we're delicate flowers.

We need a lot of back.

We're pretty grizzled at this point.

I think we're the two kind of long-standing founders in the industry.

It's true.

I mean, it's true.

I mean, it's true.

I just...

When your hair's gotten gray, mine has just gotten longer.

(Laughter) Mine's gotten gray, yours's gotten curly.

What's up?

It was always curly.

That's why I kept it short.

(Laughter) Yeah, I just...

If I had known it was going to take so long to succeed.

You would never have started.

No, I would have dropped out of college just like you.

(Laughter) Get a head start.

Well, that's a good difference between our personalities.

I think that these things have to...

You got a 12-year head start.

That's pretty good.

That's pretty good.

You know, you're doing pretty well.

I'm going to...

I'm going to be able to carry on.

Let me just put it that way.

Yeah, so...

The thing that I love about your vision of that everybody can have an AI, that every business can have an AI.

In our company, I want every engineer and every software developer to have an AI.

Yeah.

And...

Or many AI's.

The thing that I love about your vision is you also believe that everybody and every company should be able to make their own AI.

So you actually open sourced...

When you open sourced LAMA, I thought that was great.

LAMA 2.1, by the way.

I thought LAMA 2 was probably the biggest event in AI last year.

And the reason for that...

I thought it was the H100, but you know, it's... [laughter] It's a chicken or the egg question.

That's a chicken or the egg question.

No, play our part.

Yeah, which came first.

The H100. [laughter] Well, LAMA 2 was actually not the H100.

Yeah, it was A100.

Yeah, thank you.

And so...

But the reason why I said it was the biggest event was because when that came out, it activated every company, every enterprise, and every industry.

All of a sudden, every healthcare company was building AI's, every company was building AI.

Every large company, small company, startups were building AI's.

It made it possible for every researcher to be able to re-engage AI again, because they have a starting point to do something with.

And then now, 3.1 is out.

And the excitement, just so you know, you know, we work together to deploy 3.1.

We're taking it out to the world's enterprise.

And the excitement is just off the charts.

And I think it's going to enable all kinds of applications.

But tell me about your open source philosophy.

Where did I come from?

And you know, you open source PyTorch.

Yeah.

And that is now the framework by which AI is done.

And now you've open source LAMA 3.1 or LAMA.

There's a whole ecosystem built around it.

And so I think it's terrific.

Where did that all come from?

Yeah.

So there's a bunch of history on a lot of this.

I mean, we've done a lot of open source work over time.

I think part of it, you know, just bluntly, is, you know, we got started after some of the other tech companies, right, in building out stuff like the distributed computing infrastructure and the data centers.

And because of that, by the time that we built that stuff, it wasn't a competitive advantage.

We were like, all right, we might as well make this open.

And then we'll benefit from the ecosystem around that.

So we had a bunch of projects like that.

I think the biggest one was probably Open Compute, where we took our server designs and network designs and eventually the data center designs and published all of that.

And by having that become somewhat of an industry standard, all the supply chains basically got organized around it, which had this benefit of saving money for everyone.

So by making it public and open, we basically have, say, billions of dollars from doing that work.

Well, Open Compute was also what made it possible for NVIDIA HgXs that we designed for one data center all of a sudden.

Yeah, works in every data center.

Awesome.

So that was an awesome experience.

And then, you know, we've done it with a bunch of our kind of infrastructure tools, things like React, PyTorch.

So I'd say by the time that LAMA came around, we were sort of positively predisposed towards doing this.

For AI models specifically, I guess there's a few ways that I look at this.

I mean, one is, you know, it's been really fun building stuff over the last 20 years at the company.

One of the things that has been sort of the most difficult has been kind of having to navigate the fact that we ship our apps through our competitors' mobile platforms.

So in the one hand, the mobile platforms have been this huge boon to the industry.

That's been awesome.

On the other hand, having to deliver your products through your competitors is challenging, right?

And I also, you know, I grew up in a time where, you know, the first version of Facebook was on the web, and that was open.

And then, you know, as it transitioned to mobile, you know, the plus side of that was, you know, now everyone has a computer in their pockets, and that's great.

The downside is, okay, we're a lot more restricted in what we can do.

So when you look at these generations of computing, there's this big recency bias where everyone just looks at mobile and thinks, okay, because the closed ecosystem, because Apple basically won and set the terms of that, and like, yeah, I know that there's more Android phones out there technically, but like, Apple basically has the whole market, and like all the profits, and basically Android is kind of following Apple in terms of the development of it.

So I think Apple pretty clearly won this generation.

But it's not always like that, right?

If you go back a generation, you know, Apple was doing their kind of closed thing, but Microsoft, which was, you know, it obviously isn't like this perfectly open company, but compared to Apple with Windows running on all the different OEMs and different software, different hardware, was a much more open ecosystem.

Windows was the leading ecosystem.

It basically, in the kind of PC generation of things, the open ecosystem won.

And I am kind of hopeful that in the next generation of computing, we're going to return to a zone where the open ecosystem wins and is the leading one again.

There will always be a closed one and an open one.

I think that there's reasons to do both.

There are benefits to both.

I'm not like a zealot on this.

I mean, we do closed source stuff.

I'm not everything that we publish is open.

But I think in general, for the computing platforms that the whole industry is building on, there's a lot of value for that if the software especially is open.

So that's really shaped my philosophy on this.

And for both AI with LAMA and with the work that we're doing in AR and VR, where we're basically making the horizon OS that we're building for mixed reality an open operating system in the sense of kind of what Android or what Windows was and basically making it so that we're going to be able to work with lots of different hardware companies to make all different kinds of devices.

We basically just want to return the ecosystem to that level where that's going to be the open one.

And I'm pretty optimistic that in the next generation the open ones are going to win.

For us specifically, I just want to make sure that we have access to, I mean, this is sort of selfish, but after building this company for a while, one of my things for the next 10 or 15 years is like, I just want to make sure that we can build the fundamental technology that we're going to be building social experiences on because there's just been too many things that I've tried to build and then you've just been told, "Nah, you can't really build that by the platform provider."

At some level I'm just like, "Nah, fuck that."

For the next generation, we're going to go build all the way down and make sure that we're-- There goes our broadcast opportunity.

Yeah, no, sorry.

Sorry.

I think it's like, "Beep."

Yeah.

You know, we're doing okay for like 20 minutes, but-- Give me talking about closed platforms and I get angry.

So, hey, look, it is great.

I think it's a great world where there are people who are dedicated to build the best possible AIs, however they build it, and they offer it to the world as a service.

But if you want to build your own AI, you could still also build your own AI.

So, the ability-- Yeah, totally.

To use an AI, you know, there's a lot of stuff.

I prefer not to make this jacket myself.

I prefer to have this jacket made for me.

You know what I'm saying?

Yeah.

So, the fact that leather could be open source is not a useful concept for me.

But I think the idea that you could have great services, incredible services, as well as open service, open ability.

Yeah.

Then we basically have the entire spectrum.

But the thing that you did with 3.1, that was really great, was you have 4.5b, you have 70b, you have 8b.

You could use it for a synthetic data generation, use the larger models to essentially teach the model models.

And although the larger models will be more general, it's less brittle.

You could still build a smaller model that fits in whatever operating domain or operating cost that you would like to have.

You met a guard, I think.

Yeah, a lot of guard.

A lot of guard.

A lot of guard for guard railing, fantastic.

And so now, in the way that you build the model, it's built in a transparent way.

It has-- you dedicate it.

You've got a world-class safety team, world-class ethics team.

You could build it in such a way that everybody knows it's built properly.

And so, I really love that part of it.

Yeah, and I mean, just to finish the thought from before I got sidetracked there for D-Tor.

I do think there's this alignment where-- and we're building it because we want the thing to exist and we want to knock it cut off from some closed model.

Right?

But this isn't just like a piece of software that you can build.

You need an ecosystem around it.

And so, it's almost like it kind of almost wouldn't even work that well if we didn't open source it.

It's not-- we're not doing this because we're kind of altruistic people, even though I think that this is going to be helpful for the ecosystem.

And we're doing it because we think that this is going to make the thing that we're building the best by kind of having a robust ecosystem around it.

Well, look, how many people contributed to PyTorch ecosystem?

Yeah, totally.

Mountains of engineering.

Yeah.

I mean, in video alone, we probably have a couple of hundred people just dedicated to making PyTorch better and scalable and more performant and so on and so forth.

Yeah, and it's also just when something becomes something of an industry standard, other folks do work around it.

Right?

So, like all of the silicon in the systems will end up being optimized to run this thing really well, which will benefit everyone, but it will also work well with the system that we're building.

And that's, I think, just one example of how this ends up being just being really effective.

So, yeah, I mean, I think that the open source strategy is going to be-- Yeah, it's going to be a good one as a business strategy.

I think people still don't quite get-- Well, we love it so much.

We built an ecosystem around it.

We built this thing.

Yeah, you guys have been awesome on this.

Yeah, yeah.

I mean, you guys have been awesome on this.

I mean, every time we're shipping something, you guys are the first to release this and optimize it and make it work.

And so, I mean, I appreciate that.

What can I say?

We have good engineers.

You know?

And so-- Well, you always just jump on this stuff quickly, too.

So, you know, I'm a senior citizen, but I'm agile. [laughter] That's what CEOs have to do.

And I recognize an important thing.

I recognize an important thing.

And I think that LAMA is genuinely important.

We built this concept called AI Factory, AI Foundry Around It, so that we can help everybody build, take-- You know, a lot of people, they have a desire to build AI.

And it's very important for them to own the AI because once they put that into their flywheel, their data flywheel, that's how their company's institutional knowledge is encoded and embedded into an AI.

So they can't afford to have the AI flywheel, the data flywheel, that experienced flywheel somewhere else.

And so, open source allows them to do that, but they don't really know how to turn this whole thing into an AI.

And so, we created this thing called an AI Foundry.

We provide the tooling.

We provide the expertise.

LAMA technology.

We have the ability to help them turn this whole thing into an AI service.

And then when we're done with that, they take it, they own it.

The output of what we call a NIMM, and this NIMM, this neuromicro-ambidea inference microservice, they just downloaded, they take it, and they run it anywhere they like, including on-prem.

And we have a whole ecosystem of partners from OEMs that can run the NIMMs to GSIs like Accenture that we've trained and work with to create LAMA-based NIMMs and pipelines.

And now we're off helping enterprises all over the world do this.

I mean, it's really quite an exciting thing.

It's really all triggered off of the LAMA open sourcing.

Yeah, I think especially the ability to help people distill their own models from the big model is going to be a really valuable new thing.

Because there's this, you know, just like we talked about on the product side, how, at least I don't think that there's going to be like one major AI agent that everyone talks to.

It's at the same level, I don't think that there's going to necessarily be one model that everyone uses.

We have a chip AI, chip design AI.

We have a software coding AI.

And our software coding AI understands USD, because we code in USD for omnivore stuff.

We have software AI that understands Verilog, our Verilog.

We have software AI that understands our bugs database and knows how to help us triage bugs and sends it to the right engineers.

And so each one of these AI's are fine-tuned off of LAMA.

And so we fine-tuned them, we guardrail them.

If we have an AI design for chip design, we're not interested in asking it about politics, you know, and religion and things like that.

So we guardrail it.

And so I think every company will essentially have, for every single function that they have, they will likely have AI's that are built for that.

And they need help to do that.

**Yeah, I mean, I think it's one of the big questions that's going to be in the future to what extent are people just using the kind of the bigger, more sophisticated models versus just training their own models for the uses that they have.**

At least I would bet that they're going to be just a vast proliferation of different models.

People...

We use the largest ones.

And the reason for that is because our engineers are...

Our times are still valuable.

And so we get...

Right now we're getting 405B optimized for performance.

And as you know, 405B doesn't fit in any GPU no matter how big.

And so that's why the NVLink performance is so important.

We have this...

Every one of our GPUs connected by this non-blocking switch called NVLink switch.

And in a HDX, for example, there are two of those switches.

And we make it possible for all these GPUs to work and run the 405B's really performant.

The reason why we do it is because the engineers' times are so valuable to us.

You know, we want to use the best possible model, the fact that it's cost effective by a few pennies.

Who cares?

And so we just want to make sure that the best quality of result is presented to them.

Yeah, well, I mean, the 405, I think, is about half the cost to inference of the GPT-4-0 model.

So, I mean, at that level it's already...

I mean, it's pretty good.

But yeah, I mean, I think people are doing stuff on devices or want smaller models.

They're just going to distill it down.

So, that's like a whole different set of services.

That AI is running...

And let's pretend for a second that we're hiring that AI.

That AI for chip design is probably $10 an hour.

You're using...

You know, and...

If you're using it constantly and you're sharing that AI across a whole bunch of engineers, so each engineer probably has an AI that's sitting with them that doesn't cost very much.

And we pay the engineers a lot of money.

And so, to us, a few dollars an hour amplifies the capabilities of somebody that's really valuable.

Yeah.

(Laughter) I mean, you don't need to convince me.

(Laughter) If you haven't hired an AI, do it right away.

That's all we're saying.

And so, let's talk about the next wave.

One of the things that I really love about the work that you guys do, computer vision, one of the models that we use a lot internally, is segment everything.

And you know that we're now training AI models on video so that we can understand the world model.

Our use case is for robotics and industrial digitalization and connecting these AI models into Omniverse so that we can model and represent the physical world better, have robots that operate in these omniverse worlds better.

Your application, the Ray-Ban Metaglass, your vision for bringing AI into the world and bringing AI into the virtual world is really interesting.

Tell us about that.

Yeah.

Well, okay.

A lot to unpack in there.

The segment anything model that you're talking about, we're actually presenting, I think, the next version of that here at SIGGRAPH, segment anything too.

And it now works.

It's faster.

It works with, oh, here we go.

It works in video now as well.

I think these are actually cattle from my ranch and kawaii.

By the way, these are what they're called.

Delicious cows.

Delicious marks cows.

There you go.

Yeah, another.

Next time we do, so Mark came up to my house and we made Philly cheesesteak together.

Next time you're bringing the cow.

You did.

I was more of a sous chef.

Boy, that was really good.

It was really good.

I was a sous chef comment.

Okay, listen.

And then at the end of the night, though, you were like, hey, so you ate enough, right?

And I was like, I don't know.

I could eat another one.

You're like, really?

You know, usually when you say something like, you're being your guest.

I was definitely like, yeah, we're making more.

We're making more.

Did you get enough to eat?

Usually your guest says, oh, yeah, I'm fine.

Make me another cheesesteak, Jensen.

Just to let you know how OCD he is, so I turn around, I'm prepping the cheesesteak.

And I said, Mark, cut the tomatoes.

And so Mark, I handed him a knife.

I'm a precision cutter.

And so he cuts the tomatoes.

Every single one of them are perfectly to the exact millimeter.

But the really interesting thing is I was expecting all the tomatoes to be sliced and kind of stacked up kind of like a deck of cards.

When I turned around, he said he needed another plate.

And the reason for that was because all of the tomatoes he cut, none of them touched each other.

Once he separates, one slice of tomato from the other tomato, they shall not touch again.

Yeah, look, man, if you wanted them to touch, you needed to tell me that, right?

You need-- I'm just a sous chef, OK?

That's why he needs an AI that doesn't judge.

Yeah, it's like-- This is super cool.

OK, so it's recognizing the cows track-- it's recognizing tracking the cows.

Yeah.

Yeah, so it's-- a lot of fun effects will be able to be made with this.

And because it'll be open a lot of more serious applications across the industry, too.

So I mean, scientists use this stuff to study like coral reefs and natural habitats and kind of evolution of landscapes and things like that.

I mean, it's being able to do this in video and having a B-Zero shot and be able to kind of interact with it and tell it what you want to track is-- it's pretty cool research.

So for example, the reason why we use it, for example, you have a warehouse and there's got a whole bunch of cameras.

And the warehouse AI is watching everything that's going on.

And let's say a stack of boxes fell or somebody spilled water on the ground.

Or whatever accident is about to happen, the AI recognizes it, generates the text, send it to somebody, and help will come along the way.

And so that's one way of using it.

Instead of recording everything, if there's an accident, start recording every nanosecond of video, and then going back and retrieve that moment, it just records the important stuff because it knows what it's looking at.

So having a video understanding model, a video language model is really, really powerful for all these interesting applications.

Now what else are you guys going to work on beyond, Ray, talk to me about-- Yes, there's all the smart classes.

So I think when we think about the next computing platform, we kind of break it down into mixed reality, the headsets, and the smart classes.

And the smart classes, I think, it's easier for people to wrap their head around that and wearing it because it's pretty much**everyone who's wearing a pair of glasses today will end up upgraded to smart glasses, and that's more than a billion people in the world. So that's going to be a pretty big thing.**

The VRMR headsets, I think, some people find it interesting for gaming or different uses, some don't yet.

My view is that they're going to be both in the world.

I think the smart classes are going to be sort of the mobile phone, kind of always on the next version of the next computing platform.

And the mixed reality headsets are going to be more like your workstation or your game console where when you're sitting down for a more immersive session and you want access to more compute, I mean, look, I mean, the glasses are just very small form factor.

There are going to be a lot of constraints on that, just like you can't do the same level of computing on a phone.

It came at exactly the time when all of these breakthroughs and generative AI happened.

Yeah, so we basically, for smart glasses, we've been going at the problem from two different directions.

On the one hand, we've been building what we think is sort of the technology that you need for the kind of ideal holographic AR glasses.

And we're doing all the custom silicon work, all the custom display stack work, like all the stuff that you would need to do to make that work.

And they're glasses, right?

It's not a headset.

It's not like a VRMR headset.

They look like glasses.

But there's still quite a bit far off from the glasses that you're wearing now.

I mean, those are very thin.

But even the Raybans that we make, you couldn't quite fit all the tech that you need to into that yet for kind of full holographic AR.

We're getting close and over the next few years, I think we'll basically get closer.

It'll still be pretty expensive, but I think that'll start to be a product.

The other angle that we've come at this is let's start with good looking glasses.

By partnering with the best glasses maker in the world, Estler Luxotica, they basically make, they have all the big brands that you use, you know, with Raybans or Oakley or Oliver Peoples or just like a handful of others.

It's kind of all Estler Luxotica.

The Nvidia glasses.

I think that, you know, it's, I think they would probably like that analogy.

But I mean, who wouldn't?

Who wouldn't at this point?

So we've been working with them on the Raybans.

We're on the second generation.

And the goal there has been, okay, let's constrain the form factor to just something that looks great.

And within that, let's put in as much technology as we can, understanding that we're not going to get to the kind of ideal of what we want to fit into it technically.

But it'll, but at the end, it'll be like great looking glasses.

And we, at this point we have, we have camera sensors so you can, you can take photos and videos, you can actually live stream to Instagram, you can take video calls on WhatsApp and stream to the other person, you know, what you're seeing.

You can, I mean, it has, it has a microphone and speaker.

So I mean, the speaker's actually really good.

It's like, it's open ears.

So a lot of people find it more comfortable than, than earbuds.

You can listen to music and it's just like this private experience.

That's pretty neat.

People love that. calls on it.

But then it just turned out that that sensor package was exactly what you needed to be able to talk to AI, too.

So that was sort of an accident.

If you'd asked me five years ago were we going to get holographic AR before AI, I would have said, yeah, probably.

I mean, it just seems like the graphics progression and display progression on all the virtual and mixed reality stuff and building up the new display stack-- we're just making continual progress towards that.

And then this breakthrough happened with LLMs.

And it turned out that we have sort of really high quality AI now and getting better at a really fast rate before you have holographic AR.

So it's sort of this inversion that I didn't really expect.

I mean, we're fortunately well positioned because we were working on all these different products.

But I think what you're going to end up with is just a whole series of different potential glasses products at different price points with different levels of technology in them.

So I kind of think based on what we're seeing now with the Ray Ban Meadows, I would guess that displayless AI glasses at a $300 price point are going to be a really big product that tens of millions of people or hundreds of millions of people eventually are going to have.

And then-- So you're going to have super interactive AI that you're talking to.

Yeah.

You have visual language understanding that you just showed.

You have real time translation.

You could talk to me in one language.

I hear it in another language.

And then the display is obviously going to be great too.

But it's going to add a little bit of weight to the glasses.

And it's going to make them more expensive.

So I think there will be a lot of people who want the kind of full holographic display.

But there are also going to be a lot of people for whom they want something that eventually is going to be really thin glasses.

Well, for industrial applications and for some work applications, we need that.

We need that for consumer stuff too.

You think so?

Yeah.

I think I was thinking about this a lot during COVID when everyone kind of went remote for a bit.

I was like, you're spending all this time on Zoom.

I'd say, OK, this is-- like, it's great that we have this.

But in the future, we're like not them in years away from being able to have a virtual meeting where it's like, I'm not here physically.

It's just my hologram.

And it just feels like we're there.

And we're physically present.

We can work on something and collaborate on something together.

But I think this is going to be especially important with AI.

If that's a vacation, I could live with a device that I'm not wearing all the time.

Oh, yeah.

But I think we're going to get to the point where it actually is.

It'll be-- I mean, within glasses, there's thinner frames and there's thicker frames and there's all these styles.

But so I think we're a while away from having full holographic glasses in the form factor of your glasses.

But I think having it in a pair of stylish, kind of chunkier frame glasses is not that far off.

These sunglasses are a little face size these days.

I could see that.

Yeah.

And you know what?

That's a very helpful style.

Yeah, exactly.

That's a very helpful style.

So whoever you know, it's like-- I'm trying to make my way into becoming a style influencer so I can influence this before the glasses come to the market.

But I don't know.

Well, I could see you attempting it.

How's your style influencing working out for you?

No, it's early.

Yeah.

[LAUGHTER] It's early.

It's early.

But I don't know.

I feel like if a big part of the future of the business is going to be building kind of stylish glasses that people wear, this is something I should probably start paying a little more attention to.

Right then.

Totally agree.

We're going to have to retire the version of me that wore the same thing every day.

But I mean, that's the thing about glasses, too.

I think it's unlike even the watch or phones.

People really do not want to all look the same.

And so I do think that it's a platform that I think is going to lend itself, going back to the theme that we talked about before, towards being an open ecosystem.

Because I think the diversity of form factors and styles that people are going to demand is going to be immense.

It's not like everyone is not going to want to put the one kind of pair of glasses that whoever else designs.

That's not-- I don't think that's going to fly for this.

Yeah.

I think that's right.

Well, Mark, it's sort of incredible that we're living through a time where the entire computing stack is being reinvented.

How we think about software, what Andre calls software 1 and software 2, and now we're basically in software 3 now, the way we compute from general purpose computing to these generative neural network processing way of doing computing, the capabilities, the applications we could develop now are unthinkable in the past.

And this technology, generative AI, I don't remember another technology that in such a fast rate influenced consumers, enterprise, industries, and science.

And to be able to cut across all these different fields of science from climate tech to biotech to physical sciences, in every single field that we're encountered, generative AI is right in the middle of that fundamental transition.

And in addition to that, the things that you're talking about, generative AI is going to make a profound impact in society, the products that we're making.

And one of the things that I'm super excited about, and somebody asked me earlier, is there going to be a Jensen AI?

Well, that's exactly the creative AI you were talking about, where we just build our own AI's.

And I load it up with all of the things that I've written.

And I fine-tune it with the way I answer questions.

And hopefully, over time, the accumulation of use becomes a really, really great assistant and companion for a whole lot of people who just wants to ask questions or bounce ideas off of.

And it'll be the version of Jensen that, as you were saying earlier, that's not judgmental.

You're not afraid of being judged.

And so you could come and interact with it all the time.

But I just think that those are really incredible things.

And we write a lot of things all the time.

And how incredible is it just to give it three or four topics?

These are the basic themes of what I want to write about and write it in my voice and just use that as a starting point.

So there's just so many things that we can do now.

It's really terrific working with you.

And I know that it's not easy building a company.

And you pivot at yours from desktop to mobile to VR to AI, all these devices.

It's really, really, really extraordinary to watch.

And NVIDIA has pivoted many times ourselves.

And I know exactly how hard it is doing that.

And both of us have gotten kicked in our teeth a lot, plenty over the years.

But that's what it takes to want to be a pioneer and innovate.

So it's really great watching you.

Well, thank you.

[APPLAUSE] And likewise, I mean, it's not sure if it's a pivot if you keep doing the thing you were doing before.

But it's as well.

But you add to it.

I mean, there's more chapters to all this.

And I think the same thing for-- it's been fun watching the journey that you guys have been on.

We went through this period where everyone was like, now, everything is going to move to these devices.

And it's just going to get super cheap compute.

And you guys just kept on plugging away at this.

And it's like, no, actually, you're going to want these big systems that can paralyze-- We went the other way.

Yeah, no.

Yeah.

We went-- instead of building smaller and smaller devices, we made computers as accessible for a while.

A little unfashionable.

Super unfashionable.

Yeah.

But now it's cool.

And instead of-- we started building a graphics chip, a GPU.

And now, when you're deploying a GPU, you still call it Hopper, H100.

So you guys know when Zuck calls it H100, his data center of H100s, there's like, I think you're coming up on 600,000.

And they're-- We're good customers.

[LAUGHTER] That's how you get the Jensen Q\&A at SIGGRAPH.

[LAUGHTER] Wow.

Hang on, I was getting the Mark Zuckerberg Q\&A.

You were my guest.

I wanted to make sure that Mark-- It's cold one day.

And you're like, hey, yeah, you know, in like a couple of weeks we're doing this thing at SIGGRAPH.

I'm like, yeah, I don't think I'm doing anything that day.

I'll find a Denver.

It sounds fun.

Exactly.

So I'm not doing anything that afternoon just showed up.

And-- but the thing is just incredible, these systems that you guys build.

They're giant systems, incredibly hard to orchestrate, incredibly hard to run.

And you said that you got into the GPU journey later than most, but you're operating larger than just about anybody.

And it's incredible to watch.

And congratulations to everything that you've done.

And you are quite the style icon now.

Check out this guy.

Early stage working on it.

Ladies and gentlemen, Mark Zuckerberg.

Thank you.

[APPLAUSE] Hang on, hang on.

Well, you know, so it turns out the last time that we got together after dinner, Mark and I were-- Jersey swap.

Jersey swap.

And we took a picture and it turned into something viral.

And-- [LAUGHTER] Now, I thought that he has no trouble wearing my jacket.

I don't know.

Is that my look?

[LAUGHTER] I don't think I can-- Should be.

Should be.

Is that right?

Yeah.

Actually, I made one for you.

You did?

You did?

Yeah.

That one's Mark's.

I mean, hey, let's say we got a box back here.

It's black and leather and shearling.

Oh!

[LAUGHTER] [APPLAUSE] I didn't make this.

I just ordered it online.

Hang on a second.

Hang on a second.

It's a little chilly in here.

I think I'll try this on.

I think this is my goodness.

I mean-- It's a vibe.

You just need-- Is this me? --will be pretty-- I mean-- get this guy a chain.

All right.

Next time I see him bring your gold chain.

So fair is fair.

So I let you know-- I was telling everybody that Laurie bought me a new jacket to celebrate this year's SIGGRAPH.

SIGGRAPH is a big thing in our company, as you could imagine.

RTX was launched here.

Amazing things that were launched here.

And this is a brand new jacket.

It's literally two hours old.

Wow.

And so I think we got a jersey swap again.

All right.

Well-- This one's yours.

I mean, this is worth more because it's used.

[LAUGHTER] What?

[LAUGHTER] Let's see.

I don't know.

I think Mark is pretty buff.

He's the guy who's pretty jacked.

I mean, you two, man.

[LAUGHTER] All right.

All right, everybody.

Thank you.

Gentlemen, Mark Zuckerberg.

Have a great SIGGRAPH.

[APPLAUSE] (upbeat music) (upbeat music)