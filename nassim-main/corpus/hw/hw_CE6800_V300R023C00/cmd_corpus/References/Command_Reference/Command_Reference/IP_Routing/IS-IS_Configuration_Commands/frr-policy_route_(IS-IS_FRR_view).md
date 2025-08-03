frr-policy route (IS-IS FRR view)
=================================

frr-policy route (IS-IS FRR view)

Function
--------



The **frr-policy route** command filters IS-IS backup routes before the routes are added to the IP routing table.

The **undo frr-policy route** command cancels the filtering function.



By default, the filtering function is disabled.


Format
------

**frr-policy route** { **route-policy** *route-policy-name* }

**undo frr-policy route**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of a route policy to filter IS-IS backup routes. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

IS-IS FRR view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

With the development of networks, Voice over Internet Protocol (VoIP) and on-line video services require high-quality real-time transmission. Nevertheless, if an IS-IS fault occurs, multiple processes, including fault detection, LSP update, LSP flooding, route calculation, and FIB entry delivery, must be performed to switch the traffic to a new link. As a result, it takes much more than 50 ms to rectify the fault, unable to meet the requirement for real-time services.The **frr-policy route** command can be configured as required. In this case, the IS-IS backup route matching specified rules can be added to the IP routing table and delivered to the forwarding table. When a fault occurs on the route, the system can fast switch the forwarded traffic to the IS-IS backup route to protect the traffic.You can use IP prefix lists or ACLs to filter the IS-IS backup routes.

**Prerequisites**

An IS-IS instance has been created, and fast reroute has been enabled.

**Precautions**

In the isis-frr view, if route-policy route-policy-name is specified in this command, the following items can be matched: the outbound interface, ACL list of the next hop address of IP routing information, prefix list of the next hop address of IP routing information, route cost, route type, route tag, routing protocol type, and route priority. No action can be set.If route-policy route-policy-name is specified in the command in the IS-IS IPv6 FRR view, the following items can be matched: the outbound interface, ACL list of the next hop address of IP routing information, prefix list of the next hop address of IP routing information, route cost, route type, route tag, routing protocol type, and route priority. No action can be set.If the referenced policy contains unsupported attribute matching or setting an action, unexpected results may occur.


Example
-------

# Configure IS-IS to add the IS-IS backup routes that match the route policy abc to the IP routing table.
```
<HUAWEI> system-view
[~HUAWEI] route-policy abc permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] isis
[*HUAWEI-isis-1] frr
[*HUAWEI-isis-1-frr] frr-policy route route-policy abc

```