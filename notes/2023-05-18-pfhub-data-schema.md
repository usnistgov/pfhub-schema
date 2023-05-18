# 2023-05-18 PFHub Data & Schema Musings

[![hackmd-github-sync-badge](https://hackmd.io/kkgyfcoJTDWphNh3TRqAKg/badge)](https://hackmd.io/kkgyfcoJTDWphNh3TRqAKg)

Attendees:

- Daniel Wheeler
- Yannick Congo
- Trevor Keller

## Agenda

Discuss [PFHub], [MaRDA], [OPTIMADE], [RO-Crate], and [PFHub Schema].

* Specific LinkML schema implementation:
  <https://github.com/usnistgov/pfhub-schema/blob/main/src/pfhub_schema/schema/pfhub_schema.yaml>

<!-- links -->
[PFHub]: https://pages.nist.gov/pfhub
[PFHub Schema]: https://github.com/usnistgov/pfhub-schema
[MaRDA]: https://www.marda-alliance.org
[OPTIMADE]: https://www.optimade.org
[RO-Crate]: https://www.researchobject.org/ro-crate/

## Resources

Example working group: [MaRDA Extractors](https://github.com/marda-alliance/metadata_extractors)

## Questions

- What's unique about phase field data?
- Why is this necessary?
- Can Yannick provide a list of tools that capture simulations so that we have a reference of similar schema?
  - Sumatra
  - CoRR
  - Optimade
- Is there something obvious that we're missing?
- Will this serve a purpose and will people adopt it?
- Can we imagine what the data might be used for (Jon's question)?
- Is a "Phase Field Schema group" the right level. 

## The Schema

We need a modest goal.

1. The description of the mathematical problem being solved
   - This could just be a link to a description such as a notebook
2. The most boring metadata: who, why, when
3. Metadata about the compuation
   - link to an environment
   - link to input files
   - how long, how much memory
   - description of numerical technique (to make PFHub more searchable 
     for example)
4. The data
   - a way to describe the data and its location
 
## What do we need for the proposal?

### Working Group Members

### Work plan

### Goals and Expected Impact

### Deliverables

- a suggested schema
- a tool to lint schema and data
- a simple tool to display some examples of the and data
- implementation as part of PFHub
- an easy way to register schema uploads
- example of using schema on Zenodo, other databases
