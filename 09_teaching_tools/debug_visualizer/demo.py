import numpy as np

# put "x" in the Debug Visualizer and use step by step
# debugging to see the diffrent types of data visualization

x = 5
x = "asdf"
x = 5.5
x = [1, 2, 3, 4, 5, 6, "a", "b"]
x = ["b", "a", "c", "d", "e"]
x.sort()
x = {
    "asdf1": "dasdf",
    "asdf2": "dasdf",
    "asdf3": {"foo": "bar"},
}

x = [1, 2, 3, 4, 5, 6]
# histogram
x = np.concatenate([np.arange(i) for i in range(9)])
x = x.reshape(2, -1)


# one dimension
x = np.arange(100)
x = np.linspace(-np.pi, np.pi, 100)
x = np.sin(x)

# 2 dimension
x = x.reshape(5, 20)
# 2 dimension transpose
x = x.transpose()
x = x.transpose()

# 3 dimensions
x = x.reshape(2, 5, 10)

# 4 dimensions
x = x.reshape(2, 5, 2, 5)

# big number
x = np.empty(2 ** 24)
x[0:1000000] = 1
x[1000000:10000000] = 5
