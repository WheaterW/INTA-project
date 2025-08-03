Configuring MSTP Protection Functions
=====================================

Multiple Spanning Tree Protocol (MSTP) protection functions are as follows, and you can configure one or more functions as required.

#### Applicable Environment

MSTP provides the following protection functions, as listed in [Table 1](#EN-US_TASK_0172363635__tab_dc_vrp_mstp_cfg_0003_01).

**Table 1** MSTP protection
| MSTP Protection | Scenario | Configuration Impact |
| --- | --- | --- |
| BPDU protection | An edge port changes to be a non-edge port after receiving a BPDU, which triggers spanning tree recalculation. If an attacker keeps sending bogus BPDUs to a device, network flapping occurs. | After BPDU protection is enabled on the device, the device shuts down the edge port if the edge port receives an RST BPDU, and notifies the NMS of the shutdown event. The attributes of the edge port are not changed. |
| TC protection | Generally, after receiving TC-BPDUs (packets for advertising network topology changes), a device needs to delete MAC entries and ARP entries. Frequent deletion operations will exhaust CPU resources. | TC protection is used to suppress TC-BPDUs. The number of times that TC-BPDUs are processed by a device within a given time period is configurable. If the number of TC-BPDUs that the device receives within the given time exceeds the specified threshold, the device handles TC-BPDUs only for the specified number of times. Excessive TC-BPDUs are processed by the device as a whole for once after the timeout period expires. This protects the device from frequently deleting MAC entries and ARP entries, thus avoiding over-burden. |
| Root protection | Due to incorrect configurations or malicious attacks on the network, a root bridge may receive BPDUs with a higher priority. Consequently, the legitimate root bridge is no longer able to serve as the root bridge, and the network topology is illegitimately changed, triggering spanning tree recalculation. This may transfer traffic from high-speed links to low-speed links, causing traffic congestion. | To address this issue, the root protection function can be configured to protect the root bridge by preserving the role of the designated port. With this function, when the designated port receives RST BPDUs with a higher priority, the port enters the Discarding state and does not forward the BPDUs. If the port does not receive any RST BPDUs with a higher priority for a certain period (double the Forward Delay), the port transitions to the Forwarding state. |
| Loop protection | A root port or an alternate port will age if link congestion or a one-way link failure occurs. After the root port ages, a device may re-select a root port incorrectly and after the alternate port ages, the port enters the Forwarding state. Loops may occur in such a situation. | The loop protection function can be used to prevent such network loops. If the root port or alternate port cannot receive RST BPDUs from the upstream device, the root port is blocked and the device notifies the NMS that the port enters the Discarding state. The blocked port remains in the Blocked state and no longer forwards packets. This prevents loops on the network. The root port restores the Forwarding state after new RST BPDUs are received. |
| Share-link protection | In the scenario where a device is dual-homed to a network, when the share link of multiple processes fails, loops may occur. | Share-link protection can address such a problem. This function forcibly changes the working mode of the local device to RSTP. Share-link protection needs to be used together with root protection to avoid network loops. |
| Abnormal packet filtering | On a network running STP, RSTP, or MSTP, a device may receive unexpected STP, RSTP, or MSTP BPDUs due to incorrect configurations or malicious network attacks. If these unexpected packets are transparently transmitted on the network, spanning tree calculation may be affected, causing network flapping. | After the function to filter abnormal packets is enabled, the device discards the packets carrying a specified source MAC address or VLAN ID. In this manner, unexpected packets are not transparently transmitted on the network, preventing network flapping. |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

* After a device normally starts, there is a default MSTP process with the ID 0. MSTP configurations in the system view and interface view both belong to this process.
* For more information about MSTP multi-process configuration, see [Configuring MSTP Multi-process](dc_vrp_mstp_cfg_0013.html).


#### Pre-configuration Tasks

Before configuring MSTP protection functions on a device, complete the following task:

* Configure basic MSTP functions.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configure an edge port on the device before configuring BPDU protection.


[Configuring BPDU Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0028.html)

After bridge protocol data unit (BPDU) protection is enabled on a device, the device shuts down an edge port if the edge port receives a BPDU, and notifies the NMS of the shutdown event.

[Configuring TC Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0029.html)

After Topology Change (TC) protection is enabled, you can set the number of times for a Multiple Spanning Tree Protocol (MSTP) process to process TC-BPDUs within a specified time. TC protection avoids frequent deletion of MAC address entries and ARP entries, thereby protecting devices.

[Configuring TC/TCN Packet Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0026.html)

If TC/TCN packets do not need to be flooded, you can enable TC/TCN packet suppression.

[Configuring Root Protection on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0030.html)

The root protection function on a device protects a root bridge by preserving the role of a designated port.

[Configuring Loop Protection on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0031.html)

The loop protection function suppresses the loops caused by link congestion.

[Configuring Share-Link Protection on a Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0032.html)

The share-link protection function on a device helps automatically transition to the Rapid Spanning Tree Protocol (RSTP) working mode. It can also be used together with root protection to avoid network loops.

[Configuring Abnormal Packet Filtering](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0035b.html)

You can configure the device to process or discard specified packets in order to filter unexpected packets.

[Verifying the MSTP Protection Function Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0033.html)

After Multiple Spanning Tree Protocol (MSTP) protection functions are configured, verify the configuration.