def remove_duplicates(nums):
    '''This function takes a sorted array and
    filters out the repeating values on place'''

    appearences = {}
    list_to_count_by = list(set(nums))
    list_to_count_by.sort()

    for item in list_to_count_by:
        appearences[item] = nums.count(item)

    delete_from = 1

    for key in appearences.keys():
        if appearences[key] > 1:
            del nums[delete_from:delete_from+appearences[key]-1]
        delete_from += 1
    return len(nums)
