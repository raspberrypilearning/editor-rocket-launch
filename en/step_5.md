## Blast off!

Decrease the y coordinate `rocket_position` by 1 each time it is drawn to make an animation.

> [!TIP]
> You can make it move faster or slower by changing the decrease number.

```python line_numbers="true" line_number_start="22" line_highlights="23-24"
    # Rocket
    global rocket_position
    rocket_position = rocket_position - 1   
    image(rocket, width/2, rocket_position, 64, 64)    
```

## Now run your code

![A rocket flying at a steady speed from the bottom to the top of the screen.](images/fly.gif){:width="300px"}

Run your code and check that the rocket blasts off from the bottom of the screen.
