<h2 class="c-project-heading--task">Lots of circles</h2>

Add a loop to draw multiple circles, to make the exhaust effect even better.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

### Tip

<div class="c-project-callout c-project-callout--tip">

Indent the `ellipse()` so that it is in the loop.

</div>

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 22
line_highlights: 27-28
---
    # Rocket
    global rocket_position
    rocket_position = rocket_position - 1   
    image(rocket, width/2, rocket_position, 64, 64)    
    fill(200, 200, 200, 100) 
    for i in range(20):
        ellipse(width/2, rocket_position, randint(5,10))
--- /code ---
</div>

## Now run your code

Run your program. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other!


<div class="c-project-output">
![Lots of small circles at the bottom of the rocket](images/rocket_circles.png)
</div>

Confirm the observable result.
