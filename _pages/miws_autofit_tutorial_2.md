---
title: "MIW's AutoFit -- Tutorial 2 -- Special Functions"
date: 2023-11-14
permalink: /MIWs_AutoFit_Tutorial_2/
author_profile: true
---

Tutorial Sections: 
[1](https://mattingliswhalen.github.io/MIWs_AutoFit_Tutorial_1/) 
[2](https://mattingliswhalen.github.io/MIWs_AutoFit_Tutorial_2/)
[3](https://mattingliswhalen.github.io/MIWs_AutoFit_Tutorial_3/)
[4](https://mattingliswhalen.github.io/MIWs_AutoFit_Tutorial_4/)
[5](https://mattingliswhalen.github.io/MIWs_AutoFit_Tutorial_5/)

---

_Thanks for joining the second tutorial! Today we learn about polynomials,
sigmoid functions, histograms, and Gaussians._

---

Let’s make sure AutoFit has a fresh start so we’re all on the same page. After closing the window, open AutoFit again 
and load up 
<a href="http://mattingliswhalen.github.io/data/MIWsAutoFitTutorial/logistic.csv">
logistic.csv⭳
</a>. When we fit the data, it looks decent enough, but if you care to look at the residuals, 
at least one of the measures on the console will tell you that the fit isn’t quite right, meaning the data might 
have features which are not reflected in the linear model we have chosen.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/logistic_linear.jpg">

Now let’s try to find a better model from the quick options. Hover over the dropdown menu currently called Linear. 
It will show a list of options, and for now let’s choose Polynomial.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/logistic_poly.jpg">

The default polynomial will be of order two (i.e. a quadratic equation). The arrows which have appeared below the 
dropdown handle will allow you to choose the degree. You can go as low as 0, and up to one less than the number 
of data points you have.

You can play around with it to find the fit that suits you best. Personally I like the 3rd degree fit. After a 
certain point (for me degree 15) the uncertainties become NaN (not a number) meaning the algorithm isn’t stable, 
and which I interpret as the fit losing statistical meaning.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/logistic_3rd.png">

Now let’s try another dropdown, this time picking Sigmoid. The sigmoid function here is defined as

$$\mathrm{sig}(x) = F + \frac{H}{ 1+e^{-\frac{x-x_0}{w}} }$$

which you should also be able to see in the console area.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/logistic_sigmoid.jpg">

Next let’s do something a bit different. Load in random sample from 
<a href="http://mattingliswhalen.github.io/data/MIWsAutoFitTutorial/normal_distribution.csv">
normal_distribution.csv⭳
</a>. This is just a list of numbers, but AutoFit will find an appropriate bin size 
to make a nice histogram of the data.

The fit line will look terrible since we’re still on Sigmoid. If you’re used to Gaussian functions or 
Normal distributions, try estimating by eye the mean and the standard deviation of the sample 
before moving on to the next step.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/normal_sigmoid.jpg">

Now change the fit-type dropdown list to Gaussian. You should get a beautiful fit, showing a mean 
of 5 and a standard deviation of 2, give or take.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/normal_gaussian.jpg">

Since this is a histogram, you might want to normalize the histogram to show 
probabilities instead. On the right side of the image, you can press Normalize to set the integral over all bins to 1.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/normal_normal.jpg">

Since AutoFit knows the histogram has been normalized, you might also notice that the console displays 
a different function with different fit estimates, corresponding to the Normal distribution rather than a Gaussian.

---

In the [next tutorial](https://mattingliswhalen.github.io/MIWs_AutoFit_Tutorial_3/), we take a look at finding the best model
when we don’t know in the first place which model should fit!
