# Examples of using CWL to build ML training workflow
The repository contains examples of using CWL to build ML workflows

# Example 1
Dataset: a subset of Iris dataset
Model: random forest
Data preprocessing: the workflow constains an independent step of preprocessing data. In the example, target values are replaced with numerical targets. 

# Example 2
Dataset: a subset of Iris dataset
Model: multilayer perceptron (MLP); random forest. In this example, two ML models are trained in parallel given the same input.
Data preprocessing: the workflow constains an independent step of preprocessing data. In the example, target values are replaced with numerical targets. 