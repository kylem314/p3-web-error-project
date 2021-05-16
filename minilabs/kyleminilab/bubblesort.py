import sys
sorting_list = []
count = 0

i=1
while (i < len(sys.argv)):
   sorting_list.append(int(sys.argv[i]))
   i += 1

def SortAlgorithm(test_list):
    global count
    result = True
    iterations = len(test_list)
    while result:
        result = False
        i=0
        while (i < iterations - 1):

# Logic for sorting the list

            if (test_list[i] > test_list[i + 1]):
                var = test_list[i]
                test_list[i] = test_list[i + 1]
                test_list[i + 1] = var
                result = True

            i = i + 1
            count += 1

    return test_list

sorting_list_result = str(SortAlgorithm(sorting_list))
