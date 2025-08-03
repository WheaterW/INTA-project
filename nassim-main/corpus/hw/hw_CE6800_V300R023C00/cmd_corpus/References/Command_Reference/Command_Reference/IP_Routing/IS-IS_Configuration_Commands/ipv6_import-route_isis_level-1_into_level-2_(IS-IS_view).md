ipv6 import-route isis level-1 into level-2 (IS-IS view)
========================================================

ipv6 import-route isis level-1 into level-2 (IS-IS view)

Function
--------



The **ipv6 import-route isis level-1 into level-2** command enables IPv6 route leaking from a Level-1 area to a Level-2 area.

The **undo ipv6 import-route isis level-1 into level-2** command disables IPv6 route leaking from a Level-1 area to a Level-2 area.

The **ipv6 import-route isis level-1 into level-2 disable** command disables IS-IS Level-1 area IPv6 routes from leaking to a Level-2 area.

The **undo ipv6 import-route isis level-1 into level-2 disable** command enables IS-IS Level-1 area IPv6 routes to leak to a Level-2 area.



By default, all IPv6 routes can leak from a Level-1 area to a Level-2 area.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 import-route isis level-1 into level-2** [ **tag** *tag* | **filter-policy** { *acl6-number* | **acl6-name** *acl6-name-string* | **ipv6-prefix** *ipv6-prefix-name* | { **route-policy** *route-policy-name* } } | **direct** **allow-filter-policy** ] \*

**ipv6 import-route isis level-1 into level-2 disable**

**undo ipv6 import-route isis level-1 into level-2**

**undo ipv6 import-route isis level-1 into level-2** { **tag** *tag* | **filter-policy** { *acl6-number* | **acl6-name** *acl6-name-string* | **ipv6-prefix** *ipv6-prefix-name* | { **route-policy** *route-policy-name* } } | **direct** **allow-filter-policy** } \*

**undo ipv6 import-route isis level-1 into level-2 disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tag** *tag* | Assigns administrative tags to the imported routes. | The value is an integer ranging from 1 to 4294967295. |
| **filter-policy** | Indicates a route filtering policy. | - |
| *acl6-number* | Specifies a basic ACL6 number. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name-string* | Specifies the name of a named basic ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 prefix list. Only the routes that match the specified IPv6 prefix can leak from a Level-1 area to a Level-2 area. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **direct** | Specifies the direct routes. | - |
| **allow-filter-policy** | Indicates a filtering policy to filter the direct routes. If the parameter is configured, only the IS-IS Level-1 area direct routes that match the filtering policy can leak to a Level-2 area. If the parameter is not configured, all Level-1 area direct routes will leak to a Level-2 area. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the maximum number of IPv6 IS-IS equal-cost routes for load balancing, run the ipv6 maximum load-balancing command. The ipv6 maximum load-balancing command takes effect only after IPv6 is enabled for the IS-IS process. For details, see isis ipv6 enable.

**Precautions**

This command takes effect only on Level-1-2 devices.For the routing policy used in this command, only if-match clauses can be configured to set matching rules, and apply clauses cannot be configured to set route attributes.When locator routes are leaked between IS-IS levels or imported between processes, locator TLVs are advertised in the target area by default. This behavior may affect path calculation of devices in the target area. You can use segment-routing ipv6 locator-inter-area disable to eliminate the impact.If route-policy route-policy-name is specified in this command, the following items can be matched: the outbound interface, route cost, route type, route tag, IPv6 route next-hop ACL, IPv6 route next-hop prefix list, and routing protocol type. No action can be set.If the referenced policy contains unsupported attribute matching or setting an action, unexpected results may occur.


Example
-------

# Use the IPv6 prefix list named list to control IPv6 route leaking from a Level-1 area to a Level-2 area.
```
<HUAWEI> system-view
[~HUAWEI] ip ipv6-prefix list deny 2001:db8::1 64
[*HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 import-route isis level-1 into level-2 filter-policy ipv6-prefix list

```