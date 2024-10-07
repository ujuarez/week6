# Partner activity.. Names: Ulysses and Fabio
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"


# Find the student who is making an A and upgrade it to an A +
school["class"]["students"]["student1"] = "A+"

# Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
oranges = product_inventory["warehouse1"]["quantities"][1]
print(f"The total amount of oranges is: {oranges}")

# Sum up all the quantities in the warehouse
quantity_1 = product_inventory["warehouse1"]["quantities"]
quantity_2 = product_inventory["warehouse2"]["quantities"]
print(sum(quantity_1) + sum(quantity_2))
