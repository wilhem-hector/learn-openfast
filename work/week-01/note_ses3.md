# Working Case
1. All input files and initial conditions remain the same as what was given by the IEA turbine, except the simulation time which was changed to 120 secs, to potentially eliminate transients.

# Chosen channels to investigate
1. Rotor speed from ElastoDyn
2. B1WvsFxi from HydroDyn 
3. Overall rotor CT from AeroDyn
4. Generator torque from ServoDyn

# Attempt to explain what I see on the plots
1. Rotor speed plot: We initially set the rotor speed to be 7.55 RPM. I'm not sure why it jumps out. Perhaps the controller is trying to maintain that speed, and before the controller hits its steady state, it oscillates a little bit around the set point. Afterward, the rotor speed settles at about the initial condition. I don't know if you could compute what the rotor speed should be based on a fixed tip speed ratio if we know the incoming wind speed.
2. Wave excitation total force:  For this plot, I'm not sure I can explain what's going on. We have an irregular sea state, but the total wave excitation force (first order and second order) just oscillates around zero. Not sure why. 
3. Thrust coefficient: For the thrust coefficient plot, I'm not necessarily sure what goes on. It starts from 1 and then goes down and settles at about 0.25. I imagine that the controller must be doing something with the pitch, sort of like reducing the thrust of the turbine and also probably reducing the power that it's capturing from the wind. But I'm not sure why that would go down because we have a steady wind speed, a steady inflow condition. 
4. Generator torque: This one doesn't oscillate much. I imagine that's prescribed by the controllers. The controller is pretty good at quickly setting a generator torque. Actually, it settles at the rated generated torque, but then I think version control has to be 5 for the controller to try to put it at the rated generated torque in region 3. Instead, we have a user-defined from-bladed-style DLL version control, and I'm not sure what that is, so I can't necessarily explain why the generator torque just settles at around the rated generator torque for region 3 wind speed. 

# Second attempt lmao
1. That this explanation was mostly correct. The only thing is that I didn't realize that the turbine is operating above the rated wind speed, at which point the controller is trying to maintain the rated rotor speed, which is set to be 7.56. The tip speed ratio tracking is no longer hitting the optimal tip speed ratio because that only applies when we are below rated wind speed. 
2. I guess this one is wave excitation. It's not necessarily like wave force. The force is heating the body, and the body is getting excited in, I would imagine, multiple directions, given that the waves have different frequencies, some of which are canceling each other. It kind of makes sense that, within that direction, there is an occlusion because the x direction is not just impacted by the force that is traveling in that same direction. It could also be impacted by some other force in another direction that has some second-order effects. 
3. My explanation for the pitch, for the thrust coefficient, is pretty accurate, I would say, because when I plot the pitch, it follows a pretty similar path: the pitch angle increases. Therefore, the aerodynamic torque from the blade decreases because the turbine initially starts above rated wind speed, and the controller is trying to use pitch control to maintain the power production at 15 MW. 
4. The explanation for the generator torque is that the above-rated condition is defined by the Rosco controller, which sets a fixed generator torque once we pass the rated wind speed. The turbine is effectively just setting that constant torque pretty quickly, as soon as the simulation starts. 

## Repeatability was not tested

# A response measurement does not necessarily identify the cause
It's very interesting, kind of looking at the thrust coefficient case. You see it go down, but you can't necessarily know what exactly causes it until you actually explore some other responses. That coupled physics idea is quite interesting and something that I hope is going to help me understand how a wind turbine works, at least the intricacies behind the wind turbine mechanism.

I guess it would apply to the same thing too if you were to look at structural root bending moment. You couldn't necessarily know what aerodynamic force caused it. You could have various values along the blade, a different blade pitch, and platform motion. All of these things could affect the thing. 

# Peaks are not representative staticstics
Another thing that's great and interesting is that there are those transient responses where the thing hasn't necessarily settled and the controller hasn't done its thing. Even with the power, potentially, you see that it goes above the rated, but those transient states do not necessarily represent the kind of long-term statistics.

Even when I'm doing analysis, I'm going to have to be very careful about how I phrase it because a 120-second simulation is still small. You could take the average response to have a better representation. 
