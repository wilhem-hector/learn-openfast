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

**Question:** what does this simulation show, and what conclusions does the evidence support?

1. Use a working copy of the IEA 15-MW/VolturnUS-S case that passed your startup check: `Examples/Test_Cases/IEA-15-240-RWT/IEA-15-240-RWT-UMaineSemi/IEA-15-240-RWT-UMaineSemi.fst` in ROSCO v2.10.6. Copy the whole parent `IEA-15-240-RWT` directory to preserve shared inputs. Record the source revision, input changes, executable identity, command, working directory, wind/wave settings, and random seeds.
2. Set `TMax = 120` s and `TStart = 0` in the copied case, checking that time-dependent inputs cover that interval. Keep the physical conditions, initial conditions, controller settings, and integration step unchanged. A completed startup check need not be repeated separately.
3. Inspect the terminal log and every warning. Confirm that time reaches the requested end, requested channels exist, and numerical data are finite.
4. Select three available channels: rotor speed, a platform motion, and one load. Identify each channel's module, units, frame, sign, and location from the version-matched documentation. Request missing outputs explicitly.
5. Load the output in Python or MATLAB and make labelled time-series plots. A documented reader is acceptable; if using text output, inspect the header before deciding where numerical rows begin.
6. For a repeatability check, save the first outputs and rerun the same case on the same computer, with identical inputs, seeds, executable, and controller. Compare each selected channel at common simulation times and report its maximum absolute difference, with units. No second computer or different build is required. If you skip this check, record repeatability as not tested.

**Before running:** predict initial signal values where possible and identify which responses you expect to contain startup transients.

**Interpretation — answer these two general questions in a short paragraph each:**

- **Observation versus cause:** explain why a measured response does not necessarily identify its cause. Using one of your plots as an illustration, separate what you observe from your proposed explanation. Name an additional signal or controlled comparison that could test that explanation. You do not need to run that additional test in this exercise.
- **Record statistics versus sea-state statistics:** explain why averages and peaks from one short run may not represent the sea state as a whole. A peak is a valid statistic of this particular record; it is not automatically a characteristic or extreme value for the wider sea state. State the time window used and recognise the effects of startup, finite duration, and the particular random wave realisation. No statistical convergence study is required here.

**Save:** plots, analysis code/notebook, the run record, the two interpretation paragraphs, and repeatability results if the check was performed.

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
