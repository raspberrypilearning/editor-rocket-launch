<h2 class="c-project-heading--task">A different planet?</h2>

➡️ Choose a different planet image.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

## Step 1

Click on the image icon to view the image gallery. 


<div class="c-project-output">
![Choose a different planet](images/image_gallery.png)
</div>

## Step 2

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

## Now run your code

Find a planet that you want to use for your animation.

Confirm the observable result.
