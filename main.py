def myfunction2(n, count=1):
    print(f"Call {count}: myfunction2({n})")
    if n <= 1:
        print("Codingal")
        print(f"Total Recursive Calls: {count}")
        print("Recurrence Relation: T(n) = T(n-1) + 1")
        print("Time Complexity: O(n)")
        return
    myfunction2(n - 1, count + 1)

myfunction2(5)
