.. _quickstart:

Quick Start
***********************


Containment in Leader-Follower Networks for single-integrator systems
==================================================================================

In this page, we show how to run a basic distributed cooperative robotics scenario in **ChoiRbot**.
Specifically, we consider a containment problem in leader-follower networks as described in [MeEg11]_.


Prerequisites
----------------------------

We assume a working installation of **ChoiRbot** and RVIZ is available
(see the :ref:`installation page <installation>`).
Moreover, we assume the reader to be familiar with the basic concepts
of ROS 2 launch files and Python.


Maths of the problem
----------------------------

We consider a team of :math:`N` robots moving 
in the :math:`(x,y)` plane.
Each robot is modelled as single-integrator dynamical system

.. math::

   \dot{x}_i(t) = u_i(t),

where for all :math:`i \in \{1, \ldots, N\}`, :math:`x_i \in \mathbb{R}^2` is the
:math:`i`-th system state (i.e., position) and :math:`u_i \in \mathbb{R}^2`
is the :math:`i`-th system input (i.e., velocity).
We assume the robots communicate according to a given
undirected graph :math:`\mathcal{G} = (\mathcal{V}, \mathcal{E})`, where
:math:`\mathcal{V} = \{1, \ldots, N\}` is the set of robots and
:math:`\mathcal{E} \subset \mathcal{V} \times \mathcal{V}` is the set of
edges. If :math:`(i,j) \in \mathcal{E}`, then also :math:`(j,i) \in \mathcal{E}`
and robots :math:`i` and :math:`j` can send information to each other.
The set of neighbors of each agent :math:`i` is denoted by
:math:`\mathcal{N}_i = \{j \in \mathcal{V} \mid (i,j) \in \mathcal{E}\}`.

Robots are partitioned in two groups, namely leaders and followers. 
The goal for the followers is to converge to the convex hull of the leaders’ positions. 
To this end, the robots implement the dynamics

.. math::

  \begin{split}
  \dot{x}_i(t) &= 0 \hspace{4cm} & \text{(leaders)},
  \\
  \dot{x}_i(t) &= \sum_{j \in \mathcal{N}_i} (x_j(t) - x_t(t)) & \text{(followers)}.
  \end{split}


Simulation Launch File
--------------------------------
The launch file to run the simulation is 

.. literalinclude:: ../../../choirbot_examples/launch/containment.launch.py
  :language: Python
  :linenos:



.. rubric:: References

.. [MeEg11] Notarstefano, G., Egerstedt, M., Haque, M. (2011). Containment in leader--follower networks with switching communication topologies. Automatica, 47(5), 1035-1040.
