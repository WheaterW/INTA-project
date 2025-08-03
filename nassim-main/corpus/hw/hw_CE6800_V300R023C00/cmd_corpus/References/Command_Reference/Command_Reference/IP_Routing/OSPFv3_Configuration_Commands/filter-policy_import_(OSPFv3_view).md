filter-policy import (OSPFv3 view)
==================================

filter-policy import (OSPFv3 view)

Function
--------



The **filter-policy import** command filters the routes calculated by OSPFv3. Only the routes that pass the filtering are added to the RIB.

The **undo filter-policy import** command cancels the configuration.



By default, the received routes are not filtered.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**filter-policy** *acl-number* **import**

**filter-policy** { **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* } **import**

**undo filter-policy** [ *acl-number* | **acl6-name** *acl6-name* | **ipv6-prefix** *ipv6-prefix-name* | **route-policy** *route-policy-name* ] **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 address prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **filter-policy import** command to set a filtering policy for the received routes. Only the routes that pass the filtering are added to the routing table. The routes that do not pass the filtering are not added to the RIB. OSPF is a link-state dynamic routing protocol, with routing information carried in the link-state database (LSDB). Therefore, the **filter-policy import** command cannot be used to filter the advertised or received LSAs. Actually, this command is used to filter the routes calculated by OSPF. Only the routes that meet the filtering rules are added to the RIB.

**Precautions**

When the rule (basic ACL6 view) command is used to configure a filtering rule for a named IPv6 ACL, only the source address range is specified in source and the time period is specified in time-range take effect on the filtering rule.


Example
-------

# Filter the received routes based on the IPv6 address prefix list named abc.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix abc deny 2001:db8::1 64
[*HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] filter-policy ipv6-prefix abc import

```