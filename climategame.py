import webbrowser

def show_details(choice):
    details = {
        "1": {
            "impact": "Reduces 88.50-102.20 gigatons CO2",
            "ranking": "High Impact",
            "co_benefits": "Improves nutrition, reduces food insecurity",
            "action": "Learn about food expiration labels, support food rescue organizations",
            "link": "https://drawdown.org/solutions/reduced-food-waste"
        },
        "2": {
            "impact": "Reduces 78.33-103.11 gigatons CO2",
            "ranking": "High Impact",
            "co_benefits": "Improves health, reduces meat consumption",
            "action": "Host plant-based potlucks, encourage meatless entrees at restaurants",
            "link": "https://drawdown.org/solutions/plant-rich-diets"
        },
        "3": {
            "impact": "Reduces 68.90 gigatons CO2",
            "ranking": "High Impact",
            "co_benefits": "Advances gender equality, improves well-being",
            "action": "Support education and family planning initiatives",
            "link": "https://drawdown.org/solutions/family-planning-and-education"
        },
        "4": {
            "impact": "Reduces 57.15 gigatons CO2",
            "ranking": "Medium Impact",
            "co_benefits": "Improves air quality, reduces health risks",
            "action": "Choose eco-friendly refrigerants, recycle old units properly",
            "link": "https://drawdown.org/solutions/refrigerant-management"
        },
        "5": {
            "impact": "Reduces 54.45-85.14 gigatons CO2",
            "ranking": "Medium Impact",
            "co_benefits": "Supports biodiversity, improves local ecosystems",
            "action": "Support tropical forest restoration initiatives",
            "link": "https://drawdown.org/solutions/tropical-forest-restoration"
        }
        
    }

    if choice in details:
        info = details[choice]
        print(f"\nImpact: {info['impact']}")
        print(f"Ranking: {info['ranking']}")
        print(f"Co-Benefits: {info['co_benefits']}")
        print(f"What You Can Do: {info['action']}\n")
        webbrowser.open(info["link"])
    else:
        print("Invalid choice. Please try again.")

def main():
    print("Welcome to Climate Choices!")
    print("In this game, you make decisions that impact the environment. Choose wisely!")
    
    print("\nChoose an action:")
    print("1. Reduce Food Waste")
    print("2. Adopt a Plant-Rich Diet")
    print("3. Support Family Planning and Education")
    print("4. Manage Refrigerants Properly")
    print("5. Restore Tropical Forests")

    choice = input("Enter your choice (1-5): ")
    show_details(choice)

if __name__ == "__main__":
    main()
