Multicast NAT Fundamentals
==========================

[Figure 1](#EN-US_CONCEPT_0000001147870144__fig_feature_image_multicast_nat_02) shows the multicast NAT networking. The multicast NAT device (Device) converts the input multicast stream StreamIn into one or more output multicast streams.

**Figure 1** Multicast NAT networking  
![](figure/en-us_image_0000001432235737.png)
#### Multicast NAT Process

Multicast stream characteristics include the source MAC address, source IP address, destination IP address, source UDP port number, and destination UDP port number. The multicast NAT function can be used to translate characteristics for output streams. As shown in the following table, the input multicast stream StreamIn is converted into output multicast streams StreamOut1 and StreamOut2 through multicast NAT. For StreamOut1, only the source MAC address is translated; for StreamOut2, all multicast stream characteristics are translated.

**Table 1** Multicast stream characteristics
| Multicast Stream Characteristics | StreamIn | StreamOut1 | StreamOut2 |
| --- | --- | --- | --- |
| Source MAC address | 00e0-fc00-0001 | 00e0-fc00-0002  NOTE:  By default, the post-translation MAC address (00e0-fc00-0002 in this example) is the MAC address of an outbound interface. | 00e0-fc00-0003  NOTE:  By default, the post-translation MAC address (00e0-fc00-0003 in this example) is the MAC address of an outbound interface. |
| Source IP address | 10.10.1.1 | 10.10.1.1 | 10.10.2.2 |
| Destination IP address | 239.0.0.1 | 239.0.0.1 | 239.1.0.2 |
| Source UDP port number | 10000 | 10000 | 10002 |
| Destination UDP port number | 10000 | 10000 | 10003 |

1. Traffic policies are applied to the inbound interface (Interface1) to match the source MAC address, source IP address, destination IP address, source UDP port number, and destination UDP port number of StreamIn. The traffic behavior is to associate the stream with a multicast NAT instance. The mapping between StreamIn and the multicast NAT instance is established based on the traffic policies.
2. Multicast stream translation rules are configured on outbound interfaces (such as Interface2 and Interface3) to translate the characteristics of output multicast streams. The output multicast streams are bound to the multicast NAT instance, thereby implementing the association between the input and output multicast streams.
3. Each multicast NAT instance can be bound to multiple outbound interfaces. This allows one input multicast stream to be replicated to multiple outbound interfaces. The characteristics of output multicast streams are then modified.