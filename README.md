# OpenSlideGenerator
This is one of the repository in the breast cancer research project at Ashoka University. This repository contains the code to the implementation of the OpenSlide API to generate patches for our Whole Slide Images. We then use a [model](https://github.com/mraoaakash/Differentiator) to separate out whiteSpace patches from cellSpace patches. 

This framework is to serve as an input to various models that are trained for semantic segmentation. They are:
- [Deep Spectral Segmentation](https://github.com/mraoaakash/deep-spectral-segmentation) based of the paper by [Luke et. al.](https://arxiv.org/abs/2205.07839)

