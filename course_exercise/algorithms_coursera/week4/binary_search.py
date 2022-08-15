def binary_search(keys, low, high, query):
    # keys are what we are searching for in the sorted query
    if high < low:
        return -1
    
    mid = int((low + (high-low)/2))
    
    if query == keys[mid]:
        return mid
    elif query < keys[mid]:
        return binary_search(keys, low, mid-1,query)
    else:
        return binary_search(keys, mid+1, high,query)

A = [1,5,8,12,13]
B = [8, 1, 23, 1, 11]

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, 0, len(input_keys)-1, q), end=' ')
