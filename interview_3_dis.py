a = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

def makeListofLists(a):
    
    new_list = []
    for i in a:  
        c, d = i
        new_list.append(list(range(c,d+1)))
        
    return new_list

def giveMinMax(alist):
    return (min(alist), max(alist))

def merge_ranges(a):
    #Sorting the tuples
    a = sorted(a)
    
    #making them lists of lists
    new_list = makeListofLists(a)
    
    meeting_times = []
    
    #examining any intersection points
    for l in range(len(new_list)-1):
        if l+1 >= len(new_list):
            break
        
        #finding intersection among first list and second list
        inter = list (set(new_list[l]) & set(new_list[l+1]))
        
        #If there is an intersection then
        if len(inter) >= 1:
            total_hours = sorted(new_list[l] + new_list[l+1])
            new_time = giveMinMax(total_hours)
            meeting_times.append(new_time)
            new_list.pop(l+1)
        #If no intersection then just take note of the times
        else:
            non_intersect_range = giveMinMax(new_list[l])
            meeting_times.append(non_intersect_range)
      
    return meeting_times
