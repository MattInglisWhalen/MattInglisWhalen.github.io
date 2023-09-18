---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
 {% if post.path contains '2025' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2024' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2023' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2022' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2021' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2020' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2019' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2018' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2017' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2016' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
 {% if post.path contains '2015' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

