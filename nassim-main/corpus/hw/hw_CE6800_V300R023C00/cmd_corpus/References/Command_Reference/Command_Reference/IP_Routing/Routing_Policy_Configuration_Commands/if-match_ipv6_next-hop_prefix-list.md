if-match ipv6 next-hop prefix-list
==================================

if-match ipv6 next-hop prefix-list

Function
--------



The **if-match ipv6 next-hop prefix-list** command configures a filtering rule that is based on next-hop addresses of IPv6 routes.

The **undo if-match ipv6 next-hop prefix-list** command cancels the configuration.



By default, no filtering rule based on next-hop addresses of IPv6 routes is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**if-match ipv6 next-hop prefix-list** *ipv6-prefix-name*

**undo if-match ipv6 next-hop** [ **prefix-list** *ipv6-prefix-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **prefix-list** *ipv6-prefix-name* | Specifies the name of the IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you run the **if-match ipv6 next-hop prefix-list** command to match the next hop address of an IPv6 route, the matching condition must be used together with the IPv6 prefix. Example:

* If if-match ipv6 next-hop prefix-list aa is configured but ip ipv6-prefix aa is not configured, all routes are permitted.
* If if-match ipv6 next-hop prefix-list aa and ip ipv6-prefix aa permit 2001:db8:1::1 128 are configured, the route with the next hop being 2001:db8:1::1 is permitted.

**Prerequisites**

A route-policy has been configured using the route-policy command.An IPv6 prefix has been configured using the **ip ipv6-prefix** command.

**Configuration Impact**

When you filter routes based on the next hop addresses of IPv6 routes, the routes that match the filtering rule are permitted and the route that do not match the filtering rule are denied.

**Precautions**

If the next hop address or source address of a route to be filtered is 0::0, by default, the system matches the route and considers its mask length as 0.If the next hop address or source address of a route to be filtered is not 0::0, by default, the system matches the route and considers its mask length as 128.


Example
-------

# Define a rule to match the routes with the IPv6 routing information in the IPv6 prefix list named p1.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match ipv6 address prefix-list p1
[*HUAWEI-route-policy] if-match ipv6 next-hop prefix-list p1
[*HUAWEI-route-policy] if-match ipv6 route-source prefix-list p1

```