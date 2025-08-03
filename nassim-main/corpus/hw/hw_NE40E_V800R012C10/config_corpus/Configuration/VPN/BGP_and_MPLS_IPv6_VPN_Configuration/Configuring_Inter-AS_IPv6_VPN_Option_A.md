Configuring Inter-AS IPv6 VPN Option A
======================================

In inter-AS IPv6 VPN Option A, an ASBR views the peer ASBR as a CE and uses EBGP+ to advertise IPv6 routes to the peer ASBR.

#### Usage Scenario

If the MPLS backbone network carrying IPv6 VPN routes spans multiple ASs, the inter-AS VPN solution is required.

If the number of VPNs that access PEs and the number of IPv6 VPN routes are small, inter-AS VPN Option A is recommended. In inter-AS VPN Option A, ASBRs are required to support VPN instances so that they will be capable of managing IPv6 VPN routes. In addition, ASBRs need provide dedicated interfaces for inter-AS IPv6 VPNs, which can be sub-interfaces or physical interfaces. Therefore, the requirement for ASBRs' performance is rather high, but no inter-AS configurations need to be performed on ASBRs.


#### Pre-configuration Tasks

Before configuring inter-AS VPN Option A, complete the following tasks:

* Configure an IGP for the MPLS backbone network in each AS for IP connectivity of the backbone network in each AS.
* Enable MPLS on the PEs and ASBRs.
* Establish tunnels (LSPs, MPLS TE tunnels, or SR-MPLS TE tunnels) between PEs and ASBRs in the same AS.
* Enable IPv6 on interfaces to be configured with IPv6 addresses.

#### Procedure

1. Configure a basic BGP/MPLS IPv6 VPN for each AS. For details, see [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).
2. Configure ASBRs in different ASs to view each other as a CE.
3. Configure an IPv6-address-family-supporting VPN instance on each PE and ASBR. For configuration details, see [Configuring a VPN Instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html).
   
   
   
   After the configurations are complete, the PEs can access their attached CEs, and ASBRs in different ASs can access each other.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In inter-AS VPN Option A, on the same IPv6 VPN, the VPN targets of the IPv6-address-family-supporting VPN instances of the ASBR and PE that are in the same AS must match. This is not required for the PEs in different ASs.

#### Checking the Configurations

After completing the configurations, run the following commands to check the configurations:

Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **all** **peer** command on the PE or ASBR to check information about BGP peer relationships.

Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) **all** **routing-table** command on the PE or ASBR to check VPNv6 routing information.

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) [ *vpn-instance-name* ] command on the PE or ASBR to check the routing table of the VPN instance IPv6 address family.