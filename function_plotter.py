"""
Function Plotter (函数绘图器)

This script allows users to input a mathematical formula as a string (in terms of 'x'),
and it will generate a plot of the function over a specified range.

这个脚本允许用户输入一个以 'x' 为变量的数学公式字符串，
并生成该函数在指定范围内的图像。

It uses:
- Sympy: For parsing the string formula into a mathematical expression and then
           converting it to a callable Python function.
- Numpy: For generating numerical data for plotting.
- Matplotlib: For creating and displaying the plot.

使用的库：
- Sympy: 用于将字符串公式解析为数学表达式，并转换为可调用的Python函数
- Numpy: 用于生成绘图所需的数值数据
- Matplotlib: 用于创建和显示图像

To run the script:
  python function_plotter.py
The script will then prompt for the formula and plotting parameters.

运行方法：
  python function_plotter.py
脚本会提示输入公式和绘图参数。
"""
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify
from sympy.parsing.mathematica import parse_mathematica
from sympy.abc import x


def parse_formula(formula_str):
    """
    Parses a mathematical formula string into a callable Python function.
    将数学公式字符串解析为可调用的Python函数。

    Args:
        formula_str (str): The mathematical formula (e.g., "x**2 + sin(x)").
                         数学公式字符串（例如："x**2 + sin(x)"）

    Returns:
        callable: A Python function that takes a numerical input (x-value)
                  and returns the corresponding y-value.
                  Returns None if parsing fails.
                 返回一个接受数值输入（x值）并返回对应y值的Python函数。
                 如果解析失败则返回None。
    """
    try:
        # Parse the formula using sympify
        # 使用sympify解析公式
        expr = sympify(formula_str)

        # Convert the sympy expression to a callable Python function
        # We use 'numpy' for the numerical evaluation for compatibility with numpy arrays
        # and handle common numpy functions.
        # 将sympy表达式转换为可调用的Python函数
        # 使用'numpy'进行数值计算，以确保与numpy数组的兼容性
        # 并处理常见的numpy函数
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
    生成并显示给定函数的图像。

    Args:
        func (callable): The Python function to plot.
                        要绘制的Python函数
        x_min (float): The minimum x-value for the plot.
                      图像的最小x值
        x_max (float): The maximum x-value for the plot.
                      图像的最大x值
        num_points (int): The number of points to use for plotting.
                         用于绘图的点数
        formula_str (str): The original formula string, for display purposes.
                          原始公式字符串，用于显示
    """
    if func is None:
        print("Cannot plot function because parsing failed.")
        return

    # Generate evenly spaced x values
    # 生成均匀分布的x值
    x_vals = np.linspace(x_min, x_max, num_points)

    try:
        # Calculate corresponding y values
        # 计算对应的y值
        y_vals = func(x_vals)
    except Exception as e:
        print(f"Error during function evaluation for plotting: {e}")
        print("This might be due to undefined points (e.g., division by zero, log of non-positive number).")
        # Create an error plot
        # 创建错误提示图像
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

    # Create the plot
    # 创建图像
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals)

    # Add title and labels
    # 添加标题和标签
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
    # Display welcome message and instructions
    # 显示欢迎信息和说明
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

    # Get the formula from user input
    # 获取用户输入的公式
    formula_str = input("Enter formula (e.g., x**2 + sin(x)): ")

    # Basic validation for the formula string
    # 对公式字符串进行基本验证
    if not formula_str.strip():
        print("Error: Formula cannot be empty.")
    else:
        # Parse the formula into a function
        # 将公式解析为函数
        parsed_func = parse_formula(formula_str)

        if parsed_func:
            # Get plotting parameters from user
            # 从用户获取绘图参数
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

            # Generate and display the plot
            # 生成并显示图像
            plot_function(parsed_func, x_min, x_max, num_points, formula_str)
        else:
            print(f"Could not plot the formula: '{formula_str}'")
