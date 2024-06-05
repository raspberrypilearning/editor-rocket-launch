<h2 class="c-project-heading--task">A different planet?</h2>

--- task ---
✅ Click on the image icon to the left to view the image gallery. 

![Choose a different planet](images/image_gallery.png)

✅ Change the planet image (optional).
--- /task --- 

If you want to change the planet image, change `planet.png` in the code to the filename of your chosen planet, for example, `orange_planet.png`. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 18 
line_highlights: 23
---
def setup():
    # Set up your animation here
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet
    planet = load_image('planet.png')
--- /code ---
</div>


