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

## 2023
{% for post in site.publications reversed %}
 {% if post.path contains '2023' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

## 2022
{% for post in site.publications reversed %}
 {% if post.path contains '2022' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

## 2021
{% for post in site.publications reversed %}
 {% if post.path contains '2021' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

## 2020
{% for post in site.publications reversed %}
 {% if post.path contains '2020' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

## 2019
{% for post in site.publications reversed %}
 {% if post.path contains '2019' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

## 2018
{% for post in site.publications reversed %}
 {% if post.path contains '2018' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

## 2017
{% for post in site.publications reversed %}
 {% if post.path contains '2017' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

## 2015
{% for post in site.publications reversed %}
 {% if post.path contains '2015' %}
  {% include archive-single-pub.html %}
 {% endif %}
{% endfor %}

