---
title: Preventing Poverty
has_children: false
nav_order: 4
---

# How to prevent GCE from making you poor

Google Compute Engine is _less_ likely to make you poor compared to the more "autoscaling on-demand" services such as Cloud Functions and App Engine. [Why?](#gae-and-cloud-functions)
Since the auto scaling capability is quite less compared to Compute Engine, it is harder to get a surprisingly larger bill than expected, conversely you will never see a bill smaller than expected.

A few things you can do to help reduce costs:

1. Don't use expensive servers unless you really need it. Stick to the (generous) [free tier](https://cloud.google.com/free).
2. Create budgets.
3. [Use pub/sub to automatically shut down servers.](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications).

#### GAE and Cloud Functions

With an improper GAE configuration, it is possible to over-scale the number of instances and hence end up with an unnecessary and underutilised instances that you will be paying for.
For Cloud Functions, the main issues are when you have unnecessary calls to the function, and the bigger one is when you create a loop of cloud functions that never stop calling each other. When you have a loop, GCF will constantly and almost linearly increase the number of running instances per function which can cost thousands of dollars per day.
