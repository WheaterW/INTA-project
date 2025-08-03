ip path detection enable
========================

ip path detection enable

Function
--------



The **ip path detection enable** command enables the IPv4 or IPv6 path detection function.

The **undo ip path detection enable** command disables the IPv4 or IPv6 path detection function.



By default, the IPv4 or IPv6 path detection function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip path detection enable ipv6 dscp** *dscpvalue*

**ip path detection enable dscp** *dscpvalue*

**undo ip path detection enable ipv6 dscp** *dscpvalue*

**undo ip path detection enable dscp** *dscpvalue*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dscp** *dscpvalue* | Specifies a DSCP value. | The value is an integer that ranges from 0 to 63 . |
| **ipv6** | Specifies the IPv6 path detection function. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To use the IPv4 path detection function, a controller, such as iMaster NCE-Fabric is required. The controller sends path detection packets to detect the traffic path between any two VTEPs or VMs, and displays the detection result. iMaster NCE-Fabric delivers the **ip path detection enable** command to the switch through NETCONF to enable path detection. iMaster NCE-Fabric sends the Packet-out message carrying the path detection packet to the switch. The switch calculates the outbound interfaces based on MAC address or routing table, sends the outbound interface, inbound interface, and path detection packet to the controller, and sends the path detection packet out. The controller calculates the entire path through which traffic passes based on the information reported by the switch. If network traffic is interrupted, O&M personnel can quickly locate the faulty device.To use the DSCP-based IPv6 path detection function, a controller, such as iMaster NCE-Fabric is required. This function is applied to detect the traffic path between any two VTEPs or VMs on the IPv6 over IPv4 VXLAN network, and the detection result is displayed on iMaster NCE-Fabric. iMaster NCE-Fabric delivers the **ip path detection enable ipv6 dscp** command to the switch through NETCONF to enable DSCP-based IPv6 path detection, and then iMaster NCE-Fabric sends the Packet-out message carrying the path detection packet to the switch. The switch calculates the outbound interfaces based on MAC address or routing table, sends outbound interfaces, inbound interfaces, and path detection packets to the controller, and sends the path detection packets out. The controller calculates the entire path through which traffic passes based on the information reported by the switch. If network traffic is interrupted, O&M personnel can quickly locate the faulty device.

**Precautions**



The path detection service and IOAM service cannot be configured at the same time.




Example
-------

# Enable the DSCP-based IPv4 path detection function and set the DSCP value to 60.
```
<HUAWEI> system-view
[~HUAWEI] ip path detection enable dscp 60

```

# Enable the DSCP-based IPv6 path detection function and set the DSCP value to 60.
```
<HUAWEI> system-view
[~HUAWEI] ip path detection enable ipv6 dscp 60

```