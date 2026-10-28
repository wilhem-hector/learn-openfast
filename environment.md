# Environment

Fill this in during Week 1 using evidence from WSL. Reported details have not yet been independently verified.

| Item | Current record |
| --- | --- |
| Runtime | WSL; Ubuntu 24.04.5 LTS |
| OpenFAST version | Reported: `OpenFAST-v5.0.0` |
| OpenFAST executable | /home/user/openfast/build/glue-codes/openfast/openfast |
| OpenFAST source | 2895884d2be01862173c88d70f86b358d2f1a50acd |
| Turbine / platform | IEA Wind 15-MW / UMaine VolturnUS-S |
| Model source | [IEAWindSystems/IEA-15-240-RWT](https://github.com/IEAWindSystems/IEA-15-240-RWT); 28ae083f6e4d2e2e4ea35ac9100fcab104940484|
| Controller | ROSCO version 2.10.6, /home/wilhem/GitHub/ROSCO/v2.10.6/install/lib/libdiscon.so|
| Analysis | Install openfast and setup environment following https://openfast.readthedocs.io/en/main/source/install/OFcompile_WSL_VScode.html, Pandas v2.3.3 |
| Compatibility | The IEA original turbine currently does not work with OpenFAST v5.0.0. Use the IEA 15-MW/VolturnUS-S from the ROSCO v2.10.6 example |
| Baseline run | Startup log dated 28 October 2026, 14:15 UTC: reached 10/10 seconds and terminated normally.  |

## First exercise

1. Identify the WSL distribution and exact OpenFAST executable being used.
2. Inspect build provenance and the reason for the reported `dirty` suffix. Preserve local changes.
3. Locate or clone the turbine repository in WSL; record its revision and preserve shared input paths.
4. Identify the ROSCO library and controller input version. Establish a compatible executable/model/controller combination.
5. Run a short startup check, then record the evidence here. A successful startup does not establish numerical convergence or physical validity.

## Verification notes

To complete during the first exercise. Include commands and key output; do not record credentials.
