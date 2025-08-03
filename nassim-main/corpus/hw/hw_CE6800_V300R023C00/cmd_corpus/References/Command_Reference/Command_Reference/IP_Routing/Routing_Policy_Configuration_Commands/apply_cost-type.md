apply cost-type
===============

apply cost-type

Function
--------



The **apply cost-type** command sets the cost type of a route.

The **undo apply cost-type** command cancels the configuration.



By default, no cost type of a route is set.


Format
------

**apply cost-type** { **external** | **internal** | **type-1** | **type-2** | **internal-inc-ibgp** | **med-plus-igp** }

**undo apply cost-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **external** | Sets the cost type to IS-IS external. | - |
| **internal** | Sets the cost type to IS-IS internal or sets the MED of a BGP route to the cost of the IGP route to which the BGP route recurses. This parameter takes effect only on EBGP peers. | - |
| **type-1** | Sets the cost type to OSPF external Type 1. | - |
| **type-2** | Sets the cost type to OSPF external Type 2. | - |
| **internal-inc-ibgp** | Sets the cost type to IS-IS internal or enables the MED of a BGP route to inherit the cost of the IGP route to which the BGP route recurses. This parameter takes effect both on EBGP and IBGP peers. | - |
| **med-plus-igp** | Sets the MED of a BGP route by adding the original MED to the cost of the IGP route to which the BGP route recurses. This parameter takes effect both on EBGP and IBGP peers. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the cost type for the routes that match an if-match clause, run the **apply cost-type** command. After the cost type of the routes that match a route-policy is set, the routes that are imported using the route-policy carry the set cost type.

* Run the **route-policy** command to enter the Route-policy view.
* A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the route matches the route-policy, and the system no longer matches it against other nodes.
* Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.

**Prerequisites**



A route-policy has been configured using the **route-policy** command.



**Configuration Impact**



After routes match the route-policy, the cost type of the routes is changed.



**Precautions**

The apply cost-type { internal | internal-inc-ibgp } command has different functions on IS-IS routes and BGP routes:

* When it is applied to IS-IS routes, it configure the routes as IS-IS internal routes.
* When it is applied to BGP routes, the device sets the MED of each BGP route to be advertised to a peer to the cost of the IGP route to which the BGP route recurses.The internal parameter takes effect only on EBGP peers, whereas the internal-inc-ibgp parameter takes effect both on EBGP and IBGP peers.


Example
-------

# Set the cost type to OSPF external Type-1.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply cost-type type-1

```