"""
For the 2024_08 blog post "Comparing Classifier Performance -- Introduction to BEA"
"""
# numerical analysis
import numpy as np

# visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_style('darkgrid')
sns.set_palette('colorblind')

N_SAMPLES: int = 100

def delta_degree(deg1, deg2):
    """
    Returns the difference between two angles, ensuring that the range
    lies within [-180,180]. This is important since -179 and +179 have
    are only 2 degrees apart
    """
    delta = deg1 - deg2
    while delta > +180:
        delta -= 360
    while delta < -180:
        delta += 360
    return delta

def accuracy_from_hearing_simulation(C: int = 2):
    """
    Simulates an experiment where a participant is asked to choose where a noise comes from.
    They are given C category choices, and the noise comes from a random angle in [-pi,pi].
    """
    global N_SAMPLES
    C = max(2, C)

    # generate the bin centers. 0 is forward, 90 is right, -90 is direct left,
    # -180 is directly back, on the left
    forward_degree = 360 * (C - 1) / (2 * C)
    center_degrees = [360 * i / C - forward_degree for i in range(C)]

    degree_truths = [0] * N_SAMPLES
    class_choices = [0] * N_SAMPLES
    class_truths = [0] * N_SAMPLES
    for isample in range(N_SAMPLES):

        # where the sound comes from
        trial_degree = 180 * (np.random.random() * 2 - 1)

        # point towards the sound
        response_degree = np.random.normal(trial_degree, scale=10)
        choice = np.argmin(np.abs([delta_degree(response_degree, c) for c in center_degrees]))

        # the true bin the sound came from
        truth = np.argmin(np.abs([delta_degree(trial_degree, c) for c in center_degrees]))

        degree_truths[isample] = trial_degree
        class_choices[isample] = choice
        class_truths[isample] = truth

        if isample < 0:
            # for debugging set 0 -> e.g. 10
            print(f"Degree {trial_degree:.1f} closest to {center_degrees[truth]:.2f}. "
                  f"Choice {choice} with truth {truth}")

    n_correct = np.sum([choice == truth for choice, truth in zip(class_choices,class_truths)])
    print(f"{C}, {100*n_correct/N_SAMPLES}%, "
          f"{binary_equivalent_accuracy(n_correct / N_SAMPLES, C):.3F}")

    return n_correct/N_SAMPLES

def binary_equivalent_accuracy(acc_c, n_cats):
    """
    Returns the binary-equivalent accuracy, i.e. it doesn't account for the performance
    of randomly guessing.
    """
    nbea = acc_c ** (1 / (n_cats-1))
    return nbea

def run_and_plot_accuracies():
    """
    Goes through n_classes = 2...360 to perform a "hearing test". The accuracies are plotted,
    as well as their binary-equivalent counterparts
    """
    cats = []

    accs = []
    beas = []
    sigmas_acc = []
    sigmas_bea = []
    for n_cats in range(2,300):
        cats.append(n_cats)

        acc = accuracy_from_hearing_simulation(n_cats)
        bea = binary_equivalent_accuracy(acc, n_cats)

        sigma_acc = (acc*(1-acc)/N_SAMPLES)**0.5
        sigma_bea = sigma_acc * acc**(1/(n_cats-1)-1) / (n_cats-1)

        accs.append(acc)
        sigmas_acc.append(sigma_acc)

        beas.append(bea)
        sigmas_bea.append(sigma_bea)

    # accuracy plotting
    fig, ax = plt.subplots()
    sns.scatterplot(x=cats, y=accs, label="Accuracy")
    ax.errorbar(x=cats,
                y=accs,
                yerr=sigmas_acc,
                ecolor=sns.color_palette()[0],
                ls='None'
                )
    sns.scatterplot(x=cats, y=beas, label="BEA")
    ax.errorbar(x=cats,
                y=beas,
                yerr=sigmas_bea,
                ecolor=sns.color_palette()[1],
                ls='None'
                )
    plt.show()


if __name__ == "__main__":
    run_and_plot_accuracies()
