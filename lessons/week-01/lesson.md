# Week 1 — From installation to an explainable simulation

**Budget:** five 150-minute sessions. Start with Session 1; you do not need to read every exercise in advance.

**Outcome:** identify exactly what software and model you ran, trace its inputs, interpret selected outputs, reproduce a result, and diagnose simple failures.

## How to work

Read the assigned sections, write your prediction or initial explanation, attempt the exercise, then discuss your evidence with the tutor. Ask for a hint when stuck; use worked solutions after your attempt. Keep unanswered questions visible.

Use [environment.md](../../environment.md) for installation facts and one notebook or Markdown record in `work/week-01/` for exercise answers. Save a short final synthesis in `reports/week-01.md`. These are outputs you create while learning, not extra templates to complete beforehand.

Run copied cases, preserving the upstream directory layout and shared inputs. Keep generated files in `runs/week-01/` or a recorded WSL working directory. Record all input changes and upstream revisions so ignored working copies remain reproducible.

## The concepts you need this week

OpenFAST couples physics modules through a coordinating glue code. The main `.fst` file selects modules and references their inputs. An input-file dependency tree describes where data lives; it is not a time-ordered description of how the physics is solved. Motion affects aerodynamic and hydrodynamic loads, while those loads affect motion.

A module switch selects a model; a degree-of-freedom switch selects which motions the structural model can represent. Disabling a degree of freedom changes the physical system. Disabling a load-producing module is a different change.

An output name is insufficient to interpret a signal. Establish its producing module, units, coordinate frame, sign convention, and location. An aerodynamic blade-section force and a structural blade-root moment answer different questions.

Distinguish the integration time step, output sampling interval, and simulation duration. Frequent saved samples do not prove integration accuracy; a long file does not prove the initial transient has decayed. A repeatable simulation can still represent the wrong physics.

Use the [module manuals](https://openfast.readthedocs.io/en/main/source/user/index.html) and the selected executable's source documentation to check these concepts against the actual files. Online documentation can differ from your pinned version.

## Session 1 — What exactly is installed?

**Read:** the version and execution sections of [Working with OpenFAST](https://openfast.readthedocs.io/en/main/source/working.html), then the requirements in the [IEA turbine README](https://github.com/IEAWindSystems/IEA-15-240-RWT).

**Do:** [Exercise 1](exercises.md#exercise-1--environment-audit).

**Time:** 20 min reading, 20 min concept review, 75 min audit, 25 min recording evidence, 10 min next-step note.

**Stop when:** the environment record distinguishes measured facts from unknowns and identifies the compatibility question. A successful floating run is not required tonight.

## Session 2 — How is the model assembled?

**Read:** the top-level `.fst` and referenced ElastoDyn, ServoDyn, SeaState, HydroDyn, and MoorDyn files; skim only their relevant manual sections. Consult the turbine report's overview and main-parameter table.

**Do:** [Exercise 2](exercises.md#exercise-2--trace-the-model).

**Time:** 20 min reading, 20 min concept review, 80 min tracing/setup, 20 min explanations, 10 min next-step note.

**Stop when:** you can trace shared inputs and the controller, explain active modules and degrees of freedom, and have either a working startup check or an actionable compatibility diagnosis.

## Session 3 — What does a successful run tell you?

**Read:** quick start, troubleshooting, and output-visualization sections in Working with OpenFAST; inspect your case's output settings and header.

**Do:** [Exercise 3](exercises.md#exercise-3--run-and-interpret).

**Time:** 15 min reading, 15 min predictions, 85 min running/plotting, 25 min interpretation, 10 min next-step note.

**Stop when:** you can reproduce the run and explain three signals, including their limits as evidence.

## Session 4 — What changes when you save fewer samples?

**Read:** the documentation for the selected main-file output interval and output format. Revisit sampling, aliasing, and integration versus observation.

**Do:** [Exercise 4](exercises.md#exercise-4--controlled-output-sampling).

**Time:** 15 min reading, 20 min prediction, 80 min experiment, 25 min comparison, 10 min next-step note.

**Stop when:** your comparison separates output sampling from numerical integration and makes no unsupported convergence claim.

## Session 5 — Can you explain and repair the setup?

**Read:** your own notes and the troubleshooting guidance; avoid reading ahead for a fix.

**Do:** [Exercise 5](exercises.md#exercise-5--diagnose-and-repair), then [the assessment](assessment.md).

**Time:** 10 min recap, 15 min prediction, 60 min diagnosis/repair, 45 min assessment and synthesis, 20 min progress update and review.

**Stop when:** the evidence meets the assessment criteria, or your progress record names the specific remaining gap.

## If setup takes longer

Time-box unsupported input conversion or controller setup to 45 minutes per session. Save the exact command, first useful error, versions, and your diagnosis; bring this evidence to the tutor. Continue input tracing while resolving the runtime issue.

A version-matched small OpenFAST example may support output and troubleshooting practice meanwhile. This is an installation exercise, not a replacement for the IEA 15-MW research model. If you use it, label it explicitly. Week 1 remains incomplete until the target floating baseline and its compatibility are checked.

**Next week:** steady rotor and sectional aerodynamics, using the established IEA rotor data.
