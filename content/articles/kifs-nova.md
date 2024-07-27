title: KIFS Fractals in Nova
date: 2024-06-04 10:00
tags: university, shaders, realtime, final major project, scifi, animation, unreal engine
summary: In my final major project, Nova, I made use of KIFS fractals to represent an alien anomaly.
cover: /images/covers/nova-cover-1920.png


<div class="w-full aspect-w-16 aspect-h-9">
    <iframe title="vimeo-player" src="https://player.vimeo.com/video/953466769?h=7f169bcecd" frameborder="0"    allowfullscreen></iframe>
</div>
## Introduction
Before getting onto the fractal effect, I will briefly discuss the film in general.

I created Nova for my Final Major Project in the BA (Hons) CATA course at Bournemouth University. The project was supervised by Rehan Zia.

I primarily wanted to focus on creating a complete and whole project. I had made many interesting things through my course, but for the final project I wanted to make something that is complete in itself. To do this I made heavy use of procedural techniques and minimal complex animation. This allowed me to create the entire two and a half minute long short as a solo project. The only external assets used are the texture maps for the earth, as I sadly don't have access to a spacecraft to capture my own.

I worked in Unreal Engine, as it allowed fast render times and quick iteration, which was essential to create the project in the time available. It also provided a unique workflow, less linear than the traditional pipeline, as rough blockouts slowly transformed into final shots as they were smoothly iterated bit by bit. While this worked well for a solo project, I would be interested it see how it could be adapted to work for a team.

## The Anomaly
I knew that I wanted the film to end with an encounter with a truly alien entity, following a similar structure to Interstellar and 2001: A Space Odyssey. Where a journey through space results in an encounter with something truly alien.

Another specific inspiration was the entity at the end of Annihilation, which is represented with a Mandelbulb, one generalization of the mandelbrot into 3D. This effect has been used across several films. To differentiate the effect in my film, I chose to create a custom KIFS fractal.

KIFS (Kaleidoscopic Iterated Function System) fractals, are a variation on the more common IFS (Iterated Function System) fractals, which add the reflection and folding of space to the possible functions. This allows the creation of very intricate structures with a great deal of artistic control over how they form.

<http://blog.hvidtfeldts.net/index.php/2010/06/folding-space-ii-kaleidoscopic-fractals/> Has some great examples of other KIFS fractals.

Raymarching against an SDF is a well known algorithm to render 3d fractals in realtime. It involves taking a ray from each pixel in the camera's view, finding the distance to the surface via a distance estimator function for the start of that ray, then stepping that distance forward along the ray, estimating the distance at that point and then repeating until either the surface distance is near zero or the ray hits some maximum distance. This allows you to render arbitrary mathematical functions, as long as they have a distance estimation.
![A 3d fractal shown through a plane in the viewport, as if it were a window](/images/misc/nova-fractal-viewport.png)
How the fractal is viewed through a plane attached to the camera.

rotating and mirroring the input point before estimating the distance to a common primitive, such as a sphere, or in this instance, a cube. By defining these operations, you can achieve a great degree of artistic control over the results, and create a range of interesting shapes.

This degree of control allowed me to create a fractal which was in line with the other design elements of the film. I used blocky elements to reference back to the alien architecture, before allowing this to dissolve into more chaotic and organic forms, representing the truly alien nature of the fractal, compared to the more understandable designs of the aliens.

## Designing the Fractal
The GLSL version of the code and a realtime preview of it can be seen at:
<div class="w-full aspect-w-16 aspect-h-9">
    <iframe frameborder="0" src="https://www.shadertoy.com/embed/4fVSRt?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>
</div>
<https://www.shadertoy.com/view/4fVSRt>
Please note - This shader requires a powerful GPU to run and may freeze the browser if run on a weak computer.

I made use of Shadertoy to design the fractal in GLSL with quick updates after any changes. This did require me to adapt the syntax for HLSL in Unreal Engine, but this was pretty trivial. The design process was mostly trial and error, just tweaking and adjusting numbers until it looked right. I hope to investigate ways to improve this design process in the future, as I think KIFS fractals have a lot of potential for a range of effects.

As the anomaly was used in only one scene, and that scene didn't have much else going on, I could push the performance by using more expensive rendering techniques.


![A 3d fractal in the viewport, a selection outline is visible](/images/misc/nova-fractal-viewport-2.png)
An image of the fractal

I used SDF raymarching to render the fractal onto a plane attached to the camera. This allowed me to output depth and normal data, allowing the fractal to be integrated into unreal engines lighting system natively. In an earlier version I raymarched from the surface of a sphere. This had the advantage of being a physical object in the scene, which could be positioned like any other. However, it was impossible to go inside the fractal, as it was marched from the sphere surface. This proved too limiting and made some shots impossible.
