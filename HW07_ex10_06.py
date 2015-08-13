# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def is_sorted(list_):
    index = 0
    for item in list_:
        if  index <= len(list_):
            if (item >= list_[index+1]):
                return False
        else:
            index +=1

    return True

def main():
    #print is_sorted([1,2,3,4,2])
    pass
        
main()
