if-match prefix mod
===================

if-match prefix mod

Function
--------



The **if-match prefix mod** command configures a matching rule that is based on the route prefix modulo operation result.

The **undo if-match prefix mod** command deletes a matching rule that is based on the route prefix modulo operation result.



By default, no matching rule that is based on the route prefix modulo operation result is configured.


Format
------

**if-match prefix mod** *mod-value* **equal** *mod-result*

**undo if-match prefix mod** [ *mod-value* **equal** *mod-result* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mod-value* | Specifies a route prefix modulus value. | The value is an integer ranging from 1 to 128. |
| **equal** | Indicates that the route prefix modulo operation result must be the specified mod-result. | - |
| *mod-result* | Specifies the route prefix modulo operation result. | The value is an integer ranging from 0 to 127.  The value of mod-result must be less than that of mod-value. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure a matching rule that is based on the route prefix modulo operation result, run the **if-match prefix mod** command. In addition, a route prefix modulo operation rule needs to be configured so that IP address-based load balancing can be implemented.In most cases, the route prefix modulus value is set to the number of devices that participate in load balancing.You need to configure a route-policy for the matching rule.

* To enter the route-policy view, run the **route-policy** command.
* A route-policy may consist of multiple nodes, and the relationship between these nodes is "OR". The system matches routes against the nodes in order of node ID. If a route matches a node in the route-policy, the route is not matched against the next node.
* The relationship between the if-match clauses in a node of a route-policy is "AND". That is, a route must match all the if-match clauses of the node so that the action defined in the apply clause is applied to the route. If no if-match clause is specified, all routes will match the node in the route-policy.

**Prerequisites**



The **route-policy** command has been run.



**Precautions**



For the same node in a route-policy, if the **if-match prefix mod** command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Configure a route-policy to set the cost of the routes that match route prefix modulo operation result 1 to 10 and set the cost of the routes that match route prefix modulo operation result 2 to 20.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match prefix mod 4 equal 1
[*HUAWEI-route-policy] apply cost 10
[*HUAWEI-route-policy] quit
[*HUAWEI] route-policy policy permit node 20
[*HUAWEI-route-policy] if-match prefix mod 4 equal 2
[*HUAWEI-route-policy] apply cost 20

```