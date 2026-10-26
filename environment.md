# Environment

Fill this in during Week 1 using evidence from WSL. Reported details have not yet been independently verified.

| Item | Current record |
| --- | --- |
| Runtime | WSL; distribution and version to record |
| OpenFAST version | Reported: `OpenFAST-v5.0.0-dirty` |
| OpenFAST executable | Absolute path and file checksum to record |
| OpenFAST source | Commit, local changes, and build/compiler details to record if available |
| Turbine / platform | IEA Wind 15-MW / UMaine VolturnUS-S |
| Model source | [IEAWindSystems/IEA-15-240-RWT](https://github.com/IEAWindSystems/IEA-15-240-RWT); local path, tag, and commit to record |
| Controller | ROSCO; installed version, Linux library path, and matching DISCON input to verify |
| Analysis | Python; interpreter, environment, and package versions to record |
| Compatibility | Unverified; see the checkpoint in [syllabus.md](syllabus.md) |
| Baseline run | Not yet verified; record command, case, duration, warnings, and outcome |

## First exercise

1. Identify the WSL distribution and exact OpenFAST executable being used.
2. Inspect build provenance and the reason for the reported `dirty` suffix. Preserve local changes.
3. Locate or clone the turbine repository in WSL; record its revision and preserve shared input paths.
4. Identify the ROSCO library and controller input version. Establish a compatible executable/model/controller combination.
5. Run a short startup check, then record the evidence here. A successful startup does not establish numerical convergence or physical validity.

## Verification notes

To complete during the first exercise. Include commands and key output; do not record credentials.
