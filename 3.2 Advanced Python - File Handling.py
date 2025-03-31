# Read
data = open('./data.txt', mode='r', encoding='utf-8')

string = data.read()
string = string.replace('adalah', 'merupakan')
print(string)

# Append
data = open('./data.txt', mode='w', encoding='utf-8')
data.write("Yuk belajar Bitcoin!")
data.close()