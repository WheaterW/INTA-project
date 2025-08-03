ping arp ip
===========

ping arp ip

Function
--------



The **ping arp ip** command configures a device on a LAN to send ARP packets to check whether an IP address is used by another device.




Format
------

**ping arp ip** *ip-host* [ **interface** { *interface-name* | *interface-type* *interface-number* } [ *vlan-id* *vlanId* ] ] [ **timeout** *timeout* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-host* | Specifies a destination IP address or host name. | If the value is an IP address, it is in dotted decimal notation. If the value is a host name, it is a string of 1 to 255 case-sensitive characters, spaces not supported. |
| **interface** *interface-name* | Specifies the name of the interface that sends ARP packets. | - |
| **interface** *interface-type* *interface-number* | Specifies the interface that sends ARP packets. | - |
| *vlan-id* | Specifies the VLAN to which the interface that sends ARP messages belongs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. If this parameter is not specified, the VLAN ID of 0 is used. When the specified outbound interface is a Layer 2 interface, you must configure vlan-id; when the specified outbound interface is a Layer 3 interface, you cannot configure vlan-id.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. If this parameter is not specified, the VLAN ID of 0 is used. When the specified outbound interface is a Layer 2 interface, you must configure this parameter; when the specified outbound interface is a Layer 3 interface, you cannot configure this parameter. |
| *vlan-id* *vlanId* | Specifies the VLAN to which the interface that sends ARP messages belongs. | The value is an integer ranging from 1 to 4094. If this parameter is not specified, the VLAN ID of 0 is used. When the specified outbound interface is a Layer 2 interface, you must configure vlan-id; when the specified outbound interface is a Layer 3 interface, you cannot configure vlan-id. |
| *vlanId* | Specifies the VLAN to which the interface that sends ARP messages belongs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. If this parameter is not specified, the VLAN ID of 0 is used. When the specified outbound interface is a Layer 2 interface, you must configure vlan-id; when the specified outbound interface is a Layer 3 interface, you cannot configure vlan-id.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. If this parameter is not specified, the VLAN ID of 0 is used. When the specified outbound interface is a Layer 2 interface, you must configure this parameter; when the specified outbound interface is a Layer 3 interface, you cannot configure this parameter. |
| **timeout** *timeout* | Specifies the timeout period of a test when ARP packets are used to detect whether an IP address is being used by another device. This parameter is recommended when the local IP address is to be detected. | The value is an integer ranging from 1 to 10, in seconds. The default value is 3s. |



Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

To use ARP messages to check whether an IP address is used by another devices on a LAN, run this command.Alternatively, you can run the **ping** command to check whether an IP address is used by another device on the network. If the destination host and the Routing device that are enabled with the firewall function are configured not to respond to ping packets, after the **ping** command is run, the destination host and the Router do not respond to the ping packets. Therefore, the initiator mistakenly considers that the IP address is not in use. As ARP is a Layer 2 protocol, in most cases, ARP messages can pass through the firewall of the device that is configured not to respond to ping packets. In this manner, the preceding situation does not occur.In addition, an ARP request message is smaller than an ICMP packet used in ping operations, and therefore running the arp-ping ip command consumes fewer network resources. This command is recommended for IP address detection.

**Prerequisites**

ARP has been enabled, and ARP messages can be properly sent and received.

**Configuration Impact**

If you specify a local IP address or loopback address in the **ping arp ip** command, the probe will fail.

**Precautions**

The **ping arp ip** command cannot be used to detect a local IP address, whereas the **ping** command can.


Example
-------

# Run the ping arp ip command to configure a device to send ARP messages to check whether an IP address is in use.
```
<HUAWEI> ping arp ip 10.1.1.1
ARP-Pinging 10.1.1.1:
10.1.1.1 is used by 00e0-fc91-8d70

```

**Table 1** Description of the **ping arp ip** command output
| Item | Description |
| --- | --- |
| 10.1.1.1 is used by 00e0-fc91-8d70 | Check response:  x.x.x.x: checked target IP address.  xxxx-xxxx-xxxx: MAC address of the responding device. |
| ARP-Pinging | Check whether the IP address is in use. |