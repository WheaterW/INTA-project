Understanding Path Detection
============================

Understanding Path Detection

#### Path Detection Function

**Differentiated services code point (DSCP)-based IPv4 path detection**

The device identifies path detection packets based on the detection flag (DSCP value) and detection data (OAM PDU). During DSCP-based IPv4 path detection, iMaster NCE-Fabric delivers IPv4 UDP, TCP, or ICMP packets as the detection packets. [Figure 1](#EN-US_CONCEPT_0000001563874701__fig13021532195013) shows the packet format.

![](public_sys-resources/note_3.0-en-us.png) 

The IPv4 path detection function can detect only the traffic path between any two devices when no tunnel is configured or when a VXLAN tunnel is configured.The CE6820H, CE6820H-K, or CE6820S cannot function as a VTEP when a VXLAN tunnel is configured.

Before using DSCP-based IPv4 path detection, plan an unoccupied DSCP value that will be used to identify detection packets.


**Figure 1** DSCP-based IPv4 path detection packet  
![](figure/en-us_image_0000001564114813.png)

**DSCP-based IPv6 path detection**

During DSCP-based IPv6 path detection, iMaster NCE-Fabric delivers IPv6 UDP, TCP, or ICMP packets as the detection packets. [Figure 2](#EN-US_CONCEPT_0000001563874701__fig15280112311317) shows the packet format. The device identifies path detection packets based on the detection flag (DSCP value) and detection data (OAM PDU).

![](public_sys-resources/note_3.0-en-us.png) 

DSCP-based IPv6 path detection can be used on IPv6 over IPv4 and IPv6 over IPv6 VXLAN networks. The CE6820H, CE6820H-K, or CE6820S cannot function as a VTEP on IPv6 over IPv6 VXLAN networks.

Before using DSCP-based IPv6 path detection, plan an unoccupied DSCP value that will be used to identify detection packets.

The CE6885-LL in low latency mode does not support IPv6 functions.


**Figure 2** DSCP-based IPv6 path detection packet  
![](figure/en-us_image_0000001563994997.png)

#### Path Detection Process

As shown in [Figure 3](#EN-US_CONCEPT_0000001563874701__fig_dc_cfg_path_detection_01), DeviceA and DeviceB are Layer 3 devices on an IP network, DeviceC to DeviceF are VXLAN Layer 3 gateways, DeviceG to DeviceJ are transparent transmission devices on the VXLAN network, and DeviceK to DeviceR are VXLAN Layer 2 gateways; and two physical network zones exist. O&M personnel need to detect the path from VM1 to VM3. Assume that the path is DeviceL -> DeviceG -> DeviceC -> DeviceA -> DeviceE -> DeviceI -> DeviceP -> VM3. The path detection process is as follows:

1. iMaster NCE-Fabric creates a path detection packet based on the configuration where the source IP address is the IP address of VM1 and the destination IP address is the IP address of VM3.
2. iMaster NCE-Fabric sends a packet-out message carrying the path detection packet to DeviceL.
3. When DeviceL receives the packet-out message, it identifies the detection flag in the packet, calculates the outbound interface based on its MAC address table, and sends a packet-in message carrying the outbound interface, inbound interface, and path detection packet to iMaster NCE-Fabric. DeviceL then encapsulates the path detection packet into a VXLAN packet and sends it to DeviceG.
4. When DeviceG receives the VXLAN packet, it calculates the outbound interface based on its MAC address table, and sends a packet-in message carrying the outbound interface, inbound interface, and VXLAN packet to iMaster NCE-Fabric. DeviceG then transparently transmits the VXLAN packet to DeviceC.
5. When DeviceC receives the VXLAN packet, it calculates the outbound interface based on its routing table, and sends a packet-in message carrying the outbound interface, inbound interface, and VXLAN packet to iMaster NCE-Fabric. DeviceC then decapsulates the VXLAN packet to obtain the path detection packet and forwards it to DeviceA.
6. When DeviceA receives the path detection packet, it calculates the outbound interface based on its routing table, and sends a packet-in message carrying the outbound interface, inbound interface, and path detection packet to iMaster NCE-Fabric. DeviceA then forwards the path detection packet to DeviceE.
7. When DeviceE receives the path detection packet, it calculates the outbound interface based on its routing table, and sends a packet-in message carrying the outbound interface, inbound interface, and path detection packet to iMaster NCE-Fabric. DeviceE then encapsulates the path detection packet into a VXLAN packet and sends it to DeviceI.
8. When DeviceI receives the VXLAN packet, it calculates the outbound interface based on its MAC address table, and sends a packet-in message carrying the outbound interface, inbound interface, and VXLAN packet to iMaster NCE-Fabric. DeviceI then transparently transmits the VXLAN packet to DeviceP.
9. When DeviceP receives the VXLAN packet, it calculates the outbound interface based on its MAC address table, and sends a packet-in message carrying the outbound interface, inbound interface, and VXLAN packet to iMaster NCE-Fabric. DeviceP then decapsulates the VXLAN packet to obtain the path detection packet and forwards it to VM3.
10. iMaster NCE-Fabric calculates the entire path from VM1 to VM3 based on the information reported by DeviceL, DeviceG, DeviceC, DeviceA, DeviceE, DeviceI, and DeviceP.

**Figure 3** Path detection diagram  
![](figure/en-us_image_0000001513154722.png)