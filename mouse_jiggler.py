import random
import time
import pyautogui

pyautogui.FAILSAFE = True

# Get the screen wirdth and hight 
screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)

def move_mouse():
    # Randomize stuff

    # Set the number of steps to move the mouse
    num_steps = random.randint(1, 5)

    # Set a random time for the movement
    random_time = random.randint(1, 5)

    print(f"random time: {random_time} sec, random_steps: {num_steps}")

    time.sleep(random_time)
    print("move in 2 sec")
    time.sleep(2)


    # Create a loop
    for i in range(num_steps):
        # Calculate a random movment in the x and y direction
        x_movement = int(screen_width * (random.random() - 0.5))
        y_movement = int(screen_height * (random.random() - 0.5))
        # Get the current postion of the mouse pointer
        x, y = pyautogui.position()
        # Check if the movement is outside the bounds of the screen and adjust if necessary
        if (x_movement + x) > screen_width:
            x_movement = -x_movement * 0.5
        if (x_movement + x) <= 0:
            x_movement = -x_movement * 0.5
        if (y_movement + y) > screen_height:
            y_movement = -y_movement*0.5
        if (y_movement + y) <= 0:
            y_movement = -y_movement *0.5
        # Move the mouse by the calculated amount
        pyautogui.moveRel(x_movement, y_movement, duration=0.5)
                          
    # interupt by crtl + c in the terminal 

    # or add pyautogui.FAILSAFE = True and go fast to coordinate 0/0

                        

if __name__ == "__main__":
    while True:
        move_mouse()