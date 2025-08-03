Configuring VXLAN in Distributed Gateway Mode Using BGP EVPN
============================================================

Distributed VXLAN gateways can be configured to address problems that occur in centralized gateway networking. Such problems include sub-optimal forwarding paths and bottlenecks on Layer 3 gateways in terms of ARP or ND entry specifications.

#### Usage Scenario

In legacy networking, a centralized Layer 3 gateway is deployed on a spine node. On the network shown in [Figure 1](#EN-US_TASK_0172363804__fig_dc_vrp_vxlan_cfg_106601), packets across different networks must be forwarded through a centralized Layer 3 gateway, resulting in the following problems:

* Forwarding paths are not optimal. All Layer 3 traffic must be transmitted to the centralized Layer 3 gateway for forwarding.
* The ARP or ND entry specification is a bottleneck. ARP or ND entries for tenants must be generated on the Layer 3 gateway, but only a limited number of ARP or ND entries are allowed by the Layer 3 gateway, impeding DCN expansion.

**Figure 1** Network diagram of centralized VXLAN gateways  
![](images/fig_dc_vrp_vxlan_cfg_106401.png)

To address these problems, distributed VXLAN gateways can be configured. On the network shown in [Figure 2](#EN-US_TASK_0172363804__fig_dc_vrp_vxlan_cfg_106602), Server1 and Server2 on different subnets both connect to Leaf1. When Server1 and Server2 communicate, traffic is forwarded only through Leaf1, not through any spine node.

**Figure 2** Network diagram of distributed VXLAN gateways  
![](images/fig_dc_vrp_vxlan_cfg_106402.png)
Distributed VXLAN gateways have the following characteristics:

* Flexible deployment. A leaf node can function as both Layer 2 and Layer 3 VXLAN gateways.
* Improved network expansion capabilities. Unlike a centralized Layer 3 gateway, which has to learn the ARP or ND entries of all servers on a network, a leaf node needs to learn the ARP or ND entries of only the servers attached to it. This addresses the problem of the ARP or ND entry specifications being a bottleneck for packet forwarding faced by centralized Layer 3 gateways.

Either IPv4 or IPv6 addresses can be configured for the VMs and Layer 3 gateways. This means that a VXLAN overlay network can be an IPv4 or IPv6 network. [Figure 2](#EN-US_TASK_0172363804__fig_dc_vrp_vxlan_cfg_106602) shows an IPv4 overlay network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If only VMs on the same subnet need to communicate with each other, Layer 3 VXLAN gateways do not need to be deployed. If VMs on different subnets need to communicate with each other or VMs on the same subnet need to communicate with external networks, Layer 3 VXLAN gateways must be deployed.

The following table lists the differences in distributed gateway configuration between IPv4 and IPv6 overlay networks.

| Configuration Task | IPv4 Overlay Network | IPv6 Overlay Network |
| --- | --- | --- |
| Configure a VPN instance for route leaking with an EVPN instance. | Enable the IPv4 address family of the involved VPN instance and then complete other configurations in the VPN instance IPv4 address family view. | Enable the IPv6 address family of the involved VPN instance and then complete other configurations in the VPN instance IPv6 address family view. |
| Configure an IPv6 Layer 3 VXLAN gateway. | Configure an IPv4 address for the VBDIF interface of the Layer 3 gateway. | Configure an IPv6 address for the VBDIF interface of the Layer 3 gateway. |
| Configure a gateway on an IPv6 VXLAN to advertise a specific type of route. | * For IP prefix routes, perform the configuration in the BGP-VPN instance IPv4 address family view. * For IRB routes, run the [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) command. * For IP prefix routes, run the [**arp vlink-direct-route advertise**](cmdqueryname=arp+vlink-direct-route+advertise) command in the IPv4 address family view of the VPN instance to which the involved VBDIF interface is bound. | * For IP prefix routes, perform the configuration in the BGP-VPN instance IPv6 address family view. * For IRBv6 routes, run the [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command. * For IP prefix routes, run the [**nd vlink-direct-route advertise**](cmdqueryname=nd+vlink-direct-route+advertise) command in the IPv6 address family view of the VPN instance to which the involved VBDIF interface is bound. |



#### Pre-configuration Tasks

Before configuring VXLAN in distributed gateway mode using BGP EVPN, complete the following task:

* Configure IP connectivity on the network.


[Configuring a VXLAN Service Access Point](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0018c.html)

Layer 2 sub-interfaces are used for service access on VXLANs. These Layer 2 sub-interfaces can have different encapsulation types configured to transmit various types of data packets. A Layer 2 sub-interface can transmit data packets through a BD after being associated with it.

[Configuring a VXLAN Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1062.html)

To allow VXLAN tunnel establishment using EVPN, configure an EVPN instance, establish a BGP EVPN peer relationship, and configure ingress replication.

[(Optional) Configuring a VPN Instance for Route Leaking with an EVPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1217-1.html)

To enable communication between VMs on different subnets, configure a VPN instance for route leaking with an EVPN instance. This configuration enables Layer 3 connectivity. To isolate multiple tenants, you can use different VPN instances.

[Configuring a Layer 3 VXLAN Gateway](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1217.html)

To enable communication between VMs on different subnets, configure Layer 3 gateways on the VXLAN, enable the distributed gateway function, and configure host route advertisement.

[(Optional) Configuring VXLAN Gateways to Advertise Specific Types of Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1217-2.html)

To enable communication between VMs on different subnets, configure VXLAN gateways to exchange IRB or IP prefix routes. This configuration enables the gateways to learn the IP routes of the related hosts or the subnets where the hosts reside.

[(Optional) Configuring a Static MAC Address Entry](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0023c.html)

Using static MAC address entries to forward user packets helps reduce BUM traffic on the network and prevent bogus attacks.

[(Optional) Configuring a Limit on the Number of MAC Addresses Learned by an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan6_cfg_0021c.html)

MAC address learning limiting helps improve VXLAN network security.

[Verifying the Configuration of VXLAN in Distributed Gateway Mode Using BGP EVPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vxlan_cfg_1053.html)

After configuring VXLAN in distributed gateway mode using BGP EVPN, verify the configuration, and you can find that VXLAN tunnels are dynamically established and are in the Up state.