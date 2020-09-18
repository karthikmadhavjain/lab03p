#Author: Karthik Madhav Jain kmj5614@psu.edu

def sum_n(n):
  if n == 0:
    return n
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if n>0:
    print(f"{s}")
    print_n(s,n-1)

def run():
  integer = int(input('Enter an int: '))
  added = sum_n(integer)
  print(f"sum is {added}.")
  string = input('Enter a string: ')
  print_n(string,integer)

if __name__ == "__main__":
    run()
  

