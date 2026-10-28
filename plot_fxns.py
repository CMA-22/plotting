import matplotlib.pyplot as plt

def plot_hist(data):

    plt.hist(data,bins=7)
    plt.ylabel('counts')
    plt.title('frequency of letters')

    plt.show()
