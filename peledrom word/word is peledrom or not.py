#Define a function.
def peledrom (input_string):
# read the word in reverse order
   reserve_word=input_string[::-1]
   return input_string==reserve_word
# if word is correct in reverse order display true
input=input("Enter a peledrom word:")
output=peledrom(input)
print(output)
