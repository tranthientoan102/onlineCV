# Data Engineer - Transport for NSW (Job #107904)
**Location:** Macquarie Park NSW | **Closes:** Check JD for deadline

---

## Q1: Can you provide an example of how you have communicated a controversial or complicated message related to a data engineering aspect to both internal and external stakeholders? How did you approach this? What choices did you make to ensure the message was received well? What could you have done differently to be even more effective?

At eHealth NSW, I faced a significant communication challenge when I proposed replacing the existing Mirth Connect and sTunnel integration stack — which had been in place for years — with a cloud-native Java REST API service. This was a controversial message. The existing stack touched critical clinical data flows across multiple live environments, and in a healthcare setting, any architectural change carries real operational risk. I was communicating this to both engineers who understood the system deeply and to clinical project managers and system owners who cared only about data reliability and continuity.

**My approach: separate each concern before addressing any of them**

Rather than presenting the full picture at once and asking stakeholders to hold all of it simultaneously, I broke the message into three distinct, independently addressable concerns — each with its own evidence and its own audience.

**Concern 1 — Technical (for engineers):** I focused entirely on why the existing architecture was becoming unsustainable: tight coupling between environments, manual configuration drift across PJX, REL, SUP and PRD, and no viable CI/CD path for updates. I ran a parallel POC and presented measured benchmarks — processing speed, memory footprint, and deployment complexity — to ground the conversation in evidence rather than preference. This was a peer-level technical discussion with no business framing.

**Concern 2 — Operational (for team leads and project managers):** I reframed the message entirely. Not "we want to change the architecture" but "we want to reduce the manual effort and error risk that the current system creates." I quantified the number of manual configuration steps per environment change, and showed how the proposed solution would replace them with a single deployable artefact. The word "rewrite" never appeared in that conversation.

**Concern 3 — Interface continuity (for clinical system owners):** I separated this concern from the architectural decision entirely. The message was simple: the HL7 message formats, delivery guarantees, and integration endpoints would be identical. The change would be invisible to their systems. I provided a side-by-side comparison of input/output message structures to confirm nothing changed from their perspective.

By isolating each concern and matching it with the right evidence for that audience, I avoided the common failure mode of either oversimplifying the technical case or overwhelming non-technical stakeholders with architecture diagrams that weren't relevant to their decision.

**What I could have done differently:** I moved through the POC phase quickly and could have involved clinical system representatives earlier — even just to validate the interface continuity assumption before finalising the design. Getting that sign-off earlier would have reduced the back-and-forth at the review stage and shortened the overall approval cycle.

---

## Q2: Tell us about a time when you worked in a team that was not functioning effectively, experiencing collaboration challenges. How did you identify the root causes, influence improvements, how effective were you? And what was the overall impact on delivery?

At NSWHP, I was part of a cross-functional team working on a complex clinical data migration project that involved data migration engineers, DevOps engineers, and clinical interface specialists — three groups with different toolsets, different delivery cadences, and different definitions of success. Over time, the team started missing milestones. Handoffs were failing, blockers weren't surfacing until they had already delayed downstream work, and there was visible tension building between the streams.

**Identifying root causes: treat the dysfunction as separate problems, not one**

Rather than diagnosing this as a single "team culture" issue — which would have been unactionable — I tried to isolate the underlying causes as distinct, independent concerns and address each one on its own terms.

**Root cause 1 — Ownership ambiguity:** Nobody had a complete picture of who was responsible for each stage of the pipeline. Extracted data files were sitting unprocessed because both the migration team and the integration team assumed the other had picked them up. I drafted an explicit handoff map — a simple diagram of pipeline stages with a named owner for each — and walked each team through it to get agreement. Once each team could see exactly where their responsibility started and ended, the invisible gaps became visible and fixable.

**Root cause 2 — Communication latency:** Blockers were being raised in weekly standups rather than as they occurred. By the time a blocker was on the table, it had already caused days of downstream delay. I proposed a lightweight daily async update on Slack — three lines per person: what's done, what's next, what's blocked. Critically, blockers required a same-day response from the relevant team. This didn't add meeting overhead but dramatically shortened the time between a problem appearing and someone acting on it.

**Root cause 3 — Technical coupling:** Some pipeline stages were tightly coupled in a way that meant one team couldn't test their work without the other having completed theirs. I proposed decoupling the test fixtures so that each team could validate their own stage independently using agreed sample data. This is a direct application of separation of concern at the technical level — and it unblocked two parallel workstreams that had been stuck waiting on each other.

**Root cause 4 — No shared definition of done:** What the migration team considered "complete" output wasn't what the integration team needed to start. We introduced a per-stage handoff checklist — a short, agreed list of what constituted a valid handoff — so each team had a concrete target and the receiving team had a basis for accepting or querying the output.

**Effectiveness and impact:** The combination of the ownership map and the async update cadence had a visible effect within two weeks — blockers surfaced faster, the two main delivery streams stopped operating in silos, and we recovered roughly two weeks of lost schedule over the following month.

**What I would do differently:** I would establish these structures at the start of the project, not after dysfunction becomes visible. Ownership maps, handoff checklists, and communication norms are cheap to build at kickoff and expensive to retrofit mid-delivery. I've carried that lesson into every multi-team engagement since.
