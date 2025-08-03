if-match route-type
===================

if-match route-type

Function
--------



The **if-match route-type** command configures a filtering rule based on route types.

The **undo if-match route-type** command cancels the configuration.



By default, no filtering rule based on route types is configured.


Format
------

**if-match route-type** { **external-type1** | **external-type2** | **external-type1or2** | **is-is-level-1** | **is-is-level-2** | **internal** | **nssa-external-type1** | **nssa-external-type2** | **nssa-external-type1or2** }

**if-match route-type** { **ibgp** | **ebgp** }

**if-match route-type evpn** { **inclusive** | **mac** | **prefix** } \*

**undo if-match route-type** { **external-type1** | **external-type2** | **external-type1or2** | **is-is-level-1** | **is-is-level-2** | **internal** | **nssa-external-type1** | **nssa-external-type2** | **nssa-external-type1or2** }

**undo if-match route-type** { **ibgp** | **ebgp** }

**undo if-match route-type evpn**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **external-type1** | Indicates OSPF external Type 1 routes. | - |
| **external-type2** | Indicates OSPF external Type 2 routes. | - |
| **external-type1or2** | Indicates OSPF external routes. | - |
| **is-is-level-1** | Indicates IS-IS Level-1 routes. | - |
| **is-is-level-2** | Indicates IS-IS Level-2 routes. | - |
| **internal** | Indicates internal routes, including OSPF inter-area routes and intra-area routes. | - |
| **nssa-external-type1** | Indicates NSSA external Type 1 routes. | - |
| **nssa-external-type2** | Indicates NSSA external Type 2 routes. | - |
| **nssa-external-type1or2** | Indicates NSSA external routes. | - |
| **ibgp** | Indicates IBGP routes. | - |
| **ebgp** | Indicates EBGP routes. | - |
| **evpn** | Indicates EVPN routes. | - |
| **inclusive** | Indicates EVPN inclusive multicast routes. | - |
| **mac** | Indicates MAC advertisement routes. | - |
| **prefix** | Indicates EVPN IP prefix routes. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To filter routes based on the route type, run the **if-match route-type** command.

* Run the **route-policy** command to enter the Route-policy view.
* A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the route matches the route-policy, and the system no longer matches it against other nodes.
* Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.

**Prerequisites**



A route-policy has been configured using the **route-policy** command.



**Precautions**



For the same node in a route-policy, if two if-match route-type clauses are the same, the latter if-match route-type will not override the previous one. After the latter clause is configured, both clauses take effect. The relationship between if-match route-type clauses is "OR". That is, the actions defined in apply clauses can be performed on a route if the route matches one of the filtering rules. For example, if both the if-match route-type is-is-level-1 and **if-match route-type external-type1or2** commands are configured on the same node of a route policy, both IS-IS Level-1 routes and OSPF external routes can match the route-policy.NOTE:external-type1or2 refers to external-type1 or external-type2. For the same node in a route policy, configuring both the if-match route-type external-type1 and if-match route-type external-type2 is equivalent to configuring the **if-match route-type external-type1or2** command. The two operations generate the same configuration file.Similarly, nssa-external-type1or2 refers to nssa-external-type1 or nssa-external-type2. For the same node in a route policy, configuring both the if-match route-type nssa-external-type1 and **if-match route-type nssa-external-type2** commands is equivalent to configuring the **if-match route-type nssa-external-type1or2** command. The two operations generate the same configuration file.




Example
-------

# Define a rule to match the routes of the specified type.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match route-type nssa-external-type1

```