# Week 1 exercises

Attempt these in order, one per evening. Use documentation freely. Save predictions before running and add observations afterwards. No full solutions are included.

## Exercise 1 — Environment audit

**Question:** could another researcher identify and reproduce your software/model combination?

1. Fill the measured fields in [environment.md](../../environment.md). Identify the actual WSL distribution, executable, Python interpreter, and available source checkout.
2. Inspect the build version, source commit, and local changes if the source is available. The reported `dirty` suffix is a provenance clue, not a diagnosis of a broken solver. A current source checkout may differ from the one used to build the executable; record that uncertainty.
3. Locate or clone the [IEA turbine repository](https://github.com/IEAWindSystems/IEA-15-240-RWT) separately in WSL. Record its commit; retain the common turbine folder and floating-model folder together.
4. Inspect the floating `DISCON.IN` header and ServoDyn library path. Distinguish the requested ROSCO input version from evidence of the installed controller binary.
5. State the compatibility issue and your proposed resolution. The upstream release/test requirements are linked in the syllabus; do not assume v5 accepts an older deck unchanged.

Useful read-only Bash checks, run in WSL:

```bash
cat /etc/os-release
command -v openfast
python --version
```

If OpenFAST is not on PATH, locate your known executable and use its absolute path. Consult its help banner. In the relevant source checkout, use `git rev-parse HEAD`, `git status --short`, and `git diff`. Obtain a binary checksum with `sha256sum` and its actual path.

**Save:** the environment table, supporting command output, and a short compatibility diagnosis. Do not reset source changes or upgrade components speculatively.

## Exercise 2 — Trace the model

**Question:** which files and models determine the response?

1. Open `OpenFAST/IEA-15-240-RWT-UMaineSemi/IEA-15-240-RWT-UMaineSemi.fst`. Trace the enabled input references, including nested airfoil, blade, tower, hydrodynamic, and controller data.
2. Make a compact table: module, selected option, input file, principal role, and quantities exchanged. Explain why a path beginning with `../` must be interpreted relative to the referring file.
3. List enabled ElastoDyn degrees of freedom. Identify the six platform coordinates and distinguish platform yaw, nacelle yaw, platform pitch, and blade pitch.
4. Find the controller-library path and the floating controller-input file. Identify any machine-specific path that needs adapting in your working copy.
5. Adopt a documented compatible combination, preserving existing installations and recording any conversion. Run a short startup check on a copy. Record all changes separately from the untouched upstream model.

**Before running:** predict which modules initialise, which external files are needed, and which missing dependency would prevent startup.

**Save:** your dependency table, coordinate sketch, compatibility decision, and startup log or diagnosis. A startup-only run is not evidence of settled floating response.

## Exercise 3 — Run and interpret

**Question:** what evidence supports calling this run successful?

1. Make a documented working case from the compatible baseline. Record input changes, model revision, executable identity, command, working directory, wind/wave settings, and random seeds where relevant.
2. Inspect duration and output settings. Run the startup check, then produce a short 60–120 s record for learning output interpretation, provided all input fields cover that interval. This duration is not prescribed for later scientific statistics.
3. Inspect the terminal log and every warning. Confirm that time reaches the requested end, requested channels exist, and numerical data are finite.
4. Select three available channels: rotor speed, a platform motion, and one load. Identify each channel's module, units, frame, sign, and location from the version-matched documentation. Request missing outputs explicitly.
5. Load the output in Python or MATLAB and make three labelled time-series plots. A documented reader is acceptable; if using text output, inspect the header before deciding where numerical rows begin.
6. Repeat the identical case. Compare the selected channels quantitatively at matching times. Explain discrepancies rather than assuming exact agreement across different builds or hardware.

**Before running:** predict the initial values from the inputs where possible. State what you expect to be transient and what evidence you would need to establish stationarity.

**Save:** plots, analysis code/notebook, the run record, and repeatability evidence. Explain why a structural root moment cannot by itself establish the aerodynamic mechanism. Do not treat short-record averages or peaks as representative sea-state statistics.

## Exercise 4 — Controlled output sampling

**Question:** does saving fewer samples change the underlying response or your ability to observe it?

1. From the working case, make an otherwise identical variant with output interval twice the original interval. If the original uses `default`, determine its effective value first.
2. Keep the integration step, module/controller timing, physical settings, seeds, initial conditions, and duration unchanged. Verify that the new output interval is valid for your version.
3. Use the same text precision or binary format for both cases. Predict the sample count and what should happen at shared sample times.
4. Overlay rotor speed and platform motion; compute differences at common saved times with a stated tolerance. Compare sample counts and visible extrema. Do not invent a difference when the signal is sufficiently slow.
5. Explain what sampling could hide, why interpolation cannot recover lost information, and why this test does not demonstrate time-step convergence.

**Save:** a table of changed and held-fixed settings, the comparison, and a short conclusion.

**Optional, within spare time:** halve the integration step with a common output interval and controlled module/controller timing. Explain why this is a different experiment, and why two short runs are insufficient to establish general convergence.

## Exercise 5 — Diagnose and repair

**Question:** can you locate the cause using evidence rather than trial-and-error edits?

Use disposable copies of the working case; introduce one fault at a time.

1. Change one enabled input-file reference to a nonexistent filename. Before running, predict the failure stage. Run, identify the first informative error and the referring file, then repair it.
2. Request a clearly nonexistent output channel in one module. Predict whether it will abort or warn; observe the actual version's behaviour and whether the channel appears in the output. Repair the request.
3. Re-run the repaired case and compare selected channels with the original working result.

**Save:** for each fault, record symptom, first useful message, cause, repair, and evidence of recovery. Keep these separate from the numerical-baseline comparison.

**Finish:** complete [assessment.md](assessment.md). Update [progress.md](../../progress.md) with evidence and unresolved questions; do not mark an exercise complete solely because it ran.
