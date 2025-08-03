ipv6 filter-policy import
=========================

ipv6 filter-policy import

Function
--------



The **ipv6 filter-policy import** command configures IS-IS to filter received IPv6 routes so that only given routes are added to the IPv6 routing table.

The **undo ipv6 filter-policy import** command removes the configuration.



By default, IS-IS does not filter received IPv6 routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 filter-policy** { *acl6-number* | **acl6-name** *acl6-name-string* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* } **import**

**undo ipv6 filter-policy** [ *acl6-number* | **acl6-name** *acl6-name-string* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies a basic ACL6 number. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name-string* | Specifies the name of a named basic ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 address prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy to filter routes based on tags and other protocol parameters. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To set the maximum number of IPv6 IS-IS equal-cost routes for load balancing, run the ipv6 maximum load-balancing command. The ipv6 maximum load-balancing command takes effect only after IPv6 is enabled for the IS-IS process. For details, see isis ipv6 enable.


Example
-------

# Filter received IPv6 routes based on ACL6 2003.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2003
[*HUAWEI-acl6-basic-2003] quit
[*HUAWEI] isis
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 filter-policy 2003 import

```