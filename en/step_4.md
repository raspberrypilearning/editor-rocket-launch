## Draw the rocket

Make the rocket appear on the screen.

## Step 1

First add `rocket_position` to start at 400 (the screen height).

Then add another `image()` and use `rocket_position` as the y coordinate.

## Step 2

Move your rocket and change it to the size you want by editing the code.

```python line_numbers="true" line_number_start="4" line_highlights="5,22-23"
# Define variables
rocket_position = 400

def setup():
    # Set up your animation here
    size(400, 400)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('planet.png')
    rocket = load_image('rocket.png')

def draw():
    # Draw background
    background(0, 0, 0)

    # Planet
    image(planet, width/2, 400, 300, 300)

    # Rocket
    image(rocket, width/2, rocket_position, 64, 64)    
```

## Now run your code

Run your code and check that the rocket appears.
