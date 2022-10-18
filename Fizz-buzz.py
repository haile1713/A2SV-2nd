class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
         answer_array = []

         for index in range(1,n+1):

            if ((index % 3 == 0) and (index % 5 == 0)):
                answer_array.append("FizzBuzz")
            elif index % 3 == 0:
                answer_array.append("Fizz")
            elif index % 5 == 0:
                answer_array.append("Buzz")
            else:
                answer_array.append(str(index))

         return answer_array
