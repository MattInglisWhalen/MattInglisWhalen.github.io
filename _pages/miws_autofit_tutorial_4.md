---
title: 'MIWs AutoFit -- Tutorial 4 -- Procedural Fits'
date: 2023-11-16
permalink: /MIWs_AutoFit_Tutorial_4/
author_profile: true
tags:
  - tutorial
  - mathematics
  - statistics
  - curve fitting
  - MIW's AutoFit
---

_So you’ve made it through the Brute-Forcing tutorial! If you were frustrated with how long the program takes 
to find a good model, have understood how AutoFit contructs models from base functions, and you would like more 
control, then this tutorial is for you! Here, we'll discover how to turn off and on certain base functions, 
and how to create your own base functions._

---

In the last tutorial it took ~40 seconds and 900 model fits to find a good model for the data. Let's do it again, but 
with the knowledge that the model only contains exponential and logarithmic functions.

This time, after loading in 
<a href="http://mattingliswhalen.github.io/data/MIWsAutoFitTutorial/sudakov.csv">
sudakov.csv⭳
</a>, select the Procedural dropdown option. 
You will be presented with some checkboxes. Ensure `exp` and `log` are selected, and change the depth to 4 
(this is the max number of base functions which will be allowed in the generated model list).

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/sudakov_options.png">

When you click Fit Data, a list of possible models will be created according to the given parameters. 
This list is then trimmed of invalid models according to various rules (like no exp(exp) or log(log)), then 
each model in the trimmed list is fit to the data. In ~7 seconds, we find the same model as in Tutorial 3.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/sudakov_procedural.png">

Let’s do one more example. Opening 
<a href="http://mattingliswhalen.github.io/data/MIWsAutoFitTutorial/sin_cosine.csv">
sin_cosine.csv⭳
</a>, we see a wavelike structure. Assuming now that there are no logarithmic, exponential, or 1/x base functions, 
we turn on only `sin` and `cos` base functions.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/sin_cos_data.png">

Pressing the Fit Data button, in ~4 seconds we find the correct model that was used to generate the data: 
a sum of sins and cosines, with different frequencies.

<img src="https://mattingliswhalen.github.io/images/MIWsAutoFitTutorial/sin_cos_fit.png">

---

In the [final tutorial](https://mattingliswhalen.github.io/MIWs_AutoFit_Tutorial_5/), we will talk about manual functions, for those cases where MIW’s AutoFit has failed 
to find the correct model and you know which model it should have found.