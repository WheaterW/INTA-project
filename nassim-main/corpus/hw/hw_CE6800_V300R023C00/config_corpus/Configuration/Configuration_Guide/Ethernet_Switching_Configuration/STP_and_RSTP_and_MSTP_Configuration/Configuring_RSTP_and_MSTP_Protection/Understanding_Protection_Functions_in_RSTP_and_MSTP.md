Understanding Protection Functions in RSTP/MSTP
===============================================

Understanding Protection Functions in RSTP/MSTP

#### BPDU Protection

In [Figure 1](#EN-US_CONCEPT_0000001291918968__fig781314151104), the port connecting DeviceC to a PC is configured as an edge port. When the edge port receives BPDUs, DeviceC automatically sets it to a non-edge port and performs spanning tree recalculation. If the bridge priority in the BPDUs sent by an attacker is higher than the priority of the root bridge, the network topology will change, thereby interrupting service traffic. This is known as a Denial of Service (DoS) attack.

If this situation occurs after BPDU protection is enabled on DeviceC, DeviceC sets the edge port to the error-down state, while keeping the port attributes unchanged.

**Figure 1** BPDU protection  
![](figure/en-us_image_0000001345158197.png "Click to enlarge")

#### TC Protection

A device deletes its MAC address entries and ARP entries after receiving TC BPDUs. If an attacker sends a large number of forged TC BPDUs to the device within a short period, the device frequently deletes these entries, increasing the device load and affecting network stability.

After enabling TC protection on a device, you can set the number of TC BPDUs that the device can process within a specified period. If this number exceeds the specified threshold, the device processes only the specified number of TC BPDUs. After the time period, the device processes all the excess TC BPDUs together. This prevents the device from frequently deleting MAC address entries and ARP entries, reducing the device load.


#### Root Protection

The root bridge on a network may receive superior BPDUs due to incorrect configurations or malicious attacks. If this occurs, the root bridge can no longer function and the network topology will change incorrectly. As a result, traffic may be switched from high-rate links to low-rate links, leading to network congestion.

In [Figure 2](#EN-US_CONCEPT_0000001291918968__fig661335316334), DeviceA and DeviceB are deployed at the core layer of the network. The bandwidth of the link between these two devices is 100 Gbit/s. DeviceA is the root bridge on the network. DeviceC is deployed at the access layer. The bandwidth of the links between DeviceC and DeviceA and between DeviceC and DeviceB is 10 Gbit/s. Normally, the link between DeviceB and DeviceC is blocked. When a new device, DeviceD, is deployed and connected to DeviceC, DeviceD is elected as the new root bridge because it has a higher bridge priority than DeviceA. If the 100 Gbit/s link between DeviceA and DeviceB is blocked, VLAN traffic is transmitted through the two 10 Gbit/s links. As a result, network congestion and traffic loss may occur.

**Figure 2** Root protection  
![](figure/en-us_image_0000001292078988.png "Click to enlarge")

In this case, root protection can be configured on the port of DeviceC connected to DeviceD. If root protection is enabled on a designated port, the port role cannot be changed. When the designated port receives a superior BPDU, it enters the Discarding state and does not forward packets. If the port does not receive any superior BPDUs within a specified period (twice the Forward Delay timer value by default), it automatically enters the Forwarding state.

Root protection takes effect only on designated ports.


#### Loop Prevention

On a network running a spanning tree protocol, a device maintains the root port and blocked port states based on BPDUs received from upstream devices. However, if the ports cannot receive BPDUs from upstream devices because of link congestion or unidirectional link failures, the device re-selects a root port. In this case, the original root port becomes a designated port, and the original blocked port changes to the Forwarding state, which may cause network loops. In [Figure 3](#EN-US_CONCEPT_0000001291918968__fig89751225192816), when the link between BP 2 and CP 1 is congested, the root port CP 1 on DeviceC cannot receive BPDUs from the upstream device. After a specified period, the alternate port CP 2 becomes the root port, and CP 1 becomes the designated port, resulting in a loop.

**Figure 3** Topology change upon link congestion  
![](figure/en-us_image_0000001345238593.png "Click to enlarge")

If the root port or alternate port does not receive BPDUs from the upstream device for a long time, the device enabled with loop prevention sends a notification to the NMS. In this case, the root port enters the Discarding state and becomes the designated port, while the alternate port remains blocked and becomes the designated port. This prevents loops. After link congestion is cleared or unidirectional link failures are rectified, the port receives BPDUs for negotiation and restores its original role and status.

Loop prevention takes effect only on the root port and alternate ports.


#### Shared Link Protection

Shared link protection is used in the scenario where a device is dual-homed to a network.

On an MSTP network, when a shared link fails, shared link protection forcibly changes the working mode of a local device to RSTP, which can also be used together with root protection to avoid network loops.