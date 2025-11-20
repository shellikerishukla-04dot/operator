import sys
if len(sys.argv) > 1:
    scores = sys.argv[1:] 
    print("User provided input values:")
else:
    print("No command-line input provided. Using default values:")
    scores = ["10", "20", "30", "40"]
total = sum(eval(x) for x in scores)
average = total / len(scores)
maximum = max(scores, key=eval)
minimum = min(scores, key=eval)
print("Sum of scores =", total)
print("Average of scores =", average)
print("Maximum score =", eval(maximum))
print("Minimum score =", eval(minimum))


