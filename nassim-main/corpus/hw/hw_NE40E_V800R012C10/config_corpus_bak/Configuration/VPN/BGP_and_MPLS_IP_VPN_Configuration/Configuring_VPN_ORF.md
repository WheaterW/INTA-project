Configuring VPN ORF
===================

After BGP peer relationships are established in the BGP-VPN-target address family, VPN ORF filters the routes to be advertised to PEs based on the VPN target of each VPN instance bound to each PE.

#### Usage Scenario

As a network increases in size and complexity, PEs receive larger numbers of routes. To enable PEs to receive only desired routes, thereby reducing pressure on the PEs, intra-AS RR, and ASBR, configure VPN ORF. After VPN ORF is configured, a device filters the routes to be advertised to a peer device based on the VPN targets of the VPN instance bound to the peer device.

The following uses the intra-AS RR scenario as an example to describe VPN ORF. On the network shown in [Figure 1](#EN-US_TASK_0172369419__fig_dc_vrp_mpls-l3vpn-v4_cfg_204501), before VPN ORF is enabled, the RR advertises all the VPN routes received from the VPN instances on PE1 to PE2. However, only the ERT 1:1 in these routes matches the IRT 1:1 of PE2. Similarly, the RR also advertises all the VPN routes received from the VPN instances on PE2 to PE1, and only the ERT 1:1 in these routes matches the IRT 1:1 of PE1. In this case, PE1 and PE2 both receive many unwanted routes. To prevent this issue, you can establish VPN ORF route-based peer relationships between the RR and PE1 and between the RR and PE2 in the BGP-VPN-target address family. The VPN ORF route-based peers negotiate the VPN ORF capability. Then, PE1 and PE2 send VPN ORF routes to their peer (the RR). These VPN ORF routes carry the IRTs of the expected routes and original AS numbers. Based on the received routes, the RR constructs an export policy. The RR learns the routes matching IRTs 1:1 and 2:2 from PE1 and the routes matching IRTs 1:1 and 3:3 from PE2. The RR advertises only the routes with ERT 1:1 to PE1 and PE2.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The implementation in an ASBR scenario is similar to that in an intra-AS RR scenario.


**Figure 1** Networking for VPN ORF  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_204501.png)

#### Pre-configuration Tasks

Before configuring VPN ORF, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).
* [Configure a basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) and establish VPNv4 connections.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  By default, VPN ORF is enabled for VPNv4 and VPNv6 after the BGP-VPN-target address family is configured. To disable VPN ORF, run the [**vpn-orf disable**](cmdqueryname=vpn-orf+disable) command.

#### Procedure

* Perform the following steps on the PE:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-target** command to enter the BGP-VPN-target address family view.
  4. Run the [**peer**](cmdqueryname=peer) { *peeripv4addr* | *peeripv6addr* | *group-name* } **enable** command to establish a VPN ORF peer relationship and enable the device to exchange VPN ORF routing information with the specified peer or peer group.
  5. (Optional) Run the [**timer wait-for-eor**](cmdqueryname=timer+wait-for-eor) *eor-time* command to configure the maximum period during which the BGP-VPN-target address family waits for the End-Of-RIB flag.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following steps on the RR:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-target** command to enter the BGP-VPN-target address family view.
  4. Run the [**peer**](cmdqueryname=peer) { *peeripv4addr* | *peeripv6addr* | *group-name* } **enable** command to establish a VPN ORF peer relationship and enable the device to exchange VPN ORF routing information with the specified peer or peer group.
  5. Run the [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **reflect-client** command to configure the local device as an RR and the specified peer or peer group as an RR client.
  6. (Optional) Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv4-address* | *group-name* } **allow-cluster-loop** [ *loop-number* ] command to set the maximum number of times the local cluster ID can be included in the Cluster\_List of each received route.
  7. (Optional) Run the [**peer**](cmdqueryname=peer) *ipv4-address* [**default-route-advertise**](cmdqueryname=default-route-advertise) command to configure the device to advertise default VPN ORF routes to the specified peer or peer group.
     
     
     
     If a device that does not support VPN ORF exists on the network, you can configure the RR to advertise the default VPN ORF route to the peer or peer group in the BGP-VPN-target address family view so that the RR can establish a VPN ORF route-based peer relationship with the specified peer or peer group. On the network shown in [Figure 1](#EN-US_TASK_0172369419__fig_dc_vrp_mpls-l3vpn-v4_cfg_204501), if PE2 does not support VPN ORF, run this command to enable the RR to send the default VPN ORF route to PE1. PE1 then sends all its local VPN routes to the RR. As a result, PE1 receives routes with the VPN target 1:1, and PE2 receives routes with the VPN targets 1:1 and 2:2.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following steps on the ASBR:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-target** command to enter the BGP-VPN-target address family view.
  4. Run the [**peer**](cmdqueryname=peer) { *peeripv4addr* | *peeripv6addr* | *group-name* } **enable** command to establish a VPN ORF peer relationship and enable the device to exchange VPN ORF routing information with the specified peer or peer group.
  5. (Optional) Run the [**external-path**](cmdqueryname=external-path) *path-number* command to set the maximum number of EBGP peers in the VPN-target address family.
     
     
     
     By default, after a BGP device receives VPN ORF routes with the same prefix from different peers, it selects one of these routes as the preferred route and advertises only VPN routes that match VPN ORF to the peer from which the preferred route is received. As a result, FRR and load balancing cannot be implemented. To enable FRR and load balancing between ASBRs, run this command to set the maximum number of EBGP peers allowed in the VPN-target address family.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After enabling VPN ORF, run the [**display bgp vpn-target routing-table**](cmdqueryname=display+bgp+vpn-target+routing-table) command to check route information in the BGP-VPN-target address family.

Run the [**display bgp vpnv4 routing-table**](cmdqueryname=display+bgp+vpnv4+routing-table) command to check information about BGP VPNv4 routes and BGP VPN routes.