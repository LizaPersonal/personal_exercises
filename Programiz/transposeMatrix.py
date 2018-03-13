# Program to transpose a matrix using nested loop

def matrixNestedLoop():
    X = [[12, 7],
         [4, 5],
         [3, 8]]

    result = [[0, 0, 0],
              [0, 0, 0]]

    # iterate through rows
    for i in range(len(X)):
        # iterate through columns
        for j in range(len(X[0])):
            result[j][i] = X[i][j]

    for r in result:
        print(r)


# Program to transpose a matrix using list comprehension
def matrixListComprehension():
    X = [[12, 7],
         [4, 5],
         [3, 8]]

    result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

    for r in result:
        print(r)

matrixNestedLoop()
matrixListComprehension()