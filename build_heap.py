# python3


def build_heap(data):
    swaps = []
    x=len(data)
    for i in range(x//2,-1,-1):
        sort(data,i,swaps)

    return swaps

def sort(data,i,swaps):
    x=len(data)
    right=2*i+2
    left=2*i+1
    lir=i 
    if left<x and data[left]<data[lir]:
        lir=left
    if right<x and data[right]<data[lir]:
        lir=right
    if i!=lir:
        data[i],data[lir]=data[lir],data[i]
        swaps.append((i,lir))
        sort(data,lir,swaps)
def main():
    
   t=input()
    if 'F' in t:
        t_file=input()
        with open("tests/"+t_file, 'r') as f:
            x=int(f.readline())
            data=list(map(int, f.readline().split()))
    else:
       n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
