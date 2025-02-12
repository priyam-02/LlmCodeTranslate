#GPT 4o second attempt
# def swapc(x, c):
#     if x > c:
#         return c, x  # Return swapped values
#     return x, c  # Return as-is if no swap is needed

# def main():
#     n = int(input())
#     for _ in range(n):
#         a, b, c = map(int, input().split())
        
#         # Reassign swapped values to a, b, c
#         a, c = swapc(a, c)
#         b, c = swapc(b, c)

#         if a * a + b * b == c * c:
#             print("YES")
#         else:
#             print("NO")

# if __name__ == "__main__":
#     main()


#3rd Attempt
# def swapc(x, c):
#     temp = x
#     if x > c:
#         x = c
#         c = temp
#     else:
#         pass

# def main():
#     n = int(input())
#     for _ in range(n):
#         a, b, c = map(int, input().split())
#         swapc(a, c)
#         swapc(b, c)

#         if a*a + b*b == c*c:
#             print("YES")
#         else:
#             print("NO")

# if __name__ == "__main__":
#     main()




#2nd attempt
# def swapc(x, c):
#     temp = x
#     if x > c:
#         x = c
#         c = temp
#     else:
#         pass

# def main():
#     n = int(input())
#     for i in range(n):
#         a, b, c = map(int, input().split())
#         swapc(a, c)
#         swapc(b, c)

#         if a*a + b*b == c*c:
#             print("YES")
#         else:
#             print("NO")

# if __name__ == "__main__":
#     main()



# GPT 4o
# def swap(x, c):
#     return min(x, c), max(x, c)

# def main():
#     n = int(input())
#     for _ in range(n):
#         a, b, c = map(int, input().split())
        
#         # Use the corrected swap function and reassign
#         a, c = swap(a, c)
#         b, c = swap(b, c)
        
#         if a * a + b * b == c * c:
#             print("YES")
#         else:
#             print("NO")

# if __name__ == "__main__":
#     main()



#Initial attempt Llama 3.1
# def swap(x, c):
#     x, c = (min(x, c), max(x, c))

# def main():
#     n = int(input())
#     for _ in range(n):
#         a, b, c = map(int, input().split())
#         swap(a, c)
#         swap(b, c)
        
#         if a*a + b*b == c*c:
#             print("YES")
#         else:
#             print("NO")

# if __name__ == "__main__":
#     main()




#Database solution
# for i in range(int(input())):
#     a,b,c=map(lambda x:int(x)**2,input().split())
#     if a+b==c or b+c==a or c+a==b:
#         print("YES")
#     else:
#         print("NO")



#Llama 3.1 solution p00004
# import math


# def solve_linear_system(a, b, c, d, e, f):
#     """
#     Solve a system of linear equations.

#     Args:
#         a (float): Coefficient of x in the first equation.
#         b (float): Coefficient of y in the second equation.
#         c (float): Constant term in the first equation.
#         d (float): Coefficient of x in the second equation.
#         e (float): Coefficient of y in the second equation.
#         f (float): Constant term in the second equation.

#     Returns:
#         tuple: Solutions to the system, x and y.
#     """
#     bai = d / a
#     aa = a * bai
#     bb = b * bai
#     cc = c * bai

#     try:
#         # Try to solve for y first using the formula (f - cc) / (e - bb)
#         y = (f - cc) / (e - bb)

#         # Now that we have y, substitute it into the second equation and solve for x
#         x = (c - b * y) / a

#         return x, y

#     except ZeroDivisionError:
#         # If e == bb, then we cannot solve for y, so return None
#         return None



# def main():
#     """
#     Main function that reads input from the user and prints output.
#     """
#     while True:
#         try:
#             # Read six floating point numbers from the user
#             a, b, c, d, e, f = map(float, input("Enter 6 numbers separated by spaces: ").split())

#             solution = solve_linear_system(a, b, c, d, e, f)

#             if solution is None:
#                 print("No solution exists.")
#             else:
#                 x, y = solution
#                 # Print the solutions to three decimal places
#                 print(f"{x:.3f} {y:.3f}")

#         except ValueError as e:
#             # If the input cannot be parsed into 6 numbers, raise an error
#             print("Invalid input. Please enter 6 numbers separated by spaces.")


# if __name__ == "__main__":
#     main()




#Chatgpt solution
# import sys

# def main():
#     for line in sys.stdin:
#         if not line.strip():
#             continue
#         a, b, c, d, e, f = map(float, line.split())
#         solution = solve_linear_system(a, b, c, d, e, f)
#         if solution is None:
#             print("No solution exists.")
#         else:
#             x, y = solution
#             print(f"{x:.3f} {y:.3f}")

# if __name__ == "__main__":
#     main()




# import sys

# def solve_linear_system(a, b, c, d, e, f):
#     try:
#         bai = d / a
#         aa = a * bai
#         bb = b * bai
#         cc = c * bai
#         y = (f - cc) / (e - bb)
#         x = (c - b * y) / a
#         return round(x, 3), round(y, 3)
#     except ZeroDivisionError:
#         return None

# for line in sys.stdin:
#     try:
#         a, b, c, d, e, f = map(float, line.split())
#         solution = solve_linear_system(a, b, c, d, e, f)
#         if solution is not None:
#             print(f"{solution[0]} {solution[1]}\n")
#     except ValueError:
#         continue





# import sys

# def solve_linear_system(a, b, c, d, e, f):
#     try:
#         bai = d / a
#         aa = a * bai
#         bb = b * bai
#         cc = c * bai
#         y = (f - cc) / (e - bb)
#         x = (c - b * y) / a
#         return f"{x:.3f} {y:.3f}"

#     except ZeroDivisionError:
#         return None

# for line in sys.stdin:
#     try:
#         a, b, c, d, e, f = map(float, line.split())
#         print(solve_linear_system(a, b, c, d, e, f))
#     except ValueError:
#         continue



# for line in sys.stdin:
#     n = int(line)
#     for _ in range(n):
#         a, b, c = map(int, input().split())
#         if min(a, c) == c and max(a, c) == c and abs(b - c) <= 1 or \
#            (min(a, b) == b and max(a, b) == b and abs(c - b) <= 1):
#             print("YES")
#         else:
#             print("NO")



# def swapc(x, c):
#     if x > c:
#         return c, x
#     else:
#         return x, c

# for line in sys.stdin:
#     try:
#         n = int(line)
#         for _ in range(n):
#             a, b, c = map(int, input().split())
#             a, c = swapc(a, c)
#             b, c = swapc(b, c)
#             if a**2 + b**2 == c**2:
#                 print("YES")
#             else:
#                 print("NO")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")




# import sys

# def swapc(x, c):
#     if x > c:
#         return c, x
#     else:
#         return x, c

# for line in sys.stdin:
#     try:
#         n = int(line)
#         for _ in range(n):
#             a, b, c = map(int, input().split())
#             a, c = swapc(a, c)
#             b, c = swapc(b, c)
#             if a**2 + b**2 == c**2:
#                 print("YES")
#             else:
#                 print("NO")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")




# import sys

# def LCM(a, b):
#     if b == 0:
#         return a
#     else:
#         r = a % b
#         return LCM(b, r)

# def swap(x, y):
#     x, y = sorted([x, y])

# def main():
#     for line in sys.stdin:
#         a, b = map(int, line.split())
#         lcm, gcd = LCM(a, b), a // LCM(a, b) * b
#         print(f"{lcm} {gcd}")

# if __name__ == "__main__":
#     main()




# import sys

# def reverse_string(s):
#     return s[::-1]

# for line in sys.stdin:
#     print(reverse_string(line.strip()))



# import sys

# def calculate_value(n):
#     a = 100000
#     for _ in range(n):
#         a *= 1.05
#         if a % 1000 != 0:
#             a += (1000 - a % 1000)
#     return int(a)

# for line in sys.stdin:
#     n = int(line.strip())
#     print(calculate_value(n))



# import sys

# def calculate_count(n):
#     count = 0
#     for a in range(10):
#         for b in range(10):
#             for c in range(10):
#                 for d in range(10):
#                     if a + b + c + d == n:
#                         count += 1
#     return count

# for line in sys.stdin:
#     n = int(line.strip())
#     print(calculate_count(n))



# import sys

# def count_primes(n):
#     a = [0] * (n + 1)
#     for i in range(2, n + 1):
#         if a[i] == 0:
#             j = 1
#             while i * j <= n:
#                 a[i * j] = 1
#                 j += 1
#     return sum(a)

# for line in sys.stdin:
#     m = int(line.strip())
#     print(count_primes(m))







# import sys

# def count_primes(n):
#     a = [0] * (n + 1)
#     ans = 0  # Correctly track the number of primes
#     for i in range(2, n + 1):
#         if a[i] == 0:
#             ans += 1  # Count the prime
#             j = 1
#             while i * j <= n:
#                 a[i * j] = 1
#                 j += 1
#     return ans  # Corrected return statement

# for line in sys.stdin:
#     m = int(line.strip())
#     print(count_primes(m))




# import sys

# def count_primes(m):
#     a = [0] * (m + 1)
#     ans = 0
#     for i in range(2, m + 1):
#         if a[i] == 0:
#             ans += 1
#             j = 1
#             while i * j <= m:
#                 a[i * j] = 1
#                 j += 1
#     return ans

# m = int(sys.stdin.readline().strip())
# while m != -1:
#     print(count_primes(m))
#     m = int(sys.stdin.readline().strip() or "-1")


# import sys

# def main():
#     max_val = float('-inf')
#     second_max_val = float('-inf')
#     third_max_val = float('-inf')

#     for _ in range(10):
#         n = int(sys.stdin.readline().strip())
#         if n > max_val:
#             third_max_val = second_max_val
#             second_max_val = max_val
#             max_val = n
#         elif n > second_max_val and n != max_val:
#             third_max_val = second_max_val
#             second_max_val = n
#         elif n > third_max_val and n not in (max_val, second_max_val):
#             third_max_val = n

#     print(max_val)
#     print(second_max_val)
#     print(third_max_val)

# if __name__ == "__main__":
#     main()


# import sys

# def main():
#     max_val = float('-inf')
#     second_max_val = float('-inf')
#     third_max_val = float('-inf')

#     for _ in range(10):
#         n = int(sys.stdin.readline().strip())
#         if n >= max_val:
#             third_max_val = second_max_val
#             second_max_val = max_val
#             max_val = n
#         elif n >= second_max_val and n != max_val:
#             third_max_val = second_max_val
#             second_max_val = n
#         elif n > third_max_val and n not in (max_val, second_max_val):
#             third_max_val = n

#     print(max_val)
#     print(second_max_val)
#     print(third_max_val)

# if __name__ == "__main__":
#     main()

# import sys
# import math

# def calculate_distance():
#     n = int(sys.stdin.readline())
#     while n > 0:
#         x1, y1, x2, y3, x3, y2 = map(float, sys.stdin.readline().split())
#         x12 = 2 * (x2 - x1)
#         y12 = 2 * (y2 - y1)
#         z12 = x1*x1 - x2*x2 + y1*y1 - y2*y2
#         x23 = 2 * (x3 - x2)
#         y23 = 2 * (y3 - y2)
#         z23 = x2*x2 - x3*x3 + y2*y2 - y3*y3
#         try:
#             x = (y12*z23 - y23*z12) / (x12*y23 - x23*y12)
#             y = (z12*x23 - z23*x12) / (x12*y23 - x23*y12)
#             r = math.hypot(x1 - x, y1 - y)
#             print("{:.3f} {:.3f} {:.3f}\n".format(x, y, r))
#         except ZeroDivisionError:
#             print("Error: Division by zero encountered.")
#         n -= 1

# if __name__ == "__main__":
#     calculate_distance()

# import sys
# import math

# def calculate_point(n):
#     while n > 0:
#         x1, y1, x2, y2, x3, y3 = map(float, sys.stdin.readline().split())
#         x12 = 2 * (x2 - x1)
#         y12 = 2 * (y2 - y1)
#         z12 = x1*x1 - x2*x2 + y1*y1 - y2*y2
#         x23 = 2 * (x3 - x2)
#         y23 = 2 * (y3 - y2)
#         z23 = x2*x2 - x3*x3 + y2*y2 - y3*y3
#         x = (y12*z23 - y23*z12) / (x12*y23 - x23*y12)
#         y = (z12*x23 - z23*x12) / (x12*y23 - x23*y12)
#         r = math.hypot(x1 - x, y1 - y)
#         print("%.3lf %.3lf %.3lf" % (x, y, r))
#         n -= 1

# calculate_point(int(sys.stdin.readline()))


# import sys

# def swap(temp, a, b):
#     temp1 = temp[a]
#     temp[a] = temp[b]
#     temp[b] = temp1

# temp = list(range(31))

# w, n = map(int, sys.stdin.readline().split())
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     swap(temp, a-1, b-1)

# for i in range(1, w+1):
#     print(temp[i])

# import sys

# # Read w and n
# w, n = map(int, sys.stdin.readline().split())

# # Initialize the list with 1-based indexing (1, 2, ..., w)
# temp = list(range(w+1))  # range(w+1) ensures we have indices from 0 to w

# # Swap the positions based on input
# for _ in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     temp[a], temp[b] = temp[b], temp[a]  # Swap directly

# # Print the modified sequence, skipping index 0
# for i in range(1, w+1):
#     print(temp[i])

# import sys
# import math

# def main():
#     x = [0] * 3
#     y = [0] * 3
#     xp = 0
#     yp = 0
#     cp = [0] * 3

#     while True:
#         line = sys.stdin.readline()
#         if not line:
#             break

#         values = list(map(float, line.split()))
#         if len(values) != 8:
#             continue

#         x[0], y[0], x[1], y[1], x[2], y[2], xp, yp = values
#         for i in range(3):
#             j = (i + 1) % 3
#             cp[i] = (x[j] - x[i]) * (yp - y[i]) - (y[j] - y[i]) * (xp - x[i])

#         if ((cp[0] > 0 and cp[1] > 0 and cp[2] > 0) or
#             (cp[0] < 0 and cp[1] < 0 and cp[2] < 0)):
#             print("YES")
#         else:
#             print("NO")

# if __name__ == "__main__":
#     main()


# import sys

# def main():
#     a = b = c = 0
#     for i in range(10):
#         n = int(sys.stdin.readline())
#         if n >= a:
#             c = b
#             b = a
#             a = n
#         elif n >= b:
#             c = b
#             b = n
#         elif n > c:
#             c = n
#     print(f"{a}\n{b}\n{c}")
    
# if __name__ == "__main__":
#     main()

# def main():
#     a = b = c = 0
#     for i in range(10):
#         n = int(input())
#         if n >= a:
#             c = b
#             b = a
#             a = n
#         elif n >= b:
#             c = b
#             b = n
#         elif n > c:
#             c = n
#     print(a)
#     print(b)
#     print(c)

# if __name__ == "__main__":
#     main()


# import sys

# def main():
#     a = b = c = 0
#     for _ in range(10):
#         n = int(sys.stdin.readline())
#         if n >= a:
#             c = b
#             b = a
#             a = n
#         elif n >= b:
#             c = b
#             b = n
#         elif n > c:
#             c = n
#     print(a)
#     print(b)
#     print(c)

# if __name__ == "__main__":
#     main()

# import sys

# def main():
#     a = b = c = 0
#     for _ in range(10):
#         n = int(sys.stdin.readline())
#         if n >= a:
#             c = b
#             b = a
#             a = n
#         elif n >= b:
#             c = b
#             b = n
#         elif n > c:
#             c = n
#     print(a)
#     print(b)
#     print(c)

# if __name__ == "__main__":
#     main()


# import sys
# import math

# def main():
#     n = int(sys.stdin.readline())
    
#     while n > 0:
#         x1, y1, x2, y2, x3, y3 = map(float, sys.stdin.readline().split())
        
#         # Intermediate calculations
#         x12 = 2 * (x2 - x1)
#         y12 = 2 * (y2 - y1)
#         z12 = x1**2 - x2**2 + y1**2 - y2**2
        
#         x23 = 2 * (x3 - x2)
#         y23 = 2 * (y3 - y2)
#         z23 = x2**2 - x3**2 + y2**2 - y3**2
        
#         # Compute coordinates
#         denominator = x12 * y23 - x23 * y12
#         if denominator == 0:
#             print("Error: Division by zero")
#             exit()
            
#         x = (y12 * z23 - y23 * z12) / denominator
#         y = (z12 * x23 - z23 * x12) / denominator
        
#         r = math.hypot(x1 - x, y1 - y)
        
#         # Print results formatted to 3 decimal places
#         print("{0:.3f} {1:.3f} {2:.3f}".format(x, y, r))
        
#         n -= 1

# if __name__ == "__main__":
#     main()

# import sys

# def main():
#     cars = [0] * 10
#     cnt = 0
#     for line in sys.stdin:
#         line_str = line.strip()
#         if not line_str:
#             in_car = 0
#         else:
#             try:
#                 in_car = int(line_str)
#             except ValueError:
#                 in_car = 0
#         if in_car != 0:
#             if cnt < len(cars):
#                 cars[cnt] = in_car
#                 cnt += 1
#         else:
#             if cnt > 0:
#                 cnt -= 1
#                 print(f"{cars[cnt]}")
#     return

# if __name__ == "__main__":
#     main()

# import sys

# def main():
#     a = [None] * 100
#     w = int(input().strip())
    
#     for i in range(w):
#         a[i] = i + 1
    
#     n = int(input().strip())
    
#     for j in range(n):
#         b, c = map(int, input().strip().split(','))
        
#         if a[c-1] == c and a[b-1] == b:
#             a[c-1] = b
#             a[b-1] = c
#         elif a[c-1] != c and a[b-1] == b:
#             a[b-1] = a[c-1]
#             a[c-1] = b
#         elif a[c-1] == c and a[b-1] != b:
#             a[c-1] = a[b-1]
#             a[b-1] = c
#         else:
#             d = a[b-1]
#             e = a[c-1]
#             a[b-1] = e
#             a[c-1] = d
    
#     for i in range(w):
#         print(a[i])

# if __name__ == "__main__":
#     main()


# w = int(input())
# a = [i + 1 for i in range(w)]
# n = int(input())

# for _ in range(n):
#     b, c = map(int, input().split(','))
#     if a[c-1] == c and a[b-1] == b:
#         a[c-1], a[b-1] = b, c
#     elif a[c-1] != c and a[b-1] == b:
#         a[b-1], a[c-1] = a[c-1], b
#     elif a[c-1] == c and a[b-1] != b:
#         a[c-1], a[b-1] = a[b-1], c
#     else:
#         d, e = a[b-1], a[c-1]
#         a[b-1], a[c-1] = e, d

# for num in a[:w]:
#     print(num)




# # Read integer w from input
# w = int(input())

# # Initialize array a with values 1 to w
# a = [i + 1 for i in range(w)]

# # Read integer n from input
# n = int(input())

# # Process each pair of integers b and c
# for _ in range(n):
#     # Read pair as a list split by comma
#     b, c = map(int, input().split(','))
    
#     # Check the conditions based on values at positions (b-1) and (c-1)
#     if a[c - 1] == c and a[b - 1] == b:
#         # Swap the values
#         a[c - 1], a[b - 1] = a[b - 1], a[c - 1]
#     elif a[c - 1] != c and a[b - 1] == b:
#         # Another swap scenario
#         a[c - 1], a[b - 1] = a[b - 1], a[c - 1]
#     elif a[c - 1] == c and a[b - 1] != b:
#         # Yet another swap situation
#         a[c - 1], a[b - 1] = a[b - 1], a[c - 1]
#     else:
#         # Handle the fourth case where both values are different
#         d, e = a[c - 1], a[b - 1]
#         a[c - 1], a[b - 1] = e, d

# # Output the resulting array up to w elements
# for num in a[:w]:
#     print(num)



# def main():
#     import sys
#     a = 0
#     while True:
#         try:
#             line = sys.stdin.readline()
#             if not line:
#                 break
#             value = int(line.strip())
#             a = value
#             if a == 0:
#                 break
#             b = 600 / a
#             # Convert to integer since it's used in range
#             b = int(b)
            
#             sum_total = 0
#             for i in range(1, b):
#                 e = i * a
#                 d = e ** 2
#                 c = a * d
#                 sum_total += c
            
#             print(sum_total)
#         except ValueError:
#             break
#     return

# if __name__ == "__main__":
#     main()


# import sys

# def main():
#     while True:
#         line = sys.stdin.readline()
#         if not line:
#             break
#         a_str = line.strip()
#         if not a_str:
#             continue
#         try:
#             a = int(a_str)
#         except ValueError:
#             break
#         if a == 0:
#             print(0)
#             break
#         b = 600 // a
#         sum_total = 0
#         for i in range(1, b):
#             e = i * a
#             d = e ** 2
#             c = a * d
#             sum_total += c
#         print(sum_total)
#     return

# if __name__ == "__main__":
#     main()

# import sys

# def convert(char_num):
#     int_num = []
#     for i in range(len(char_num) - 1, -1, -1):
#         int_num.append(int(char_num[i]) - 48)
#     return int_num

# def main():
#     sys.stdin.readline() # ignore first line
#     while True:
#         try:
#             dataSet = int(sys.stdin.readline())
#             break
#         except ValueError:
#             continue

#     for _ in range(dataSet):
#         count = 1
#         firstNum = sys.stdin.readline().strip()
#         secondNum = sys.stdin.readline().strip()

#         if len(firstNum) > 80 or len(secondNum) > 80:
#             print("overflow")
#             continue

#         fNum = [0] * 128
#         sNum = [0] * 128
#         sum_ = [0] * 128

#         convert(firstNum, fNum)
#         convert(secondNum, sNum)

#         for i in range(128):
#             sum_[i] = fNum[i] + sNum[i]

#         for i in range(128):
#             if sum_[i] >= 10:
#                 sum_[i] %= 10
#                 sum_[i + 1] += 1

#         k = 0
#         j = 127
#         while j >= 0:
#             if sum_[j] == 0 and j != 0:
#                 k += 1
#                 j -= 1
#             else:
#                 break

#         if k < 128 - 80:
#             print("overflow")
#         else:
#             for l in range(127 - k - 1, -1, -1):
#                 print(sum_[l], end='')

#             print()

# if __name__ == "__main__":
#     main()

# import sys

# def convert(char_num, int_num):
#     j = 0
#     for i in range(len(char_num) - 1, -1, -1):
#         int_num[j] = ord(char_num[i]) - 48
#         j += 1

# LEN = 128

# def main():
#     sys.stdin.readline() # ignore first line
#     while True:
#         try:
#             dataSet = int(sys.stdin.readline())
#             break
#         except ValueError:
#             continue

#     for _ in range(dataSet):
#         count = 1
#         firstNum = sys.stdin.readline().strip()
#         secondNum = sys.stdin.readline().strip()

#         if len(firstNum) > 80 or len(secondNum) > 80:
#             print("overflow")
#             continue

#         fNum = [0] * LEN
#         sNum = [0] * LEN
#         sum_ = [0] * LEN

#         convert(firstNum, fNum)
#         convert(secondNum, sNum)

#         for i in range(LEN):
#             sum_[i] = fNum[i] + sNum[i]

#         for i in range(LEN):
#             if sum_[i] >= 10:
#                 sum_[i] %= 10
#                 sum_[i + 1] += 1

#         k = 0
#         j = LEN - 1
#         while j >= 0:
#             if sum_[j] == 0 and j != 0:
#                 k += 1
#                 j -= 1
#             else:
#                 break

#         if k < LEN - 80:
#             print("overflow")
#         else:
#             for l in range(LEN - k - 1, -1, -1):
#                 print(sum_[l], end='')

#             print()

# if __name__ == "__main__":
#     main()



# import sys

# def convert(char_num, int_num):
#     j = 0
#     for i in range(len(char_num) - 1, -1, -1):
#         int_num[j] = ord(char_num[i]) - 48
#         j += 1

# def main():
#     LEN = 128
#     data = sys.stdin.read().split()
#     index = 0
#     dataSet = int(data[index])
#     index += 1
#     count = 1
    
#     while count <= dataSet:
#         count += 1
#         if index >= len(data):
#             break
#         first_num = data[index]
#         index += 1
        
#         if index >= len(data):
#             break
#         second_num = data[index]
#         index += 1
        
#         if len(first_num) > 80 or len(second_num) > 80:
#             print("overflow")
#             continue
        
#         f_num = [0] * LEN
#         s_num = [0] * LEN
#         sum_num = [0] * LEN
        
#         convert(first_num, f_num)
#         convert(second_num, s_num)
        
#         for i in range(LEN):
#             sum_num[i] = f_num[i] + s_num[i]
        
#         for i in range(LEN - 1):
#             if sum_num[i] >= 10:
#                 sum_num[i] %= 10
#                 sum_num[i + 1] += 1
        
#         k = 0
#         j = LEN - 1
#         while j >= 0:
#             if sum_num[j] == 0 and j != 0:
#                 k += 1
#                 j -= 1
#             else:
#                 break
        
#         if k < LEN - 80:
#             print("overflow")
#         else:
#             print("".join(map(str, sum_num[:LEN - k][::-1])))

# if __name__ == "__main__":
#     main()


# import math
# import sys

# def main():
#     d, r = 0, 0
#     x, y = 0, 0
#     rad = 90
#     while True:
#         line = sys.stdin.readline()
#         if not line: break
#         tokens = line.split(',')
#         d = int(tokens[0])
#         r = int(tokens[1])
#         if not d and not r: break
#         x += d * math.cos(rad * math.pi / 180)
#         y += d * math.sin(rad * math.pi / 180)
#         rad -= r
#     a = int(x)
#     b = int(y)
#     print(a, '\n', b, '\n')

# if __name__ == '__main__': main()


# import sys
# import math

# x = 0
# y = 0
# rad = 90

# for line in sys.stdin:
#     d, r = map(float, line.strip().split(','))
    
#     if not d and not r:
#         break
    
#     x += d * math.cos(math.radians(rad))
#     y += d * math.sin(math.radians(rad))
    
#     rad -= r

# a = int(x)
# b = int(y)

# print(a)
# print(b)



# import sys

# MAX = 81

# def get_line():
#     line = []
#     while True:
#         c = sys.stdin.read(1)
#         if c == '\n' or c == '':
#             break
#         line.append(c)
#     return ''.join(line)

# def judge(word):
#     for i in range(26):
#         if word.lower() in ["the", "this", "that"]:
#             return i
#         shift_word(word)
#     return -1

# def shift_word(word):
#     for i in range(len(word)):
#         if 'a' <= word[i] <= 'z':
#             word = list(word)
#             word[i] = chr((ord(word[i]) - ord('a') + 1) % 26 + ord('a'))
#             word = ''.join(word)
#     if word[-1] == '.':
#         word = word[:-1]

# def shift_line(n, line):
#     for i in range(len(line)):
#         if 'a' <= line[i] <= 'z':
#             line = list(line)
#             line[i] = chr((ord(line[i]) - ord('a') + n) % 26 + ord('a'))
#             line = ''.join(line)

# while True:
#     str_ = get_line()
#     line = str_
#     word = str_.split()[0]
#     if (shift_num := judge(word)) != -1:
#         shift_line(shift_num, line)
#     else:
#         while (word := next((w for w in str_.split() if w), None)) is not None and (shift_num := judge(word)) != -1:
#             shift_line(shift_num, line)
#             break
#     print(line + '\n')


# import sys

# MAX = 81

# def get_line():
#     str_ = []
#     while True:
#         c = sys.stdin.read(1)
#         if c == '\n' or c == '':
#             break
#         else:
#             str_.append(c)
#     return ''.join(str_) + '¬'

# def judge(word):
#     for i in range(26):
#         if word.lower() in ["the", "this", "that"]:
#             return i
#         shift_word(word)
#     return -1

# def shift_word(word):
#     word = list(word)
#     len_ = len(word)
#     for i in range(len_):
#         if 'a' <= word[i] <= 'z':
#             word[i] = chr((ord(word[i]) - ord('a') + 1) % 26 + ord('a'))
#     if word[-1] == '.':
#         word[-1] = '¬'
#     return ''.join(word)

# def shift_line(n, line):
#     for i in range(len(line)):
#         if 'a' <= line[i] <= 'z':
#             line[i] = chr((ord(line[i]) - ord('a') + n) % 26 + ord('a'))
#     return line

# while True:
#     str_ = get_line()
#     line = list(str_)
#     word = next((x for x in str_.split() if x), None)
#     if word is not None and (shift_num := judge(word)) != -1:
#         shift_line(shift_num, line)
#     else:
#         for word in str_.split():
#             if (shift_num := judge(word)) != -1:
#                 shift_line(shift_num, line)
#                 break
#     print(''.join(line) + '\n')





# import sys

# MAX = 81

# def get_line(str):
#     i = 0
#     c = ''
#     while (c != '\\n' and c != EOF) :
#         str[i] = c
#         i += 1
#     return i

# def judge(word):
#     for i in range(26) :
#         if word == 'the' or word == 'this' or word == 'that':
#             return i
#         shift_word(word)
#     return -1

# def shift_word(word) :
#     len = len(word)
#     for i in range(len):
#         if ('a' <= word[i] and word[i] <= 'z') :
#             word[i] = (word[i] - 'a' + 1) % 26 + 'a'
#     if word[len - 1] == '.':
#         word[len - 1] = ''

# def shift_line(n, line):
#     for i in range(len(line)):
#         if ('a' <= line[i] and line[i] <= 'z') :
#             line[i] = (line[i] - 'a' + n) % 26 + 'a'

# while True:
#     str = input()
#     line = ''
#     word = ''
#     if get_line(str) == 0:
#         break
#     strcpy(line, str)
#     word = strtok(str, " ")
#     shift_num = judge(word)
#     if shift_num != -1 :
#         shift_line(shift_num, line)
#     else:
#         while True:
#             word = strtok(NULL, " ")
#             shift_num = judge(word)
#             if shift_num != -1:
#                 shift_line(shift_num, line)
#                 break
#     print(line)

# import sys
 
# def LCM(a, b):
#  if b == 0:
#    return a
#  else:
#    r = a % b
#    return LCM(b, r)
 
# def swap(x, y):
#  temp = x
#  x = y
#  y = temp
 
# if __name__ == "__main__":
#  while True:
#    try:
#      a, b = map(int, input().split())
#      swap(a, b)
#      lcm = LCM(a, b)
#      gcd = a // lcm * b
#      print(lcm, end=" ")
#      print(gcd)
#    except EOFError:
#      break

# def lcm(a: int, b: int) -> int:
#     """Compute the least common multiple (LCM) of a and b."""
#     def gcd(x: int, y: int) -> int:
#         if y == 0:
#             return x
#         else:
#             return gcd(y, x % y)
    
#     # Use the formula: LCM(a, b) = |a*b| / GCD(a, b)
#     return abs(a * b) // gcd(a, b)


# def swap_values(x: int, y: int) -> tuple:
#     """Swap values of two variables x and y."""
#     if x < y:
#         x, y = y, x
#     return x, y


# def main():
#     while True:
#         try:
#             a, b = map(int, input().split())
#         except ValueError:
#             print("Invalid input. Please enter two integers separated by space.")
#             continue
        
#         # Swap values for printing
#         a, b = swap_values(a, b)
        
#         lcm_result, gcd_result = lcm(a, b)
        
#         print(f"{lcm_result} {gcd_result}")


# if __name__ == "__main__":
#     main()

# def reverse_string(input_str: str) -> None:
#     """Prints the reversed input string."""
#     print("".join(reversed(input_str)))


# if __name__ == "__main__":
#     user_input = input()
#     reverse_string(user_input)

# import math

# def calculate_result():
#     n = int(input())
#     a = 100000
    
#     for _ in range(n):
#         a = a * 1.05
#         if a % 1000 > 0:
#             a = (a + 999) // 1000 * 1000
            
#     return math.floor(a)

# result = calculate_result()
# print(result)


# import math
# n = int(input())
# a = 100000
# for i in range(n):
#     a *= 1.05
#     if a % 1000 != 0:
#         a = (math.floor(a/1000) + 1) * 1000
# print(a)

# import math
# n = int(input())
# while n > 0:
#     n -= 1
#     x1, y1, x2, y2, x3, y3 = map(float, input().split())
#     x12 = 2 * (x2 - x1)
#     y12 = 2 * (y2 - y1)
#     z12 = x1*x1 - x2*x2 + y1*y1 - y2*y2
#     x23 = 2 * (x3 - x2)
#     y23 = 2 * (y3 - y2)
#     z23 = x2*x2 - x3*x3 + y2*y2 - y3*y3
#     x = (y12*z23 - y23*z12) / (x12*y23 - x23*y12)
#     y = (z12*x23 - z23*x12) / (x12*y23 - x23*y12)
#     r = math.hypot(x1 - x, y1 - y)
#     print(f"{x:.3f} {y:.3f} {r:.3f}")




# import sys

# def main():
#     # Read all input at once
#     data = list(map(int, sys.stdin.read().split()))
    
#     # Convert to integers and ensure exactly 5 elements are present
#     if len(data) != 5:
#         print("Error: Exactly 5 integers required")
#         return
    
#     a = data[:]
    
#     for i in range(5):
#         for j in range(5):
#             if a[i] > a[j]:
#                 temp = a[i]
#                 a[i] = a[j]
#                 a[j] = temp
                
#     # Print the sorted array
#     for num in a:
#         print(num, end=' ')
#     print()

# if __name__ == "__main__":
#     main()


# import sys

# def main():
#     n = int(sys.stdin.readline())
#     k = 1
#     for i in range(n, 0, -1):
#         k *= i
#     print(k)

# if __name__ == "__main__":
#     main()

# import sys

# def main():
#     c = sys.stdin.read()
#     for char in c:
#         print(char.upper(), end='')

# if __name__ == "__main__":
#     main()

# import sys

# while True:
#     c = input()
#     if c == EOF:
#         break
#     print(c.upper())


# import sys

# def main():
#   while True:
#     c = sys.stdin.read(1)
#     if c == '': break
#     print(c.upper())

# if __name__ == "__main__":
#   main()


# import sys
# import math

# # Function to convert a character to uppercase
# def toupper(c):
#     return chr(ord(c) - 32) if ord(c) > 96 else c

# # Read input from stdin
# while True:
#     try:
#         # Read a character from stdin
#         c = sys.stdin.read(1)
        
#         # Check if EOF was reached
#         if not c:
#             break
        
#         # Convert the character to uppercase and print it
#         print(toupper(c))
    
#     except KeyboardInterrupt:
#         break

# import sys

# def main():
#     for c in sys.stdin.read():
#         print(c.upper())

# if __name__ == "__main__":
#     main()


# import sys

# def main():
#     allowed_chars = {'\x00', '\n', '\r', '\t', '\v', '\b'}
    
#     while True:
#         line = sys.stdin.readline()
#         if not line:
#             break
#         if line.strip() == '':
#             continue
#         for c in line:
#             if c in allowed_chars:
#                 print(chr(ord(c)).upper())
#         # Press Enter to exit the program

# if __name__ == "__main__":
#     main()

import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:  # Exit when EOF is reached
            break
        print(line.upper(), end="")  # Convert to uppercase and maintain format

if __name__ == "__main__":
    main()