Understanding Fixed ARP
=======================

Understanding Fixed ARP

#### Related Concepts

Fixed ARP can be implemented in three modes, as described in [Table 1](#EN-US_CONCEPT_0000001130781870__tab_dc_fd_ARP_SEC_000901).

**Table 1** Fixed ARP modes
| Mode | Function | Application Scenario |
| --- | --- | --- |
| fixed-all | When receiving an ARP message, a device discards the message if the MAC address, interface number, or VLAN ID does not match an ARP entry. | This mode applies to networks where user MAC addresses and user access locations are fixed. |
| fixed-mac | When receiving an ARP message, a device discards the message if the MAC address in the message does not match that in the corresponding ARP entry. If the MAC addresses match but the interface number or VLAN ID does not match that in the ARP entry, the device updates the interface number or VLAN ID in the ARP entry. | This mode applies to networks where user MAC addresses are unchanged but user access locations frequently change. |
| send-ack | If the MAC address, interface number, or VLAN ID in ARP message A received by a device is different from that in the currently saved ARP entry, the device does not immediately update the ARP entry. Instead, the device sends a unicast ARP request message to the user with the IP address mapped to the MAC address to be updated in the ARP entry. The device then determines whether to update the ARP entry depending on a response from the user.   * If the device receives ARP reply message B within 3 seconds, and the IP address, MAC address, interface number, and VLAN ID in this message are the same as those in the ARP entry but different from those in ARP message A, the device considers ARP message A invalid and does not update the ARP entry. * If the device does not receive ARP reply message B within 3 seconds or receives ARP reply message B but the IP address, MAC address, interface number, and VLAN ID in this message are different from those in the ARP entry, the device sends a unicast ARP request message to the user with the IP address mapped to the source MAC address in ARP message A.   + If the device receives ARP reply message C within 3 seconds, and the IP address, MAC address, interface number, and VLAN ID in this message are the same as those in ARP message A, the device considers that the ARP entry is invalid and needs to be updated based on ARP message A.   + If the device does not receive ARP reply message C within 3 seconds or receives ARP reply message C but the IP address, MAC address, interface number, and VLAN ID in this message are different from those in ARP message A, the device considers ARP message A invalid and does not update the ARP entry. | This mode applies to networks where user MAC addresses and user access locations frequently change. |



#### Fundamentals

As shown in [Figure 1](#EN-US_CONCEPT_0000001130781870__fig_dc_fd_ARP_SEC_000901), the attacker poses as HostA to send a bogus ARP message to Device. Device then records an incorrect ARP entry for HostA. As a result, HostA cannot communicate with Device.

**Figure 1** ARP spoofing attack  
![](figure/en-us_image_0000001962618513.png)

To defend against ARP spoofing attacks, configure fixed ARP on Device. After learning an ARP entry for the first time, Device does not update the entry, updates only part of the entry, or sends a unicast ARP request message to check the validity of the ARP message for updating the entry.