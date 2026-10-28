### Notes from exploring the IEA 15-240 RWT FOWT

1. Generally we dont need to enable echo. Its just a dianostic

# What are the modules for
1. ElastoDyn is the main structural module for the turbine. It does not represent the exact geometry. That d be BEAM Dyn
2. ServoDyn is the controller module. It sets the turbine controller parameter and uses the ROSCO toolbox to operate the controller
3. MoorDyn is the mooring dynamics module. It outputs the loads on the mooring lines
4. HydroDyn describes the hydrodynamic loads on the platform for the different DoF
5. The SeaState module allows us to define the sea the waves and currents that are hitting the platform

A path starting with ../ is interpreted relative to the referring file because they are being called from the main .fst file. We can easily point toward the connecting module from the directory where the main .fst file is

# Reference files
1. Turbine blade files. There are three of them and they refer to the same file. The latter has the distributed blade properties, and mode shapes
2. The inflow file is currently set to steady, but one has the option of generating a more intricate wind profile, and use that instead.
3. Hydrodynamic data has various types depending on whether we consider the frequency dependent added mass, or direction of wave excitation...

# Enabled DoFs from ElastoDyn
All of the DoFs are enabled except for the Blade pitch, Rotor teeter (which is not used for 3blades), drivetrain rotational flexibility, and yaw.

The rotor is allowed to move in most direction. I am surprised that the pitch is not enabled, because it seems like we define a pitch control mode in the controller

I ultimate have to be able to visualize what each of the enabled DOF are

# Startup run
Already ran it.