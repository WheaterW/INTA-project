multicast boundary
==================

multicast boundary

Function
--------



The **multicast boundary** command configures a multicast forwarding boundary on an interface.

The **undo multicast boundary** command deletes the configured multicast forwarding boundary from an interface.



By default, no multicast forwarding boundary is configured on an interface.


Format
------

**multicast boundary** *group-address* { *mask* | *mask-length* }

**undo multicast boundary** *group-address* { *mask* | *mask-length* }

**undo multicast boundary all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Address of a multicast group. | The value is a string case-sensitive characters. It cannot contain spaces. |
| *mask* | Specifies the mask of a multicast group address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a multicast group address. | The value is an integer that ranges from 4 to 32. |
| **all** | Deletes all the IPv6 multicast forwarding boundaries configured on an interface. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **multicast boundary** command is used to configure a multicast forwarding boundary to set the forwarding range for multicast data packets.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

To configure multiple IPv6 multicast forwarding boundaries for different multicast groups on an interface, run this command on the interface for several times.

**Precautions**

Assume that A and B are two multicast group ranges to be configured with multicast forwarding boundaries, and B is a subset of A. If A is first configured on an interface, B cannot be configured. If B is configured on the interface first and then A is configured, the configuration of B is substituted by that of A.Common tunnel interfaces do not support this command. Only the GRE Tunnel interface supports this command.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Configure VLANIF 1 as the boundary of multicast group 239.2.0.0/16.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] multicast boundary 239.2.0.0 16

```