

def is_prime(num):
    counts = []
    for number in range(1, num+1):
        if num % number == 0:
           counts.append(number)
           if len(counts) > 2:
               print("False")
           else:
                print("True")

is_prime(74)
