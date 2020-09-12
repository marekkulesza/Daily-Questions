#Write a function that would take two lists and return one merged list,
# e.g. for the lists ['Washington, D.C.', 'Chicago', 'New York'] 
# and ['Los Angeles', 'Las Vegas'] the result should be 
# ['Washington, D.C.', 'Chicago', 'New York', 'Los Angeles', 
# 'Las Vegas'].


def merge_lists(list_one, list_two):
    new_list = list_one + list_two
    return new_list

merge_lists(['Washington, D.C.', 'Chicago', 'New York'],['Los Angeles', 'Las Vegas'])