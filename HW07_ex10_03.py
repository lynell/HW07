# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(list_):
   return [count(list_[0:list_.index(item)+1]) for item in list_ ]

def count(item):
   return sum(item)
    
def main():
    print cumulative_sum([1, 2, 3])
main()
