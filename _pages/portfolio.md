---
layout: archive
title: "Portfolio"
permalink: /portfolio/
author_profile: true
---

{% include base_path %}


{% for post in site.portfolio %}
  {% include archive-single.html %}
{% endfor %}

# Demos

Try these models yourself!

## Natural Language Processing

### Movie Review Sentiment

A small project for me to learn how to deploy models to a server. Here a simple bag-of-words model to predict the sentiment of a provided movie review. [Try it out yourself](mattingliswhalen.github.io/demos/movie_review_sentiment.html) or read more about the model at the [GitHub repository](https://github.com/MattInglisWhalen/MovieReviewSentiments)!

## Time-Series Analysis

## Audio Processing

## Image Processing

# Projects without Demos

For various reasons these projects are not available through the web. 

## Curve-Fitting

### MIW's AutoFit

This project was originally meant to be marketed online to researchers and professionals that needed a quick way to determine the best functional model to fit their 1D data. This multiplatform GUI is compatible with Windows, MacOSX, and Ubuntu.

