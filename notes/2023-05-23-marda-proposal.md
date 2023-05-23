# MaRDA Proposal for Phase Field Schema

[![hackmd-github-sync-badge](https://hackmd.io/i0_rypRqS5WU_I2sI4W2kg/badge)](https://hackmd.io/i0_rypRqS5WU_I2sI4W2kg)


Meeting agenda, notes, and minutes for the discussion on 23 May 2023.

Organizer
: Daniel Wheeler, NIST

Invitees
: - David Elbert, JHU
  - Olga Wodo, U. Buffalo
  - Jon Guyer, NIST
  - Trevor Keller, NIST
  - Zach Trautt, NIST
  - Jim Warren, NIST

## Background

[PFHub] and [PFHub Schema].

* [Benchmark dataset schema] implemented using [LinkML]
* Similar effort? [Data dictionaries](https://github.com/marda-dd/docs)

## Agenda

 - [Short presentation on PFHub/ phase field](https://slides.com/danielwheeler-1/bag-lunch-2023-05-24) (Daniel)
 - PFHub / LinkML usage (Trevor)
 - Feedback from David, Olga, Zach
 - Questions
     - Is phase field too specific or right level?
     - Is this likely to be adopted?
 - Possible participants?

## Meeting Notes

- We're getting smarter about _when_ to use phase-field in industry.

- DE: our scope is quite broad, and spider-like. Plan to firm that up in discussions with the community.
  - Is the goal to produce the website, or steer the community in some way?
  - What can we do first? For the schema, perfect is the enemy of good; having one is a great start.
  - Little things: 
    - new directions in PFM (encoding grain structure as a network graph)
    - homegrown codes & one-offs
    - input from practitioners outside of our group (LANL, OpenFOAM, Abaqus, ...)
      (bring these people in to meetings as plenary speakers?)
  - Brainstorming opportunity around where this work will happen: is a web form right, or should e.g. MOOSE have a function to dump `pfhub.json` directly?
    - We can implement this on open-source toolchains as PRs.
    - Convince people that this is _our community schema_, which they adopt for themselves and voluntarily write these metadata writers.
  - What are the questions we want to ask of the data?
  - Tie-in to MaRDA Extractor: when a schema changes, automagically update the data extractor. (?)
  - Motivating the community... create a false narrative or grand challenge to produce data by a number of methods, then aggregate it back together in one dataset?
    - What would a phase-field grand challenge look like?
    - JW: what kind of "prizes" would our community care about, and be willing to compete to win?

- OD: leveraging the schema for training and teaching, ...
  - Working group could find out how people might use the schema as a resource, teaching tool, in practice

- JW: schemas are most powerful in translating from one space to another.
  - If somebody wants to go from MOOSE to something else, having a schema is crucial. Possibly another way to slice the discussion.
  - Aside: [AI is better at multiplying matrices than you are.](https://www.quantamagazine.org/ai-reveals-new-possibilities-in-matrix-multiplication-20221123/)

- JG: many people see schemas a high-effort, low-return. Need to teach the potential value.
  - Shadow goal for the upcoming CHiMaD PF workshop.


## Action Items

Definitely create a working group. There's a formal application process; describe the goals, timeline (18 to 24 months).
- Should be bounded to quickly generate output that can be reported at an annual meeting (February).
- Follow-up work? Create a new working group!
- A new MaRDA website is launching soon, with better granularity on working group details.
- Olga is interested in joining the group; at least one executive council member is required for each working group.
 
<!-- links -->
[Benchmark Dataset Schema]: https://github.com/usnistgov/pfhub-schema/blob/main/src/pfhub_schema/schema/pfhub_schema.yaml
[LinkML]: https://linkml.io
[MaRDA]: https://www.marda-alliance.org
[OPTIMADE]: https://www.optimade.org
[PFHub]: https://pages.nist.gov/pfhub
[PFHub Schema]: https://github.com/usnistgov/pfhub-schema
[RO-Crate]: https://www.researchobject.org/ro-crate/
