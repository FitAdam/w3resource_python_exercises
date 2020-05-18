"""26. Write a Python program to create a histogram from a given list of integers."""

histogram = []

def create_hist():
    n = int(input("Give some integers to create history: "))
    histogram.append(n)
    print(f"This is our historgram: {histogram}")
    for x in histogram:
        print(x * "*")

while True:
   create_hist()
