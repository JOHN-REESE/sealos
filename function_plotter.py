"""
Function Plotter

This script allows users to input a mathematical formula as a string (in terms of 'x'),
and it will generate a plot of the function over a specified range.

It uses:
- Sympy: For parsing the string formula into a mathematical expression and then
           converting it to a callable Python function.
- Numpy: For generating numerical data for plotting.
- Matplotlib: For creating and displaying the plot.

To run the script:
  python function_plotter.py
The script will then prompt for the formula and plotting parameters.
"""
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify
from sympy.parsing.mathematica import parse_mathematica
from sympy.abc import x


def parse_formula(formula_str):
    """
    Parses a mathematical formula string into a callable Python function.

    Args:
        formula_str (str): The mathematical formula (e.g., "x**2 + sin(x)").

    Returns:
        callable: A Python function that takes a numerical input (x-value)
                  and returns the corresponding y-value.
                  Returns None if parsing fails.
    """
    try:
        # Parse the formula using sympify
        expr = sympify(formula_str)

        # Convert the sympy expression to a callable Python function
        # We use 'numpy' for the numerical evaluation for compatibility with numpy arrays
        # and handle common numpy functions.
        func = lambdify(x, expr, modules=['numpy', 'sympy'])
        return func
    except (SyntaxError, TypeError, ValueError) as e_sympy_parse:
        print(f"Error parsing formula with Sympy: {e_sympy_parse}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during formula parsing: {e}")
        return None


def plot_function(func, x_min=-10, x_max=10, num_points=500, formula_str=""):
    """
    Generates and displays a plot of the given function.

    Args:
        func (callable): The Python function to plot.
        x_min (float): The minimum x-value for the plot.
        x_max (float): The maximum x-value for the plot.
        num_points (int): The number of points to use for plotting.
        formula_str (str): The original formula string, for display purposes.
    """
    if func is None:
        print("Cannot plot function because parsing failed.")
        return

    x_vals = np.linspace(x_min, x_max, num_points)

    try:
        y_vals = func(x_vals)
        # Replace any potential infinities or NaNs with a placeholder if necessary,
        # or let matplotlib handle them (it usually does so gracefully by not plotting those points).
        # For simplicity, we'll let matplotlib handle them.
        # y_vals = np.nan_to_num(y_vals, nan=np.nan, posinf=np.nan, neginf=np.nan) # Optional
    except Exception as e:
        print(f"Error during function evaluation for plotting: {e}")
        print("This might be due to undefined points (e.g., division by zero, log of non-positive number).")
        # Optionally, create a plot showing where evaluations failed, or just return.
        plt.figure(figsize=(10, 6))
        plt.text(0.5, 0.5, f"Error evaluating function: {e}", ha='center', va='center', fontsize=12, color='red')
        if formula_str:
            plt.title(f"Plot of y = {formula_str} - Evaluation Error")
        else:
            plt.title("Plot of Function - Evaluation Error")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        return

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals)

    if formula_str:
        plt.title(f"Plot of y = {formula_str}")
    else:
        plt.title("Plot of Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("--------------------")
    print("  Function Plotter  ")
    print("--------------------")
    print("Enter a mathematical formula in terms of 'x'.")
    print("Examples:")
    print("  - Basic arithmetic: x**2, x/2 + 3*x - 1")
    print("  - Powers: x**3, x**0.5 (for sqrt(x))")
    print("  - Trigonometric: sin(x), cos(x*pi/2), tan(x)")
    print("  - Exponential/Logarithmic: exp(x), log(x) (natural log), log(x, 10) (log base 10)")
    print("  - Symbolic constants: pi, E")
    print("  - Factorial: factorial(x)")
    print("  - Absolute value: Abs(x) or abs(x)")
    print("  - For more complex functions (e.g., Gamma, Bessel), use Sympy syntax directly:")
    print("    e.g., 'gamma(x)', 'besselj(0, x)' (0th order Bessel function of the first kind)")
    print("Multiplication often needs to be explicit, e.g., '2*x' instead of '2x'.")
    print("--------------------")

    formula_str = input("Enter formula (e.g., x**2 + sin(x)): ")

    # Basic validation for the formula string
    if not formula_str.strip():
        print("Error: Formula cannot be empty.")
    else:
        parsed_func = parse_formula(formula_str)

        if parsed_func:
            while True:
                try:
                    x_min_str = input("Enter minimum x value (default: -10): ")
                    if not x_min_str:
                        x_min = -10.0
                        break
                    x_min = float(x_min_str)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for minimum x.")

            while True:
                try:
                    x_max_str = input("Enter maximum x value (default: 10): ")
                    if not x_max_str:
                        x_max = 10.0
                        break
                    x_max = float(x_max_str)
                    if x_max <= x_min:
                        print("Maximum x must be greater than minimum x. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for maximum x.")

            while True:
                try:
                    num_points_str = input("Enter number of points (default: 500): ")
                    if not num_points_str:
                        num_points = 500
                        break
                    num_points = int(num_points_str)
                    if num_points <= 1:
                        print("Number of points must be greater than 1. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for number of points.")

            plot_function(parsed_func, x_min, x_max, num_points, formula_str)
        else:
            print(f"Could not plot the formula: '{formula_str}'")
