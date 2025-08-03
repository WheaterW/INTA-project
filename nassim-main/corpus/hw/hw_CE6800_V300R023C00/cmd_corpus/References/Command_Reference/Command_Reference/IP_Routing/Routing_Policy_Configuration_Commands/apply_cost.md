apply cost
==========

apply cost

Function
--------



The **apply cost** command sets the MED value for BGP routes or cost value for routes of other protocols.

The **undo apply cost** command cancels the configuration.



By default, no MED value is set for BGP routes nor cost value is set for routes of other protocols.


Format
------

**apply cost** [ + | **-** ] *cost*

**apply cost inherit**

**apply cost none**

**undo apply cost**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| + | Increases the route cost. If the link quality is poor or the link bandwidth is low, specify this parameter to increase the route cost, which helps control route selection. | If the MED of BGP routes or cost of non-BGP routes is greater than the maximum value (4294967295) after the adjustment, 4294967295 takes effect. |
| **-** | Reduces the route cost. If the link quality is good or the link bandwidth is high, specify this parameter to reduce the route cost, which helps control route selection. | If the MED of BGP routes or cost of non-BGP routes is less than the minimum value (0) after the adjustment, 0 takes effect. |
| *cost* | Specifies the route cost. To control route selection, adjust the route cost to prevent routing loops. | The value is an integer ranging from 0 to 4294967295. |
| **inherit** | Inherits the original route cost.  This function applies to IGP routes, not to BGP routes. | - |
| **none** | Delete the MED value of BGP routes. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the filtering conditions specified by if-match clauses are met, you can run the **apply cost** command to change the cost of the route to control the route selection sequence. After the cost of the routes to be matched is set, the cost of the routes imported by using the policy changes accordingly.

* Run the **route-policy** command to enter the route-policy view.
* A route-policy can consist of multiple nodes. The relationship between different nodes is OR. The system checks each node according to the node sequence number. If a route matches one node, the route matches the route-policy and is no longer matched against other nodes.
* Each node can consist of a group of if-match and apply clauses. The if-match clauses define the matching rules. The matching objects are some attributes of the routing information. The relationship between multiple if-match clauses for different attributes of a node is AND. A node can pass the matching test only when all the matching conditions specified by the if-match clauses are met. The relationship between multiple if-match clauses for the same attribute is OR, the system checks the if-match clauses in sequence. If a route matches one of the if-match clauses, the route matches the route-policy and does not match other if-match clauses. For example, in node 10, the if-match community-filter 1 and if-match as-path-filter 1 commands are used to filter routes based on different attributes. The relationship between the two commands is AND. In node 20, if-match community-filter 1 and if-match community-filter 2 are used to filter routes based on communities. The relationship between if-match community-filter 1 and if-match community-filter 2 is OR. The apply clauses specify actions. That is, the apply clauses set some attributes of the route after the route matches the node.
* By default, no cost is set for routes.

**Prerequisites**



A route-policy has been configured using the **route-policy** command.



**Configuration Impact**



After routes match the route-policy, the cost of the routes is changed.



**Precautions**



The costs of imported routes are independent of the route-policy after the **undo apply cost** command is used to cancel the configuration of route costs.




Example
-------

# Define an apply clause to set the route cost to 120.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply cost 120

```