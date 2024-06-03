<h2 class="c-project-heading--task">Exhaust effects</h2>

--- task ---

The rocket will look more realistic with some special effects to simulate the exhaust trail. 

![A slow animation of the smoke effect.](images/rocket_smoke.gif)

--- /task ---

In each frame of the animation, draw 20 ellipses of random sizes at random positions. 

--- code ---
---
language: python
filename: main.py - draw_rocket()
line_numbers: true
line_number_start: 18
line_highlights: 22-24
---

    for i in range(25):  
        fill(255, 255 - i * 10, 0)   
        ellipse(width/2, rocket_y + i, 8, 3)    

    fill(200, 200, 200, 100)  # Transparent grey   
    for i in range(20):  # Draw 20 random smoke ellipses    
        ellipse(width/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))    
    
    image(rocket, width/2, rocket_y, 64, 64)

--- /code ---




**Test:** Run your program and you should see exhaust fumes. 


