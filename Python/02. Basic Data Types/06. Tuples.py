if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    list_tuple = tuple(integer_list)
    
    print(hash(list_tuple))