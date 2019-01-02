# HOPF

Higher Order Propagation Framework for Deep Collective Classification
A modular framework for node classification in graphs with node attributes. 

Paper Links: HOPF: https://arxiv.org/abs/1805.12421
             F-GCN: https://arxiv.org/abs/1805.12528


Table of contents:
Installation:
Usage:
Credits:
License:


Running tests:


The Frameworks provides different kernels for performing Semi-supervised Node classification.

Few Available Kernels: </br>
1> Graph Convolutional Networks (GCN)  </br>
2> Node Information Preserving Kernel </br>
3> Fusion GCN </br>

Available bases:</br>
1> Binomial </br>
    - Supports Node only and Neighbor only baselines </br>
    - Skip connection supported for Graph Convolutions </br>
    - Supported kernels: simple | kipf </br> 
    - Fusion model available: binomial_fusion </br>
2> Chebyshev </br>
    - Skip connection internally turned Off (as it will change basis) </br>
    - Supported kernels: chebyshev (Default internally) </br>
3> Krylov </br>
    - Skip connection internally turned Off (as it will change basis) </br>
    - Supported kernels: simple | kipf (Kipf to be preferred)</br>

view parser.py to </br>
1> Specify the kernel </br>
2> Specify the number of hops </br>
3> Specify the node and neighbor features </br>
4> Specify Folds and Percentages to run </br>
5> Add Skip Connections </br>
6> Specify Gated GCN Models </br>
7> Specify Datset, batch size, learning rate, dropout, dimensions </br>
8> Specify weighted cross entropy loss </br>
9> Partial Neighborhood </br>
.. etc </br>
</br>
View script_cora.sh and run_cora.py to know how to run multiple kernels in parallel  