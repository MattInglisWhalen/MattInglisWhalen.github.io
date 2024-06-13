---
title: 'Clustering points in 2D -- From the LHC to Art Exhibits'
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

## Parable of the Tigerlike Cat

Imagine you've built some classification algorithm that can handle sorting input data into
something like 5000 categories. Think of some classical Machine Learning algorithm like 
a Random Forest, or maybe some large neural net architecture, each with a sufficiently 
large dataset for training. If this chosen algorithm is forced to only 
distinguish between 2 categories, the accuracy of this binary classification task is going to be 
much higher than if the same algorithm is asked to determine the correct category amongst 1000
possible classes. 

To see this, let's imagine that we're working with an image classification task on
animals, with 5000 categories [Dog, Cat, Horse, ..., Tiger, ...]. If we input some image of a cat,
the probabilities the algorithm outputs might be something like [1e-5, 0.1, 1e-6, ..., 0.3, ...].
Apparently the `Tiger` category is more probable than the `Cat`. Maybe because the cat
in the image has been 
painted with stripes, or is baring its teeth, or is set within the backdrop of a jungle. Who knows.
On a binary classification task between `Dog` and `Cat`, the algorithm still gets a **success**, 
boosting its accuracy from this one trial. But if we were doing the classification on 1000 classes, 
with `Tiger` included, the algorithm has gotten this one incorrect. Repeated across many test
images, these same edge effects cause the algorithm to perform worse when more categories
are provided as options.

But it's not that the algorithm is performing *worse*. It's the same model, after all. Rather,
it's the *measure* we're using to rate the algorithm that appears to show a drop in performance.
Let's try to invent a measure that doesn't drop as more categories are introduced.

## Getting a Handle with Hearing Tests

Imagine you've been asked to participate in an experiment. The researchers sit you down in a quiet
room and ask you to indicate whether a sound originated from your 
left or your right side. The sound comes from a random point in the half-circle in front of you.
For sounds from your far left or right the task is easy, and you can always identify where 
the sound is coming from. Your accuracy will be something like 99.5%, with the incorrect trials
coming from times where you mixed up the response switches, or the sound bounced funnily in the room,
or you were distracted thinking about some funny joke. Alternatively, when 
the sound is from directly in front of you, but shifted ever so slightly to the left or right, 
you're basically just guessing where the sound came from. Your accuracy will drop to ~50%. 

The statistic that these researchers are likely to use to determine whether or not you can distinguish
left and right sounds is called the **p-value**, often denoted $\alpha$. This quantity represents
the probability that you performed as well as you did (or better) under the assumption that you were simply
guessing. This probability is calculated using the 
[Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution). This probability
distribution is written as 

$P(n;N,p) = [N \mathrm{choose} n] p^n q^{N-n}$

which is interpreted as the probability that with $N$ trials, 
you have been correct $n$ times. The parameter $p$ is the assumed probability that you are correct
on any given trial, and $q$ is the probability that you were incorrect.

## Derivation

## Quick Tool






Tags: #classification #algorithm #statistics #binomial #CDF 