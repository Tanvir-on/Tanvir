crop_data = [
    {"name": "ধান", "pH_min": 5.5, "pH_max": 7.0, "N_min": 80, "N_max": 100, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 70},
    {"name": "আলু", "pH_min": 5.0, "pH_max": 6.5, "N_min": 60, "N_max": 90, "P_min": 25, "P_max": 40, "K_min": 45, "K_max": 65},
    {"name": "গম", "pH_min": 6.0, "pH_max": 7.5, "N_min": 85, "N_max": 100, "P_min": 35, "P_max": 60, "K_min": 55, "K_max": 75},
    {"name": "ভুট্টা", "pH_min": 5.8, "pH_max": 7.2, "N_min": 80, "N_max": 110, "P_min": 40, "P_max": 60, "K_min": 50, "K_max": 70},
    {"name": "সরিষা", "pH_min": 6.0, "pH_max": 7.5, "N_min": 60, "N_max": 85, "P_min": 25, "P_max": 45, "K_min": 45, "K_max": 65},
    {"name": "পাট", "pH_min": 5.5, "pH_max": 7.5, "N_min": 70, "N_max": 90, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 70},
    {"name": "আখ", "pH_min": 6.0, "pH_max": 7.0, "N_min": 100, "N_max": 140, "P_min": 45, "P_max": 60, "K_min": 60, "K_max": 80},
    {"name": "শাক", "pH_min": 6.2, "pH_max": 7.5, "N_min": 60, "N_max": 85, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 65},
    {"name": "লালশাক", "pH_min": 5.5, "pH_max": 6.8, "N_min": 50, "N_max": 75, "P_min": 20, "P_max": 40, "K_min": 40, "K_max": 60},
    {"name": "টমেটো", "pH_min": 5.5, "pH_max": 6.8, "N_min": 70, "N_max": 95, "P_min": 30, "P_max": 50, "K_min": 50, "K_max": 70},
    {"name": "বার্লি", "pH_min": 6.0, "pH_max": 7.5, "N_min": 60, "N_max": 80, "P_min": 15, "P_max": 25, "K_min": 30, "K_max": 50},
    {"name": "কাউন", "pH_min": 5.5, "pH_max": 7.0, "N_min": 60, "N_max": 80, "P_min": 20, "P_max": 30, "K_min": 30, "K_max": 50},
    {"name": "চীনা", "pH_min": 5.5, "pH_max": 6.5, "N_min": 60, "N_max": 80, "P_min": 15, "P_max": 25, "K_min": 30, "K_max": 50},
    {"name": "ব্রোকলি", "pH_min": 6.0, "pH_max": 7.0, "N_min": 100, "N_max": 140, "P_min": 25, "P_max": 35, "K_min": 60, "K_max": 80},
    {"name": "চাইনিজ বাঁধাকপি", "pH_min": 6.0, "pH_max": 7.0, "N_min": 160, "N_max": 210, "P_min": 35, "P_max": 50, "K_min": 100, "K_max": 150}
]

def suggestion(pH, N, P, K):
    suitable_crop = []
    for x in crop_data:
        if (x["pH_min"] <= pH <= x["pH_max"] and
            x["N_min"] <= N <= x["N_max"] and
            x["P_min"] <= P <= x["P_max"] and
            x["K_min"] <= K <= x["K_max"]):
            suitable_crop.append(x["name"])

    if suitable_crop:
        print("The suitable crop list based on soil parameter:", end=" ")
        for i in range(len(suitable_crop)):
            if i == len(suitable_crop) - 1:
                print(suitable_crop[i])
            else:
                print(suitable_crop[i], end=", ")
    else:
        print("No suitable crops found based on soil parameters.")

def month_suggest(month1):
    season_list = {}
    try:
        with open("E:\\rabi (2).txt") as file:
            for line in file:
                line = line.strip()
                key1 = line.split(",")[0]
                list1 = line.split(",")[1:]
                season_list[key1] = list1
    except FileNotFoundError:
        print("File E:\\rabi (2).txt not found.")
        return None

    for key, month2 in season_list.items():
        if month1 in month2:
            return key
        return None

def season_suggest(season_key):
    season_list2 = {}
    current_season = None
    with open("E:\\rabi (1).txt") as file:
        for line in file:
            line = line.strip()
            line4 = line.split(",")
            if len(line4) == 1:
                current_season = line4[0].strip()
                season_list2[current_season] = {}
            else:
                catagory = line4[0]
                crop = line4[1:]
                if current_season == season_key:
                    season_list2[season_key][catagory] = crop

    
    return season_list2[season_key]

def suggestion_crop_based_on_month():
    while True:
        print(" ")
        print("input pH, N, P, K values serially")
        a = float(input("enter the value of pH: "))
        b = float(input("enter the value of N: "))
        c = float(input("enter the value of P: "))
        d = float(input("enter the value of K: "))

        month = input("enter the month name: ").lower()

        season_key = month_suggest(month)
        if season_key:
            print(f"season found: {season_key.capitalize()}")
            print(" ")
            crops_data = season_suggest(season_key)
            if season_key in crops_data:
                for x, y in crops_data.items():
                    print("crop recomanded:")
                    print(f"{x}: {', '.join(y)}")
            else:
                print("No crops data found for this season.")
        else:
            print("\nNo season found for the given month.")

        suggestion(a, b, c, d)

# Start the program
suggestion_crop_based_on_month()
