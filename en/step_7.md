<h2 class="c-project-heading--task">Exhaust effects</h2>

--- task ---

The rocket will look more realistic with some special effects to simulate the exhaust trail. 

![A slow animation of the smoke effect.](images/rocket_smoke.gif)

--- /task ---

Set the fill colour for the smoke to transparent grey. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 14
---

def draw_rocket():
    global rocket_position
    rocket_position = rocket_position - 1
    image(rocket, width/2, rocket_position, 64, 64)
    fill(200, 200, 200, 100) 
    

--- /code ---


Generate a random number between 5 and 10 for the size of the circle, then draw it at the bottom of the rocket.

--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 15-16
---

fill(200, 200, 200, 100) 
circle_size = randint(5,10) 
ellipse(screen_size/2, rocket_position, circle_size, circle_size)   

--- /code ---
   


**Test:** Run your program and you should see a grey circle appear at the bottom of the rocket. 


<div class="c-project-callout c-project-callout--tip">

### Tip

The function which draws the circle is called `ellipse` as it can also draw ovals too. Setting both the width and height to the same value (`circle_size`) draws a circle. 
</div>
