"""
For the 2024_06 blog post "Comparing Classifiers with Different Class Counts"
"""
# numerical analysis
import numpy as np
import pandas as pd
import scipy

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
    lies within [-180,180]. This is important since -179 and +179 have a difference of 2 degrees
    """
    delta = deg1 - deg2
    while delta > +180:
        delta -= 360
    while delta < -180:
        delta += 360
    return delta

def response_function(degree, degree_C, width):
    """
    The unnormalized probability that a sound from direction theta will be interpreted
    by the partcipant to be in category C with bin-center theta_C. The width controls how
    fast the response drops.
    """
    delta = delta_degree(degree,degree_C)
    exp_arg = delta / width
    return np.exp(-exp_arg ** 2)


def get_bin_mids_props_sigmas(df, col_name, positive_label, nbins=10):
    """
    Get bin position, the proportion of correct responses, and the associated standard error
    """

    bins = np.linspace(-180, 180, nbins, endpoint=True)
    bin_mids = []
    props = []
    errs = []

    for bin_low, bin_high in zip(bins[:-1], bins[1:]):
        mask = (bin_low <= df[col_name]) & (df[col_name] < bin_high)
        tmp_prop = df[mask][positive_label].mean()  # the proportions
        tmp_count = len(df[mask])  # count all in the bin. For error bars

        bin_mids.append((bin_low + bin_high) / 2)
        props.append(tmp_prop)

        # from usual binomial variance V_count = np(1-p), sigma_count = sqrt(np(1-p))
        # so sigma prop = sqrt(p(1-p)/n)
        if tmp_count > 1:
            err_low = np.sqrt(tmp_prop * (1 - tmp_prop) / (tmp_count - 1))
            err_high = np.sqrt(tmp_prop * (1 - tmp_prop) / (tmp_count - 1))
        else:
            err_low =  0.5 if tmp_prop > 0.5 else 0
            err_high = 0.5 if tmp_prop < 0.5 else 0
        errs.append((err_low,err_high))
        # also correct for fact you can't estimate variance from a single data point

    for idx, prop in enumerate(props):
        if np.isnan(prop):
            props[idx] = np.nanmean(props)

    return bin_mids, props, np.transpose(errs)

def histogram_accuracy_by_angle(bins_props_sigmas):
    bins, props, sigmas = bins_props_sigmas
    fig, ax = plt.subplots()
    sns.scatterplot(x=bins, y=props, ax=ax)
    ax.errorbar(x=bins,
                y=props,
                yerr=sigmas,
                xerr=(bins[1] - bins[0]) / 2,
                ecolor=sns.color_palette()[0],
                ls='None'
                )
    # ax.legend()
    plt.show()

def plot_accuracy_by_degree(degrees, choices, truths, nbins=10):
    df_dict = {
        'deg': degrees,
        'choice': choices,
        'truth': truths,
    }
    df = pd.DataFrame(df_dict)
    df['correct'] = (df['choice'] == df['truth'])
    bins_props_sigmas = get_bin_mids_props_sigmas(df, 'deg', positive_label='correct', nbins=nbins)
    histogram_accuracy_by_angle(bins_props_sigmas)


def run_hearing_simulation(C: int = 2):
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

    degree_truths = []
    class_choices = []
    class_truths = []
    for isample in range(N_SAMPLES):

        # where the sound comes from
        trial_degree = 180 * (np.random.random() * 2 - 1)

        # # the human response to the sound, for each bin
        # # need to emulate "the abilitity to distinguish each category at the maximum category count"
        # # word of the day -- cardinality
        # # max bins = 36 so 360/36 = 10 degrees per bin, so 5 degree sigma
        # responses = [response_function(trial_degree, c, 50) for c in center_degrees]
        # responses = np.array(responses) / np.sum(responses)
        #
        # # the human's choice based on the relative size of the response
        # choice = np.random.choice(C, p=responses)

        # point towards the sound
        response_degree = np.random.normal(trial_degree, scale=2)
        choice = np.argmin(np.abs([delta_degree(response_degree, c) for c in center_degrees]))

        # the true bin the sound came from
        truth = np.argmin(np.abs([delta_degree(trial_degree, c) for c in center_degrees]))

        degree_truths.append(trial_degree)
        class_choices.append(choice)
        class_truths.append(truth)

        if isample < 0:
            print(f"Degree {trial_degree:.1f} closest to {center_degrees[truth]:.2f}. Choice {choice} with truth {truth}")

    n_correct = np.sum([choice == truth for choice, truth in zip(class_choices,class_truths)])
    #print(f"Accuracy is {100*n_correct/N_SAMPLES}%")
    print(f"{C}, {100*n_correct/N_SAMPLES}")

    # # plot_accuracy_by_degree(degree_truths, class_choices, class_truths, nbins=180)
    #
    # # probability that n_correct successes or more occurred by chance
    # chance = scipy.stats.binom.sf(n_correct,N_SAMPLES,1/N_SAMPLES)
    # print(f"{chance=}")

def binary_equivalent_accuracy_pvalue(acc_c, n_cats):
    """
    Returns the self-coined "Binary-Equivalent Accuracy".
    This method is based on matching z-scores for measured accuracies (n=M*acc, mu=Mp, var = Mpq)
    (assuming chance p = 1/n_cats in the limit of M trials -> infinity)
    and comparing to the same z-score for n_cats = 0
    """
    p2, pc = 1 / 2, 1 / n_cats
    q2, qc = 1 - p2, 1 - pc
    R = (pc / qc) ** 0.5
    return p2 + (acc_c - pc) * R * ( (p2*q2) / (pc * qc) ) ** 0.5

def binary_equivalent_accuracy(acc_c, n_cats):
    """
    Returns the self-coined "Binary-Equivalent Accuracy".
    This method is based on assuming that for n_cats, a success occurs if all pairwise
    comparisons are also successful, with the success probability for each pair in the
    gauntlet being equal to the equivalent binary accuracy
    """
    return acc_c ** (1 / (n_cats-1))

# TODO: from the autofit printout, does this tell me anything about how to "correct for"
#  number of categories? Or how to compare different numbers of categories? Cardinality?
if __name__ == "__main__":

    chance0 = scipy.stats.binom.sf(5,6,1/1000)
    print(f"{chance0=}")

    for acc in range(101):
        a = acc/100

        print(f"{a}: {binary_equivalent_accuracy(a, 6):.3f}")

        # print( f"{a}: {scipy.stats.norm.sf(z,0,1):.3f}" )
        # print(f"{a}: {scipy.stats.binom.sf(M*a,M, p):.3f}")
    # for d in [2,6,36]:
    # for d in range(360):
    #     run_hearing_simulation(d+2)

