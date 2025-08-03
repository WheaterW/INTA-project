preference (OSPF view)
======================

preference (OSPF view)

Function
--------



The **preference** command sets a priority for OSPF routes.

The **undo preference** command restores the default value.



By default, the priority of OSPF routes is 10. When ASE is specified, the default value is 150.


Format
------

**preference** { *preferencevalue* | { **route-policy** *route-policy-name* } } \*

**preference** { **ase** | **intra** | **inter** } { *preferencevalue* | { **route-policy** *route-policy-name* } } \*

**undo preference**

**undo preference** { **ase** | **intra** | **inter** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *preferencevalue* | Specifies a priority of OSPF routes.  The smaller the priority value, the higher the priority. | The value is an integer ranging from 1 to 255. |
| **route-policy** *route-policy-name* | Specifies the name of the route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ase** | Sets a priority for AS external routes. | - |
| **intra** | Sets a priority for intra-area routes. | - |
| **inter** | Sets a priority for inter-area routes. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a device runs multiple dynamic routing protocols at the same time, routing information may be shared and selected among the routing protocols. The system sets a default preference for each routing protocol. If different protocols have routes to the same destination, the route with a higher priority is selected. To set a preference for an OSPF route, run this command.When configuring the route-policy parameter, you can set the preference for matched routes by using the routing policy.

* If the apply preference clause is configured for the route-policy, the route preference is as follows:
* Matched routes: The preference is set by the apply clause.
* Routes that do not match the route-policy: The preference of these routes is the one set using the **preference** command.In the following example, the preference of the routes that match the route-policy abc is set to 50 and the preference of the routes that do not match the route-policy abc is set to 30.route-policy abc permit node 1if-match cost 20apply preference 50ospf 1preference 30 route-policy abc
* If the apply preference clause is not configured in the route-policy, the preference of routes is the one set by the **preference** command.In the above example, if the apply preference 50 clause is not included in the policy abc, the preference of all routes is set to 30.

**Configuration Impact**

When there are routes discovered by multiple routing protocols on the same router, you can enable the router to prefer OSPF routes by setting highest priority for them.

**Precautions**

When a device runs multiple routing protocols at the same time, changing the OSPF preference may change the inter-protocol route selection result in the routing table.


Example
-------

# Set the priority of external routes in OSPF process 200 to 130.
```
<HUAWEI> system-view
[~HUAWEI] ospf 200
[*HUAWEI-ospf-200] preference ase 130

```

# Set the priority of routes in OSPF process 100 to 150.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] preference 150

```