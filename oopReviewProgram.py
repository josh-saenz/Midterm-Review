import csv
import oopReviewClass as o
import csv
# 1) create a class called 'Pet' and give it the following attributes. The user should assign the values of the attributes. Make sure the attributes are hidden
'''
type (string) ex: 'dog'
weight (string) ex: '24.7 lbs'
limbs (int) ex: 4
age (float) ex: 2.5
name (string) ex: 'Dug'
'''


# 2) in your class, create get methods for each of the attributes



# 3) Create 3 different instances of your class. These can be whatever you would like them to be, as long as they are different.
dog = o.Pet('dog', '10 lbs', 4, 5, 'Oliver')
cat = o.Pet('cat', '5 lbs', 4, 8, 'Bentley')
bird = o.Pet('bird', '1 lbs', 2, 3, 'Jane')

# 4) Create a dictionary called 'pets' that has the pet name as the key, and the rest of the attributes as the values in a list
pets = {}
pets[dog.get_name()] = [dog.get_type(), dog.get_weight(), dog.get_limbs(), dog.get_age()]
pets[cat.get_name()] = [cat.get_type(), cat.get_weight(), cat.get_limbs(), cat.get_age()]
pets[bird.get_name()] = [bird.get_type(), bird.get_weight(), bird.get_limbs(), bird.get_age()]
# 5) Create a new method of your class called 'move.' This should have the user assign a value and the method will multiply it by the limbs attribute.
# create a get attribute for this method.



# 6) print out the distance each of your pets move
dog.move(5)
print(dog.get_move())
cat.move(2)
print(cat.get_move())
bird.move(8)
print(bird.get_move())


# 7) create a csv file with the following format:
'''
name,type,weight,limbs,age
'''
outfile = open('pets.csv', 'w', newline='')
writer = csv.writer(outfile, delimiter=',')

writer.writerow('name, type, weight, limbs, age\n')


for key in pets:
    writer.write(key + ',')
    writer.write(pets[key][0] + ',')
    writer.write(pets[key][1]+ ',')
    writer.write(str(pets[key][2]) + ',')
    writer.write(str(pets[key][3]) + '\n')

outfile.close()