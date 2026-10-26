# OpenFAST self-study syllabus

**Duration:** 8 weeks, five 2.5-hour evenings per week (100 core hours).
**Optional extensions:** up to 20 additional hours across the course.
**Research focus:** blade aerodynamic loading of floating offshore wind turbines in irregular sea states.

## Aim and scope

Develop independent, research-ready proficiency in configuring, running, checking, and interpreting relevant OpenFAST simulations. Refresh undergraduate theory as it becomes necessary. Expertise across the entire code is a longer-term goal.

Core modules: AeroDyn, InflowWind, ElastoDyn, ServoDyn with ROSCO, SeaState, HydroDyn, and MoorDyn. Include working knowledge of the glue code and module coupling. BeamDyn, OLAF, linearization, and advanced hydrodynamics are extensions.

Use Python for analysis; MATLAB is welcome for checks. Use the IEA Wind 15-MW reference turbine with the UMaine VolturnUS-S semisubmersible. Obtain the model from the [official repository](https://github.com/IEAWindSystems/IEA-15-240-RWT): the floating configuration is in `OpenFAST/IEA-15-240-RWT-UMaineSemi/` and shared turbine inputs are in `OpenFAST/IEA-15-240-RWT/`. Keep a separate upstream checkout in WSL, preserve its relative paths, and record the chosen commit. Keep the baseline unchanged and document exercise-specific variants in the course repository.

**Compatibility checkpoint:** as checked on 26 October 2026, upstream release [v1.1.18](https://github.com/IEAWindSystems/IEA-15-240-RWT/releases/tag/v1.1.18) targets OpenFAST 4.2.0, and the current [test environment](https://github.com/IEAWindSystems/IEA-15-240-RWT/blob/28ae083f6e4d2e2e4ea35ac9100fcab104940484/tests/environment.yml) specifies OpenFAST <5.0 and ROSCO >=2.10.1. Compatibility with the installed v5.0.0 build is not yet established. Week 1 must establish a working version combination or a checked conversion before physics exercises begin.

## Weekly rhythm

| Evening | Activity | Time |
| --- | --- | --- |
| 1 | Targeted reading, theory refresher, and predictions | 2.5 h |
| 2 | Guided setup and experiment | 2.5 h |
| 3 | Independent variation or troubleshooting exercise | 2.5 h |
| 4 | Analysis, interpretation, and numerical checks | 2.5 h |
| 5 | Short report, assessment, and review | 2.5 h |

Reading and reporting fit within these hours. Keep case matrices small; long runs can continue unattended. Reduce optional work if setup or analysis takes longer than expected.

For each exercise: state the question, predict the result, configure the case, run it, check it, and explain the outcome. Commit an initial attempt before consulting a worked solution. Use documentation freely; request hints before complete implementations.

## Week 1 — Architecture and a reproducible baseline

**Refresh:** degrees of freedom, coordinate systems, units, and the distinction between aerodynamic and structural loads.

**Practice:** inspect the installed executable and source provenance, including the reported `OpenFAST-v5.0.0-dirty` suffix. Record executable identity, source commit and local changes where available, model revision, controller version, and Python environment in your Week 1 notes. Clone the official IEA 15-MW repository and inspect the VolturnUS-S model, shared turbine inputs, hydrodynamic data, and ROSCO controller inputs. Resolve compatibility with the installed OpenFAST version and the matching Linux ROSCO library; document any input conversion. Run a small documented case and a compatible IEA 15-MW/VolturnUS-S floating baseline; map the input dependencies and active modules. Read warnings, summary files, and selected outputs. Diagnose a deliberately broken input path.

**Completion:** reproduce selected reference channels, explain any differences, identify the origin and frame of each plotted quantity, and explain the enabled degrees of freedom without AI-generated setup instructions. A regression comparison checks reproducibility, not physical validity.

**Reading:** [working with OpenFAST](https://openfast.readthedocs.io/en/main/source/working.html), [regression testing](https://openfast.readthedocs.io/en/main/source/testing/regression_test.html), and the reference turbine report [R1].

## Week 2 — Steady blade and rotor aerodynamics

**Refresh:** velocity triangles, induction, lift and drag, airfoil polars, tip-speed ratio, and power/thrust coefficients.

**Practice:** use the AeroDyn driver with uniform inflow, prescribed rotor speed, and blade pitch. Vary tip-speed ratio and blade pitch over a small case matrix. Reconstruct the force at one blade section from documented local quantities, coordinate conventions, and polars. Examine spanwise loading and perform a blade-discretization sensitivity check.

**Completion:** explain the performance trends, reconcile the section calculation with the model, and distinguish sectional aerodynamic forces, integrated rotor loads, and structural blade-root moments.

**Reading:** [AeroDyn theory, coordinates, and inputs](https://openfast.readthedocs.io/en/main/source/user/aerodyn/index.html), [AeroDyn driver](https://openfast.readthedocs.io/en/main/source/user/aerodyn/driver.html), and the relevant aerodynamic data in [R1].

## Week 3 — Aerodynamic response to prescribed motion

**Refresh:** sinusoidal displacement versus velocity, amplitude and phase, reduced frequency, dynamic inflow, and unsteady airfoil response.

**Practice:** prescribe surge, then platform pitch, using the AeroDyn driver. Predict changes in relative velocity and angle of attack. Vary motion amplitude and frequency independently. Compare steady and dynamic induction treatments while holding the airfoil treatment fixed; then investigate the airfoil treatment separately. Check time-step sensitivity for one representative case.

**Completion:** explain load amplitude and phase at several blade stations; distinguish platform pitch from blade pitch and wake response from airfoil response. Discuss whether the operating conditions actually excite significant unsteady effects.

**Reading:** AeroDyn dynamic-inflow and unsteady-airfoil sections, driver motion inputs, and selected methods/results from UNAFLOW [R3]. Compare mechanisms and nondimensional conditions; the course rotor is not the UNAFLOW experiment.

## Week 4 — Elasticity and controller feedback

**Refresh:** modal response, damping, rotor-speed dynamics, generator torque, collective pitch control, and operating regions.

**Practice:** move from prescribed rotor conditions to appropriate coupled configurations. Compare selected rigid/flexible cases and examine response with the floating-model ROSCO controller, including any enabled floating-feedback or thrust-limiting features. Document changed degrees of freedom and operating points so comparisons remain interpretable. Use simple wind changes to connect rotor speed, blade pitch, thrust, and blade-root response.

**Completion:** explain the controller's role in each operating region and identify plausible aerodynamic, elastic, and control contributions to load changes. Explain why controller changes can alter platform response.

**Reading:** ElastoDyn, InflowWind, and [ServoDyn](https://openfast.readthedocs.io/en/main/source/user/servodyn/index.html) sections in the [module manuals](https://openfast.readthedocs.io/en/main/source/user/index.html); controller description in [R1].

## Week 5 — Floating-system mechanics and regular waves

**Refresh:** hydrostatics, added mass, radiation damping, wave excitation, viscous drag, and mooring restoring forces.

**Practice:** inspect the reference platform and hydrodynamic data. In suitable reduced configurations, check equilibrium, conduct small-amplitude free-decay tests, and investigate regular-wave response at a few periods. Identify coupled modes rather than assuming each platform coordinate is an isolated oscillator. Explain which hydrodynamic effects the configured model includes.

**Completion:** estimate dominant periods and damping with stated assumptions; explain equilibrium and frequency-dependent response. Distinguish potential-flow and Morison contributions and recognise the risk of double-counting loads.

**Reading:** [HydroDyn](https://openfast.readthedocs.io/en/main/source/user/hydrodyn/index.html), [MoorDyn](https://openfast.readthedocs.io/en/main/source/user/moordyn/index.html), SeaState regular-wave inputs, and platform definition [R2].

## Week 6 — Irregular seas and stochastic analysis

**Refresh:** spectral density, spectral moments, significant wave height, peak period, sampling, stationarity, and random realisations.

**Practice:** configure a JONSWAP sea using SeaState. Check the realised elevation spectrum and the approximate relation `Hs = 4 sqrt(m0)`. Examine wave-to-platform response using spectra. Test retained duration and spectral-estimation settings; compare at least three wave seeds for one condition. Check wave-grid coverage and sensitivity. Inspect a documented turbulent inflow field and run one short comparison with steady inflow.

**Completion:** explain differences between the requested spectrum and a finite realisation, justify transient removal and retained duration, and report variability without treating a small seed ensemble as a converged extreme-load estimate.

**Reading:** [SeaState inputs](https://openfast.readthedocs.io/en/main/source/user/seastate/input_files.html), relevant HydroDyn modelling guidance, and InflowWind input/output guidance.

## Week 7 — Coupled loading and mechanism tests

**Refresh:** feedback, frequency scales, and the limits of interpreting correlation as causation.

**Practice:** run coupled wind-wave cases and compare them with carefully chosen fixed-platform or reduced configurations. Track wave elevation, platform surge/pitch, rotor speed, blade pitch, and sectional aerodynamic quantities. Use controlled changes to test one proposed explanation for a load feature. Define the Week 8 question and case matrix.

**Completion:** support a physical explanation with evidence from both blade-level and system-level outputs. State what each comparison isolates and what else it changes. Select at least one relevant published comparison and explain whether it offers a qualitative check or quantitative validation.

**Reading:** revisit [R1–R3] and the theory sections relevant to the selected mechanism.

## Week 8 — Independent mini-study

**Question:** how does wave peak period affect blade aerodynamic loading at fixed significant wave height and mean wind speed?

**Minimum scope:** two peak periods, at least three wave seeds per period, one operating point, and one justified mechanism comparison. Use steady wind initially to isolate wave-related changes. Select wave conditions within the reference model's applicability; agree the exact matrix at the end of Week 7.

**Completion:** deliver a reproducible case description, analysis, and a 3–5-page report with selected figures. Compare spanwise aerodynamic quantities and integrated/structural responses. Include relevant sensitivity evidence from earlier weeks, seed variability, model limitations, and one defensible next research question. Defend the setup and interpretation using documentation, without AI constructing the cases or explanations for you.

## Completion standard and extensions

Each week is complete when you can explain the physics, configure and diagnose the case, show appropriate checks, and reproduce the reported result. Record unresolved questions in the weekly report; revisit any that undermine subsequent work.

Optional extensions, selected to address a specific question:
- Compare BEM and OLAF for one prescribed-motion case, including wake/discretization sensitivity.
- Investigate when BeamDyn changes a blade-response conclusion.
- Explore linearization, misaligned wind/waves, or second-order hydrodynamics when the required inputs are available.

Do not fit all extensions into the core schedule. Source-code development, controller design, hydrodynamic coefficient generation, and OpenFOAM/LES are outside this course.

## Reference reading and version discipline

Use manuals alongside the lessons; read only the sections needed for the current experiment.

- **[R1]** Gaertner et al. (2020), [Definition of the IEA 15-Megawatt Offshore Reference Wind Turbine](https://docs.nlr.gov/docs/fy20osti/75698.pdf).
- **[R2]** Allen et al. (2020), [Definition of the UMaine VolturnUS-S Reference Platform Developed for the IEA Wind 15-Megawatt Offshore Reference Wind Turbine](https://docs.nlr.gov/docs/fy20osti/76773.pdf).
- **[R3]** Fontanella et al. (2021), [UNAFLOW: a holistic wind tunnel experiment about the aerodynamic response of floating wind turbines under imposed surge motion](https://wes.copernicus.org/articles/6/1169/2021/).

The linked `main` documentation can evolve. Match input formats and model options to the actual executable and source revision; use the corresponding source documentation when necessary. Pin the IEA model and ROSCO versions, and record any conversion separately from physical changes. Repository updates can change properties from those in the original reports; use the pinned input deck as the numerical baseline. Use matching OpenFAST regression data for installation checks.
