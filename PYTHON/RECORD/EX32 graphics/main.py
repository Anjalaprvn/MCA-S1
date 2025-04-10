from graphics.circle import cir_area,cir_perimeter
from graphics.rect import recta_area as r_area,recta_perimeter as r_perimeter
from graphics.dgraphics.sphere import *
from graphics.dgraphics.cuboid import *

# Circle
print(f"Circle Area: {cir_area(5)}")
print(f"Circle Perimeter: {cir_perimeter(5)}")

# Rectangle
print(f"Rectangle Area: {r_area(4,6)}")
print(f"Rectangle Perimeter: {r_perimeter(4,6)}")

# Sphere
print(f"Sphere Area: {sphere_area(3)}")
print(f"Sphere Perimeter: {sphere_perimeter(3)}")

# Cuboid
print(f"Cuboid Area: {cub_area(2, 3, 4)}")
print(f"Cuboid Perimeter: {cub_perimeter(2, 3, 4)}")



# Step 1: Start  
# Step 2: Create a package graphics with modules rectangle and circle for area and perimeter methods.  
# Step 3: Create a sub-package 3D-graphics with modules cuboid and sphere for surface area and perimeter methods.  
# Step 4: using different import statement :
        # - Specific Method Import: from <module> import <method>.
        # - Alias Import: from <module> import <method> as <alias> 
        # - Import All Methods: from <module> import *.
# Step 5: Call methods to calculate and display area and perimeter of each figure.  
# Step 6: Stop

        