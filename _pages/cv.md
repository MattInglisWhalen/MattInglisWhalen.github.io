---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}


Education
======
* Ph.D. in Particle Physics, University of Toronto, 2022
* M.Sc. in Physics, with Distinction, University of Edinburgh, 2014
* B.Sc. in Physics, Highest Honours, with Minor in Mathematics, Carleton University, 2013
  
Skills
======
* Languages: Python, SQL, C++
* Deep Learning Libraries: Pytorch, Keras
* Data Science Libraries: Scikit-learn, Pandas, Numpy, Seaborn, Tableau

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

