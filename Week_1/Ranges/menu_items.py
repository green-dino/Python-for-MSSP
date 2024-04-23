appetizers = ["Salad", "Soup"]
main_courses = ["Steak", "Fish", "Pasta"]
desserts = ["Cake", "Ice Cream"]
for appetizer in appetizers:
    for main_course in main_courses:
        for dessert in desserts:
            print(f"{appetizer}, {main_course}, {dessert}")
