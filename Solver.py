# Solver.py
# Interface between GUI (python) and CubeSolver (Java)

# Import Libraries
import subprocess
import os
import jpype

# Function: solve
# Purpose: Will take the state of the cube from the GUI and use that as an argument for the solver
def solve(upper,down,front,back,left,right):

    # Define a Dictionary to convert the input from chars to ints (easier to handle in Java)
    conv = {'w' : 0, 'y' : 1, 'b' : 2, 'g' : 3, 'r' : 4, 'o' : 5} 

    # Create copies of the cube state variables to not alter them
    upper_copy = upper[:]
    down_copy = down[:]
    front_copy = front[:]
    back_copy = back[:]
    left_copy = left[:]
    right_copy = right[:]

    # Convert the input
    for i in range(4):
        upper_copy[i] = conv[upper_copy[i]]
        down_copy[i] = conv[down_copy[i]]
        front_copy[i] = conv[front_copy[i]]
        back_copy[i] = conv[back_copy[i]]
        left_copy[i] = conv[left_copy[i]]
        right_copy[i] = conv[right_copy[i]]

    # Compile the Java class if not already compiled
    if not os.path.exists("CubeSolver.class"):
        subprocess.run(["javac", "CubeSolver.java"])

    # Start the java virtual machine
    try:
        jpype.startJVM(jpype.getDefaultJVMPath())
    except:

        # Load your Java class
        CubeSolver = jpype.JClass("CubeSolver")

        # Create an instance of your Java class
        java_instance = CubeSolver()

        # Convert Python lists to Java arrays
        upper_java = jpype.JArray(jpype.JInt, 1)(upper_copy)
        down_java = jpype.JArray(jpype.JInt, 1)(down_copy)
        front_java = jpype.JArray(jpype.JInt, 1)(front_copy)
        back_java = jpype.JArray(jpype.JInt, 1)(back_copy)
        left_java = jpype.JArray(jpype.JInt, 1)(left_copy)
        right_java = jpype.JArray(jpype.JInt, 1)(right_copy)

        solve_path = java_instance.solve(upper_java, down_java, front_java, back_java, left_java, right_java)
        return(solve_path)
    
    # Load your Java class
    CubeSolver = jpype.JClass("CubeSolver")

    # Create an instance of your Java class
    java_instance = CubeSolver()

    # Convert Python lists to Java arrays
    upper_java = jpype.JArray(jpype.JInt, 1)(upper_copy)
    down_java = jpype.JArray(jpype.JInt, 1)(down_copy)
    front_java = jpype.JArray(jpype.JInt, 1)(front_copy)
    back_java = jpype.JArray(jpype.JInt, 1)(back_copy)
    left_java = jpype.JArray(jpype.JInt, 1)(left_copy)
    right_java = jpype.JArray(jpype.JInt, 1)(right_copy)

    solve_path = java_instance.solve(upper_java, down_java, front_java, back_java, left_java, right_java)

    return solve_path