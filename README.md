# Circular Animation

This project is a circular animation program built using Python's Tkinter library. The animation displays circles rotating around a central point, with user-interactive features to adjust the number of circles and their speed.

## Features

- **Dynamic Circle Creation**: Increase or decrease the number of circles displayed.
- **Speed Control**: Adjust the speed of the circle's rotation.
- **Toggle Lines**: Draw lines connecting the circles when in mode 2.
- **Full-Screen Mode**: The application runs in full-screen for an immersive experience.
- **Instructions**: On-screen instructions guide the user on how to interact with the program.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository or download the source code.

```bash
git clone https://github.com/TaluKara/tork
cd tork
```

3. Run the program using Python:

```bash
python an.py
```

## Controls

- **UP Arrow**: Increase the number of circles.
- **DOWN Arrow**: Decrease the number of circles (minimum of 1).
- **RIGHT Arrow**: Increase the speed of rotation.
- **LEFT Arrow**: Decrease the speed of rotation (minimum speed of 0.01).
- **Enter**: Toggle between drawing and not drawing lines connecting the circles.
- **ESC**: Exit the program.

## Usage

- When you run the program, you'll see a black canvas with circles rotating around a center point.
- Use the arrow keys to modify the number of circles and their speed.
- Press `Enter` to connect the circles with lines, creating a visually interesting effect.
- Press `ESC` to close the application.

## Customization

You can modify various parameters within the `CircularAnimation` class, such as:
- `radius`: Change the distance of circles from the center.
- `speed`: Set the initial speed of rotation.
- `num_circles`: Start with a different number of circles.

## Contributing

Contributions are welcome! If you'd like to add features or fix bugs, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
