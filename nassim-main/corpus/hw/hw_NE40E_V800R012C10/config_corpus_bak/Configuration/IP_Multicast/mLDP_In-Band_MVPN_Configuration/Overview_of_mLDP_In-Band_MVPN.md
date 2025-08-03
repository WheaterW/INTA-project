Overview of mLDP In-Band MVPN
=============================

Overview_of_mLDP_In-Band_MVPN

#### Definition

As an MVPN technology independent of NG MVPN, multipoint extensions for LDP (mLDP) in-band MVPN is usually deployed on an IP/MPLS backbone network that needs to carry multicast traffic. It uses mLDP signaling to transmit PIM-SM/PIM-SSM Join messages and the mLDP-based data bearer mode to transmit multicast and unicast services in the same VPN architecture. In the current version, mLDP signaling can transmit only PIM-SM/PIM-SSM (S, G) Join messages.


#### Purpose

The MVPN solution mainly uses MVPN technologies to allow multicast services to be deployed on a BGP/MPLS IP VPN and C-multicast traffic to be transmitted to remote VPN sites through the public network. mLDP in-band MVPN encapsulates the (S, G) information carried in C-multicast PIM Join messages into the Opaque value of mLDP P2MP Label Mapping messages, implementing one-to-one mapping between multicast (S, G) entries and mLDP P2MP tunnels. In this manner, C-multicast route transmission and tunnel establishment are integrated. This MVPN technology can be used to implement C-multicast or Global Table Multicast (GTM) in an MPLS domain.