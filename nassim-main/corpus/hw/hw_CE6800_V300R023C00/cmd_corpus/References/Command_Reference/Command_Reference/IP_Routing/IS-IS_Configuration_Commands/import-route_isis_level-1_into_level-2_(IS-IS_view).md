import-route isis level-1 into level-2 (IS-IS view)
===================================================

import-route isis level-1 into level-2 (IS-IS view)

Function
--------



The **import-route isis level-1 into level-2** command enables IS-IS Level-1 area routes to leak to a Level-2 area.

The **undo import-route isis level-1 into level-2** command disables IS-IS Level-1 area routes from leaking to a Level-2 area.

The **import-route isis level-1 into level-2 disable** command disables IS-IS Level-1 area routes from leaking to a Level-2 area.

The **undo import-route isis level-1 into level-2 disable** command enables IS-IS Level-1 area routes to leak to a Level-2 area.



By default, all the Level-1 area routes (except default routes) can leak to a Level-2 area.


Format
------

**import-route isis level-1 into level-2** [ **tag** *tag-value* | **filter-policy** { *acl-number* | **acl-name** *acl-name-value* | **ip-prefix** *ip-prefix-name* | { **route-policy** *route-policy-name* } } | **direct** **allow-filter-policy** ] \*

**import-route isis level-1 into level-2 disable**

**undo import-route isis level-1 into level-2**

**undo import-route isis level-1 into level-2** { **tag** *tag-value* | **filter-policy** { *acl-number* | **acl-name** *acl-name-value* | **ip-prefix** *ip-prefix-name* | **route-policy** *route-policy-name* } | **direct** **allow-filter-policy** } \*

**undo import-route isis level-1 into level-2 disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tag** *tag-value* | Specifies the administrative tag assigned to the imported routes. | The value is an integer ranging from 1 to 4294967295. |
| **filter-policy** | Indicates a filtering policy to filter imported routes. Only the IS-IS Level-1 area routes that match the filtering policy can leak to a Level-2 area. | - |
| *acl-number* | Specifies the number of a basic ACL. Only the IS-IS Level-1 area routes that match the ACL rule can leak to a Level-2 area. | The value is an integer ranging from 2000 to 2999. |
| **acl-name** *acl-name-value* | Specifies the name of a named basic ACL. Only the IS-IS Level-1 area routes that match the ACL rule can leak to a Level-2 area. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **ip-prefix** *ip-prefix-name* | Specifies the name of an IP prefix list. Only the IS-IS Level-1 area routes that match the IP prefix list can leak to a Level-2 area. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. Only the IS-IS Level-1 area routes that match the route-policy can leak to a Level-2 area. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **direct** | Configures the device to import direct routes. | - |
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

When multiple Level-1-2 devices in an IS-IS Level-1 area are connected to a Level-2 area, information about all the routes except the default route in the Level-1 area leak to the Level-2 area. The routes in the Level-1 area destined for one device in the Level-2 area may be forwarded by the same Level-1-2 device, causing traffic imbalance.You can run the **import-route isis level-1 into level-2** command on one Level-1-2 device to enable some Level-1 routes to leak to the Level-2 area and run the command on other Level-1-2 devices to enable the rest Level-1 routes to leak to the Level-2 area. Then, traffic that is sent from the Level-2 area and destined for different network segments in the Level-1 area will be forwarded to different Level-1-2 routers.

**Prerequisites**



An IS-IS process has been created using the **isis** command.



**Configuration Impact**



After the undo **import-route isis level-1 into level-2** command is run, the IS-IS backbone area cannot obtain the routes in the Level-1 area, causing area disconnection.



**Precautions**



For the routing policy used in this command, only if-match clauses can be configured to set matching rules, and apply clauses cannot be configured to set route attributes.When configuring route-policy route-policy-name in this command, the following items can be matched: the outbound interface, ACL list of the next hop address of IP routing information, ACL list of the next hop address of IP routing information, route cost, route type, route tag, and routing protocol type. You cannot set the action.If the referenced policy contains unsupported attribute matching or setting an action, unexpected results may occur.




Example
-------

# Use a route-policy to control route leaking from a Level-1 area to a Level-2 area.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] isis 1
[*HUAWEI-isis-1] import-route isis level-1 into level-2 filter-policy route-policy policy1

```