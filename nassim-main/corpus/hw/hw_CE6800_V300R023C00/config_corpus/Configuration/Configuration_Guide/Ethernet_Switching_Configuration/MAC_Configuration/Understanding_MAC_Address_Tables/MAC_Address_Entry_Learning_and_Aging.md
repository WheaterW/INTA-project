MAC Address Entry Learning and Aging
====================================

MAC Address Entry Learning and Aging

#### MAC Address Entry Learning

Most MAC address entries are dynamically created based on source MAC addresses learned from received data frames.

**Figure 1** MAC address entry learning  
![](figure/en-us_image_0000001176664499.png)

In [Figure 1](#EN-US_CONCEPT_0000001130624936__dc_fig_100601), Host1 sends a data frame to DeviceA. When receiving the data frame, DeviceA obtains the source MAC address (Host1's MAC address) and VLAN ID of the frame.

* If Host1's MAC address does not exist in the MAC address table, DeviceA adds a new entry with Host1's MAC address, interface 1, and VLAN ID to the MAC address table.
* If Host1's MAC address exists in the MAC address table, DeviceA resets the aging time of the MAC address entry and updates the entry.

![](public_sys-resources/note_3.0-en-us.png) 

* If interface 1 is a member interface of an Eth-Trunk interface, for example, Eth-Trunk A, the outbound interface in the MAC address entry is Eth-Trunk A.
* All device interfaces belong to VLAN 1 by default. If the VLAN to which an interface belongs is not changed, the VLAN ID of the corresponding MAC address entry is VLAN 1.
* A device does not learn the BPDU MAC address, of which the format is 0180-c200-xxxx.

MAC address entry learning and update are triggered on a device only when the device receives data frames.


#### MAC Address Entry Aging

A device needs to update its MAC address table continuously to adapt to changing network topologies. The dynamic entries automatically created in a MAC address table are not always valid. Each entry has a lifecycle (aging time) and will be deleted if it is not updated within the aging time. If an entry is updated within the aging time, the aging timer for the entry is reset.

**Figure 2** MAC address entry aging  
![](figure/en-us_image_0000001176744415.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001130624936__fig4201181211719), the aging time of MAC address entries is set to T. At t1, packets with source MAC address 00e0-fc00-0001 and VLAN ID 1 arrive at an interface, which has joined VLAN 1. If no entry with MAC address 00e0-fc00-0001 and VLAN 1 exists in the MAC address table, the MAC address is learned as a dynamic MAC address entry, and the hit flag of the entry is set to 1.

The device checks all dynamic MAC address entries at an interval of T.

1. At t2, if the device finds that the hit flag of the matching dynamic MAC address entry with MAC address 00e0-fc00-0001 and VLAN 1 is 1, the device sets the hit flag to 0 and retains the MAC address entry.
2. If no packet with source MAC address 00e0-fc00-0001 and VLAN 1 enters the device between t2 and t3, the hit flag of the matching MAC address entry is always 0.
3. At t3, the device finds that the hit flag of the matching MAC address entry is 0. The device considers the MAC address entry as expired and deletes it.

The minimum holdtime of a dynamic MAC address entry ranges from T to 2T on the device.

You can set the aging time of MAC address entries to control their lifecycle in the MAC address table.