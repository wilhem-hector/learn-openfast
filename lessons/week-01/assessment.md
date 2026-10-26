# Week 1 assessment

Use documentation, but answer in your own words before asking the tutor for feedback. Spend about 45 minutes on this assessment and the short weekly synthesis.

## Explain

1. Trace one path from the main `.fst` file to an airfoil or hydrodynamic data file. From which directory is each relative path resolved?
2. Explain the difference between activating a module and enabling a structural degree of freedom. Give an example of each from your case.
3. Describe the wave → platform motion → blade loading → platform response interaction. Why is the input-file tree not a description of the coupling algorithm?
4. Distinguish platform pitch from blade pitch, and an aerodynamic section force from a structural root moment. Explain the frame of one actual output you plotted.
5. Distinguish integration time step, output interval, and total duration. Which did Exercise 4 change? What numerical questions remain unanswered?
6. What does the reported `dirty` suffix establish, and what does it leave uncertain about your executable?
7. Why does a repeatable, successfully completed run not prove physical validity? What can you legitimately conclude from a 60–120 s startup record?

## Demonstrate

Using your notes, reproduce the target floating case and locate:
- The executable identity, upstream model revision, controller version, and input changes.
- The active modules and degrees of freedom.
- Three checked outputs with units and frame/measurement definitions.
- The repeated-run comparison and controlled-sampling experiment.
- Both deliberate faults and the repaired result.

If no published baseline output matches the exact model/software combination, state this limitation. Repeating your own run checks repeatability; it is not an independent reference comparison.

## Submit and review

Use one notebook or Markdown record in `work/week-01/` and a brief `reports/week-01.md` synthesis: what ran, what you learned, the key evidence, and remaining questions. Three well-chosen figures are sufficient. Link the report from the progress record.

Week 1 is complete when all four are supported by evidence:
- **Setup:** a reproducible, compatible IEA 15-MW/VolturnUS-S case.
- **Understanding:** correct explanations of file dependencies, modules, degrees of freedom, frames, and sampling.
- **Checks:** inspected logs and outputs, repeatability evidence, and controlled comparison.
- **Independence:** diagnosis and repair of both faults, plus a defensible explanation of what the results do and do not show.

Where an explanation or check is missing, revise that part and repeat the relevant exercise. Do not rerun unrelated work.
