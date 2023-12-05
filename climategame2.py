import webbrowser

# List of solutions
solutions = {
    "1": {
        "title": "Reduced Food Waste",
        "impact": "88.50-102.20 gigatons CO2 reduced",
        "description": "Reducing food waste improves nutrition and reduces food insecurity.",
        "action": "Learn about food labels, support food rescue.",
        "link": "https://drawdown.org/solutions/reduced-food-waste"
    },
    "2": {
        "title": "Plant-Rich Diets",
        "impact": "78.33-103.11 gigatons CO2 reduced",
        "description": "Adopting plant-rich diets reduces meat consumption and deforestation.",
        "action": "Host plant-based potlucks, encourage meatless entrees.",
        "link": "https://drawdown.org/solutions/plant-rich-diets"
    },
    "3": {
        "title": "Family Planning and Education",
        "impact": "68.90 gigatons CO2 reduced",
        "description": "Increases access to family planning and education, fostering equality.",
        "action": "Support education and reproductive health rights.",
        "link": "https://drawdown.org/solutions/family-planning-and-education"
    },
    # Add more solutions here following the same structure...
}

def display_solution(solution_id):
    if solution_id in solutions:
        solution = solutions[solution_id]
        print(f"\nTitle: {solution['title']}")
        print(f"Impact: {solution['impact']}")
        print(f"Description: {solution['description']}")
        print(f"What You Can Do: {solution['action']}\n")
        webbrowser.open(solution['link'])
    else:
        print("Invalid choice. Please try again.")

def main():
    print("Welcome to Climate Choices!")
    print("Explore various environmental solutions and their impacts.")

    for id, solution in solutions.items():
        print(f"{id}. {solution['title']}")

    choice = input("Select a solution to learn more (e.g., 1, 2, 3): ")
    display_solution(choice)

if __name__ == "__main__":
    main()
