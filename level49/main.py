#map-გამოიყენება მაშინ, როცა გინდა ყველა ელემენტზე ერთი და იგივე რაღაცა გააკეთოს
#filter-გამოიყენება მაშინ როცა გინდა მხოლოდ გარკვეული ელემენტები დატოვო

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers2 = list(filter(lambda x: x % 2 != 0, numbers))
# print(numbers2)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers2= list(map(lambda x: x**2, numbers))
# print(numbers2)

# names = ["ანა","გიორგი","ალეკო","ჯემალა","ანდრია","ლუკა"]
# result = list(filter(lambda name: name.startswith("ა"), names))
# print(result)

# def food_ranking(category="food", *foods):
#     counter = 1
#     for food in foods:
#         print(category, counter, food)
#         counter = counter + 1
# food_ranking("food", "khinkali", "kai shaverma 22 lariani", "burger")

def car_builder(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
car_builder(brand="BMW", model="X5", color="black")
