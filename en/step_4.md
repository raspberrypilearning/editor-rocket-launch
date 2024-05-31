<h2 class="c-project-heading--task">Load the rocket image</h2>

--- task ---
The starter project has a rocket image provided for you. 

![Image of the rocket in the code editor image gallery.](images/rocket_image.png)

Add code to the `setup()` function to load the rocket image into a `rocket` global variable. 
--- /task --- 

<div class="c-project-code">

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 24, 26
---

def setup():   
    # Set up your animation here   
    size(screen_size, screen_size)   
    image_mode(CENTER)   
    global planet, rocket   
    planet = load_image('planet.png')    
    rocket = load_image('rocket.png')    

--- /code ---
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

The rocket will not appear on the screen yet as the code you have written only loads the image, it does not draw it.

</div>


