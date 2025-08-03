traffic-analysis tcp export host
================================

traffic-analysis tcp export host

Function
--------



The **traffic-analysis tcp export host** command configures the destination IP address and destination UDP port number for the exported packets that carry intelligent traffic analysis results of TCP flows.

The **undo traffic-analysis tcp export host** command restores the default configuration.



By default, no destination IP address or destination UDP port number is configured for the exported packets that carry intelligent traffic analysis results of TCP flows.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis tcp export host** { **ip** *ip-address* | **ipv6** *ipv6-address* } *port-number* [ **vpn-instance** *vpn-instance-name* ]

**undo traffic-analysis tcp export host** { **ip** *ip-address* | **ipv6** *ipv6-address* } *port-number* [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** *ip-address* | Specifies the destination IPv4 address for the exported packets that carry intelligent traffic analysis results of TCP flows. | The value is in dotted decimal notation. |
| **ipv6** *ipv6-address* | Specifies the destination IPv6 address for the exported packets that carry intelligent traffic analysis results of TCP flows. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *port-number* | Specifies the destination UDP port number for the exported packets that carry intelligent traffic analysis results of TCP flows. | The value is an integer ranging from 1 to 65535. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name for the exported packets that carry intelligent traffic analysis results of TCP flows. | The value must be the name of an existing VPN instance on the switch. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After intelligent traffic analysis for TCP flows is enabled on a switch, the flow tables that contain TCP flow analysis results are first stored on the switch. When a flow table meets the aging conditions, the switch sends the flow table to the specified TDA for further processing and display of flow information. You can run this command to configure the destination IP address, that is, the TDA IP address, to which the exported packets carrying TCP flow analysis results are sent.

**Prerequisites**

You need to run the **ipv4-family** or **ipv6-family** command in the VPN instance view to configure an IP address family.

**Precautions**

* You can configure two destination IP addresses in the system view to implement TDA backup. Before configuring the third destination IP address, run the **undo traffic-analysis tcp export host** { **ip** ip-address | **ipv6** ipv6-address } port-number [ **vpn-instance** vpn-instance-name ] command to delete the original destination TDA address. Otherwise, the system displays a message indicating that the maximum number of destination IP addresses is exceeded and the configuration fails.
* Before this command is executed, the system checks the IPv4 and IPv6 address families for the VPN instance. If no IP address family is configured for the VPN instance, the configuration will be lost after the upgrade. In this case, reconfigure the IP address family in the VPN instance and then run the command again.


Example
-------

# Set the destination IP address to 10.1.1.1 and UDP port number to 222 for the exported packets carrying intelligent traffic analysis results of TCP packets.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis tcp export host ip 10.1.1.1 222

```