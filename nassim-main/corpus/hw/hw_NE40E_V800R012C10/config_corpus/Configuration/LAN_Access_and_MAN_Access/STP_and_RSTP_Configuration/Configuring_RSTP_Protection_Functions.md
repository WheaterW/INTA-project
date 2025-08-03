Configuring RSTP Protection Functions
=====================================

Rapid Spanning Tree Protocol (RSTP) protection functions are as follows, and you can configure one or more functions as required.

#### Applicable Environment

RSTP provides the following protection functions, as listed in [Table 1](#EN-US_TASK_0172363552__tab_dc_vrp_stp_cfg_0003_01).

**Table 1** RSTP Protection Function
| Protection Function | Scenario | Configuration Impact |
| --- | --- | --- |
| BPDU protection | An edge port changes to be a non-edge port after receiving a BPDU, which triggers spanning tree recalculation. If an attacker keeps sending bogus BPDUs to a device, network flapping occurs. | After BPDU protection is enabled on the device, the device shuts down the edge port if the edge port receives an RST BPDU, and notifies the NMS of the shutdown event. The attributes of the edge port are not changed. |
| TC protection | Generally, after receiving TC BPDUs (packets for advertising network topology changes), a device needs to delete MAC entries and ARP entries. Frequent deletion operations will exhaust CPU resources. | TC protection is used to suppress TC-BPDUs. The number of times that TC-BPDUs are processed by a device within a given time period is configurable. If the number of TC-BPDUs that the device receives within a given time exceeds the specified threshold, the device handles TC-BPDUs only for the specified number of times. Excess TC-BPDUs are processed by the device as a whole for once after the timer (that is, the specified time period) expires. This protects the device from frequently deleting MAC entries and ARP entries, thus avoiding over-burdened. |
| Root protection | Due to incorrect configurations or malicious attacks on the network, a root bridge may receive BPDUs with a higher priority. Consequently, the legitimate root bridge is no longer able to serve as the root bridge, and the network topology is illegitimately changed, triggering spanning tree recalculation. This may transfer traffic from high-speed links to low-speed links, causing traffic congestion. | If a designated port is enabled with the root protection function, the role of the port cannot be changed. Once a designated port that is enabled with root protection receives RST BPDUs with a higher priority, the port enters the Discarding state and does not forward packets. If the port does not receive any RST BPDUs with a higher priority before a period (generally two Forward Delay periods) expires, the port automatically enters the Forwarding state. |
| Loop protection | A root port or an alternate port will age if link congestion or a one-way link failure occurs. After the root port ages, a device may re-select a root port incorrectly and after the alternate port ages, the port enters the Forwarding state. Loops may occur in such a situation. | After loop protection is configured, if the root port or alternate port does not receive RST BPDUs from the upstream device for a long time, the device notifies the NMS that the port enters the Discarding state. The blocked port remains in the Blocked state and no longer forwards packets. This prevents loops on the network. The root port restores the Forwarding state after receiving new BPDUs. |
| Abnormal packet filtering | On a network running STP, RSTP, or MSTP, a device may receive unexpected STP, RSTP, or MSTP BPDUs due to incorrect configurations or malicious network attacks. If these unexpected packets are transparently transmitted on the network, spanning tree calculation may be affected, causing network flapping. | After the function to filter abnormal packets is enabled, the device discards the packets carrying a specified source MAC address or VLAN ID. In this manner, unexpected packets are not transparently transmitted on the network, preventing network flapping. |



#### Pre-configuration Tasks

Before configuring basic RSTP functions, complete the following task:

* [Configuring basic RSTP functions](dc_vrp_stp_cfg_0004.html)
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configuring an edge port on the device before configuring bridge protocol data unit (BPDU) protection.


[Configuring BPDU Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0019.html)

After bridge protocol data unit (BPDU) protection is enabled on a device, the device shuts down an edge port if the edge port receives a BPDU and notifies the NMS of the shutdown event.

[Configuring TC Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0020.html)

After Topology Change (TC) protection is enabled, you can set the number of times for a device to process TC Bridge Protocol Data Units (BPDUs) within a specified time. TC protection avoids frequent deletion of MAC address entries and ARP entries, thereby protecting devices.

[Configuring TC/TCN Packet Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0037.html)

If TC/TCN packets do not need to be flooded, you can enable TC/TCN packet suppression.

[Configuring Root Protection on a Port](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0021.html)

The root protection function on a device protects a root bridge by preserving the role of a designated port.

[Configuring Loop Protection on a Port](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0022.html)

The loop protection function suppresses the loops caused by link congestion.

[Configuring Abnormal Packet Filtering](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0035.html)

You can configure the device to process or discard specified packets in order to filter unexpected packets.

[Verifying the RSTP Protection Function Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0023.html)

After Rapid Spanning Tree Protocol (RSTP) protection functions are configured, verify the configuration.