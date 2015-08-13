# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def nested_sum(list_):
    sum_ = 0
    #original_list = list_[:]
    for value in list_:
        if type(value) != type(list_):
            sum_ += value
        else:
            sum_ += nested_sum(value)
    return sum_
    

            
        
def main():
    pass
if __name__ == '__main__':
    main()


#list_ = [1,2,3,[1,3,4,[5,6],[7,8]]]
