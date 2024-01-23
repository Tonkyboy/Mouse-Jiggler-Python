# Intro

Mouse Jiggler in Python to keep your pc active, for example if you upload big files to a remote machine and your pc isn't able to deactivate powersaving due company policy.

# Install Requierments

```Python
pip3 install requierments.txt
```

# Function Description

This Python script generates random mouse movements on the screen at random intervals. Here's a breakdown of what the code does:

1. pyautogui.FAILSAFE = True: This line ensures that if the mouse cursor is moved to the upper-left corner of the screen, it raises a pyautogui.FailSafeException, allowing for an emergency exit.

2. screen_width, screen_height = pyautogui.size(): Retrieves the screen width and height.

3. move_mouse() function:
Generates a random number of steps (num_steps) and a random time delay (random_time) between 1 and 5 seconds.
Prints the random time and number of steps.
Waits for the random time.
Prints a message and waits for an additional 2 seconds.
Enters a loop that iterates num_steps times.
For each step:
Calculates random movement in the x and y directions.
Gets the current mouse position.
Checks if the movement would go beyond the screen boundaries and adjusts it if necessary.
Moves the mouse cursor relative to its current position by the calculated amount using pyautogui.moveRel.

4. while True: loop in the __main__ block:
Repeatedly calls the move_mouse() function, creating a continuous loop of random mouse movements.

The script can be interrupted manually using Ctrl + C in the terminal. Alternatively, if the pyautogui.FAILSAFE = True line is uncommented, the script will exit if the mouse is moved quickly to the upper-left corner (coordinates 0/0). This can act as a failsafe mechanism to quickly stop the script.
