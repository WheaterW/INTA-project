Configuring Route Import Across Address Families
================================================

In the BGP VPNv4/v6 address family, import remote EVPN IP prefix routes to generate VPNv4/v6 routes. In the EVPN address family, import remote VPNv4/v6 routes to generate EVPN IP prefix routes. Apply for SIDs in one-SID-per-route or one-SID-per-next-hop mode, so that traffic can be exchanged between the EVPN side and VPNv4/v6 side.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view of the ASBR.
   
   
   
   Perform the following steps to configure BGP VPNv4 and EVPN interworking.
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) command to enable the VPNv4 address family and enter its view.
   4. Run the [**import-rib evpn srv6 ip-prefix**](cmdqueryname=import-rib+evpn+srv6+ip-prefix) command to enable the function to import EVPN IP prefix routes into the BGP VPNv4 routing table.
   5. Run the [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target) command to cancel VPN target-based VPN route filtering. After this operation is performed, all VPN routes can be received.
   6. (Optional) Run the [**peer**](cmdqueryname=peer+next-hop-local) *ipv4-address* **next-hop-local** command to configure the device to set its IP address as the next hop of the routes to be advertised to the specified IBGP peer. If IBGP peers are configured on the network, you need to run this command.
   7. (Optional) Run the [**peer**](cmdqueryname=peer+reflect-client) *ipv4-address* **reflect-client** command to configure the device as an RR and its peer as an RR client. If IBGP peers are configured on the network, you need to run this command.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPNv4 address family view.
   9. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enable the EVPN address family and enter its view.
   10. Run the [**import-rib vpnv4 mpls**](cmdqueryname=import-rib+vpnv4+mpls) command to enable the function to import BGP VPNv4 routes into the EVPN routing table.
   11. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable the device to add the SID attribute to EVPN routes to be advertised.
   12. Run the [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target) command to cancel VPN target-based VPN route filtering. After this operation is performed, all VPN routes can be received.
   13. Run the [**segment-routing ipv6 apply-sid**](cmdqueryname=segment-routing+ipv6+apply-sid) **{ per-route | per-nexthop }** **[**import-rib**](cmdqueryname=import-rib)** **vpnv4** command to enable the function to apply for SIDs in one-SID-per-route or one-SID-per-next-hop mode for imported VPNv4 routes.
   14. (Optional) Run the [**peer**](cmdqueryname=peer+next-hop-local) *ipv6-address* **next-hop-local** command to configure the device to set its IP address as the next hop of the routes to be advertised to the specified IBGP peer. If IBGP peers are configured on the network, you need to run this command.
   15. (Optional) Run the [**peer**](cmdqueryname=peer+reflect-client) *ipv6-address* **reflect-client** command to configure the device as an RR, and its peer as an RR client. If IBGP peers are configured on the network, you need to run this command.
   16. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN address family view.
   17. Run the [**quit**](cmdqueryname=quit) command to exit the BGP instance view.
   18. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   Perform the following steps to configure BGP VPNv6 and EVPN interworking.
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6) command to enable the VPNv6 address family and enter its view.
   4. Run the [**import-rib evpn srv6 ip-prefix**](cmdqueryname=import-rib+evpn+srv6+ip-prefix) command to enable the function to import EVPN IP prefix routes into the BGP VPNv6 routing table.
   5. Run the [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target) command to cancel VPN target-based VPN route filtering. After this operation is performed, all VPN routes can be received.
   6. (Optional) Run the [**peer**](cmdqueryname=peer+next-hop-local) *ipv4-address* **next-hop-local** command to configure the device to set its IP address as the next hop of the routes to be advertised to the specified IBGP peer. If IBGP peers are configured on the network, you need to run this command.
   7. (Optional) Run the [**peer**](cmdqueryname=peer+reflect-client) *ipv4-address* **reflect-client** command to configure the device as an RR and its peer as an RR client. If IBGP peers are configured on the network, you need to run this command.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPNv6 address family view.
   9. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enable the EVPN address family and enter its view.
   10. Run the [**import-rib vpnv6 mpls**](cmdqueryname=import-rib+vpnv6+mpls) command to enable the function to import BGP VPNv6 routes into the EVPN routing table.
   11. Run the [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target) command to cancel VPN target-based VPN route filtering. After this operation is performed, all VPN routes can be received.
   12. Run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable the device to add the SID attribute to EVPN routes to be advertised.
   13. Run the [**segment-routing ipv6 apply-sid**](cmdqueryname=segment-routing+ipv6+apply-sid) **{ per-route | per-nexthop }** **[**import-rib**](cmdqueryname=import-rib)** **vpnv6** command to enable the function to apply for SIDs in one-SID-per-route or one-SID-per-next-hop mode for imported VPNv6 routes.
   14. (Optional) Run the [**peer**](cmdqueryname=peer) *ipv6-address* **next-hop-local** command to configure the device to set its IP address as the next hop of the routes to be advertised to the specified IBGP peer. If IBGP peers are configured on the network, you need to run this command.
   15. (Optional) Run the [**peer**](cmdqueryname=peer+reflect-client) *ipv6-address* **reflect-client** command to configure the device as an RR, and its peer as an RR client. If IBGP peers are configured on the network, you need to run this command.
   16. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN address family view.
   17. Run the [**quit**](cmdqueryname=quit) command to exit the BGP instance view.
   18. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.