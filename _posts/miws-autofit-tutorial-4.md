---
title: 'MIWs AutoFit -- Tutorial 1'
date: 2023-11-13
permalink: /posts/miws-autofit-tutorial-1/
tags:
  - tutorial
  - mathematics
  - statistic
  - curve fitting
  - MIW's AutoFit
---

_So you’ve made it through the Brute-Forcing tutorial! If you were frustrated with how long the program takes to find a good model, have understood how AutoFit contructs models from base functions, and you would like more control, then this tutorial is for you! In this final tutorial we show how to turn off and on certain base functions, and how to create your own base function.
_

---

In the last tutorial it took ~40 seconds and 900 model fits to find a good model for the data. In do it again, but with the knowledge that the model only contains exponential and logarithmic functions.

This time, after loading in sudakov.csv, select the Procedural dropdown option. You will be presented with some checkboxes. Ensure exp and log are selected, and change the depth to 4 (this is the max number of base functions which will be allowed in the generated model list).

When you click Fit Data, a list of possible models will be created according to the given parameters. This list is trimmed of invalid models according to various rules (like no exp(exp) or log(log)), then each model in the trimmed list is fit to the data. In ~7 seconds, we find the same model as in Tutorial 3.

Let’s do one more example. Opening sin_cosine.csv, we see a wavelike structure. Assuming now that there are no logarithmic, exponential, or 1/x base functions, we turn on only sin and cosine base functions.

Pressing the Fit Data button, in ~4 seconds we find the correct model that was used to generate the data: a sum of sins and cosines, with different frequencies.

In the final tutorial, we will talk about manual functions, for those cases where MIW’s AutoFit has failed to find the correct model and you know which model it should have found.