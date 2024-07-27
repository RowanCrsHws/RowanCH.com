title: Sand Explosion Simulation
date: 2023-01-27 11:00
tags: vfx, explosion, houdini, university, simulation, nuke
summary: Grain and Pyro simulation.
cover: /images/covers/sand-explosion-1920.png

<div class="w-full aspect-w-16 aspect-h-9">
    <iframe src="https://www.youtube.com/embed/3stjzkwr2jm?si=skgkrlu5z8adodd4" title="youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Introduction
A shot I created for the Technical Effects unit of my university course. The intention was to replicate an explosion detonating under a layer of sand. I chose this effect as I felt it offered a number of opportunities for interesting problems to solve while still being achievable within the time available for the assignment.

## Design
When I had settled on the concept for the shot I began to experiment with the design. I knew that I would need to integrate a grain sim with pyro and a solid artillery shell impact, so I first began prototyping the grains. While I initially intended to use POP grains, I was unable to get them to reliably interact with a ridged body simulation for the shell. As an alternative, I switched to vellum grains and simulated the shell as a vellum softbody with extremely high stiffness to avoid deformation. This allowed them to be integrated together in a simpler manner.

When experimenting with the sand explosion, I found that with the particle count I was able to simulate, the grains didn’t provide the level of detail in the explosion that I required. To aid with this I created a system which spawns simple POP particles, which are very fast to simulate, from any sand grains which moved above a certain velocity, adding additional secondary particles without needing to up the detail on the main sim.

With the testing completed, I went to capture the backplate and reference photography needed for the shot. On Bournemouth beach, I captured the backplate and a photogrametric 3d scan of the ground. To aid in lighting I also captured a 360 panorama for reference and ambient lighting. Unfortunately I was not able to take it in a high enough dynamic range to provide full lighting, so additional lights where needed in the scene.

When assembling the scene, I used the 3D scan for shadow catching, collision geometry and as the volume to instance the particles. A section of the scan was boolean differenced for the collision and then the inverse was obtained with an intersection to provide the grain geometry.

After completing the grain sim to the highest possible quality my hardware and available time could allow, I was not satisfied with the detail of the grains. Even with the secondary particles described earlier. To partly remedy this I used the point replicate node to add artificial detail to the simulation.

To better blend the simulated sand patch with the real world footage I scattered a ring of static sand particles arraying outwards from the simulated patch. These points used the same material as the simulated sand and helped to break up the otherwise sharp line between the sand and the footage.

For unknown reasons, Karma was unable to export velocity or motion vector AOV’s for particles or volumes. This made it impossible to get accurate motion blur in post. While karma’s built in motion blur works it drastically increases the render time, especially on the frames with volumetrics and large amounts of moving particles.

Nuke’s automatic motion blur, which approximates velocity by comparing the frames, worked well for the explosion itself. However, it did not produce acceptable results for the fast moving shell. To resolve the issues I have used Karma’s motion blur for the shell and Nuke’s approximation for the explosion.
