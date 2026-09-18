#task
#Creat a function withe usage of *args & **Kwargs with real time secenrio

'''
def student_marks(*args, **kwargs):
    """Here takes student name marks and college and bank detals"""
    for student in args:
        print("Name:", student[0])
        print("Python:", student[1])
        print("SQL:", student[2])
        print("Java:", student[3])
        print()

    print("College:", kwargs["college"])
    print("Branch:", kwargs["branch"])


student_marks(
    ("Lavanya", 85, 90, 80),
    ("Likhitha", 90, 88, 85),
    college="Amrutha College",
    branch="Computer Science"
)
'''
def electricity_bill(*args, **kwargs):

    print("\n===== ELECTRICITY MONITORING SYSTEM =====")

    # Customer Details
    print("\nCustomer Details:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    # Appliance Details
    print("\nAppliance Details:")

    total_energy = 0

    for appliance in args:

        name, watts, hours = appliance

        # Validation
        if watts <= 0 or hours < 0:
            print(f"Invalid values for {name}")
            continue

        # Daily energy calculation
        energy = (watts * hours) / 1000

        total_energy += energy

        print(f"Appliance: {name}")
        print(f"Power: {watts} W")
        print(f"Usage: {hours} hours/day")
        print(f"Daily Energy: {energy:.2f} kWh")
        print("------------------------")

    # Monthly calculation
    monthly_energy = total_energy * 30

    print("\n===== BILL SUMMARY =====")
    print(f"Total Daily Energy: {total_energy:.2f} kWh")
    print(f"Monthly Energy: {monthly_energy:.2f} kWh")


# Function call
electricity_bill(
    ("Fan", 75, 8),
    ("Light", 20, 6),
    ("AC", 1500, 4),
    customer_name="Deepika",
    meter_number="MTR101",
    location="Visakhapatnam"
)
