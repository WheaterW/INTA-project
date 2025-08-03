import-route isis level-2 into level-1 (IS-IS view)
===================================================

import-route isis level-2 into level-1 (IS-IS view)

Function
--------



The **import-route isis level-2 into level-1** command enables a Level-1-2 device to leak IS-IS routes from a Level-2 area to a Level-1 area.

The **undo import-route isis level-2 into level-1** command disables IS-IS route leaking from a Level-2 area to a Level-1 area.



By default, IS-IS route leaking is disabled from a Level-2 area to a Level-1 area.


Format
------

**import-route isis level-2 into level-1** [ **tag** *tag* | **filter-policy** { *acl-number* | **acl-name** *acl-name* | **ip-prefix** *ip-prefix-name* | { **route-policy** *route-policy-name* } } | **direct** { **allow-filter-policy** | **allow-up-down-bit** } \* ] \*

**undo import-route isis level-2 into level-1**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tag** *tag* | Specifies the administrative tag assigned to the imported routes. | The value is an integer ranging from 1 to 4294967295. |
| **filter-policy** | Specifies a route filtering rule.  Only the IS-IS Level-2 area routes that match the filtering policy can leak to a Level-1 area. | - |
| *acl-number* | Specifies the number of a basic ACL. Only the IS-IS Level-2 area routes that match the ACL rule can leak to a Level-1 area. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name* | Specifies the name of a named basic ACL. Only the IS-IS Level-2 area routes that match the ACL rule can leak to a Level-1 area. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. Only the IS-IS Level-2 area routes that match the IP prefix list can leak to a Level-1 area. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. Only the IS-IS Level-2 area routes that match the route-policy can leak to a Level-1 area. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **direct** | Configures the device to import direct routes. | - |
| **allow-filter-policy** | Applies a filtering policy to the direct routes to be leaked.  If this parameter is specified, only the Level-2 direct routes that match the filtering policy can leak to a Level-1 area. If this parameter is not configured, all direct routes in a Level-2 area can leak to a Level-1 area. | - |
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

When multiple Level-1-2 routers in an Level-1 area are connected to a Level-2 area, Level-1 routers are unable to know the network topology of the Level-2 area because they cannot learn the Level-2 routes. As a result, Routers in the Level-1 area forward traffic to the nearest Level-1-2 router, and sub-optimal routes may be generated.To address this problem, you can run the import-route isis level-2 into level-1 command to enable IS-IS route leaking from a Level-2 area to a Level-1 area to help Level-1 routers select the optimal route for traffic forwarding.The import-route isis level-2 into level-1 command can be run only on Level-1-2 routers to enable IS-IS route leaking of all or some of the Level-2 routes to the Level-1 area.

**Prerequisites**



An IS-IS process has been created using the **isis** command.



**Configuration Impact**



The imported Level-2 routes will increase the number of entries in Level-1 routing tables.



**Precautions**



For the routing policy used in this command, only if-match clauses can be configured to set matching rules, and apply clauses cannot be configured to set route attributes.When configuring route-policy route-policy-name in this command, the following items can be matched: the outbound interface, ACL list of the next hop address of IP routing information, ACL list of the next hop address of IP routing information, route cost, route type, route tag, and routing protocol type. You cannot set the action.If the referenced policy contains unsupported attribute matching or setting an action, unexpected results may occur.




Example
-------

# Use a route-policy to control IS-IS route leaking from a Level-2 area to a Level-1 area.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] isis 1
[*HUAWEI-isis-1] import-route isis level-2 into level-1 filter-policy route-policy policy1

```