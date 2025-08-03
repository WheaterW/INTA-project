Configuring DCI Functions
=========================

This section describes how to configure Data Center Interconnect (DCI) functions, which helps you understand basic DCI information.

#### Context

To meet the requirements of inter-regional operations, user access, geographical redundancy, and other scenarios, an increasing number of enterprises deploy DCs across regions and carrier networks. Currently, leased fibers or leased lines are often used for DCs to communicate across regions, bringing the following problems:

* For enterprises, the leasing prices are too high, increasing the burden of enterprises.
* For carriers, service expansion is difficult, and resource utilization is low.

Therefore, it is important to build and operate secure and reliable DCI networks that are capable of flexible scheduling. DCI allows communication between VMs in different DCs. DCI runs on carrier networks. It uses technologies such as Virtual eXtensible Local Area Network (VXLAN), Ethernet Virtual Private Network (EVPN), and BGP/MPLS IP VPN to ensure secure and reliable transmission of packets received from DCs over carrier networks, ensuring communication between VMs in different DCs.

**Figure 1** Configuring DCI functions  
![](images/fig_dc_vrp_dci_cfg_000201.png)  


#### Pre-configuration Tasks

Before configuring DCI functions, complete the following task:

Configure MPLS tunnels on the DCI backbone network.


[Configuring E2E VXLAN EVPN in a DCI scenario with Gateways Deployed](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0003.html)

An end-to-end VXLAN EVPN uses the same service platform, which helps implement unified VXLAN VNI resource management.

[Configuring a DCI Scenario with a VLAN Layer 3 Sub-interface Accessing a Common L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0004.html)

The DCI Scenario with a VLAN Layer 3 Sub-interface Accessing a Common L3VPN uses different cloud management platforms, and a Layer 3 Ethernet sub-interface is associated with a VLAN to access an L3VPN.

[Configuring a DCI Scenario with EVPN L3VPN over VXLAN Accessing Common L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0005.html)

The DCI scenario with EVPN L3VPN over VXLAN accessing common L3VPN involves different cloud management platforms, and a VXLAN tunnel is used to access the DCI backbone network.

[Configuring a DCI Scenario with VLAN Base Accessing MPLS EVPN IRB](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0029.html)

In a DCI scenario, to enable a DCI network to carry Layer 2 or Layer 3 services, you can associate Ethernet sub-interfaces with VLANs for gateway or DCN access and configure EVPN IRB.

[Configuring a DCI Scenario with EVPN VXLAN Accessing MPLS EVPN IRB](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0027.html)

In a DCI scenario with EVPN VXLAN accessing MPLS EVPN IRB, different cloud platforms are used for management. VXLAN tunnels are established to access the DCI backbone network, over which EVPN MPLS is used to carry Layer 3 services.

[Configuring a DCI Scenario with EVPN L3VPN over VXLAN Accessing EVPN L3VPN over SRv6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0045.html)

In a DCI scenario with EVPN L3VPN over VXLAN accessing EVPN L3VPN over SRv6, different cloud platforms are used for management. VXLAN tunnels are established to access the DCI backbone network, over which EVPN L3VPN over SRv6 is used to carry Layer 3 services.

[Configuring a DCI Scenario with EVPN L3VPN over VXLAN Accessing L3VPN over SRv6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0046.html)

In a DCI scenario with EVPN L3VPN over VXLAN accessing L3VPN over SRv6, different cloud platforms are used for management. VXLAN tunnels are established to access the DCI backbone network, over which L3VPN over SRv6 is used to carry Layer 3 services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dci_cfg_0009.html)

After configuring the DCI solution, check the VPN instance, EVPN instance, VXLAN tunnel, and other configurations.