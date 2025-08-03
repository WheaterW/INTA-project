IPv6 Packet Format
==================

An IPv6 packet consists of three parts: an IPv6 basic header, one or more IPv6 extension headers, and an upper-layer protocol data unit (PDU).

An upper-layer PDU is generally composed of the upper-layer protocol header and its payload. A payload is a datagram that follows an IPv6 basic header, including an IPv6 extension header. For example, a payload can be an ICMPv6, TCP6, or UDP6 message.

#### IPv6 Basic Header

An IPv6 basic header has a fixed length of 40 bytes with eight fields. An IPv6 basic header, required in every IPv6 packet, provides basic packet forwarding information, which all devices parse on the forwarding path.

[Figure 1](#EN-US_CONCEPT_0000001130622162__fig91925186264) shows an IPv6 basic header.

**Figure 1** IPv6 basic header  
![](figure/en-us_image_0000001130781962.png)

**Table 1** Fields in an IPv6 basic header
| Field | Description |
| --- | --- |
| Version | 4 bits long. In IPv6, the value of this field is set to 6. |
| Traffic Class | 8 bits long. This field indicates the class or priority of an IPv6 packet. It is similar to the ToS field in an IPv4 packet and mainly used in QoS control. |
| Flow Label | 20 bits long. This field is added in IPv6 to differentiate real-time traffic. A flow label and source IPv6 address uniquely identify a data flow. Intermediate network devices can effectively differentiate data flows based on this field. |
| Payload Length | 16 bits long. The payload refers to the extension header and upper-layer PDU that follow the IPv6 header. If the Payload Length exceeds its maximum value of 65535 bytes, the field is set to 0, and the Jumbo Payload option in the Hop-by-Hop Options header is used to express the actual payload length. |
| Next Header | 8 bits long. This field identifies the type of the first extension header (if any) that follows the IPv6 basic header or the protocol type in the upper-layer PDU. |
| Hop Limit | 8 bits long. This field is similar to the Time to Live field in an IPv4 packet, defining the maximum number of hops that an IPv6 packet can pass through. Each device that forwards the packet decrements the field value by 1. If the field value is reduced to 0, the packet is discarded. |
| Source Address | 128 bits long. This field indicates the address of the packet originator. |
| Destination Address | 128 bits long. This field indicates the address of the packet recipient. |

Unlike the IPv4 packet header, the IPv6 packet header does not carry IHL, Identification, Flags, Fragment Offset, Header Checksum, Options, or Padding fields, but it carries the Flow Label field. This facilitates IPv6 packet processing and improves processing efficiency. To support various options without changing the existing packet format, the Extension Header information field is added to the IPv6 packet header, improving flexibility. The following paragraphs describe IPv6 extension headers.


#### IPv6 Extension Header

An IPv4 packet header has an optional field (Options), which includes Security, Timestamp, and Record Route options. The variable length of the Options field results in an IPv4 packet header length range of 20 bytes to 60 bytes. When devices forward IPv4 packets with the Options field, many resources are required; therefore in practice, these IPv4 packets are rarely used.

To improve packet processing efficiency, IPv6 uses extension headers to replace the Options field in the IPv4 header. An IPv6 packet may or may not carry extension headers, and they are placed between the IPv6 basic header and upper-layer PDU. When the sender of a packet requests the destination device or other devices to perform special handling, the sender adds one or more extension headers to the packet. Unlike IPv4, IPv6 has variable-length extension headers, which are not limited to 40 bytes, to facilitate further extension. To improve extension header processing efficiency and transport protocol performance, IPv6 requires that the extension header length be an integral multiple of 8 bytes.

When multiple extension headers are used, the Next Header field of an extension header indicates the type of the next header that follows.

The Next Header field in the IPv6 basic header indicates the first extension header type, and the Next Header field in the first extension header indicates the next (second) extension header type, and so on. The Next Header field of the final extension header indicates the upper-layer protocol type. [Figure 2](#EN-US_CONCEPT_0000001130622162__fig1638611256326) shows an IPv6 extension header.

**Figure 2** IPv6 extension header  
![](figure/en-us_image_0000001130622178.png)

**Table 2** Fields in an IPv6 extension header
| Field | Description |
| --- | --- |
| Next Header | 8 bits long. This field is similar to the Next Header field in the IPv6 basic header, indicating the next extension header (if any) or upper-layer protocol type. |
| Extension Header Len | 8 bits long. This field indicates the extension header length excluding the Next Header field. |
| Extension Head Data | Variable length. This field includes a series of options and the padding field. |

RFC defines six IPv6 extension headers: Hop-by-Hop Options header, Destination Options header, Routing header, Fragment header, Authentication header, and Encapsulating Security Payload header.

**Table 3** IPv6 extension headers
| Header Type | Next Header Field Value | Description |
| --- | --- | --- |
| Hop-by-Hop Options header | 0 | This header carries information that every node must examine along the delivery path of a packet. It is used in the following applications:   * Jumbo payload (if the payload length exceeds 65535 bytes) * Device prompted to check this option before forwarding packets * Resource Reservation Protocol (RSVP) |
| Destination Options header | 60 | This header carries information that only the destination node of a packet examines. Currently, this header is used in mobile IPv6. |
| Routing header | 43 | An IPv6 source node uses this header to specify the intermediate nodes that a packet must pass through on the way to its destination. This header is similar to the Loose Source and Record Route option in IPv4. |
| Fragment header | 44 | Like IPv4 packets, when the length of IPv6 packets to be forwarded exceeds the maximum transmission unit (MTU), the packets need to be fragmented. In IPv6, the Fragment header is used by an IPv6 source node to send a packet larger than the MTU. |
| Authentication header | 51 | IPsec uses this header to provide data origin authentication, data integrity check, and packet anti-replay functions. This header also protects some fields in the IPv6 basic header. |
| Encapsulating Security Payload header | 50 | This header provides the same functions as the Authentication header with the addition of IPv6 packet encryption. |

**Conventions for IPv6 extension headers**

When a single packet uses more than one extension header, the headers must be listed in the following order:

* IPv6 basic header
* Hop-by-Hop Options header
* Destination Options header
* Routing header
* Fragment header
* Authentication header
* Encapsulating Security Payload header
* Destination Options header
* Upper-layer header

Intermediate devices do not need to examine or process all extension headers, but only those based on the Next Header field value in the IPv6 basic header.

Each extension header can only occur once in an IPv6 packet, except for the Destination Options header which may occur twice (once before a Routing header and once before the upper-layer header).