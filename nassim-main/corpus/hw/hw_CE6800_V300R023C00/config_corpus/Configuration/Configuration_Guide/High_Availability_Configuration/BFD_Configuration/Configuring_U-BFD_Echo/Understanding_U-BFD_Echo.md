Understanding U-BFD Echo
========================

BFD Echo is a rapid fault detection mechanism in which the local system sends BFD Echo packets and the remote system loops back the packets. BFD Echo is classified as either passive Echo or U-BFD Echo. These two functions adopt the same detection mechanism and apply only to single-hop IP links; however, they are used in different scenarios.

In passive Echo, two devices are directly connected, and a BFD session in asynchronous mode is set up on each device (see [BFD Detection Mechanism](vrp_bfd_cfg_0003.html#EN-US_CONCEPT_0000001130622344__section_dc_vrp_bfd_feature_000601)). After the Echo and passive Echo functions are enabled on both devices, they work in asynchronous Echo mode and send BFD packets to each other. Before passive Echo is enabled, BFD in asynchronous mode can only adopt the larger detection interval supported by one end; however, after passive Echo is enabled, the smaller interval is adopted for fast link fault detection.

In U-BFD Echo, two devices are directly connected. One device supports BFD, whereas the other device does not. A U-BFD Echo session can be established on the device that supports BFD. After receiving a BFD Echo packet, the device that does not support BFD immediately loops back the packet for quick link fault detection.

U-BFD Echo does not require Echo negotiation capabilities at both ends; that is, BFD can be configured only on one end. The device with U-BFD Echo enabled sends special BFD packets (the source and destination IP addresses in the IP header are the same as the IP address of the local device, and the My Discriminator and Your Discriminator carried in the BFD packet are the same). Upon receiving these packets, the peer device directly loops them back to the local device to check whether the link is normal. This function equips Huawei devices with a stronger adaptability to low-end devices.

#### Comparison Between Passive BFD Echo and U-BFD Echo

To ensure that passive BFD Echo or U-BFD Echo takes effect, disable strict URPF on devices that send BFD Echo packets.

If strict URPF is enabled on a device, the device obtains the source IP address and inbound interface of a packet and searches the forwarding table for an entry with the destination IP address set to the source IP address of the packet. The device then checks whether the outbound interface for the entry matches the inbound interface. If they do not match, the device considers the source IP address invalid and discards the packet, effectively protecting the device against malicious attacks initiated by modifying the source IP addresses of packets. With strict URPF enabled on a device, the device also checks the source address of a looped back BFD Echo packet, and because the source address is the IP address of the device, the packet is transmitted over the upper layer of the device instead of an interface. This means that URPF considers the packet as a spoofing packet and discards it.

[Table 1](#EN-US_CONCEPT_0000001130622358__table2096851214326) compares a common static single-hop BFD session, passive BFD Echo session, and U-BFD Echo session.

**Table 1** Comparison between BFD Echo and common static single-hop BFD sessions
| Item | Common Static Single-Hop BFD Session | Passive BFD Echo Session | U-BFD Echo Session |
| --- | --- | --- | --- |
| Supported IP types | IPv4 and IPv6 | IPv4 and IPv6 | IPv4 and IPv6 |
| Session types | Static single-hop BFD session | Static single-hop BFD session | Static single-hop BFD session |
| Discriminators | My Discriminator and Your Discriminator must be configured. | My Discriminator and Your Discriminator must be configured. | My Discriminator must be configured. |
| Negotiation prerequisites | My Discriminator and Your Discriminator must be configured. | My Discriminator and Your Discriminator must be configured. | My Discriminator must be configured. |
| IP header | My Discriminator and Your Discriminator must be configured. | My Discriminator and Your Discriminator must be configured. | If the source and destination IP addresses are not specified when a U-BFD Echo session is created, the local IP address is used as the source and destination IP addresses.  If URPF is enabled, you need to specify the source IP address when creating a U-BFD Echo session to prevent BFD packets from being incorrectly discarded. |