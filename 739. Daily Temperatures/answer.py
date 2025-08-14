def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    n = len(temperatures)
    ans = [0] * (n)
    stack = []
    for i,temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][1]:
            stack_i, stack_temperature = stack.pop()
            ans[stack_i] = i - stack_i
        stack.append((i, temperature))       

    return ans


    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # n = len(temperatures)
    # stack = []
    # result = [0] * n

    
    # for i in range (n):
    #     while stack and temperatures[i] > temperatures[stack[-1]]:
    #         prev_day = stack.pop()
    #         result[prev_day] = i - prev_day

    #     stack.append(i)

    # return result
            



        
