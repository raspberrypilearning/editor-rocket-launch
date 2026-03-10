<h2 class="c-project-heading--task">Add a planet</h2>

--- task ---

Display an image of a planet.

--- /task --- 

The `image()` function needs the following:

+ image filename
+ x coordinate
+ y coordinate
+ width
+ height

--- task ---

Change the size and position of the planet by editing the numbers in the code.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 14 
line_highlights: 18-19
---
def draw():
    # Draw background
    background(0, 0, 0)

    # Planet
    image(planet, width/2, 400, 300, 300)
--- /code ---
</div>

--- task ---

**Test:** Run your code and check that it draws a black background with half a planet at the bottom.

--- /task ---


<div class="c-project-output">
![A planet against a black background.](images/step_2.png){:width="300px"}
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

`width` is the width of the screen and `width/2` will be half this, at the centre of the screen. 

</div>



