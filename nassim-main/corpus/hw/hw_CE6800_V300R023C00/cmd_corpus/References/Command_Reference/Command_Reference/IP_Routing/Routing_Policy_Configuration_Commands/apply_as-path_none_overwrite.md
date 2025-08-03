apply as-path none overwrite
============================

apply as-path none overwrite

Function
--------



The **apply as-path none overwrite** command clears the original AS\_Path attribute.



By default, the original AS\_Path attribute is not cleared.


Format
------

**apply as-path none overwrite**


Parameters
----------

None

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



If the **apply as-path none overwrite** command is run for an export policy and the export policy is applied to an IBGP peer, the original AS\_Path attribute is changed to null.After the **apply as-path** command is run, the configuration is backed up to the slave main control board. You can run the **display route-policy** command to check whether the configuration takes effect.



**Precautions**



Running the **apply as-path** command changes the path through which network traffic passes. Use this command only when you are familiar with the network topology and impact of the command on services.The **undo apply as-path** command cancels the configuration of clearing the original AS\_Path attribute.




Example
-------

# Clears the original AS\_Path attribute.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply as-path none overwrite

```