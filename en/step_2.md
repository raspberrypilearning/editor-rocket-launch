## Add a planet

Display an image of a planet.

## Step 1

The `image()` function needs the following:

+ image filename
+ x coordinate
+ y coordinate
+ width
+ height

## Step 2

Change the size and position of the planet by editing the numbers in the code.

```python line_numbers="true" line_number_start="14" line_highlights="18-19"
def draw():
    # Draw background
    background(0, 0, 0)

    # Planet
    image(planet, width/2, 400, 300, 300)
```

## Now run your code

![A planet against a black background.](images/step_2.png){:width="300px"}

> [!TIP]
> `width` is the width of the screen and `width/2` will be half this, at the centre of the screen.

Run your code and check that you see a black background with half a planet at the bottom.
