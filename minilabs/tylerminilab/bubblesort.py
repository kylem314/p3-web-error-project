import sys,time

array=[]

i=1
while (i < len(sys.argv)):
    array.append(int(sys.argv[i]))
    i+=1

def BubbleSort(array_data):
    length=len(array_data)
    result = True
    global count
    while result:
        result = False
        i=0
        while (i < length-1):
            if (array_data[i] > array_data[i+1]):
                temporary = array_data[i]
                array_data[i] = array_data[i+1]
                array_data[i+1] = temporary
                result = True
            i=i+1
            count+=1

    return array_data
count = 0
Time = time.time()
array_result = str(BubbleSort(array))
