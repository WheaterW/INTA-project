ip ipv6-prefix description
==========================

ip ipv6-prefix description

Function
--------



The **ip ipv6-prefix description** command configures the description information of the IPv6 prefix list.

The **undo ip ipv6-prefix description** command deletes the description information of the IPv6 prefix list.



By default, no description information of the IPv6 prefix list is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip ipv6-prefix** *ipv6-prefix-name* **description** *text*

**undo ip ipv6-prefix** *ipv6-prefix-name* **description** [ *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-prefix-name* | Specifies the name of the IPv6 prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **description** *text* | Specifies the description information of the IPv6 prefix list. | It is a string of 1 to 80 characters case-sensitive characters, with spaces supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **ip ipv6-prefix** command is used to configure an IPv6 prefix list. An IPv6 prefix can be used as a filter by various protocols or used with a route-policy.

* The **ip ipv6-prefix** command can be used with the following commands to filter routes to be advertised globally with an IPv6 prefix list as a filtering condition:
* filter-policy export(OSPFv3)
* ipv6 filter-policy export(IS-IS)
* filter-policy export(BGP)
* The **ip ipv6-prefix** command can be used with the following commands to filter routes to be accepted globally with an IPv6 prefix list as a filtering condition:
* filter-policy import(OSPFv3)
* ipv6 filter-policy import(IS-IS)
* filter-policy import(BGP)
* The **ip ipv6-prefix** command can be used with the following commands to configure a route-policy based on an IPv6 prefix list for a specific peer:
* peer ip-prefix (BGP)
* The ipv6 import-route isis level-1 into level-2 filter-policy ipv6-prefix command is used to control the route leaking from a Level-1 area to a Level-2 area.
* The ipv6 import-route isis level-2 into level-1 filter-policy ipv6-prefix command is used to control route leaking from an IS-IS Level-2 area to an IS-IS Level-1 area.
* The **ip ipv6-prefix** command and the **if-match ipv6** command can be used to test received or sent routes based on an IPv6 prefix list.An IPv6 prefix list can contain several entries, and each entry specifies an IPv6 prefix range. The relationship between the nodes is "OR". That is, if a route matches one entry, the route matches the IPv6 prefix list; if a route does not match any entry, the route fails to match the IPv6 prefix list.An IPv6 prefix range is determined by prefix-length and greater-equal-value, less-equal-value. If mask-length and greater-equal-value, less-equal-value are specified, an IPv6 address must match the prefix range.

**Precautions**

The IPv6 prefix lists in use cannot be deleted.


Example
-------

# Specifies the description information of the IPv6 prefix list.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix abc description aaa

```