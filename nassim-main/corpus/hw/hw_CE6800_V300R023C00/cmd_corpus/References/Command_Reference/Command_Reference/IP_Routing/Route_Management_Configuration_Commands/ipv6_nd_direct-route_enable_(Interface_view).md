ipv6 nd direct-route enable (Interface view)
============================================

ipv6 nd direct-route enable (Interface view)

Function
--------



The **ipv6 nd direct-route enable** command configures IPv6 NDP Vlink direct route advertisement.

The **undo ipv6 nd direct-route enable** command disables IPv6 NDP Vlink direct route advertisement.



By default, IPv6 NDP Vlink direct routes are not advertised.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd direct-route enable** [ **route-policy** *name* ]

**undo ipv6 nd direct-route enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *name* | Specifies a route-policy for filtering IPv6 NDP Vlink direct routes. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,VLAN range view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device connects to two IPv6 sites (Site 1 and Site 2). The device and its peer run a dynamic routing protocol. To allow its peer to learn routes destined for Site 1 and Site 2, run the **ipv6 nd direct-route enable** command on the device to configure interfaces to advertise IPv6 NDP Vlink direct routes, and then configure a dynamic routing protocol to import the direct routes.

**Prerequisites**



If this function is to be enabled in the interface view, IPv6 has been enabled using the **ipv6 enable** command. If this function is to be enabled on the 100GE or Eth-Trunk sub-interface, the sub-interface has been enabled to terminate single-tagged packets using the **dot1q termination vid** command.



**Configuration Impact**

If route-policy is configured to filter IPv6 NDP Vlink direct routes, only eligible routes can be advertised.

**Follow-up Procedure**

After configuring IPv6 NDP Vlink direct route advertisement, import the IPv6 NDP Vlink direct routes to a dynamic routing protocol so that they can be advertised.

**Precautions**

A route-policy must be created to filter routes. For details, see "Configuring a Route-Policy".Once the **undo ipv6 enable** command is run in the interface view to disable IPv6, the configuration of the **ipv6 nd direct-route enable** command is also deleted. Exercise caution when using the **undo ipv6 enable** command.


Example
-------

# Configure a specified VLANIF interface to advertise IPv6 NDP Vlink direct routes.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] quit
[*HUAWEI] interface vlanif 100
[*HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] ipv6 nd direct-route enable

```