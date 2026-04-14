<h2 class="c-project-heading--task">A different planet?</h2>

### Step 1
➡️ Choose a different planet image.

### Step 2

Click on the image icon to view the image gallery. 


![Choose a different planet](images/image_gallery.png)

### Step 3

Change the planet image in the code to the filename of your chosen planet, for example, `orange_planet.png`. 


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 11
---
def setup():
    # Set up your animation here
    size(400, 400)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('orange_planet.png')
    rocket = load_image('rocket.png')
--- /code ---
</div>
### Step 4

**Test:** Run your code and find a planet that you want to use for your animation.
