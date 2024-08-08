title: Random 42 Masterclass
date: 2024-02-05 15:00
tags: university, simulation, nuke, houdini
summary: Simulating and Rendering microscopic enviroments
cover: /images/covers/r42-cover-1920.png

<div class="w-full aspect-w-16 aspect-h-9">
<iframe title="vimeo-player" src="https://player.vimeo.com/video/910765912?h=7d5e017dc8" frameborder="0"    allowfullscreen></iframe>
</div>

## The Project Brief

This project was a part of the 3rd year Masterclass unit on the CATA course. in this unit we received a brief and guidance from one of a number of companies. In this case, Random42. In short, the brief for this project was a snippet of audio and the general overview of some of the relevant aspects, such as how the virus and cells might be represented.

From there we had pretty much complete creative freedom on how to create the animation.
## Preproduction

My initial concept for the designs of the cells and viruses was based on ocean photography, specifically corals and sea anemones. It also informed the use of atmospheric effects and the colour scheme used. From a technical point of view I wanted to focus on organic procedural modelling and animation and to bring in simulated elements to add dynamics where needed.

The design of the virus is spiky and organic, while the cells are modelled on sea anemones with rounded soft tendrils which move gently in the wind, while the viruses motion is more erratic. This helps to create a contrast with the virus feeling dangerous.
## Modelling and Shading

The procedural modelling of the liver cells is first, a hexagonal grid, with the blood vessels placed by a spatial colonization algorithm across the surface. This grid is then used as a height field and cell details are added by their distance to scattered points. For the close up area, the cells are cubes placed on the above points and then inflated using vellum pressure to tightly pack with one another.


![A series of images showing the process of generating the large scale cell structures](/images/misc/r42-cell-generation.png) 
![A series of images showing the process of creating the close up cell details](/images/misc/r42-cell-generation-2.png)
The virus starts with a sphere distorted by a set of points to generate the spikes. A series of noise layers are then added bit by bit, before the extended strands and hair is scattered on.

![A series of images showing the process of generating the virus](/images/misc/r42-virus-generation.png)
The virus is shaded based on curvature attributes and normal data. It makes heavy use of sub surface scattering to give it a sense of microscopic shading.
Simulation

The main simulated elements are, the explosion in the final shot, the smashing section of the cell interior and the flocking parts of the cell interior. The flocking elements use a custom boid like system, with the traditional flocking, alignment and separation forces as well as additional forces to follow a set of curves, avoid viruses and be converted into viruses. This is implemented as a custom solver in Houdini, mostly using point wrangles for each element.

![An image showing the boid particles following a series of preset curves](/images/misc/r42-boids.png)

The smashing is a simple material fracture based on a set of hand placed points and an rdb simulation. For the final explosion, the cell is simulated with a tearing vellum simulation. using some custom forces and pressure to cause it to implode then explode. The strands are then simulated in a separate vellum sim onto of it. The smoke puff is a simple pyro simulation. The strands of the surrounding cells are pushed out by a simple point wrangle to add some dynamic response in the environment.
Post Processing

For the most part, post processing was quite simple, just applying atmospherics and camera effects in Nuke.

One issue was that for one shot the depth buffer was incorrect due to the way Karma renders volumetrics. To resolve this the depth buffer had to be reconstructed from the position buffer and camera position in Nuke.
