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
* Programming: Python, SQL, R, Mathematica, C++, C#, C, Bash
* Data Science: scikit-learn, PyTorch, Pandas, Seaborn, Tableau
* Dev Tools: Flask, Docker, AWS Cloud Servers, Linux, GitHub, Unity, Excel
* Mathematics: Numerical Optimization, Multivariable Calculus, Statistics, Linear Algebra
* Physics: Classical Mechanics, Quantum Field Theory, Nuclear Models, Relativity

Projects
======

### Freelance Consulting (Kolabtree) 
| Matlab | Python |

* Worked on fitting hydrological models to a measured time-series of borehole head heights
* Translated academic MATLAB code to Python, with refactoring for object-oriented styling
* Employed industry-standard best-practices for automated testing/linting/styling with GitHub

### Thread the Void VR
| Unity | C# | Steamworks |
* Built a video game using the Unity Engine for headsets compatible with SteamVR (Vive/Oculus)
* Created a framework for procedurally generating music without using audio samples
* Published the game on Steam, with beta versions currently being tested on Android

### Identifying Clusters in 2D Data
| R | GitHub |
* Developed a novel algorithm for efficiently detecting clusters in a 2D point-spread dataset in R
* Packaged and published the algorithm for use with R’s devtools/remotes install_github functionality

### Cloud Deployment of Inference Model 
| Python | Flask | Docker | Scikit-learn | AWS |
* Used Natural Language Processing techniques to predict the sentiment of a film review
* Deployed a containerized model to a scalable AWS-EC2 endpoint that was over 90% accurate
while saving 50% of server costs compared to the standard solution.
* Generated HTML programmatically to visualize word importance in the classification

### Predictive Modelling for Truancy
| Jupyter | Scikit-learn | Seaborn | Pandas |
* Data cleaning, exploratory data analysis, and predictive modelling in a Jupyter notebook
* Visualized features and their relationship with truancy rates
* Used a cross-validation grid search to tune the hyperparameters of many models

### MIW’S AutoFit
| Python | Tkinter | Multiplatform | SQL | PHP |
* Developed a GUI using Python (NumPy, SciPy, Pandas) to rank and fit models to 1D data
* Configured GitHub Actions for automated testing and code-coverage reports
* Packaged the program for distribution to Windows, MacOSX, and Linux environments
* Built a WordPress website with PHP and SQL backend support to sell software products

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

