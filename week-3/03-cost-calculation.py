def calculate_project_costs():
    # Constants
    machine_costs = {
        'A': 25000,
        'B': 40000
    }

    material_costs = {
        'a1': (335, 47),  # (cost per unit, units needed)
        'a2': (1520, 119),
        'b1': (865, 159)
    }

    labor_costs = {
        'A': 150,
        'B': 175,
        'PM': 200
    }

    # Input
    machine_type = input("Enter machine type (A or B): ").upper()
    budget = float(input("Enter budget: "))
    duration_months = float(input("Enter duration of project in months: "))

    # Calculate machine and material costs
    machine_cost = machine_costs[machine_type]
    material_cost = 0

    if machine_type == 'A':
        for material, (cost_per_unit, units_needed) in material_costs.items():
            if material in ['a1', 'a2']:
                material_cost += cost_per_unit * units_needed
    elif machine_type == 'B':
        material_cost += material_costs['b1'][0] * material_costs['b1'][1]

    total_material_cost = machine_cost + material_cost

    # Check if machine and material costs are below 25% of budget
    if total_material_cost > 0.25 * budget:
        print("Machine and material costs exceed 25% of the budget.")
        return

    # Calculate labor costs
    labor_hours_per_month = 42
    total_labor_hours = labor_hours_per_month * duration_months
    if machine_type == 'A':
        total_labor_cost = labor_costs['A'] * total_labor_hours
    else:
        total_labor_cost = labor_costs['B'] * total_labor_hours

    # Project manager cost
    pm_cost = labor_costs['PM'] * labor_hours_per_month * duration_months

    # Total cost
    total_cost = total_material_cost + total_labor_cost + pm_cost

    # Project management cost percentage
    pm_percentage = (pm_cost / total_cost) * 100

    # Check project management cost constraints
    if pm_percentage < 8 or pm_percentage > 12:
        print(f"Project management cost ({pm_percentage:.2f}) must be between 8% and 12% of total labor cost.")
        return

    # Print results
    print("\nCost Summary:")
    print(f"Machine Cost: ${machine_cost:.2f}")
    print(f"Material Cost: ${material_cost:.2f}")
    print(f"Total Material Cost: ${total_material_cost:.2f}")
    print(f"Total Labor Cost: ${total_labor_cost:.2f}")
    print(f"Project Manager Cost: ${pm_cost:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Project Manager Cost Percentage: {pm_percentage:.2f}%")


calculate_project_costs()

#Valid UseCase:
#A;10000000;4