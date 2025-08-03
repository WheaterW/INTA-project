if-match extcommunity-list soo
==============================

if-match extcommunity-list soo

Function
--------



The **if-match extcommunity-list soo** command sets a filtering rule that is based on the Source of Origin (SoO) extended community filter.

The **undo if-match extcommunity-list soo** command cancels the configuration.



By default, no filtering rule based on the SoO extended community filter is set.


Format
------

**if-match extcommunity-list soo** *extcomm-filter-name*

**undo if-match extcommunity-list soo** *extcomm-filter-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *extcomm-filter-name* | Specifies the name of an SoO extended community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. The string cannot be all numbers. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The extended community attributes help flexibly control the route-policy. You can use the **if-match extcommunity-list soo** command to configure a node to filter routes based on the SoO extended community filter.

* Run the **route-policy** command to enter the Route-policy view.
* A route-policy may consist of multiple nodes. The relationship between the nodes is "OR". The system matches a route against the nodes in sequence. If the route matches a node, the route matches the route-policy, and the system no longer matches it against other nodes.
* Each node comprises a set of if-match and apply clauses. The if-match clauses define the filtering rules that are used to match certain route attributes. The relationship among if-match clauses of the same node that are based on different route attributes is AND. A route matches a node only when the route matches all the filtering rules specified in the if-match clauses of the node. The apply clauses specify actions. The relationship among if-match clauses of the same node that are based on the same route attribute is OR. The system matches routes against the if-match clauses in order. If a route matches an if-match clause, the system no longer matches the route against the rest if-match clauses. For example, the if-match community-filter 1 and if-match as-path-filter 1 configurations in node 10 are based on different route attributes. Therefore, the relationship among if-match clauses of this node is AND. The if-match community-filter 1 and if-match community-filter 2 configurations in node 20 are both based on the community attribute. Therefore, the relationship among if-match clauses of this node is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set some attributes for the route.The **if-match extcommunity-list soo** command is applicable only to BGP routes and must work with the **ip extcommunity-list soo** command. For example:
* If the if-match extcommunity-list soo basic aaa command is used but the extended community filter 1 is not configured, all routes match the filtering rule.
* If the if-match extcommunity-list soo basic aaa command is used after the ip extcommunity-list soo basic aaa permit 1.2.3.4:5 command is used, the BGP routes with the SoO extended community attribute 1.2.3.4:5 are permitted.

**Prerequisites**



An SoO extended community filter has been configured using the **ip extcommunity-list soo** command.



**Precautions**



The relationship between these SoO extended community filters is OR. Specifically, if a route matches one of these SoO extended community filters, it matches the matching rules of the command.




Example
-------

# Define a rule to match the routes of the specified SoO extended community filter.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-list soo basic aaa permit 1.2.3.4:5
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match extcommunity-list soo aaa

```