Understanding OSPF GTSM
=======================

Understanding OSPF GTSM

#### Definition

The Generalized TTL Security Mechanism (GTSM) protects services over the IP layer by checking whether the time to live (TTL) value in the IP header is within a pre-defined range.


#### Purpose

If an attacker simulates real OSPF packets and keeps sending them to a device, an interface board on the device receives the packets and directly sends them to the control plane for OSPF processing, without checking their validity. As a result, the system becomes unexpectedly busy, and CPU usage becomes excessively high. In such cases, GTSM can be used to solve this problem.

In practice, GTSM is mainly used to protect the TCP/IP-based control plane protocols (such as routing protocols) against CPU-utilization attacks, such as CPU-overload attacks.


#### Fundamentals

A GTSM-enabled device checks the TTL value in each received packet based on a configured policy. Packets that fail to match the GTSM policy will be dropped or sent to the control plane, thereby preventing the receive end from being attacked. A GTSM policy includes:

* Source address of the IP packet sent to the device
* VPN instance to which the packet belongs
* Protocol number of the IP packet (89 for OSPF)
* Source and destination port numbers of protocols over TCP/UDP
* Valid TTL range

GTSM is implemented as follows:

* For protocol-specific neighbor/peer relationships over direct links, the TTL value in each unicast protocol packet to be sent is set to 255.
* For multi-hop OSPF neighbors, a proper TTL range is defined.

The applicability of GTSM is as follows:

* GTSM takes effect on unicast packets, rather than multicast packets. This is because the TTL value of multicast packets cannot exceed 255, avoiding the need for GTSM.
* GTSM does not apply to devices that use a tunnel to establish a neighbor relationship. The CE6885-LL in low latency mode does not support tunnels.