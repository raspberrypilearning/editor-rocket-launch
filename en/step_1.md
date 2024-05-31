<h2 class="c-project-heading--task">Draw the background</h2>

--- task ---
Add some code to load the image of the planet

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 20
---

def setup():  
    size(screen_size, screen_size)    
    planet = load_image('planet.png')  # Your chosen planet


--- /code ---
--- /task ---

<div class="c-project callout c-project-callout--tip">
### Tip

Click on the image icon to the left to view the image gallery. 

![A screenshot of the code editor, with the image gallery highlighted containing images of planets and the moon.](images/image_gallery.png)

If you want to use a different planet image, swap `planet.png` for a different filename, for example, `orange_planet.png`.

</div>