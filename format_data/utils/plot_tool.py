import matplotlib.pyplot as plt


def plot(x_data, y_data, x_label, y_label, title, bar=True):

    if bar:
        plt.bar(x_data, y_data)
    else:
        plt.plot(x_data, y_data)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
