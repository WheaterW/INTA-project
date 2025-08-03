Overview of URPF
================

Overview of URPF

#### Definition

Unicast Reverse Path Forwarding (URPF) defends against network attacks launched through source IP address spoofing.

URPF allows the device to search its Forwarding Information Base (FIB) table for a route to the source IP address of a packet and checks whether the inbound interface of the packet is the same as the outbound interface of the route. If no route to the source IP address exists in the FIB table or the inbound interface of the packet is different from the outbound interface of the matching route, the packet is discarded. This effectively protects the device against malicious attacks that change source IP addresses of packets.


#### Purpose

A Denial of Service (DoS) attack disables users from connecting to a server. Such an attack aims to occupy excessive resources by sending a large number of valid or forged connection requests, preventing authorized users from receiving responses from the server. URPF effectively prevents DoS attacks that use spoofed source IP addresses.

In [Figure 1](#EN-US_CONCEPT_0000001512671586__fig3805131131916), PC\_A sends request packets with the spoofed source IP address 10.2.2.2 to the server. If URPF is disabled on DeviceA, the server sends response packets to PC\_B (with the IP address 10.2.2.2) after receiving the request packets. In this way, PC\_A attacks both the server and PC\_B by sending the request packets. If URPF is enabled on DeviceA, DeviceA checks the inbound interface of the packets received from PC\_A and finds that packets with the source IP address 10.2.2.2 must reach DeviceA through interface 2. Therefore, DeviceA considers that the source IP address of the packets is a spoofed IP address and discards the packets. Packets from PC\_B to the server, in contrast, are allowed to pass through after passing the URPF check.

**Figure 1** Preventing source address spoofing attacks through URPF  
![](figure/en-us_image_0000001563870729.png)