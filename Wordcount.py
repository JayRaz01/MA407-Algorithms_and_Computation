# Name: Jay Razda

def wordcount(text):
    text = ' ' + text + ' ' # to prevent first index from being a non-whitespace followed by whitespace
    count = 0
    counter_list = [0] # list with non-zero elements for words and zero elements for whitespace
    for i in range(0, len(text)-1):
        if (text[i].isspace() == False) and (text[i+1].isspace() == False): # if non-whitespace followed by non-whitespace
            counter_list[-1] += 1

        elif (text[i].isspace() == True) and (text[i+1].isspace() == False): # or, if whitespace followed by non-whitespace
            counter_list[-1] += 1

        else:
            counter_list.append(0)
    for j in counter_list:
        if j != 0:
            count += 1 # counting the the number of non-zero elements in the list i.e. number of words
    return count

result = wordcount(text='Welcome, this is my word-counter function')
# print appropriate outcome based on result
if result == 0:
    print('There are no words in this text')
elif result == 1:
    print('There is 1 word in this text')
elif result > 1:
    print(f'There are {result} words in this text')
