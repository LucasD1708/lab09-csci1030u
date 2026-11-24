# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   we are trying to compare a number to the number after it in the order
    #   if the two numbers add up to our target value, then we want to return the indices
    #   gonna go through every number in the list, check them, add them and see if they equal the target, if they do it will return their position
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]



def max_profit(prices):
    # Outline:
    #   Profit = revenue - expenses
    #   therefore we want to find the lowest value of expenses so our profit is as high as possible
    #   we will compare the profit at which we are currently looking at to the highest profit (starting as 0) if current profit is larger than the last,
    #   then it will become the profit
    #   the function will return the highest profit that it can achieve
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0
    profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            current_profit = prices[j] - prices[i]

            if current_profit > profit:
                profit = current_profit

    return profit
    


def max_subarray(nums):
    # Outline:
    #   we want to find two numbers that generate the largest sum that are together in a row
    #   were gonna keep track of every sum found and compare it to the next sum in the row to ensure that it continues to be the highest
    #   if it is not, then the sum will be replaced by the new highest(generally the same idea as the last function reversed to be biggest rather than smallest)
    #   using loops in the same way once again to check the entire list
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in    pass
    
    maxSum = nums[0]

    for i in range(len(nums)):
        sum = 0

        for j in range(i, len(nums)):
            sum += nums[j]

            if sum > maxSum:
                maxSum = sum

    return maxSum

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   similair to the lecture example
    #   we are observing brackets in 's', using a stack
    #   we need each set of brackets to be closed, so we need to check for every closing bracket that there exists and opening bracket
    #   in the case that all the brackets match it should return true
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)

    newStack = []
    for parentheses in s:
        if parentheses == '(' or parentheses == '[' or parentheses == '{':
            newStack.append(parentheses)

        elif parentheses == ')' or parentheses == ']' or parentheses == '}':
            if len(newStack) == 0:
                return False

            last = newStack.pop() #most recent

            if parentheses == ')' and last != '(':
                return False
            if parentheses == ']' and last != '[':
                return False
            if parentheses == '}' and last != '{':
                return False

    return len(newStack) == 0



def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
