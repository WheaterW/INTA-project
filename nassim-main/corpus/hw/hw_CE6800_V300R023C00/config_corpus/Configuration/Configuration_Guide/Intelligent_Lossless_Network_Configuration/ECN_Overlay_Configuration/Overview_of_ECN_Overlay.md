Overview of ECN Overlay
=======================

Overview of ECN Overlay

#### Definition

Explicit Congestion Notification (ECN) Overlay is an ECN application on a VXLAN network.


#### Purpose

ECN is a congestion control technology. When network congestion occurs, an ECN-enabled forwarding device performs ECN marking for packets. The traffic receiver detects whether congestion occurs based on the ECN field in IP packets. If it detects congestion, it notifies the traffic sender through protocol packets so that the traffic sender reduces its packet transmission rate.

The ECN field in an IP packet is used to transmit the congestion status, which may be lost during VXLAN encapsulation and decapsulation of IP packets. To ensure the congestion status information is successfully transmitted to the traffic receiver over a VXLAN network, the ECN Overlay function is applied. This function can also promptly relieve congestion on a VXLAN network and maximize network performance.