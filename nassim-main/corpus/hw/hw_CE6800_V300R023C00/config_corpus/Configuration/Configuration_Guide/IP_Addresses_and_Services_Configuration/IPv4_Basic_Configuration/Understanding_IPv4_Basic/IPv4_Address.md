IPv4 Address
============

To connect a PC to the Internet, you must apply for an IP address from the Internet service provider (ISP).

An IP address is a numerical label assigned to each device on a computer network. An IPv4 address is a 32-bit binary number, expressed in dotted decimal notation, which helps you memorize and identify it. In dotted decimal notation, an IPv4 address is written as four decimal numbers, one for each byte of the address. For example, the binary IPv4 address 00001010 00000001 00000001 00000010 is written as 10.1.1.2 in dotted decimal notation.

An IPv4 address consists of two parts:

* Network ID (Net-id): identifies a network.
* Host ID (Host-id): identifies a host on a network. Network devices with the same network ID are located on the same network, regardless of their physical locations.

#### Characteristics of IPv4 Addresses

IPv4 addresses have the following characteristics:

* IPv4 addresses do not show any geographical information. The network ID represents the network to which a host belongs.
* When a host connects to two networks, it must have two IPv4 addresses with different network IDs. In this case, the host is called a multihomed host.
* Networks allocated with network IDs are in the same class.

#### IPv4 Address Classification

As shown in [Figure 1](#EN-US_CONCEPT_0000001130623786__fig_dc_fd_IPv4_000501), IPv4 addresses are classified into five classes to facilitate IPv4 address management and networking.

**Figure 1** Five classes of IPv4 addresses  
![](figure/en-us_image_0000001176743253.png)

Most IP addresses in use belong to Class A, Class B, or Class C. Class D addresses are multicast addresses, and Class E addresses are reserved. The easiest way to determine the class of an IP address is to check the first bits in its network ID. The class fields of Class A, Class B, Class C, Class D, and Class E are binary numbers 0, 10, 110, 1110, and 1111, respectively.

**Table 1** IPv4 address classes and ranges
| Class | Range | Description |
| --- | --- | --- |
| A | 0.0.0.0 to 127.255.255.255 | IP addresses with a host ID comprising all 0s are network addresses and are used for routing. IP addresses with a host ID comprising all 1s are broadcast addresses and are used for broadcasting datagrams to all hosts on a network. |
| B | 128.0.0.0 to 191.255.255.255 | IP addresses with a host ID comprising all 0s are network addresses and are used for routing. IP addresses with a host ID comprising all 1s are broadcast addresses and are used for broadcasting datagrams to all hosts on a network. |
| C | 192.0.0.0 to 223.255.255.255 | IP addresses with a host ID comprising all 0s are network addresses and are used for routing. IP addresses with a host ID comprising all 1s are broadcast addresses and are used for broadcasting datagrams to all hosts on a network. |
| D | 224.0.0.0 to 239.255.255.255 | Class D addresses are multicast addresses. |
| E | 240.0.0.0 to 255.255.255.255 | Reserved. 255.255.255.255 is a LAN broadcast address. |



#### Special IPv4 Addresses

**Table 2** Special IPv4 addresses
| Network ID | Host ID | Used as a Source Address | Used as a Destination Address | Description |
| --- | --- | --- | --- | --- |
| All 0s | All 0s | Supported | Not supported | Used for routing on a network |
| All 0s | Host ID | Supported | Not supported | Used by a specific host on a network |
| 127 | Any value that does not comprise all 0s or all 1s | Supported | Supported | Used as a loopback address |
| All 1s | All 1s | Not supported | Supported | Used as a limited broadcast address (datagrams with this IP address are never forwarded) |
| Net-id | All 1s | Not supported | Supported | Used as a directed broadcast address (datagrams with this IP address is broadcast on a specified network) |


![](public_sys-resources/note_3.0-en-us.png) 

Net-id is neither all 0s nor all 1s.



#### Private IPv4 Addresses

Private IPv4 addresses were proposed to resolve IPv4 address shortage. They are used for internal networks or hosts, and cannot be used for public networks. RFC standards describe three IPv4 address segments, which are reserved for private networks.

**Table 3** Private IPv4 addresses
| Class | Range |
| --- | --- |
| A | 10.0.0.0 to 10.255.255.255 |
| B | 172.16.0.0 to 172.31.255.255 |
| C | 192.168.0.0 to 192.168.255.255 |