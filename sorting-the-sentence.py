class Solution:
    def sortSentence(self, s: str) -> str:
        arr=s.split(" ")
        sort_sent=""
        for i in range (len (arr)):
            min_index = i
            for j in range (i+1, len(arr)):
                if arr[j][-1] < arr[min_index][-1]:
                    min_index = j
            if i != min_index:
                arr[min_index],arr[i] = arr[i], arr[min_index]
            sort_sent += arr[i][:-1] + ' '
        return (sort_sent[:-1])

        
