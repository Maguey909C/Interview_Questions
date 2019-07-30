a = [1,3,4,5,6]

def summation(alist,value):

    show_sums =  []

    for i in range(0,len(alist)):

        print ("")

        for j in range(len(alist)):

            if i == j:

                print ("Skipped because i =",i,"j=",j)

                pass

            else:

                print (alist[i],alist[j],"=",alist[i]+alist[j])

                if alist[i]+alist[j] == value:

                    show_sums.append((i,j))

    return show_sums
    
    summation(a,5)
