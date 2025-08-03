apply qos-local-id
==================

apply qos-local-id

Function
--------



The **apply qos-local-id** command sets the QoS local ID.

The **undo apply qos-local-id** command cancels the configuration.



By default, no QoS local ID is set.


Format
------

**apply qos-local-id** *qos-local-id*

**undo apply qos-local-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *qos-local-id* | Specifies a value for the QoS local ID. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Run the **route-policy** command to enter the Route-policy view.A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the route matches the route-policy, and the system no longer matches it against other nodes.Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.The QoS local ID is a local identifier of QoS. You can run the **apply qos-local-id** command to set the QoS local ID in the route-policy. The QoS local ID set in the route-policy is delivered to the FIB. During packet forwarding, the system obtains the QoS local ID from the FIB and applies the related QoS policy according to the QoS local ID.



**Prerequisites**



A route-policy has been configured using the **route-policy** command.



**Precautions**



Using the **qos-local-id** command, you can set the QoS local ID locally. You can also run the **apply qos-local-id** command in the route-policy to set the QoS local ID when BGP imports routes. If the two configuration modes coexist and the QoS local IDs are different, the QoS local ID set through the route-policy takes effect preferentially.




Example
-------

# Set the QoS local ID in the route-policy test.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test permit node 10
[*HUAWEI-route-policy] apply qos-local-id 10

```