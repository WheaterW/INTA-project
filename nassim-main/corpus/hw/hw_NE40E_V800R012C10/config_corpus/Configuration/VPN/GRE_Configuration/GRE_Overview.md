GRE Overview
============

GRE Overview

#### Definition

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If IPv4 GRE and IPv6 GRE implement a feature in the same way, details are not provided in this chapter. For implementation differences, see [Appendix](feature_0018554785.html).

The Generic Routing Encapsulation (GRE) protocol encapsulates the data packets of a variety of network layer protocols, such as Internetwork Packet Exchange (IPX), Asynchronous Transfer Mode (ATM), IPv6, and AppleTalk, so that these packets can be transmitted over an IPv4 network.

GRE provides a mechanism for transmitting the packets of one protocol over another protocol by means of encapsulation, enabling packets to be transmitted over heterogeneous networks. The channel used for transmitting such packets is called a tunnel.

The following types of GRE tunnels are supported on NE40E:

* GRE tunnel with the one-dimensional tunnel interface: also called distributed GRE tunnel. The tunnel interface is one-dimensional (named only by the interface number). GRE packets are encapsulated and decapsulated directly on the inbound interface board. If the multi-field classification and CAR services are both configured, bandwidth that services consume may double.
* GRE tunnel with the three-dimensional tunnel interface: also called integrated GRE tunnel. The tunnel interface is three-dimensional (named by the slot ID, subcard ID, and interface number). GRE packets are encapsulated and decapsulated directly on a service processing board.


#### Purpose

To ensure the packets of a wide variety of network layer protocols, such as IPX, ATM, IPv6, and AppleTalk, can be transmitted over an IPv4 network, GRE is introduced. GRE solves the transmission problem faced by heterogeneous networks.

In addition, GRE serves as a Layer 3 tunneling protocol of VPNs, and provides tunnels for transparently transmitting VPN packets. Currently, GRE is supported by IPv4 L3VPN, but not IPv6 L3VPN.


#### Benefits

GRE has low requirements for device performance and allows devices that do not support Multiprotocol Label Switching (MPLS) to establish tunnels.