import json

# Define the Employee class
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Define employee information
employees = [
    {
        "Name": "John Doe",
        "DOB": "1990-05-15",
        "Height": 175,
        "City": "Mumbai",
        "State": "Maharashtra"
    },
    {
        "Name": "Jane Smith",
        "DOB": "1985-08-23",
        "Height": 160,
        "City": "Delhi",
        "State": "Delhi"
    },
    {
        "Name": "Mike Johnson",
        "DOB": "1992-03-10",
        "Height": 185,
        "City": "Bangalore",
        "State": "Karnataka"
    },
    {
        "Name": "Sarah Williams",
        "DOB": "1994-11-05",
        "Height": 170,
        "City": "Chennai",
        "State": "Tamil Nadu"
    },
    {
        "Name": "David Brown",
        "DOB": "1988-07-18",
        "Height": 180,
        "City": "Kolkata",
        "State": "West Bengal"
    }
]

# Save employee information to JSON file
with open("employee.json", "w") as file:
    json.dump(employees, file)

# Read employee information from JSON file
employee_objects = []
with open("employee.json", "r") as file:
    data = json.load(file)
    for employee_data in data:
        employee = Employee(employee_data["Name"], employee_data["DOB"], employee_data["Height"],
                            employee_data["City"], employee_data["State"])
        employee_objects.append(employee)

# Print the list of Employee objects
for employee in employee_objects:
    print("Name:", employee.name)
    print("DOB:", employee.dob)
    print("Height:", employee.height)
    print("City:", employee.city)
    print("State:", employee.state)
    print()




# Define the dictionary of states and capitals
states = {
    "Andhra Pradesh": "Hyderabad",
    "Assam": "Dispur",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur",
    "Tamil Nadu": "Chennai"
}

# Save states and capitals to JSON file
with open("states.json", "w") as file:
    json.dump(states, file)

# Print the content of the JSON file
with open("states.json", "r") as file:
    data = json.load(file)
    print(data)
