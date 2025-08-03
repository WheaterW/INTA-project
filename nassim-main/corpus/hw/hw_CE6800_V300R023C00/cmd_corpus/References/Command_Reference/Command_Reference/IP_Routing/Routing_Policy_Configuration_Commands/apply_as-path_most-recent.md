apply as-path most-recent
=========================

apply as-path most-recent

Function
--------



The **apply as-path most-recent** command sets the number of times that the most recent AS number is added to routes.

The **undo apply as-path most-recent** command cancels the configuration of the number of times that the most recent AS number is added to routes.



By default, the number of times the most recent AS number is appended is not set.


Format
------

**apply as-path most-recent** *most-recent-value*

**undo apply as-path most-recent** [ *most-recent-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *most-recent-value* | Specifies the number of times the most recent AS number is appended to the beginning of the AS path. | The value is an integer ranging from 0 to 32. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The AS\_Path attribute is a private attribute of BGP. The **apply as-path most-recent** command is valid only for BGP routes. The AS\_Path attribute records the numbers of all ASs that a route passes through from the local end to the destination in the vector order. The AS\_Path attribute can be used to control route selection and prevent routing loops. If multiple routes to the same destination are available, BGP compares the AS\_Path attributes of these routes and considers the route with the shortest AS\_Path as the optimal route.By using a routing policy to change the AS\_Path attribute, you can control BGP route selection and the forwarding path of data traffic. If filtering conditions are specified using an if-match clause and the matching mode is permit, you can run the **apply as-path most-recent** command to append the most recent AS number in the existing AS path of each matched route to the beginning of the AS path for the specified number of times.You can run the **route-policy** command to enter the route-policy view.A route-policy can consist of multiple nodes. The relationship between different nodes is OR. The system checks each node according to the node sequence number. If a route matches one node, the route matches the route-policy and is no longer matched against other nodes.Each node can consist of a group of if-match and apply clauses. The if-match clauses define the matching rules. The matching objects are some attributes of the routing information. The relationship between multiple if-match clauses for different attributes of a node is AND. A route passes the matching test only when all the matching conditions specified by the if-match clauses of the node are met. The relationship between multiple if-match clauses for the same attribute is OR. Thai is, the system checks the if-match clauses in sequence. If a route matches one of the if-match clauses, the route matches the route-policy and is no longer matched against other if-match clauses. For example, in node 10, the if-match community-filter 1 and if-match as-path-filter 1 commands are used to filter routes based on different attributes. The relationship between the two commands is AND. In node 20, if-match community-filter 1 and if-match community-filter 2 are used to filter routes based on communities. The relationship between if-match community-filter 1 and if-match community-filter 2 is OR. The apply clauses specify actions. That is, the apply clauses set some attributes of the route after the route matches the node.



**Prerequisites**



A route-policy has been configured before you run the **apply as-path most-recent** command.



**Configuration Impact**



After this command is run, the AS\_Path attributes of the BGP routes that match the matching rules are changed. Assume that the original AS\_Path is (30, 40, 50). If the apply as-path most-recent 3 command is configured, the AS\_Path is changed to (30, 30, 30, 30, 40, 50).




Example
-------

# Set the number of times the most recent AS number is appended to 3.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply as-path most-recent 3

```