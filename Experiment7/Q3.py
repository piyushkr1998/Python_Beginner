try:
    with open("city.txt", "r") as file:
        cities = [line.strip().split() for line in file if line.strip()]

    print("All City Details:")
    total_area = 0

    for city in cities:
        name = city[0]
        population = float(city[1]) 
        area = float(city[2])         

        print(f"City: {name}, Population: {population} lakhs, Area: {area} sq km")
        if population > 10:
            print(f"→ {name} has population more than 10 lakhs")
        total_area += area

    print("\nTotal Area of all cities:", total_area)

except FileNotFoundError:
    print("File not found! Please check the file location.")
except ValueError:
    print("Error in file format! Please check data.")