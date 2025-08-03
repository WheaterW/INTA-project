Configuring the Device to Filter ARP or ND Entries When Advertising VPN Vlink Direct Routes
===========================================================================================

This section describes how to configure a device to filter ARP or ND entries when advertising VPN Vlink direct routes in a scenario where EVPN and L3VPN coexist. This configuration prevents the device from advertising the routes generated based on the ARP or ND entries that are filtered out.

#### Usage Scenario

During network evolution, some devices may be EVPN-ready, whereas other devices support only traditional functions, such as L3VPN, but not yet EVPN-ready. For example, on the network shown in [Figure 1](#EN-US_TASK_0000001324938557__fig_dc_vrp_ip-route_cfg_005501), CE1, CE2, and CE3 are access devices at different sites. CE1 is dual-homed to gateway devices PE1 and PE2. PE1, PE2, and PE3 are EVPN-ready gateways, whereas PE4 is still a traditional device. PE1, PE2, and PE3 run EVPN and implement Layer 2 and Layer 3 service interworking for the access devices. In addition, PE1, PE2, and PE4 run traditional L2VPN and L3VPN and implement Layer 2 and Layer 3 service interworking for the access devices. CE1 accesses PE1 and PE2 through Layer 2 sub-interfaces, and the same gateway address is configured for corresponding VBDIF interfaces on PE1 and PE2. CE1 accesses PE1 and PE2 in dual-homing single-active mode. PE1 is the master device, whereas PE2 is the backup device. PE1 learns the dynamic ARP entry of HOST1 and sends the ARP entry to PE2 through an EVPN IRB route for backup. PE2 then generates a remote dynamic ARP entry of HOST1. PE1 and PE2 generate Vlink routes based on the ARP entries and send VPNv4 host routes to PE4. After receiving these routes, PE4 selects one of them based on route priorities. If the route received from PE2 is selected, traffic travels along the path CE3 -> PE4 -> PE2 -> PE1 -> CE1 (with a detour to PE2) for a long time. Because EVPN does not generate IRB routes based on remote dynamic ARP entries, PE3 can receive the EVPN IRB route only from PE1, and the route is used to guide Layer 3 forwarding. Therefore, traffic from CE2 to CE1 passes through CE2 -> PE3 -> PE1 -> CE1, without a detour to PE2. To prevent a detour, configure PE2 to filter out single-active and redirection ARP entries so that it does not advertise the routes generated based on these entries. In this way, PE4 will not receive the route advertised by PE2, preventing return traffic from detouring to PE2.

**Figure 1** Coexistence of EVPN dual-homing single-active and L3VPN  
![](figure/en-us_image_0000001324738481.png)

#### Procedure

* Enable the device to filter ARP entries when advertising Vlink routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     A VPN instance is created and its view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
  4. Run [**arp vlink-direct-route advertise-filter single-active-redirect**](cmdqueryname=arp+vlink-direct-route+advertise-filter+single-active-redirect)
     
     
     
     The device is enabled to filter ARP entries when advertising Vlink routes.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable the device to filter ND entries when advertising Vlink routes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     A VPN instance is created and its view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The IPv6 address family is enabled for the VPN instance, and the VPN instance IPv6 address family view is displayed.
  4. Run [**nd vlink-direct-route advertise-filter single-active-redirect**](cmdqueryname=nd+vlink-direct-route+advertise-filter+single-active-redirect)
     
     
     
     The device is enabled to filter ND entries when advertising Vlink routes.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After enabling the device to filter ARP entries when advertising Vlink routes, run the [**display ip routing-table all-vpn-instance**](cmdqueryname=display+ip+routing-table+all-vpn-instance) **verbose** command to check information about VPN Vlink direct routes.

After enabling the device to filter ND entries when advertising Vlink routes, run the [**display ipv6 routing-table all-vpn-instance**](cmdqueryname=display+ipv6+routing-table+all-vpn-instance) **verbose** command to check information about VPN Vlink direct routes.