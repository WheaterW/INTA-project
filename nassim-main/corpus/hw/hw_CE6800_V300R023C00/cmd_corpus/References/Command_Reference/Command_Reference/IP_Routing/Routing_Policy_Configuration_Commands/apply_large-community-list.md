apply large-community-list
==========================

apply large-community-list

Function
--------



The **apply large-community-list** command applies a BGP Large-Community list.

The **undo apply large-community-list** command cancels the configuration.



By default, the BGP Large-Community list is not set.


Format
------

**apply large-community-list** *large-community-list-name* { **additive** | **overwrite** | **delete** }

**undo apply large-community-list** [ *large-community-list-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **additive** | Adds a value to the Large Community attribute carried in routes. | - |
| **overwrite** | Overwrites the existing values of the Large-Community attribute. | - |
| **delete** | Deletes the values of the Large-Community attribute carried in the matched routes. | - |
| **large-community-list** *large-community-list-name* | Specifies the name of a BGP Large-Community list. | The value is a string of 1 to 63 case-sensitive characters. Spaces are allowed only when the string is enclosed in double quotation marks (" "). |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The Large-Community attribute is a private attribute of BGP and can be flexibly applied to route-policies. To modify or set values of the Large-Community attribute in BGP routes, run the **apply large-community-list** command.



**Configuration Impact**



If the **apply large-community-list** command is run in a route-policy, the values of the Large-Community attribute in the BGP routes filtered by the route-policy will be changed to the value in the route-policy.



**Precautions**



If the **apply large-community-list** command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Configure a route-policy named setlargecommunity to filter the routes whose AS\_Path filter is 8, and specify the name of the BGP Large-community attribute list as largecommunity1.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-list largecommunity1
[*HUAWEI-large-community-list-largecommunity1] quit
[*HUAWEI] ip as-path-filter 8 permit ^2
[*HUAWEI] route-policy setlargecommunity permit node 16
[*HUAWEI-route-policy] if-match as-path-filter 8
[*HUAWEI-route-policy] apply large-community-list largecommunity1 overwrite

```