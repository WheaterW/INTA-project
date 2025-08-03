preference (IS-IS view)
=======================

preference (IS-IS view)

Function
--------



The **preference** command sets a priority for IS-IS.

The **undo preference** command restores the default value.



By default, the priority of IS-IS is 15.


Format
------

**preference** { { **route-policy** *route-policy-name* } | *preference* } \*

**undo preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *preference* | Specifies a priority of the IS-IS protocol. The smaller the value, the higher the priority. | The value is an integer that ranges from 1 to 255. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Multiple dynamic routing protocols may be run on a device, and routes discovered by various routing protocols to the same destination may exist. In this case, you can use the **preference** command to set a default priority for each routing protocol. If different protocols have routes to the same destination, the protocol with the highest priority is selected for IP packet forwarding.The **preference** command sets a priority for IS-IS or some IS-IS routes. The **preference** command is used in the following three ways:

* The **preference** command sets a priority for all IS-IS routes.
* The preference preference route-policy route-policy-name or preference route-policy route-policy-name **preference** command sets different priorities for matched and unmatched routes.
* The preference route-policy route-policy-name command sets a priority only for matched routes.

**Prerequisites**



An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.



**Precautions**

If the apply **preference** command is configured in a route-policy, the preference values of routes are as follows:

* For matched routes, the preference value set using the apply **preference** command is used.
* For unmatched routes, the preference value set using the **preference** command is used.In the following example, the preference value of the routes that match the route-policy abc is set to 50, and the preference value of the routes that do not match the route-policy abc is set to 30.#route-policy abc permit node 1if-match cost 20apply preference 50#isis 1preference 30 route-policy abcIf the apply preference 50 command is not configured in the route-policy abc, the preference values of all routes are set to 30.Multiple dynamic routing protocols may run on a device at the same time. Therefore, routing information needs to be shared and selected among the routing protocols. The system sets a preference value for each routing protocol. When different protocols discover routes to the same destination, the route with the highest priority (smallest preference value) is selected.


Example
-------

# Set the priority of IPv4 IS-IS to 25.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] preference 25

```