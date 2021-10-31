
# open file in read mode
file = open("/Users/perceval/Documents/laurette/pg42324.txt", "r")

# read the content of file and replace spaces with nothing
data = file.read().replace(" ", "")

# get the length of the data
number_of_characters = len(data)


# get number of occurrences of the substring in the string
occurrences_A = data.count("A")
occurrences_a = data.count("a")
occurrences_E = data.count("E")
occurrences_e = data.count("e")
occurrences_I = data.count("I")
occurrences_i = data.count("i")
occurrences_O = data.count("O")
occurrences_o = data.count("o")
occurrences_U = data.count("U")
occurrences_u = data.count("u")


print('Number of characters in text file :', number_of_characters)
print('Number of A characters in text file :', occurrences_A)
print('Number of a characters in text file :', occurrences_a)
print('Number of E characters in text file :', occurrences_E)
print('Number of e characters in text file :', occurrences_e)
print('Number of I characters in text file :', occurrences_I)
print('Number of i characters in text file :', occurrences_i)
print('Number of O characters in text file :', occurrences_O)
print('Number of o characters in text file :', occurrences_o)
print('Number of U characters in text file :', occurrences_U)
print('Number of u characters in text file :', occurrences_u)


print('Total A - U :', occurrences_a + occurrences_A + occurrences_E + occurrences_e +
      occurrences_I + occurrences_i + occurrences_O + occurrences_o + occurrences_U + occurrences_u)
