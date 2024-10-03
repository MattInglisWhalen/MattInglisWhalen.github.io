---
title: 'Comparing Classifier Performance -- Introduction to BEA'
date: 2024-06-10
permalink: /blog/2024-06-10--Comparing-N-vs-M-Classifiers
author_profile: true
---



<h6 align="right">Reading time: 10 minutes</h6> 

*Where'd you get the idea, Matt?*

I have a nifty program called [MIW's AutoFit](https://github.com/MattInglisWhalen/MIW_AutoFit) 
that fits 1D data to a variety of functional models.
These functional models are built procedurally from a list of primitive functions 
[sin(x), cos(x), exp(x), log(x), x, 1/x, const] that are combined in standard ways 
(addition, multiplication, composition). The cool part of this program is that MIW's AutoFit will
test each procedurally-generated functions, and of those tested it will tell you which 
model is the **best** for your data.

I was trying to come up with a way to quote a single number for the performance of this program
(let's say for a resumé).
It currently has a 95% accuracy with a depth of 1 (7 functional models), 
a 63% accuracy when the depth is 2 (15 models), 
40% accuracy when the depth is 3 (120 models), 
and a 21% accuracy when the depth is 4 (600 models). Which accuracy do I quote? 
An accuracy of 95% is deceptive, an accuracy of 20% undersells the power of the program, and
quoting many accuracies along with the context is too confusing for an impatient reader.

This got me to thinking: how do you compare the performance of classification algorithms
when the number of classes is different? Is a binary classifier with an accuracy of 99.99% 
actually better than a classifier with an accuracy of 20% across 1000 classes?

## Running the Gauntlet

Imagine you've built a model that can classify images into 5 categories. When provided 
with an image, it will output the degree of association$^†$ $\mathbf{D}$ that the image has with each 
of the 5 categories. It might look something like this

$\mathbf{D}(\mathrm{image}) = [0.10 0.05, 0.20 0.30 0.35]$

The model associates the image data most strongly with the fifth class ($D_5 > D_{1,2,3,4}$), and 
therefore the model will classify the image into that category.

Let's run some hypothetical experiments on this model. Imagine that you run many images from class 5
through the model to find its accuracy $\mathcal{A}_5$ on this category

$$\mathcal{A}_5 = P(D_5 > D_{1,2,3,4} | 5-\mathrm{image}).$$

We could also run this same model through a series of parallel experiments, where only two categories
are available at a time. If only classes 1 and 5 are available as options, then the accuracy in this scenario is

$\mathcal{A}_{5,1} = P(D_5 > D_1 | 5-\mathrm{image}),$

and this goes on up to 

$\mathcal{A}_{5,4} = P(D_5 > D_4 | 5-\mathrm{image}).$

We can imagine that when a full 5-category classification is done, it proceeds through
a gauntlet of pairwise choices. First the classes 1 and 5 are compared, and if 5 is chosen 
by the model (with probability $P(5>1|5)$),
then the classes 2 and 5 are compared. If class 5 is better pairwise than each of the other classes, 
then class 5 is chosen as the best overall ($P(5>1,2,3,4|5)$). 

Since survival probability is multiplicative, the probability of class 5 making it through 
the entire gauntlet is equal to the product of probabilities for each of the steps in the gauntlet

$ P(5>1,2,3,4 | 5) = P(5 > 1 | 5) P(5 > 2 | 5) P(5 > 3 | 5) P(5 > 4 | 5)$

If we take the geometric mean of the 4 pairwise probabilities, 

$p_{gm,5} = ^4\sqrt{P(5 > 1 | 5) P(5 > 2 | 5) P(5 > 3 | 5) P(5 > 4 | 5)}$

then we see that the accuracy on 5-class images is

$\mathcal{A}_5 = p_{gm,5}^4$

I.e. the accuracy on some particular class is equal to the geometric mean of pairwise accuracies,
dto the power of the number of classes less one.

The overall accuracy of the model will be

$\mathcal{A} = \mathcal{A}_1 P(1-class) + \ldots + \mathcal{A}_5 P(5-class)$

where the $P(i-class)$ simply accounts for the proportion of $i$-class images in the test set. For 
a perfectly balanced dataset, this reduces to the mean

$\mathcal{A} = \frac{1}{5}\left[ p_{gm,1}^4 + \ldots + p_{gm,5}^4 \right]$

Remember: we're trying to find a single number that can be used to compare models with
any number of target classes. So when we report this single number, we shouldn't
need to also report the number of classes that the models were tested on.
Let's define the average that appears on the right as

$\frac{1}{5}\left[ p_{gm,1}^4 + \ldots + p_{gm,5}^4 \right] \equiv \alpha_{bea}^4$

where the exponent on the right has been chosen to have the same "units" of probability as
on the left. This value -- $\tilde{\mathcal{A}}_{BE}$ -- is what I call the 
naive binary-equivalent accuracy.
It has the literal interpretation as the (N-1)th root of the average of (N-1)th powers of
geometric means of pairwise accuracies. What a mouthful! 
Under the *assumption* that the geometric means of 
accuracies are equal across all classes (p_{gm,1} = ... = p_{gm,5}), 
then $\tilde{\mathcal{A}}_{BE}$ is the
same as these geometric means ($\tilde{\mathcal{A}}_{BE} = {p_{gm,i}}$). A tighter interpretation might 
also be found by examining correlations between the geometric means for each class 

So we have a number

$\tilde{\mathcal{A}}_{BE} = \mathcal{A}^{1/(N-1)},$

but as we shall see in the next section, the asymptotic behaviour of $\tilde{\mathcal{A}}_{BE}$ 
as the number of classes increases is not entirely satisfactory. 



## Benchmarking Naive BEAs with Random Guesses

To get a better understanding of what the binary-equivalent accuracy is saying,
let's use a simple toy model to see how the BEA behaves as the number of categories increases.
If we have $N$ categories and all our model does is randomly guess the correct category 
(say with an N-sided die) then its accuracy will be $\mathcal{A}=1/N$, giving a corresponding
naive binary-equivalent accuracy of 

$\tilde{\mathcal{A}}_{BE} = \left(\frac{1}{N}\right)^{1/(N-1)}$

<img src="https://mattingliswhalen.github.io/images/BinaryEquivalentAccuracy/bea_random_model.jpg">

The naive binary-equivalent accuracy (nBEA) rises as the number of classes increases. Uhoh! 
While **accuracy** as a
measure unfairly disadvantages models with a higher number of class labels, 
the **naive BEA** unfairly disadvantages models with *fewer* categories. 
In short -- the naive binary-equivalent accuracy of randomly guessing isn't 50%.

There's a relatively easy fix* : we find how
close the nBEA of our model is to perfect accuracy, relative to randomness, 
then propagate that same closeness back to the BEA of randomness with only 2 classes. Using 
an interpolation/LERP parameter $t$ to measure the closeness (0 is at perfect randomness,
1 is at perfect accuracy$^‡$)

$t = \frac{ nBEA_{\mathrm{model}}(N) - nBEA_{\mathrm{randomness}}(N) }{1-nBEA_{\mathrm{randomness}(N)}$ 

Keeping the same value of closeness $t$ but placing it relative to randomness on two classes,
we finally get to our true binary-equivalent accuracy $\mathcal{A}$

$\mathcal{A}_{BE} =  nBEA_(2) + [1-nBEA_{\mathrm{randomness}}(2)] t$

Expanded out in full form, the monstrosity reads

$\mathcal{A}_{BE} =  \frac{1}{2} + \frac{1}{2} \frac{\mathcal{A}^{1/(N-1)}-\left(\frac{1}{N}\right)^{1/(N-1)}}{1-\left(\frac{1}{N}\right)^{1/(N-1)}} t$


## Hearing Experiments -- A Playground for Testing

Imagine you've been asked to participate in an experiment. The researchers sit you down 
in a quiet room and ask you to indicate whether a sound originated from your left or 
right side. The sound comes from a random point in the circuar wall that surrounds you. For sounds 
from your far left or right the task is easy, and you can always identify where the sound is 
coming from. Your accuracy will be something like 99.5%, with the incorrect trials coming from 
times where you mixed up the response switches, or the sound bounced funnily in the room, or you 
were distracted thinking about some funny joke. Alternatively, when the sound is from directly 
in front of you, but shifted ever so slightly to the left or right, you're basically just guessing 
where the sound came from. Your accuracy will drop to ~50%. Integrated over all possible sound 
locations (the 360° around you), your net accuracy might sit around 98%.

Now what happens when they add more options? Left, right, front, back? Or more? Your accuracy will
drop, and eventually drop to zero as the number of options increases to infinity,
but lets see how the binary-equivalent accuracy behaves in this setting.

I've coded up a simple simulation that 
[can be downloaded here](http://mattingliswhalen.github.io/data/2024_06/hearing_test.py).
If a beep comes from an angle $\theta$, we pretend that the
angle at which you perceive the sound will follow a normal distribution centered on $\theta$
and with some spread $\sigma$. For humans the width of the distribution is about $\sigma ~ 10°$.
You point at the perceived source of the beep, and our net accuracy is determined by how often 
you point in the correct quadrant, hextant, octant, etc. For N categories, the accuracy follows 
the following curve

<img src="https://mattingliswhalen.github.io/images/BinaryEquivalentAccuracy/accuracy_vs_ncat_hearing_experiment.jpg">

But the binary equivalent accuracy follows this curve

<img src="https://mattingliswhalen.github.io/images/BinaryEquivalentAccuracy/accuracy_vs_ncat_hearing_experiment.jpg">

The $\mathcal{A}_{BE}$, like the  falls at first, then rises slowly. Ideally the profile should be constant, 
since now one might conclude -- based only on the binary-equivalent accuracy --
that a human who can distinguish between
100 different categories of angle is better than a human who can only distinguish between 2 different 
categories of angle -- even though they're the same human!

It might be interesting to examine the large-$N$ behaviour and see if the some correction could 
be applied to force some sort of convergence to a fixed value. If you use [MIW's AutoFit] to
fit the data for $N>40$, you find that the top model is a power-law

$/

## MIW AutoFit's Binary Equivalent Accuracy

I've done some benchmarking on MIW's AutoFit.

As I increase the complexity of possible functional
models that could possibly fit a given dataset (i.e. as I increase the depth parameter $N$),
the number of models increases roughly as 2^N. With ...
For each functional model and have found that 

Depth 1: 6 classes, 83.3 -> 96.4%
Depth 2: 18 classes, 77.8% -> 98.53% 
Depth 3: 115 classes, 45% -> xx%
Depth 4: 865 classes, xx% -> xx%


$^†$: Despite being the result of a softmax function, and despite being commonly called so,
I am hesitant to call this a probability. 

*: If all we're looking for is a number that "feels" right. There are probably many ways to do this
with separate benefits and drawbacks.
$^‡$: Obviously the same process can be applied to models that perform *worse* than random, but I'll
leave it to you, the reader, to work out how to make a closeness parameter $t'$ for how close the
nBEA is to 0% accuracy.  

Tags: #classification #algorithm #statistics #binomial #CDF #binary #equivalent #accuracy