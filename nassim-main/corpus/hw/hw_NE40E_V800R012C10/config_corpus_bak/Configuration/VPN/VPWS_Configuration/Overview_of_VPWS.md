Overview of VPWS
================

Overview_of_VPWS

#### Definition

Virtual private wire service (VPWS) is a Layer 2 service bearer technology that simulates the basic behaviors and characteristics of services, such as ATM, frame relay, Ethernet, low-speed time division multiplexing (TDM) circuit, synchronous optical network (SONET), and synchronous digital hierarchy (SDH) services, on a PSN. VPWS simulates traditional leased lines on the IP network and provides asymmetric and low-cost digital data network (DDN) services. From the perspective of users, a virtual leased line is similar to a traditional leased line. VPWS is a point-to-point (P2P) virtual leased line technology and supports almost all link-layer protocols.


#### Purpose

As IP networks develop, their expansibility, upgradability, and compatibility have been greatly enhanced. Nevertheless, the expansibility, upgradability, and interworking capability of traditional communications networks are relatively poor. Confined by transmission modes and service types, resource sharing among newly constructed communications networks is also poor, complicating interworking management. In the process of upgrading and expanding a traditional communications network, you must determine whether to achieve your goal by constructing more traditional communications networks, or by utilizing existing network resources at your disposal, or by utilizing public network resources. VPWS is a solution that enables traditional communications networks to interwork with existing PSNs.


#### Benefits

VPWS offers the following benefits:

* Extended network functions and service capabilities
  
  Carriers can provide MPLS L2VPN services by using only one network. In addition, carriers can use enhanced MPLS-related technologies, such as traffic engineering (TE) and quality of service (QoS), to provide users with different classes of services to meet their requirements.
* Higher scalability
  
  On an ATM or FR network where MPLS is not enabled, virtual circuits (VCs) are used to provide the L2VPN service. For each VC, both the PE and provider (P) devices on the network need to maintain complete VC information. That means that when the PEs of a carrier connect to multiple CEs, multiple VCs are required, and information about multiple VCs must be maintained on both PEs and Ps. VPWS uses label stacking to multiplex multiple VCs on a label switched path (LSP). As a result, Ps only need to maintain information about one LSP. This improves the scalability of a system.
* Well-defined administration roles
  
  On an MPLS L2VPN, a carrier provides only Layer 2 connectivity and users are responsible for Layer 3 connectivity, such as routing. This implementation prevents route flapping caused by incorrect configurations from affecting the stability of the carrier's network.
* Support for multiple protocols
  
  Carriers provide only Layer 2 connections, whereas users can use any Layer 3 protocol, such as IPv4 and IPv6.
* Smooth network upgrade
  
  An MPLS L2VPN is transparent to users. When a carrier upgrades the network from a traditional L2VPN, such as an ATM and FR network, to an MPLS L2VPN, users do not need to perform any configuration. The network upgrade does not affect user services, except for temporary data loss during the network cutover.