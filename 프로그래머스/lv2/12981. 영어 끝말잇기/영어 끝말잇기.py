def solution(n, words):
    answer = []
    word = []
    idx = 0
    
    for i in range(len(words)):
        num = i%n + 1
        cnt = (i//n) + 1
        if words[i] in word:
            print(num, cnt)
            return [num, cnt]
        elif i >= 1 and (words[i][0] != word[i-1][-1]):
            print(num, cnt)
            return [num, cnt]
        else:
            word.append(words[i])
    

    return [0, 0]