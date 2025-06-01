# Function Plotter

This program allows you to generate plots of mathematical functions. You enter a function as a text formula (e.g., "x**2 + sin(x)"), specify a range for x, and the program will display a graph of the function.

## Features

- Parses mathematical formulas using Python's Sympy library.
- Allows specification of x-range (min and max values) and number of points for plotting.
- Uses Matplotlib to generate and display the plots.
- Basic error handling for formula parsing and numerical evaluation.

## Requirements

The program requires the following Python libraries:
- NumPy
- Matplotlib
- SymPy

## Setup

1.  **Clone the repository (if applicable) or download the `function_plotter.py` script.**
2.  **Install the required libraries:**
    Open your terminal or command prompt and navigate to the project directory. Then, run:
    ```bash
    pip install -r requirements.txt
    ```
    If you don't have the `requirements.txt` file, you can install them individually:
    ```bash
    pip install numpy matplotlib sympy
    ```

## How to Run

1.  **Navigate to the directory containing `function_plotter.py` in your terminal.**
2.  **Run the script using Python:**
    ```bash
    python function_plotter.py
    ```
3.  **Follow the on-screen prompts:**
    *   Enter the mathematical formula in terms of 'x'.
        *   Examples: `x**2`, `sin(x)`, `log(x)`, `exp(x*2)`
        *   Use Python/Sympy syntax (e.g., `**` for power, `*` for multiplication).
        *   For specific functions like Gamma or Bessel functions, use Sympy's naming (e.g., `gamma(x)`).
    *   Enter the minimum x-value for the plot (or press Enter for default: -10).
    *   Enter the maximum x-value for the plot (or press Enter for default: 10).
    *   Enter the number of points to plot (or press Enter for default: 500).

A plot window will then appear showing the graph of your function.

## Example Formulas

- `x**3 - 2*x + 5`
- `sin(x**2)`
- `exp(-x**2 / 2)` (Gaussian function)
- `1/x` (Hyperbola - be mindful of the range to avoid division by zero at x=0 if not handled)
- `log(x)` (Natural logarithm - ensure x > 0 for the range)
- `tan(x)` (Tangent function - has asymptotes)
- `abs(x**2 - 4)`

## Error Handling

- The script attempts to catch errors in formula parsing. If a formula is invalid, an error message will be displayed.
- If the function encounters numerical issues during evaluation (e.g., division by zero at a point, logarithm of a non-positive number), it will attempt to display an error message on the plot.

## Contributing

Feel free to fork this project, make improvements, and submit pull requests.
Possible enhancements:
- GUI for input and plot display.
- Option to save plots to a file.
- Plotting multiple functions on the same graph.
- More advanced parsing or symbolic manipulation features.
