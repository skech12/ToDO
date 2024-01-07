import pyautogui as gui
import time
import webbrowser

o_file = input("file name to run")

def main(total_commands, script_lines, o_file):
    number = 1  # Initialize number
    while number < len(script_lines):  # Prevent index out of range
        todo = script_lines[number].strip().strip("{}")
        if "click" in todo:
            number += 1
            gui.leftClick()
        elif "write" in todo:
            number += 1
            todo = script_lines[number].strip().strip("{}")
            gui.write(todo)
            number += 1
        elif "search" in todo:
            time.sleep(0.5)  # Short delay to ensure the browser is ready to receive the hotkey.
            gui.hotkey('ctrl', 'l')
            number += 1

        elif "window key" in todo:
            gui.press('win')
            time.sleep(1)
            number += 1
        elif "enter" in todo:
            gui.press('enter')
            time.sleep(1)
            number += 1
        elif "link" in todo:
            number += 1 
            todo = script_lines[number].strip().strip("{}")
            webbrowser.open(todo)
            number += 1  # Increment number to skip over the URL line and move to the next command

        else:
            coords = todo.replace('x=', '').replace('y=', '').split(',')
            try:
                x, y = int(coords[0]), int(coords[1])
                gui.moveTo(x, y)
                time.sleep(1)
            except ValueError:
                print(f"Invalid coordinates in line {number}: {todo}")
            number += 1

# Read the file and process commands
try:
    with open(f"{o_file}.txt", "r") as file:
        lines = file.readlines()
    try:
        command_count = int(lines[0].strip())
    except ValueError:
        print("First line must be an integer indicating the number of commands.")
        exit()
    main(command_count, lines, o_file)
except FileNotFoundError:
    print("File not found.")
