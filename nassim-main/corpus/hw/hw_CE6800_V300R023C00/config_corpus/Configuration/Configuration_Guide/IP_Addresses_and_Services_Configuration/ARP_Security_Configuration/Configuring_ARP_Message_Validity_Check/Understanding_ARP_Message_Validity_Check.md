Understanding ARP Message Validity Check
========================================

Understanding ARP Message Validity Check

#### Definition

ARP is easy to implement but lacks security mechanisms, making it vulnerable to attacks. An attacker can forge an ARP message by changing the MAC addresses carried in the Data field of an authorized user's message, which makes the source and destination MAC addresses carried in the Data field different from those carried in the Ethernet header.

This issue can be resolved by configuring ARP message validity check on devices. When a device capable of checking ARP message validity receives an ARP message, the device checks whether the source and destination MAC addresses carried in the Data field match those carried in the Ethernet header. If they match, the device considers the message valid. If they do not match, the device considers the message invalid and discards it.


#### Related Concepts

**Table 1** ARP message validity check modes
| Check Mode | Description |
| --- | --- |
| Source MAC address-based check | After receiving an ARP message, a device checks whether the source MAC address in the Data field matches that in the Ethernet header. If they match, the device considers the message valid. If they do not match, the device considers the message invalid and discards it. |
| Destination MAC address-based check (only for ARP reply messages) | After receiving an ARP message, a device checks the destination MAC address in the Data field. If the destination MAC address comprises all 1s, the device considers the ARP message invalid and discards it.  After receiving an ARP message, a device checks whether the destination MAC address in the Data field matches that in the Ethernet header. If they match, the device considers the message valid. If they do not match, the device considers the message invalid and discards it. |
| Source and destination MAC addresses-based check | After receiving an ARP request message, a device checks whether the source MAC address in the Data field matches that in the Ethernet header. If they match, the device considers the message valid. If they do not match, the device considers the message invalid and discards it.  After receiving an ARP reply message, a device checks whether the source and destination MAC addresses in the Data field match those in the Ethernet header and whether the destination MAC address comprises all 1s. If the source and destination MAC addresses in the Data field match those in the Ethernet header and the destination MAC address does not comprise all 1s, the device considers the message valid. Otherwise, the device considers the message invalid and discards it. |



#### Fundamentals

[Figure 1](#EN-US_CONCEPT_0000001176661635__fig_dc_vrp_arp-sec_feature_000701) shows how the validity of an ARP request message is checked.**Figure 1** Validity check of an ARP request message  
![](figure/en-us_image_0000001877803945.png)

As shown in [Figure 1](#EN-US_CONCEPT_0000001176661635__fig_dc_vrp_arp-sec_feature_000701), HostA is attacked, and the attacker changes the source MAC address of an ARP request message sent by HostA. As a result, the source MAC address in the Data field of the message is different from that in the Ethernet header. If ARP message validity check is not configured, both HostB and Device learn the fake address information carried in HostA's ARP request message.

If ARP message validity check is configured on Device, Device checks whether the source MAC address in the Data field of the received ARP request message matches that in the Ethernet header. If they match, Device learns the address information carried in the message. If they do not match, Device discards the message.