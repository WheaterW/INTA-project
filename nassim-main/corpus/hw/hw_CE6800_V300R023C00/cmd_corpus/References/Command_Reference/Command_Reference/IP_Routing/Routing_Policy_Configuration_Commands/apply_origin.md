apply origin
============

apply origin

Function
--------



The **apply origin** command sets the Origin attribute of BGP routes.

The **undo apply origin** command cancels the configuration.



By default, no Origin attribute is set for BGP routes.


Format
------

**apply origin** { **egp** { *egpVal* } | **igp** | **incomplete** }

**undo apply origin**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **egp** | Sets the Origin attribute of BGP routes to EGP. | - |
| *egpVal* | Specifies an AS number. | * The value is an integer ranging from 1 to 4294967295. * The value is in the format of x.y, in which x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| **igp** | Sets the Origin attribute of BGP routes to IGP. | - |
| **incomplete** | Sets the Origin attribute of BGP routes to unknown. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The Origin attribute, as a proprietary attribute of BGP, defines the origin of a route. It identifies how a BGP route is generated. You can use the **apply origin** command to set the origin of BGP routes.

* Run the **route-policy** command to enter the Route-policy view.
* A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the route matches the route-policy, and the system no longer matches it against other nodes.
* Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.

**Prerequisites**



A route-policy has been configured using the **route-policy** command.



**Configuration Impact**



After a BGP route matches a route-policy, the origin of the BGP route is changed.




Example
-------

# Set the origin of BGP routes as IGP.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply origin igp

```