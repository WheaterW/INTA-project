multicast ipv6 boundary
=======================

multicast ipv6 boundary

Function
--------



The **multicast ipv6 boundary** command configures an IPv6 multicast forwarding boundary on an interface.

The **undo multicast ipv6 boundary** command deletes the configured IPv6 multicast forwarding boundary from an interface.



By default, no IPv6 multicast forwarding boundary is configured on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast ipv6 boundary** *ipv6-group-address* *ipv6-group-mask-length*

**undo multicast ipv6 boundary** *ipv6-group-address* *ipv6-group-mask-length*

**undo multicast ipv6 boundary all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-group-address* | Specifies an IPv6 multicast group address. | The value ranges from FF00::0 to FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF, in hexadecimal notation. |
| *ipv6-group-mask-length* | Specifies the mask length of an IPv6 multicast group address. | The value is an integer ranging from 8 to 128. |
| **all** | Deletes all the IPv6 multicast forwarding boundaries configured on an interface. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **multicast ipv6 boundary** command is used to configure an IPv6 multicast forwarding boundary to set the forwarding range for IPv6 multicast data packets.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

To configure multiple IPv6 multicast forwarding boundaries for different multicast groups on an interface, run this command on the interface for several times.

**Precautions**

Assume that A and B are two multicast group ranges to be configured with IPv6 multicast forwarding boundaries, and B is a subset of A. If A is first configured on an interface, B cannot be configured. If B is configured on the interface first and then A is configured, the configuration of B is substituted by that of A.


Example
-------

# Configure 100GE1/0/1 as the boundary of multicast group FF02::101/16.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] multicast ipv6 boundary FF02::101 16

```