def qsort1(a,lo,hi):
    if(lo >= hi):
        return
    pivot = a[lo]
    m = lo;
    for i in range(lo, hi + 1):
        if (a[i] < pivot):
            m = m + 1
            a[m], a[i] = a[i], a[m]
            
            

    a[lo], a[m] = a[m], a[lo]
    
    qsort1(a,lo,m-1)
    qsort1(a,m+1,hi)


def main():
    a= [2,3,4,5,2,3,4,7,8,9,0,4,5,6,7,7]
    qsort1(a,0,7)
    median = a[len(a) // 2]
    print(median)
main()
