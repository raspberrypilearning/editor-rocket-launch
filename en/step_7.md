## Lots of circles

Add a loop to draw multiple circles, to make the exhaust effect even better.

> [!TIP]
> Indent the `ellipse()` so that it is in the loop.

```python line_numbers="true" line_number_start="22" line_highlights="27-28"
    # Rocket
    global rocket_position
    rocket_position = rocket_position - 1   
    image(rocket, width/2, rocket_position, 64, 64)    
    fill(200, 200, 200, 100) 
    for i in range(20):
        ellipse(width/2, rocket_position, randint(5,10))
```

## Now run your code

![Lots of small circles at the bottom of the rocket](images/rocket_circles.png)

Run your code and check that a flashing grey circle appears at the bottom of the rocket.
