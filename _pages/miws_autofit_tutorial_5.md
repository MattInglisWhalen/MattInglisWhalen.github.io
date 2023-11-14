---
title: 'MIWs AutoFit -- Tutorial 5 -- Manual Models'
date: 2023-11-17
permalink: /MIWs_AutoFit_Tutorial_5/
author_profile: true
tags:
  - tutorial
  - mathematics
  - statistics
  - curve fitting
  - MIW's AutoFit
---

Now that you’ve made it through the procedural models tutorial, we can discuss constructing our own models.

---

Okay, great, AutoFit is pretty good with the basic functional building blocks used in most models. But what happens when
these building blocks aren't enough? AutoFit allows you to define functions based on arbitrary Python code, assuming
that 

1. the code uses no spaces
2. the code you wish to use is base Python, or from the numpy or scipy packages

A fairly common function that isn't considered simple is 0th-order Bessel Function of the first kind, $$J_0(x)$$. 
Loading up a dataset generated with this function, 

<a href="http://mattingliswhalen.github.io/data/MIWsAutoFitTutorial/bessel_data.csv">
bessel_data.csv⭳
</a>, we can first try to fit this function using a combination of exponentials and trigonometric base functions.
A reduced chi-squared of 11.83 isn't too good, and the residuals are decidedly in favour of this model 
`sin(pow1)+exp(pow1)` not being the correct function for this dataset.

While in Procedural mode, let's head down to the custom function button in the bottom left of the window. 
After clicking, we see a pop-up allowing us to create a new base function, which will be included in all subsequent
compositions/products/sums when building a list of functional models to test.



Let’s examine the dataset 
<a href="http://mattingliswhalen.github.io/data/MIWsAutoFitTutorial/sudakov.csv">
sinexp.csv⭳
</a> generated with the function

$$f(x) = 13\sin(-0.5\exp(0.1x))$$

AutoFit can’t find the correct fit for this dataset. Let’s try to help it out by going to the Manual dropdown option.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/sinexp.png">

Putting the model into the input field, validating that the input corresponds to a valid function, and 
clicking Find Fit, we see that AutoFit has found a local minimum for the chi-squared of this model. 
The global minimum can’t be reached from here using its search strategy, but we can help it out by 
adjusting its original search parameters.


---

That wraps it up for the tutorials! You’re a pro now, so I wish you luck with all your endeavours!