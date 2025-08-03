goto next-node
==============

goto next-node

Function
--------



The **goto next-node** command further matches routes against a specified node after the routes match the current node.

The **undo goto next-node** command restores the default configuration.



By default, if a route matches the current node, it matches the route-policy and is no longer matched against other nodes.


Format
------

**goto next-node** [ *node* ]

**undo goto next-node**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *node* | Specifies the index of a node against which routes are further matched. | The value is an integer ranging from 1 to 65535 and must be greater than the index of the current node. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The relationship between the matching rules of nodes in the same route-policy is OR. Specifically, if a route matches a node, it matches the route-policy and is no longer matched against other nodes. If you need to match the route against two or more nodes, run the **goto next-node** command so that the route is further matched against a specified node after the route matches the current node.If node is not specified in the command, the route will be further matched against the next node of the current node by default.If the node specified in the command does not exist, the route will be further matched against the next node of the specified node by default. If the next node of the specified node does not exist either, the route fails to match the route-policy, and no apply clause will be applied to the route.



**Implementation Procedure**



If the **goto next-node** command is run in the route-policy view and a route matches all the specified nodes, the apply clauses of these nodes will be applied to the route.If the route fails to match one node, the route is matched against the next node until it succeeds in matching a node, and then the apply clauses of the nodes that the route matches will be applied to the route. If the route fails to match all nodes, no apply clauses will be applied to the route.




Example
-------

# Configure a route-policy named aaa and further match routes against node 20 after the routes match node 10.
```
[~HUAWEI] route-policy aaa permit node 10
Info: New Sequence of this List                                                                                                     
[*HUAWEI-route-policy] if-match tag 123
[*HUAWEI-route-policy] apply cost 10
[*HUAWEI-route-policy] goto next-node 20
[*HUAWEI-route-policy] quit
[*HUAWEI] route-policy aaa permit node 20
Info: New Sequence of this List      
[*HUAWEI-route-policy] if-match interface NULL 0
[*HUAWEI-route-policy] apply local-preference 30

```