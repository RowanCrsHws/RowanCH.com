title: Rendering and Simulating Clouds in OpenGL Shaders
date: 2023-07-12 14:00
tags: simulation, shaders, gpu, university, c++, realtime, opengl, programming
summary: Realtime Cloud Simulation and Rendering.
cover: /images/covers/cloudsim-1920.png

<div class="w-full aspect-w-16 aspect-h-9">
    <iframe src="https://www.youtube.com/embed/ZalLEHIBvNQ?si=02BYABHMktTVRntO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
The implementation of this cloud simulation is heavily based on: <http://www.markmark.net/cloudsim/harrisGH2003.pdf>

This project was made as a part of my 2nd year Personal Inquiry unit, which was supervised by Oleg Fryazinov.

The simulation is built using OpenGL compute shaders operating in a 3D volume texture, a series of compute shaders perform each step of the process one after the other. The rendering then uses basic volumetric ray marching, using similar techniques to those I used in:
<div class="w-full aspect-w-16 aspect-h-9">
    <iframe frameborder="0" src="https://www.shadertoy.com/embed/dt23Dh?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>
</div>
<https://www.shadertoy.com/view/dt23Dh>
Please note - This shader requires a powerful GPU to run and may freeze the browser if run on a weak computer.

The basis of the simulation is a simple Eulerian fluid simulation with a Jaccobi pressure solver. Similarly to the paper above, thermodynamic equations are then used on fields representing water vapour, condensed water and temperature to produce an approximation to the physical formation of clouds. These quantities are also advected, alongside the standard fluid simulation fields such as velocity. Please see the paper linked above for details of the maths and physics behind the technique.

Despite the code not being up to the quality I would have liked I have decided to release it anyway, it is available at: <https://github.com/RowanCrsHws/PI-CloudSim>

However, a simple overview of the simulation algorithm is a follows, with each step being a compute shader dispatch.

Note that between steps, relevant input and output field buffers are swapped.

Set the boundary of the domain and the surface to the required values, see the above paper.
1. Advect the fields
2. Calculate the curl of the velocity to allow vorticity confinement later
3. Apply the buoyancy and vorticity confinement to the velocity field.
4. Use the equations from the above paper to update the water vapour, condensation and temperature.
5. Calculate the divergence of the velocity field.
6. Iteratively appl  the Jaccobi pressure solver.
7. Apply the resulting pressure gradient to the velocity field.

The rendering is based on common volumetric raymarching techniques, with several optimizations, including basic temporal blending, ray jittering and others.

![A 2d diagram showing a ray being marched through a cloud, demonstrating how such a method can be used to sample the density along a view ray](/images/misc/vol-raymarch-diag.png)
