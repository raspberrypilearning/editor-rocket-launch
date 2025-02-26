<h2 class="c-project-heading--task">Add a planet</h2>

--- task ---

➡️ Display an image of a planet.

--- /task --- 

The `image()` function needs the following data:

- image filename
- x coordinate
- y coordinate
- image width
- image height

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 13 
line_highlights: 15-16
---
def draw_background():  
    background(0,0,0)
    image(planet, screen_size/2, screen_size, 300, 300)
--- /code ---
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

The code `image_mode(CENTER)` in the `setup()` function means the x,y coordinate you provide is the centre of the image not the top left corner. 

The x coordinate for the planet is `screen_size/2` to position the centre of the planet half way across the black square, horizontally. 

The y coordinate for the planet is `screen_size` to position the centre of the planet right at the bottom of the black square.

</div>

**Test:** Run your code and check that it draws a black background with half a planet at the bottom.

![A planet against a black background.](images/step_2.png){:width="300px"}









