tracert vxlan
=============

tracert vxlan

Function
--------



The **tracert vxlan** command detects the gateways that packets pass through when traveling from the source host to the destination host on a VXLAN.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tracert vxlan** [ **-t** *timeout* | **-r** *replymode* | **-a** *innersrc-address* | **-h** *maxttl* ] \* **vni** *vniid* **source** *source-address* **peer** *dest-address* [ **udp-port** *dest-port* ] [ **pipe** ] [ **load-balance** { **vxlan-source-udpport** *vxlan-source-udpport* | { **source-address** *lb-src-address* **destination-address** *lb-dst-address* **protocol** { **udp** | *lb-protocolid* } **source-port** *lb-src-port* **destination-port** *lb-dst-port* **source-mac** *lb-sourcemac* **destination-mac** *lb-destinationmac* } } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-t** *timeout* | Specifies the timeout interval for receiving a response packet. | The value is an integer ranging from 0 to 65535. The default value is 2000. |
| **-r** *replymode* | Specifies the mode in which the peer end returns response packets. | The value is 1, 2, or 3.  Each mode is described as follows:  1: do not reply  2: reply with an IPv4 or IPv6 UDP packet  3: reply through the control channel of the application plane  The default value is 2. |
| **-a** *innersrc-address* | Specifies an inner source IPv4 address. | The value is in dotted decimal notation. The default value is the IP address of the outbound interface. |
| **-h** *maxttl* | Specifies the maximum number of hops on a detected path. | The value is an integer ranging from 1 to 255. The default value is 30. |
| **vni** *vniid* | Specifies a VXLAN network indicator (NI). | The value is an integer ranging from 1 to 16777215. |
| **source** *source-address* | Specifies a source IPv4 address for a VXLAN tunnel. | The value is in dotted decimal notation. |
| **source-address** *lb-src-address* | Specifies a load balance source IPv4 address. | The value is in dotted decimal notation. |
| **peer** *dest-address* | Specifies a peer IPv4 address for a VXLAN tunnel. | The value is in dotted decimal notation. |
| **udp-port** *dest-port* | Specifies a destination UDP port number. | The value is an integer ranging from 1 to 65535. |
| **pipe** | Sets the TTL copy mode to pipe. | - |
| **load-balance** | Indicates load balancing. | - |
| **vxlan-source-udpport** *vxlan-source-udpport* | Specifies a source port number for VXLAN packets. | The value is an integer ranging from 49152 to 65535. |
| **destination-address** *lb-dst-address* | Specifies a load balance destination IPv4 address. | The value is in dotted decimal notation. |
| **protocol** | Specifies a protocol type. | - |
| **udp** | Indicates the UDP protocol type. | - |
| *lb-protocolid* | Specifies the protocol number. | The value is an integer ranging from 1 to 255. |
| **source-port** *lb-src-port* | Specifies a load balance source port number. | The value is an integer ranging from 1 to 65535. |
| **destination-port** *lb-dst-port* | Specifies a load balance destination port number. | The value is an integer ranging from 1 to 65535. |
| **source-mac** *lb-sourcemac* | Specifies a load balance source MAC address. | The value is in the format of H-H-H. |
| **destination-mac** *lb-destinationmac* | Specifies a load balance destination MAC address. | The value is in the format of H-H-H. |



Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

To detect a VXLAN tunnel fault, run the **tracert vxlan** command. In practice, if a fault occurs on a VXLAN forwarding path, causing traffic on a VXLAN tunnel to be interrupted, you can use the tracert vxlan and **ping vxlan** commands to detect and locate the faulty node.The **tracert vxlan** command uses both vxlanecho request packets and vxlanecho reply packets to check VXLAN connectivity. Packets are transmitted in the UDP format, and the port number can be configured. The receiver distinguishes vxlanecho request and vxlanecho reply packets according to the UDP port number. A vxlanecho request packet carries FEC information to be detected, and is sent along the same VXLAN tunnel as other packets carrying the same FEC information. In this manner, VXLAN connectivity is checked. Vxlanecho request packets are transmitted to the destination through VXLAN, whereas vxlanecho reply packets are transmitted to the source through IP.If a fault occurs when a VXLAN tunnel is detected using the **ping vxlan** command, and packets transmitted along this VXLAN tunnel cannot reach the egress, you can run the **tracert vxlan** command to locate the fault. Both the tracert vxlan and **ping vxlan** commands can check VXLAN connectivity and locate faults.

**Prerequisites**

Basic VXLAN configurations have been complete.The **nqa vxlanecho enable** command has been run on the responder to enable the VXLAN ping/tracert function.

**Precautions**

By default, the source IP address used to perform a ping or tracert operation on a VXLAN network is on the underlay network. If you are not sure whether there is a route from the remote end to the local end, specify the -a parameter to configure the IP address of the tunnel as the source IP address.


Example
-------

# Locate the IPv4 VXLAN tunnel fault.
```
<HUAWEI> tracert vxlan vni 111 source 1.1.1.1 peer 2.2.2.2 udp-port 5000
TRACERT VXLAN: vni 111 source 1.1.1.1 peer 2.2.2.2, press CTRL_C to break
TTL   Replier            Time    Ingress Port           Egress Port                 
1     10.1.2.2           94 ms   100GE1/0/1              100GE1/0/2  
2     2.2.2.2            94 ms   100GE1/0/1              --

```

**Table 1** Description of the **tracert vxlan** command output
| Item | Description |
| --- | --- |
| TTL | TTL in an echo request packet, indicating the number of hops through which an echo request packet passes from the source node to this node. |
| Replier | IP address of the node sending the echo reply packet. |
| Time | Packet processing time, in ms. |
| Ingress Port | Inbound interface. |
| Egress Port | Outbound interface. |