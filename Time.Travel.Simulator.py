# time_travel_simulator.py
# Simulate an "experience" of a given year
import random
import sys
from datetime import datetime

TRIVIA = {
    1900: ["the gramophone is a prized item", "horses remain common in cities"],
    1920: ["jazz is booming in speakeasies", "aviation is thrilling the public"],
    1950: ["television is entering most homes", "rock'n'roll is emerging"],
    1985: ["arcades are popular", "the personal computer is spreading"],
    2000: ["the web is maturing", "mobile phones are getting smaller"],
    2025: ["remote work is widespread", "electric vehicles are becoming mainstream"]
}

def sim_headlines(year, seed):
    random.seed(year + seed)
    templates = [
        "Scientists announce breakthrough in {}.",
        "Markets react to {} as prices {}.",
        "Artists unite across {} to protest {}.",
        "New invention promises to {}."
    ]
    topics = ["energy storage", "communication", "transport", "medicine", "space travel", "culture"]
    verbs = ["soar", "plummet", "stabilize", "transform"]
    headlines = []
    for _ in range(5):
        t = random.choice(templates)
        topic = random.choice(topics)
        vb = random.choice(verbs)
        headlines.append(t.format(topic, vb))
    return headlines

def sim_weather(year, month=7, seed=0):
    random.seed(year + month + seed)
    avg_temp = 14 + (year - 2000) * 0.02 + random.uniform(-3,3)
    precip = random.choice(["drought", "normal rains", "heavy storms", "monsoon"])
    return avg_temp, precip

def sim_cost_of_living(year):
    base = 100.0
    inflation = 1.03 ** (year - 2000) if year >= 2000 else 0.97 ** (2000 - year)
    return base * inflation

def pick_trivia(year):
    keys = sorted(TRIVIA.keys())
    pick = max([k for k in keys if k <= year], default=keys[0])
    return TRIVIA[pick]

def time_travel(year):
    seed = year % 100
    now = datetime.now().year
    headlines = sim_headlines(year, seed)
    temp, precip = sim_weather(year, 7, seed)
    col_index = sim_cost_of_living(year)
    trivia = pick_trivia(year)
    era = "future" if year > now else "past" if year < now else "present"
    profile = {
        "year": year,
        "era": era,
        "headlines": headlines,
        "avg_july_temp_c": round(temp,1),
        "precip_pattern": precip,
        "cost_of_living_index": round(col_index,2),
        "cultural_trivia": trivia
    }
    return profile

def pretty_print(profile):
    print(f"=== Time-Travel: {profile['year']} ({profile['era']}) ===")
    print("Headlines:")
    for h in profile["headlines"]:
        print(" -", h)
    print(f"Avg July Temp (C): {profile['avg_july_temp_c']}, Precip: {profile['precip_pattern']}")
    print("Cost-of-living index (2000=100):", profile["cost_of_living_index"])
    print("Cultural notes:", ", ".join(profile["cultural_trivia"]))

if __name__ == "__main__":
    year = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Enter year to travel to: ") or "1985")
    p = time_travel(year)
    pretty_print(p)
