ipv6 import-route isis level-2 into level-1 (IS-IS view)
========================================================

ipv6 import-route isis level-2 into level-1 (IS-IS view)

Function
--------



The **ipv6 import-route isis level-2 into level-1** command enables IPv6 route leaking from a Level-2 area to a Level-1 area.

The **undo ipv6 import-route isis level-2 into level-1** command disables IPv6 route leaking from a Level-2 area to a Level-1 area.



By default, IPv6 routes cannot leak from a Level-2 area to a Level-1 area.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 import-route isis level-2 into level-1** [ **tag** *tag* | **filter-policy** { *acl6-number* | **acl6-name** *acl6-name-string* | **ipv6-prefix** *ipv6-prefix-name* | { **route-policy** *route-policy-name* } } | **direct** { **allow-filter-policy** | **allow-up-down-bit** } \* ] \*

**undo ipv6 import-route isis level-2 into level-1**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tag** *tag* | Assigns administrative tags to the imported routes. | The value is an integer ranging from 1 to 4294967295. |
| **filter-policy** | Indicates a route filtering policy. | - |
| *acl6-number* | Specifies a basic ACL6 number. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name-string* | Specifies the name of a named basic ACL6. | The value is a string of 1 to 32 case-sensitive characters except spaces. The value must start with a letter or digit, and cannot contain only digits. |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of an IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **direct** | Specifies the direct routes. | - |
| **allow-filter-policy** | Applies the filtering policy to direct routes.  If the parameter is configured, only the IS-IS direct routes that match the filtering policy can leak from a Level-2 area to a Level-1 area. If the parameter is not configured, all direct routes can leak from a Level-2 area to a Level-1 area. | - |
| **allow-up-down-bit** | Sets the Up/Down bit to 1 for the leaked direct routes.  If direct allow-up-down-bit is specified, the direct routes that have already leaked to a Level-1 area cannot leak back. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The ipv6 import-route isis level-2 into level-1 command must be configured on Level-1-2 devices at the area border.The ipv6 import-route isis level-2 into level-1 command takes effect only after IPv6 is enabled for the IS-IS process. For details, see isis ipv6 enable.

**Precautions**

This command takes effect only on Level-1-2 devices.For the routing policy used in this command, only if-match clauses can be configured to set matching rules, and apply clauses cannot be configured to set route attributes.When locator routes are leaked between IS-IS levels or imported between processes, locator TLVs are advertised in the target area by default. This behavior may affect path calculation of devices in the target area. You can use segment-routing ipv6 locator-inter-area disable to eliminate the impact.When configuring route-policy route-policy-name in this command, the following items can be matched: the outbound interface, route cost, route type, route tag, IPv6 route next-hop ACL, IPv6 route next-hop prefix list, and routing protocol type. No action can be set.If the referenced policy contains unsupported attribute matching or setting an action, unexpected results may occur.


Example
-------

# Enable IPv6 route leaking from a Level-2 area to a Level-1 area.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2002
[*HUAWEI-acl6-basic-2002] quit
[*HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 import-route isis level-2 into level-1 filter-policy 2002

```