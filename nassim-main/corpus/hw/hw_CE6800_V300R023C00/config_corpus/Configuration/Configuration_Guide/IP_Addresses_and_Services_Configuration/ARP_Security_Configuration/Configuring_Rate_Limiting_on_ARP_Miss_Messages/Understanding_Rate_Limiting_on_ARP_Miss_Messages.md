Understanding Rate Limiting on ARP Miss Messages
================================================

Understanding Rate Limiting on ARP Miss Messages

#### Fundamentals

If a device is flooded with IP packets that contain unresolvable destination IP addresses, the device generates a large number of ARP Miss messages. This is because the device has no ARP entry that matches the next hop of the route. IP packets, which trigger ARP Miss messages, are sent to the CPU for processing. As a result, the device generates and delivers many temporary ARP entries based on ARP Miss messages, and sends a large number of ARP request messages to the destination network. This increases CPU usage of the device and consumes considerable bandwidth resources of the destination network.

The following describes in detail the procedure of initiating an ARP Miss attack with reference to [Figure 1](#EN-US_CONCEPT_0000001176741539__fig_dc_fd_ARP_SEC_000501).

1. The attacker sends IP packets with the unresolvable destination IP address 10.2.1.5/24 to the gateway (Device).
2. Device fails to learn the MAC address matching 10.2.1.5, and sends an ARP Miss message.
3. Device generates and delivers a temporary ARP entry based on the ARP Miss message, and sends an ARP request message to the destination network.
4. Device deletes the temporary ARP entry after the aging time of the entry expires. If no ARP entry matches the IP packets forwarded by Device and the attacker keeps sending IP packets with the unresolvable destination IP address, Device repeats steps 2 and 3. This increases CPU usage of Device and consumes considerable bandwidth resources of the destination network.

**Figure 1** ARP Miss attack  
![](figure/en-us_image_0000001886034389.png)

#### Application Scenarios

To avoid the preceding issues, the device can be configured to limit the rate of ARP Miss messages in various scenarios, as described in [Table 1](#EN-US_CONCEPT_0000001176741539__table551051810303).

**Table 1** Scenarios for rate limiting on ARP Miss messages
| Scenario | Description |
| --- | --- |
| Limiting the rate of ARP Miss messages based on source IP addresses | If the rate of ARP Miss messages triggered by IP packets from a source IP address exceeds the limit, the device considers that this address has initiated an attack. If a source IP address is specified, the rate of ARP Miss messages triggered by IP packets from this source IP address is limited. If no source IP address is specified, the rate of ARP Miss messages triggered by IP packets from any source IP address is limited. |
| Limiting the rate of ARP Miss messages globally or in a VLAN | Limiting the rate of ARP Miss messages globally: If a device is flooded with IP packets that contain unresolvable destination IP addresses, the number of ARP Miss messages to be processed on the device is limited.  Limiting the rate of ARP Miss messages in a VLAN: If all interfaces in a VLAN are flooded with IP packets that contain unresolvable destination IP addresses, the number of ARP Miss messages to be processed in the VLAN is limited. The configuration in a VLAN does not affect IP packet forwarding on interfaces in other VLANs. |
| Reducing the frequency of triggering ARP Miss messages by increasing the aging time of temporary ARP entries | When IP packets trigger ARP Miss messages, a device generates temporary ARP entries and sends ARP request messages to the destination network.  If a device does not receive an ARP reply message during the aging time of temporary ARP entries, it discards the IP packets matching the temporary ARP entries and does not generate ARP Miss messages. After receiving an ARP reply message, the device generates a correct ARP entry to replace the temporary one.  After temporary ARP entries age out, a device clears them. If no ARP entry matches the IP packets forwarded by the device, ARP Miss messages and temporary ARP entries are repeatedly generated.  If a device undergoes an ARP Miss attack, you can increase the aging time of temporary ARP entries to reduce the frequency of triggering ARP Miss messages, mitigating the impact of the attack on the device. |