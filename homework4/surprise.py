# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def print_star_names(targets):
    for name in targets:
        print(name)

def print_star_spectral_types(targets):
    for name, info in targets.items():
        print(f"{name}: {info['Spectral Type']}")

def find_bright_stars(targets):
    for name, info in targets.items():
        if info['Magnitude'] > 0.1:
            print(f"{name}: {info['Magnitude']}")  

targets["Arcturus"] = {
    "RA": "14h 15m 39.7s",
    "Dec": "+19° 10′ 57″",
    "Magnitude": -0.05,
    "Spectral Type": "K1.5III"
}

import re

def declination_to_degrees(declination):
    parts = re.findall(r"\d+(?:\.\d+)?", declination)

    degrees = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])

    result = degrees + (minutes / 60) + (seconds / 3600)

    if declination.strip().startswith(("-", "-", "-")):
        result = -result

    return result


def find_star_near_twenty(targets):
    best_star = None
    smallest_distance = float('inf')
    best_magnitude = float('inf')   

    for name, info in targets.items():
        declination = declination_to_degrees(info["Dec"])
        distance = abs(declination - 20)
        magnitude = info["Magnitude"]

        if distance < smallest_distance or (distance == smallest_distance and magnitude < best_magnitude):
            best_star = name
            smallest_distance = distance
            best_magnitude = magnitude

        elif distance == smallest_distance:
            if magnitude < best_magnitude:
                best_star = name
                best_magnitude = magnitude

    return best_star

print("1. Star Names:")
print_star_names(targets)

print("\n2. Star Spectral Types:")
print_star_spectral_types(targets)

print("\n3. Stars with Magnitude > 0.1:")
find_bright_stars(targets)

print("\n4. Added target:")
print("Arcturus:", targets["Arcturus"])

print("\n5. Star closest to declination +20 degrees:")
print(find_star_near_twenty(targets))

favorite_constellation = input("\n6. What is your favorite constellation?")
print("My favorite constellation is:", favorite_constellation)