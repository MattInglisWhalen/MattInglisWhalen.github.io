---
title: "Denoising Deep Generative Models"
collection: publications
permalink: /publication/2022-12-denoising-deep-generative-models
excerpt: 
date: 2022-11-30
authors: 'Gabriel Loaiza-Ganem, Brendan Leigh Ross, Luhuan Wu, John P. Cunningham, <b>Jesse C. Cresswell</b>, and Anthony L. Caterini'
note:
venueshort: 'NeurIPS 2022 Workshop ICBINB'
venue: 'NeurIPS 2022 Workshop on Understanding Deep Learning Through Empirical Falsification'
paperurl: 'https://arxiv.org/abs/2212.01265'
pdf: 'https://arxiv.org/pdf/2212.01265.pdf'
codeurl: 'https://github.com/layer6ai-labs/denoising_dgms'
videourl:
slidesurl:
citation: 'Gabriel Loaiza-Ganem, Brendan Leigh Ross, Luhuan Wu, John P. Cunningham, Jesse C. Cresswell, and Anthony L. Caterini. Denoising Deep Generative Models. NeurIPS 2022 Workshop on Understanding Deep Learning Through Empirical Falsification.'
---
Likelihood-based deep generative models exhibit pathological behaviour as a consequence of using high-dimensional densities to model data with low-dimensional structure. In this paper we propose two methodologies to remove the dimensionality mismatch during training. Our first approach is based on Tweedie's formula, and the second on models which take the variance of added noise as a conditional input. We show that surprisingly, while well motivated, these approaches only sporadically improve performance over not adding noise, and that other methods of addressing the dimensionality mismatch are more empirically adequate.