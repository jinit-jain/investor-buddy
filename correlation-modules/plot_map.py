import matplotlib.pyplot as plt

def plot_map (xPoints):
    x = xPoints
    x.sort()
    plt.hist(x, bins=20)
    plt.gca().set(title='Correlation Distribution', ylabel='Frequency')
    plt.xticks(rotation=90, ha='right')
    plt.show()