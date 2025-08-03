apply as-path
=============

apply as-path

Function
--------



The **apply as-path** command replaces or clears the original AS\_Path attribute, or adds, deletes a specified AS number to the AS\_Path attribute.

The **undo apply as-path** command cancels the configuration.



By default, the original AS\_Path attribute is not replaced or cleared and no AS number is added to or deleted from the AS\_Path attribute.


Format
------

**apply as-path** { *as-path-value* } &<1-128> { **additive** | **overwrite** | **delete** }

**undo apply as-path**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-path-value* | Specifies an AS number. | The value is an integer ranging from 1 to 4294967295 or the value is in the format of x.y, in which x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |
| **additive** | Adds the specified AS number to the original AS\_Path attribute. | - |
| **overwrite** | Replaces the AS numbers in the original AS\_Path attribute. | - |
| **delete** | Deletes the specified AS number from the original AS\_Path attribute. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The AS\_Path attribute is a private attribute of BGP used to record all ASs that a route passes through from the local area to the destination in distance-vector (DV) order. The AS\_Path attribute can be used to control route selection and prevent routing loops. When the filtering conditions specified by if-match clauses are met and the matching mode is set to permit, you can use the **apply as-path** command to set the AS\_Path attributes of the routes that match the filtering conditions.

* Run the **route-policy** command to enter the Route-policy view.
* A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the system no longer matches it against other nodes.
* Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.

**Prerequisites**



A route-policy has been configured using the **route-policy** command.



**Configuration Impact**



After the **apply as-path** command is run, the AS\_Path attributes of the BGP routes that meet the matching rules change. Assume that the original AS\_Path is (30, 40, 50). If apply as-path 60 70 80 10.10 additive is configured, the AS\_Path is changed to (60, 70, 80, 10.10, 30, 40, 50). For the apply as-path overwrite and apply as-path none overwrite commands, if an export policy is applied to EBGP, the apply as-path overwrite command can replace only non-local AS numbers in the AS\_Path of the device, and the apply as-path none overwrite command can clear only non-local AS numbers in the AS\_Path of the device. This restriction does not apply to IBGP. For example, if apply as-path 60 70 80 10.10 overwrite is configured, the AS\_Path is changed to (60, 70, 80, 10.10). If the apply as-path none overwrite command is run, the AS\_Path attribute is cleared.After the **apply as-path** command is run, the configuration is backed up to the standby main control board. You can run the **display route-policy** command to check whether the configuration takes effect.After the **undo apply as-path** command is run, no operation is performed on the AS\_Path of the routes that match the route-policy, and the path that the routes pass through is not modified.The **apply as-path** command takes effect before the local AS number is added when EBGP is used and an export policy is applied. Assume that the original AS\_Path is (30, 40, 50), the local AS number is 100, and the matching conditions are met. If apply as-path 60 70 80 10.10 additive is configured, the AS\_Path of the BGP route received by the EBGP peer is changed to (100, 60, 70, 80, 10.10, 30, 40, 50).



**Precautions**



The apply as path or **undo apply as-path** command directly affects the path through which network traffic passes. Therefore, you must be familiar with the network topology and the impact of the command before running this command.The apply as-path and apply as-path(enhance) commands have the same function. The difference is that the **apply as-path** command supports a maximum of 128 AS numbers, whereas the apply as-path(enhance) command supports a minimum of 129 AS numbers and a maximum of 256 AS numbers.If the overwrite or delete parameter is used, the AS\_Path is modified, causing a routing loop.Deleting or modifying the AS\_Path may cause routing loops.




Example
-------

# Change the AS number in the original AS\_Path attribute to 200, 10.10.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply as-path 200 10.10 overwrite

```