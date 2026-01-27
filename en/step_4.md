<h2 class="c-project-heading--task">A different planet?</h2>

--- task ---
➡️ Choose a different planet image.
--- /task --- 

--- task ---

Click on the image icon to view the image gallery. 

--- /task ---

![Choose a different planet](images/image_gallery.png)

--- task ---

Change the planet image in the code to the filename of your chosen planet, for example, `orange_planet.png`. 

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 4
line_highlights: 9
---
def setup():
    # Set up your animation here
    size(400, 400)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('planet.png')
    rocket = load_image('rocket.png')
--- /code ---
</div>


