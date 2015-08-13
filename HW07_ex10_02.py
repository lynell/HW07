# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def capitalize_nested(list_):
    index = 0
    #original_list = list_[:]
    for value in list_:
        if type(value) != type(list_):
            
            temp = value.capitalize()
            list_[index] = temp
            index +=1
            
        else:
            capitalize_nested(value)
            index +=1
    return list_
    

            
        
def main():
    print capitalize_nested(['a','n','j',['a','b','k']])
if __name__ == '__main__':
    main()


#list_ = [1,2,3,[1,3,4,[5,6],[7,8]]]
