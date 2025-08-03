ping vxlan
==========

ping vxlan

Function
--------



The **ping vxlan** command checks VXLAN connectivity.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ping vxlan** [ **-c** *count* | **-m** *interval* | **-t** *timeout* | **-r** *replymode* | **-a** *innersrc-address6* ] \* **ipv6** **vni** *vniid* **source** *source-address6* **peer** *dest-address6* [ **udp-port** *dest-port* ] [ **load-balance** { **vxlan-source-udpport** *vxlan-source-udpport* [ *vxlan-source-end-udpport* ] | { **source-address** *lb-src-address* **destination-address** *lb-dst-address* **protocol** { **udp** | *lb-protocolid* } **source-port** *lb-src-port* **destination-port** *lb-dst-port* **source-mac** *source-mac* **destination-mac** *destination-mac* } } ]

**ping vxlan** [ **-c** *count* | **-m** *interval* | **-t** *timeout* | **-r** *replymode* | **-a** *innersrc-address* | **-tos** *tos* ] \* **vni** *vniid* **source** *source-address* **peer** *dest-address* [ **udp-port** *dest-port* ] [ **load-balance** { **vxlan-source-udpport** *vxlan-source-udpport* [ *vxlan-source-end-udpport* ] | { **source-address** *lb-src-address* **destination-address** *lb-dst-address* **protocol** { **udp** | *lb-protocolid* } **source-port** *lb-src-port* **destination-port** *lb-dst-port* **source-mac** *source-mac* **destination-mac** *destination-mac* } } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **-c** *count* | Specifies the number of times that echo request packets are to be sent.  If the network quality is low, you can increase the parameter value to determine the network quality based on the packet loss rate. | The value is an integer ranging from 1 to 4294967295. The default value is 5. |
| **-m** *interval* | Specifies the time to wait before the next echo request packet is sent. | The value is an integer ranging from 1 to 10000, in milliseconds. The default value is 500. |
| **-t** *timeout* | Specifies the timeout period for waiting for an echo request packet. | The value is an integer ranging from 0 to 65535. The default value is 2000. |
| **-r** *replymode* | Specifies the mode in which the peer responds with echo reply messages. | The value is 1, 2, or 3.  Each mode is described as follows:  1: do not reply  2: reply with an IPv4 or IPv6 UDP packet  3: reply through the control channel of the application plane  The default value is 2. |
| **-a** *innersrc-address* | Specifies an inner source IP address. | The value is in dotted decimal notation. |
| *innersrc-address6* | Specifies an inner source IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| **ipv6** | Configures a rule for IPv6 packets. | - |
| **vni** *vniid* | Specifies a VXLAN network indicator (NI). | The value is an integer ranging from 1 to 16777215. |
| **source** *source-address* | Indicates source IPv4 address. | The value is in dotted decimal notation. |
| *source-address6* | Specifies a source IPv6 address for a VXLAN tunnel. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| **peer** *dest-address* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *dest-address6* | Specifies a peer IPv6 address for a VXLAN tunnel. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| **udp-port** *dest-port* | Specifies a destination UDP port number. | The value is an integer ranging from 1 to 65535. |
| **load-balance** | Indicates load balancing. | - |
| **vxlan-source-udpport** *vxlan-source-udpport* | Specifies a start source port number or VXLAN packets. | The value is an integer ranging from 49152 to 65535. |
| *vxlan-source-end-udpport* | Specifies an end source port number for VXLAN packets. | The value is an integer ranging from 49152 to 65535. |
| **source-address** *lb-src-address* | Specifies a load balance source IPv4 address. | The value is in dotted decimal notation. |
| **destination-address** *lb-dst-address* | Specifies a load balance destination IPv4 address. | The value is in dotted decimal notation. |
| **protocol** | Specify a protocol type. | - |
| **udp** | Indicates the UDP protocol type. | - |
| *lb-protocolid* | Specify a protocol number. | The value is an integer ranging from 1 to 255. |
| **source-port** *lb-src-port* | Specifies a load balance source port number. | The value is an integer ranging from 1 to 65535. |
| **destination-port** *lb-dst-port* | Specifies a load balance destination port number. | The value is an integer ranging from 1 to 65535. |
| **source-mac** *source-mac* | Specifies a source MAC address. | The value is in the format of H-H-H. |
| **destination-mac** *destination-mac* | Specifies the destination MAC address. | The value is in the format of H-H-H. |
| **-tos** *tos* | Specifies the priority of an echo request packet to be sent. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

All views


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

**Usage Scenario**

To detect a VXLAN tunnel fault, run the **ping vxlan** command. In practice, if a fault occurs on a VXLAN forwarding path, causing traffic on a VXLAN tunnel to be interrupted, you can use the ping vxlan and **tracert vxlan** commands to detect and locate the faulty node.The **tracert vxlan** command uses both vxlanecho request packets and vxlanecho reply packets to check VXLAN connectivity. Packets are transmitted in the UDP format, and the port number can be configured. The receiver distinguishes vxlanecho request and vxlanecho reply packets according to the UDP port number. A vxlanecho request packet carries FEC information to be detected, and is sent along the same VXLAN tunnel as other packets carrying the same FEC information. In this manner, VXLAN connectivity is checked. Vxlanecho request packets are transmitted to the destination through VXLAN, whereas vxlanecho reply packets are transmitted to the source through IP.If a fault occurs when a VXLAN tunnel is detected using the **ping vxlan** command, and packets transmitted along this VXLAN tunnel cannot reach the egress, you can run the **tracert vxlan** command to locate the fault. Both the ping vxlan and **tracert vxlan** commands can check VXLAN connectivity and locate faults.

**Prerequisites**

Basic VXLAN configurations have been complete.The **nqa vxlanecho enable** command has been run on the responder to enable the VXLAN ping/tracert function.

**Precautions**

By default, the source IP address used to perform a ping or tracert operation on a VXLAN network is on the underlay network. If you are not sure whether there is a route from the remote end to the local end, specify the -a parameter to configure the IP address of the tunnel as the source IP address.


Example
-------

# Check IPv6 VXLAN tunnel connectivity.
```
<HUAWEI> ping vxlan ipv6 vni 60 source 2001:DB8:1::1 peer 2001:DB8:2::1
PING VXLAN IPV6: vni 60 source 2001:DB8:1::1 peer 2001:DB8:2::1, press CTRL_C to break
    Reply from 2001:DB8:2::1 
    bytes=52 Sequence=1 time=167 ms
    Reply from 2001:DB8:2::1 
    bytes=52 Sequence=2 time=2 ms
    Reply from 2001:DB8:2::1 
    bytes=52 Sequence=3 time=1 ms
    Reply from 2001:DB8:2::1 
    bytes=52 Sequence=4 time=2 ms
    Reply from 2001:DB8:2::1 
    bytes=52 Sequence=5 time=2 ms

  --ping vxlan statistics--
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 1/34/167 ms

```

# Check IPv4 VXLAN tunnel connectivity.
```
<HUAWEI> ping vxlan vni 111 source 10.1.1.1 peer 10.2.2.1 udp-port 5001
PING VXLAN: vni 111 source 10.1.1.1 peer 10.2.2.1, press CTRL_C to break
    Reply from 10.2.2.1 bytes=52 Sequence=1 time=3 ms
    Reply from 10.2.2.1 bytes=52 Sequence=2 time=3 ms
    Reply from 10.2.2.1 bytes=52 Sequence=3 time=2 ms
    Reply from 10.2.2.1 bytes=52 Sequence=4 time=3 ms
    Reply from 10.2.2.1 bytes=52 Sequence=5 time=3 ms

  --- ping vxlan statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 2/2/3 ms

```

**Table 1** Description of the **ping vxlan** command output
| Item | Description |
| --- | --- |
| PING VXLAN | Checks VXLAN connectivity. |
| press CTRL\_C to break | You can press CTRL+C to stop the ongoing ping test. |
| Reply from x.x.x.x | Response from the destination host to each echo request packet, including:   * bytes: length of an echo reply packet. * Sequence: sequence number of an echo reply packet. * time: delay after which the destination host responds to an echo reply packet, in ms.   If no echo reply packet is received before the timeout period expires, "Request time out" is displayed. |
| --- ping vxlan statistics --- | VXLAN ping test statistics, including:   * packet(s) transmitted: number of sent Echo Request packets. * packet(s) received: number of received Echo Reply packets. * % packet loss: percentage of the number of packets with no responses to the total number of packets with responses. * round-trip min/avg/max: minimum, average, or maximum response time, in ms. |