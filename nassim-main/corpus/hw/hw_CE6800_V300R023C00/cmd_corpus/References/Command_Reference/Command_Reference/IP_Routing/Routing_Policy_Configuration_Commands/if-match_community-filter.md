if-match community-filter
=========================

if-match community-filter

Function
--------



The **if-match community-filter** command sets a filtering rule that is based on the community filter.

The **undo if-match community-filter** command cancels the configuration.



By default, no filtering rule based on the community filter is set.


Format
------

**if-match community-filter** { *basIndex* [ **whole-match** ] | *AdvIndex* } &<1-16>

**if-match community-filter** *cfName* [ **whole-match** ]

**undo if-match community-filter** { *basIndex* | *AdvIndex* } &<1-16>

**undo if-match community-filter** *cfName*

**undo if-match community-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basIndex* | Specifies the number of the basic community filter. | The value is an integer ranging from 1 to 99. |
| **whole-match** | Indicates complete matching. That is, all the communities in the command must be matched. Complete matching is valid only for the basic community filter. | - |
| *AdvIndex* | Specifies the number of the advanced community filter. | The value is an integer ranging from 100 to 199. |
| *cfName* | Specifies the name of the community filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. The string cannot be all numbers. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The community attribute is a proprietary attribute of BGP. The **if-match community-filter** command is applicable mainly to BGP routes. The **ip community-filter** command must be used to define a community filter so that the filtering rule based on this community filter can take effect. For example:

* If the if-match community-filter 1 command is used but community filter 1 is not configured, all routes match the filtering rule.
* If the if-match community-filter 1 command is used after the ip community-filter 1 permit 1:1 command is used, the BGP routes with the community attribute 1:1 are permitted.

**Prerequisites**



A community filter has been configured using the **ip community-filter** command.A route-policy has been configured using the route-policy command.



**Configuration Impact**



When you filter routes based on the community attributes, the routes that match the filtering rule are permitted and the routes that do not match the filtering rule are denied.



**Precautions**



The community filters can be configured in the **if-match community-filter** command. The relationship between these community filters is OR. Specifically, if a route matches one of these community filters, it matches the matching rules of the command. If the **if-match community-filter** command is run more than once, the relationship between its configurations is OR.The parameter whole-match is valid only for its front community filter. If multiple community filters are specified in the **if-match community-filter** command and packets are required to completely match each filter, you need to specify the parameter whole-match behind each community filter.The parameter sort-match is valid only for its front community filter. If multiple community filters are specified in the **if-match community-filter** command and packets are required to wholly match the regular expansion in the filter in sequence, you need to specify the parameter sort-match behind each community filter.The name of a community filter cannot be all numbers.




Example
-------

# Set the complete filtering rule for community attribute filters 1 and 2.
```
<HUAWEI> system-view
[~HUAWEI] ip community-filter 1 permit
[*HUAWEI] ip community-filter 2 permit
[*HUAWEI] route-policy test permit node 11
[*HUAWEI-route-policy] if-match community-filter 1 whole-match 2 whole-match

```

# Set a filtering rule that is based on the community filter named aa.
```
<HUAWEI> system-view
[~HUAWEI] ip community-filter basic aa permit
[*HUAWEI] route-policy test permit node 12
[*HUAWEI-route-policy] if-match community-filter aa

```

# Set a filtering rule that is based on the community filter 1.
```
<HUAWEI> system-view
[~HUAWEI] ip community-filter 1 permit 100:200
[*HUAWEI] route-policy test permit node 10
[*HUAWEI-route-policy] if-match community-filter 1

```