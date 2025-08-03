apply comm-filter delete
========================

apply comm-filter delete

Function
--------



The **apply comm-filter delete** command deletes a BGP community attribute based on the specified value in a community filter.

The **undo apply comm-filter** command cancels the configuration.



By default, the community attributes of BGP routes are not deleted.


Format
------

**apply comm-filter** { *basIndex* | *advIndex* } **delete**

**apply comm-filter** *cmntyName* **delete**

**undo apply comm-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basIndex* | Specifies the number of a basic community filter. | The value is an integer that ranges from 1 to 99. |
| *advIndex* | Specifies the number of an advanced community filter. | The value is an integer ranging from 100 to 199. |
| *cmntyName* | Specifies the name of a community filter. | The value is a string of 1 to 51 case-sensitive characters and cannot contain digits only. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The community attribute is a private attribute of BGP, and the **apply comm-filter delete** command is valid only for BGP routes.When the **apply comm-filter delete** command is run in the Route-policy view to delete the values from the community filter, only one community attribute can be specified in the **ip community-filter** command. If multiple community attributes are configured in the same community filter, running the **apply comm-filter delete** command cannot delete these community attributes. To delete the community attributes, you need to run the **ip community-filter** command several times to configure community attributes one by one, and then run the **apply comm-filter delete** command to delete these community attributes.

* Run the **route-policy** command to enter the route-policy view.
* A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the route matches the route-policy, and the system no longer matches it against other nodes.
* Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.

**Prerequisites**



A route-policy has been configured using the **route-policy** command.



**Configuration Impact**



After routes match the filtering conditions, the specified community attributes are deleted from these routes.



**Precautions**

1. Only one community attribute can be configured for the specified community attribute list. To delete multiple community attributes, configure multiple community attribute lists. For example, if community attribute list 1 is used to delete 100:100 200:200 from the community attribute 100:100 200:200 300:300 carried in a route, perform the following configurations on community attribute list 1:[~DeviceA] ip community-filter 1 permit 100:100[\*DeviceA] ip community-filter 1 permit 200:200[\*DeviceA] display ip community-filterCommunity filter Number: 1index: 10 permit 100:100index: 20 permit 200:200[~DeviceA] route-policy RP1 permit node 10[\*DeviceA-route-policy] apply comm-filter 1 deleteWhile in the following case, you cannot delete the community attributes 100:100 and 200:200.[\*DeviceA] ip community-filter 1 permit 100:100 200:200[\*DeviceA] display ip community-filterCommunity filter Number: 1index: 30 permit 100:100 200:200[~DeviceA] route-policy RP1 permit node 10[\*DeviceA-route-policy] apply comm-filter 1 delete
2. When the **apply community** and **apply comm-filter delete** commands are configured on the same node of a route-policy, the system does not care about the configuration sequence and deletes the configuration before performing the configuration operation.The contents of the Route-Policy RP1 are as follows:[\*DeviceA] display route-policyRoute-policy: RP1permit : 10 (matched counts: 0)Apply clauses:apply comm-filter 1 deleteapply community 999:9 additiveThe contents of community filter 1 are as follows:[\*DeviceA] display ip community-filterCommunity filter Number: 1index: 10 permit 111:1index: 20 permit 999:9The community attribute 111:1 of the corresponding BGP route is deleted and community attribute 999:9 is added.


Example
-------

# Delete BGP route community attributes 1:200, 2:200, and 3:200 from the community filter.
```
<HUAWEI> system-view
[~HUAWEI] ip community-filter 1 permit 1:200
[*HUAWEI] ip community-filter 1 permit 2:200
[*HUAWEI] ip community-filter 1 permit 3:200
[*HUAWEI] route-policy test permit node 10
[*HUAWEI-route-policy] apply comm-filter 1 delete

```