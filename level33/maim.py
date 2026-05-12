# setis და listis განსხვავება ის არის რომ სეტი დაულაგებელია
# set_arr = {1, 2, 3, 4, 5, 6}
# set_arr.add(7)
# set_arr.remove(4)

# print(set_arr)

# me ={
#     "name" : "lazare",
#     "last name" : "bubuteishvili",
#     "age" : "12",
#     "grade" : "7", 
# }
# print(me)
#.keys ფუნქცია აბრუნებს dictionary-ის ყველა გასაღებს
#.values ფუნქცია აბრუნებს dictionary-ის ყველა მნიშვნელობას
#.get ფუნქციას გადაეცემა არგუმენტად გასაღები და გვიბრუნებს შესაბამის მნიშვნელობას
#.items ფუნქცია აბრუნებს dictionary-ის ყველა წყვილს (key-value) ტუპლედ





#1)
#.add() ფუნქცია setის ბოლოში ახალ ელემენტს ამატებს
#.remove() ფუნქცია setიდან ამოიღებს არგუმენტად მიღებულ ელემენტს
#.clear() ფუქნცია setიდან ყველა ელემენტს შლის
#.union() ფუნქცია ორი set-ის გაერთიანებულ ელემენტებს აბრუნებს
#.difference() ფუნქცია პირველ set-ში არსებულ, მაგრამ მეორე set-ში არმონაცემ ელემენტებს აბრუნებს
 
#dictionary - არის მეოაცემტამტა ტიპი და ის ინახავს ინფორმაციას წყვილების სახით(tuple) ის ინახავს key  და value 
# set_arr = {1, 2, 3, 4, 5, 6}
# set_arr.add(7)
# set_arr.remove(4)

sixseven={
    "ihate" : 67,
    "i also hate" : "labubu",
    "i dont drink" : "soda",
    "i love" : "water"
} 
print(sixseven.keys())
print(sixseven.items())