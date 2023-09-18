---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Projects
======
* Future: Transformers in NLP / computer vision / 
* 2023 : Daily London Weather -- Comparing models when seasonal periods are long
* 2022-2023 : MIW's AutoFit -- A desktop app to automatically find the best function to fit a given dataset

Education
======
* Ph.D. in Particle Physics, University of Toronto, 2022
* M.Sc. in Physics, with Distinction, University of Edinburgh, 2014
* B.Sc. in Physics, Highest Honours, with Minor in Mathematics, Carleton University, 2013
  
Skills
======
* Languages: Python, SQL, C++
* Deep Learning Libraries: Pytorch, Keras
* Data Science Libraries: Scikit-learn, Pandas, Numpy, Scipy

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

