# linelist=[line.rstrip('\n') for line in open("currencies.txt")]
# print(linelist)

enteredString = "USDCNH"

# CHECK IF THE LENGTH IS 6
if len(enteredString) == 6:
    print('length is six')

# SPLIT THE STRING INTO TWO EQUAL PARTS OF 3 CHARACTERS EACH
def currencysep(word):
        s= ([word[i:i+3] for i in range(0, len(word), 3)]) 
        buy_currency= s[0]
        base_currency= s[1]
        return [buy_currency,base_currency]
inputCurrencies = currencysep(enteredString)
print(inputCurrencies)

# NOW CHECK IF THESE EXIST IN OUR CURRENCY LIST
if(all(x in linelist for x in inputCurrencies)):
     print ("Yes, we found both the currencies.")
else : 
    print ("No, Wrong input.") 
      
