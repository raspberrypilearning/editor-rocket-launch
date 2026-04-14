<h2 class="c-project-heading--task">Remove the outline</h2>

### Step 1

Add some code to remove the outline of the circles to make them look more like smoke.

<div class="c-project-callout c-project-callout--tip">

### Tip

The outline around the circles is called the **stroke**. `no_stroke()` turns it off.

</div>

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 22
line_highlights: 26
---
# Rocket
    global rocket_position
    rocket_position = rocket_position - 1   
    image(rocket, width/2, rocket_position, 64, 64)    
    no_stroke()
    fill(200, 200, 200, 100) 
    for i in range(20):
        ellipse(width/2 + randint(-5,5), rocket_position + randint(20,50), randint(5,10))
--- /code ---
</div>

### Step 2

**Test:** Run your program and you should see the same exhaust trail but without the outlines.


<div class="c-project-output">
![A slow animation of the smoke effect.](images/rocket_smoke.gif)
</div>
