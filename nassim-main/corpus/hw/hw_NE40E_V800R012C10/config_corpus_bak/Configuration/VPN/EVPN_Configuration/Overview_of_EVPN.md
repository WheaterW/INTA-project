Overview of EVPN
================

Overview_of_EVPN

#### Definition

Ethernet Virtual Private Network (EVPN) is a next-generation VPN solution for full-service transport. It unifies the control planes for L2VPN and L3VPN services and uses BGP extensions to transmit Layer 2 or Layer 3 reachability information, separating the forwarding plane from the control plane.


#### Purpose

EVPN was initially proposed to overcome the drawbacks of traditional L2VPN. The following uses virtual private LAN service (VPLS) as an example to describe the issues of traditional L2VPN.

**Figure 1** VPLS networking  
![](images/fig_feature_image_0003996350.png)

* Difficult network deployment: PEs need to learn the MAC addresses of all CEs but have only limited capacity in their MAC address tables. In addition, PEs require high specifications due to extensive manual configurations.
* Limited network scale: VPLS requires full-mesh PWs to be established between PEs, and is therefore not suitable for large-scale networks.
* Low link bandwidth utilization: PEs must work in single-active mode to ensure that loops do not form between them and CEs. Consequently, the link bandwidth utilization is low.

EVPN integrates the following characteristics to overcome the preceding drawbacks:

* EVPN uses BGP extensions to implement MAC address learning and advertisement on the control plane instead of the data plane. This function allows a device to manage MAC addresses in the same way as it manages routes, implementing load balancing between EVPN routes with the same destination MAC address but different next hops.
  
  **Figure 2** Comparison between EVPN and traditional L2VPN  
  ![](figure/en-us_image_0000001920150840.png)
* EVPN does not require PEs on the ISP backbone network to be fully meshed. This is because PEs on an EVPN communicate using BGP, which provides the route reflection function. As such, a route reflector (RR) can be deployed on the carrier backbone network to reflect EVPN routes to PEs with which the RR has established peer relationships. This significantly reduces network complexity and the number of network signaling messages.
* EVPN supports all-active access, fully utilizing access-side multi-homing to significantly improve network bandwidth utilization.


#### Benefits

EVPN offers the following benefits:

* Improved link utilization and transmission efficiency: EVPN supports load balancing, fully utilizing network resources and alleviating network congestion.
* Reduced network resource consumption: By deploying RRs on the public network, EVPN decreases the number of logical connections required between PEs on the public network. In addition, EVPN enables PEs to respond to ARP requests from connected sites using locally cached MAC addresses, minimizing the amount of broadcast ARP requests.