"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

temperatures = [15.0, 12.7, 13.4, 14.0, 15.2, 17.0, 16.6]
city_population = {
    "Riga": 591882,
    "Jelgava": 61304,
    "Talinn": 456518,
    "Vilnius": 607667,
    "Klaipeda": 160885,
}

average_temperature = sum(temperatures) / len(temperatures)
largest_city = ""
largest_population = 0
total_population = 0

for city, population in city_population.items():
    total_population += population
    if population > largest_population:
        largest_city = city
        largest_population = population

print("Average temperature:", average_temperature)
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
