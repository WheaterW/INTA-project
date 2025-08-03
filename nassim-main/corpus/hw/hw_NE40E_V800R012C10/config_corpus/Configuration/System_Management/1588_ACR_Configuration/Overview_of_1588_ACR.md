Overview of 1588 ACR
====================

Overview of 1588 ACR

#### Purpose

All-IP has become the trend for future networks and services. Therefore, traditional networks based on the Synchronous Digital Hierarchy (SDH) have to overcome various constraints before migrating to IP packet-switched networks. Transmitting Time Division Multiplexing (TDM) services over IP networks presents a major technological challenge. TDM services are classified into two types: voice services and clock synchronization services. With the development of VoIP, technologies of transmitting voice services over an IP network have become mature and have been extensively used. However, development of technologies of transmitting clock synchronization services over an IP network is still under way.

1588v2 is a software-based technology that carries out time and frequency synchronization. To achieve higher accuracy, 1588v2 requires that all devices on a network support 1588v2; if not, frequency synchronization cannot be achieved.

Derived from 1588v2, 1588 ACR implements frequency synchronization with clock servers on a network with both 1588v2-aware devices and 1588v2-unaware devices. Therefore, in the situation where only frequency synchronization is required, 1588 ACR is more applicable than 1588v2.


#### Definition

The 1588 adaptive clock recovery (ACR) algorithm is used to carry out clock (frequency) synchronization between the NE40E and clock servers by exchanging 1588v2 messages over a clock link that is set up by sending Layer 3 unicast packets.

Unlike 1588v2 that achieves frequency synchronization only when all devices on a network support 1588v2, 1588 ACR is capable of implementing frequency synchronization on a network with both 1588v2-aware devices and 1588v2-unaware devices.

After 1588 ACR is enabled on a server, the server provides 1588 ACR frequency synchronization services for clients.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

1588 ACR records PDV performance statistics in the CF card. The performance statistics indicate the delay and jitter information about packets but not information in the packets.