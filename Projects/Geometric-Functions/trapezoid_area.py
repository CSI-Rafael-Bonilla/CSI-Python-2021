# trapezoid_area.py

# Calculate the area of the trapezoid by first adding both bases and dividing them by 2
def area(a:float, b:float, height:float):
    return(((a + b) / 2) * height)

# Format a value using 2 decimal places and scientific notation. 
# Print a verbal representation with units.
def printTrapezoidScientific(area:float, unit:str):
    print(f"The area of the trapezoid in scientific notation is: {area:.2e} {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating various areas: \n")

printTrapezoidScientific(area(100, 60.0), "m^2")
printTrapezoidScientific(area(55.5, 1), "m^2")
printTrapezoidScientific(area(1.27E4, 290), "m^2")
printTrapezoidScientific(area(1.27E-8, 0.001), "m^2")