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

Let’s examine the dataset sinexp.csv generated with the function

$$\mathrm{f(x) = 13\sin(-0.5\exp(0.1x))}$$

AutoFit can’t find the correct fit for this dataset. Let’s try to help it out by going to the Manual dropdown option.

Putting the model into the input field, validating that the input corresponds to a valid function, and hitting Find Fit, we see that MIW’s AutoFit has found a local minimum for the chi-squared of this model. The global minimum can’t be reached from here using its search strategy, but we can help it out by adjusting its original search parameters.

That wraps it up for the tutorials! You’re a pro now, so good luck with all your endeavours!