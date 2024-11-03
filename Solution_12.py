if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = set(arr)
    maximum=max(score)
    score.remove(max(score))
    
    print(max(score))
