import seaborn as sns
import matplotlib.pyplot as plt

def plot_map (xPoints):
    sns.set(color_codes=True)
    sns.distplot(xPoints, bins=20)
    plt.show()


