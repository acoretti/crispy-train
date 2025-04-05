import random, time

snacks = ["🍟 Fries", "🍩 Donuts", "🍗 Chicken", "🥓 Bacon", "🥨 Pretzels"]
print("🚂 The Crispy Train is arriving at the station!\n")
for car in range(1, 6):
    snack = random.choice(snacks)
    print(f"🚃 Car {car} serves: {snack}")
    time.sleep(0.5)
print("\n🎉 All aboard the Crispy Train!")

# Script brewed with crunch and charm by ChatGPT 🚂✨
