Overview of MSDP
================

Overview of MSDP

#### Definition

The Multicast Source Discovery Protocol (MSDP) is an inter-domain multicast solution developed for interconnection between multiple Protocol Independent Multicast Sparse Mode (PIM-SM) domains. MSDP enables devices in a PIM-SM domain to discover information about multicast sources in other PIM-SM domains.

Currently, MSDP can be deployed only on IPv4 networks, is applicable only to PIM-SM domains, and is effective only in the Any-Source Multicast (ASM) model.


#### Purpose

On a PIM-SM network, a source designated router (DR) registers with the rendezvous point (RP) in the local PIM domain, and a receiver DR and user hosts send Join messages to the RP in the local PIM domain. An RP is only aware of the multicast sources in the local domain, and only distributes data sent by the multicast sources in the local domain to local users. As networks expand in scale, a PIM network is divided into multiple PIM-SM domains to better control multicast resources. The RP in a PIM-SM domain cannot communicate with RPs in other domains, nor can it obtain multicast source information in other domains.

MSDP can solve this problem by enabling multicast devices (usually RPs) in different PIM-SM domains to set up MSDP peer relationships. These MSDP peers exchange Source-Active (SA) messages to share multicast source information, so that multicast users in one PIM-SM domain can receive multicast data from multicast sources in other domains.

MSDP can be used to set up peer relationships between devices on different Internet service provider (ISP) networks. To prevent network security problems and poor user experience, an ISP typically avoids relying on another ISP's RPs to provide services for its users. MSDP enables each ISP to use its own RPs to send and receive multicast data to and from the Internet, thereby ensuring network security and service quality.

MSDP also provides anycast RP â a special application in PIM-SM domains. Anycast RP supports two or more RPs with the same address in a PIM-SM domain, and MSDP peer relationships are established between these RPs to implement load balancing and redundancy backup among RPs in the domain.


#### Benefits

MSDP implements inter-domain multicast and provides the following benefits to ISPs:

* A PIM-SM domain provides services using the local RP, decreasing the dependency on RPs in other PIM-SM domains. In addition, MSDP controls whether source information in a domain can be transmitted to others, improving network security.
* If a domain only has receivers, group memberships only need to be reported within the local PIM-SM domain rather than the entire network for the receivers to receive multicast data, facilitating management.
* Devices in a PIM-SM domain do not need to maintain network-wide multicast source information and routing entries, conserving system resources.