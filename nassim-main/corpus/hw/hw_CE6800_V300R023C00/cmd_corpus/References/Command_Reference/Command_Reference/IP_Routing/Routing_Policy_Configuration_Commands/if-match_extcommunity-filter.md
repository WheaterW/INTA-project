if-match extcommunity-filter
============================

if-match extcommunity-filter

Function
--------



The **if-match extcommunity-filter** command sets a filtering rule that is based on the VPN-Target extended community filter.

The **undo if-match extcommunity-filter** command cancels the configuration.



By default, no filtering rule based on the VPN-Target extended community filter is set.


Format
------

**if-match extcommunity-filter** { *basIndex* [ **matches-all** | **whole-match** ] | *advIndex* } &<1-16>

**if-match extcommunity-filter** *ecfName* [ **matches-all** | **whole-match** ]

**undo if-match extcommunity-filter** { *basIndex* | *advIndex* } &<1-16>

**undo if-match extcommunity-filter** *ecfName*

**undo if-match extcommunity-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basIndex* | Specifies the basic VPN-Target extended community filter number. | The value is an integer ranging from 1 to 199. |
| **matches-all** | Matches all the VPN-Target attributes of the VPN-Target filter. This parameter is valid only for basic extended community filters. | - |
| **whole-match** | Exactly matches the VPN-Targets in routes against the VPN-Targets in the filter. That is, the number of VPN-Targets and their values in routes must be the same as those of the VPN-Targets in the filter, but the sequences can be different. This parameter is valid only for basic extended community filters. | - |
| *advIndex* | Specifies the advanced VPN-Target extended community filter number. | The value is an integer ranging from 200 to 399. |
| *ecfName* | Specifies the VPN-Target extended community filter name. | The value is a string of 1 to 51 case-sensitive characters and cannot contain digits only. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The extended community attributes help flexibly control the route-policy. You can use the **if-match extcommunity-filter** command to configure a node to filter routes based on the VPN-Target extended community filter. After such a filtering rule is configured, you can apply the apply clauses to change the attributes of the routes that match the VPN-Target extended community attributes-based filtering rule.The **if-match extcommunity-filter** command is applicable only to BGP routes and must work with the **ip extcommunity-filter** command. For example:

* If the if-match extcommunity-filter 1 command is used but the VPN-Target extended community filter 1 is not configured, all routes match the filtering rule.
* If the if-match extcommunity-filter 1 command is used after the ip extcommunity-filter 1 permit rt 1:1 command is used, the BGP routes with the VPN-Target extended community attribute 1:1 are permitted.

**Prerequisites**



A VPN-Target extended community filter has been configured using the **ip extcommunity-filter** command.



**Configuration Impact**



When you filter routes based on the VPN-Target extended community attributes, the routes that match the filtering rule are permitted and the routes that do not match the filtering rule are denied.



**Precautions**



A maximum of 16 VPN-Target extended community filters can be configured in the **if-match extcommunity-filter** command. The relationship between these VPN-Target extended community filters is OR. Specifically, if a route matches one of these VPN-Target extended community filters, it matches the matching rules of the command.




Example
-------

# Define a rule to match the routes of the specified VPN-Target extended community filter.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-filter 1 permit rt 100:1
[*HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match extcommunity-filter 1

```