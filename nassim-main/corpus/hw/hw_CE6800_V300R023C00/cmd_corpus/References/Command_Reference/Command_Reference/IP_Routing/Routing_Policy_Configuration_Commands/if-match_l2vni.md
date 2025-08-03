if-match l2vni
==============

if-match l2vni

Function
--------



The **if-match l2vni** command configures a matching rule based on a Layer 2 VNI list.

The **undo if-match l2vni** command cancels the configuration.



By default, no matching rule based on a Layer 2 VNI list is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match l2vni** [ *l2vni-list-name* ]

**undo if-match l2vni** [ *l2vni-list-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *l2vni-list-name* | Specifies the name of a Layer 2 VNI list. If l2vni-list-name is not specified, a route is matched if only it carries Layer 2 VNI information. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure a matching rule based on a Layer 2 VNI list, run the **if-match l2vni** command.

* Run the **route-policy** command to configure a route-policy or enter the view of an existing route-policy.
* A route-policy may consist of multiple nodes, and the relationship among these nodes is OR. The system matches routes against the nodes in ascending order of node IDs. If a route matches a node in the route-policy, the route is not matched against the next node.
* Each node comprises a set of if-match and applyclauses. The if-match clauses define matching rules that are based on route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. Specifically, a route matches a node only when it meets all the if-match clauses of the node. The relationship among if-match clauses of the same node that are based on the same route attribute is OR; the system matches routes against the if-match clauses in order; if a route matches an if-match clause, the route matches the route-policy, and the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 30 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set route attributes for the route.

**Prerequisites**

A VNI list has been created using the **filter-list vni** command.

**Precautions**

If you run this command multiple times, only the latest configuration takes effect.Multiple MAC addresses can be configured in a MAC address list. The relationship between the MAC addresses is OR. That is, a route passes the filtering if it matches one of the MAC addresses.


Example
-------

# Configure a matching rule based on a Layer 2 VNI list.
```
<HUAWEI> system-view
[~HUAWEI] filter-list vni abc
[*HUAWEI-vni-list-abc] quit
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match l2vni abc

```