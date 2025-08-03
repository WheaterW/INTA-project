Configuring Interworking Between L3VPN HoVPN and EVPN L3VPN over SRv6
=====================================================================

During the evolution from L3VPN HoVPN to EVPN L3VPN over SRv6, these two types of services may coexist. In this case, you need to configure interworking between an L3VPN HoVPN and an EVPN L3VPN over SRv6.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0289315208__fig1258918722520), a traditional L3VPN HoVPN is deployed between the UPEs and SPEs, and an EVPN L3VPN over SRv6 is deployed between the SPEs and NPEs. In this case, you need to configure each SPE for interworking between the L3VPN HoVPN and the EVPN L3VPN over SRv6.

**Figure 1** Interworking between L3VPN HoVPN and EVPN L3VPN over SRv6  
![](figure/en-us_image_0289520887.png)

#### Pre-configuration Tasks

Before configuring interworking between L3VPN HoVPN and EVPN L3VPN over SRv6, complete the following tasks:

* Configure an IGP between UPEs and SPEs and between SPEs and NPEs to implement network-layer connectivity.
* Configure an L3VPN HoVPN between the UPEs and SPEs. For details, see [Configuring an HoVPN](dc_vrp_mpls-l3vpn-v4_cfg_0165.html).
* Complete the task of [Configuring EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0252.html), [Configuring EVPN L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy.html), or [Configuring EVPN L3VPNv6 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpnv6_over_srv6-te_policy.html) between the SPEs and NPEs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family vpnv4**](cmdqueryname=ipv4-family+vpnv4) or [**ipv6-family vpnv6**](cmdqueryname=ipv6-family+vpnv6)
   
   
   
   The BGP-VPNv4 or BGP-VPNv6 address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+import+reoriginate) *ipv4-address* **import** **reoriginate** or [**peer**](cmdqueryname=peer+import+reoriginate) *group-name* **import** **reoriginate**
   
   
   
   The device is enabled to add the re-origination flag to VPNv4 or VPNv6 routes received from UPEs that function as peers.
   
   The *ipv4-address* parameter specifies the IP address of a UPE peer, and the *group-name* parameter specifies the name of a UPE peer group.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP-EVPN address family view is displayed.
7. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) *peerIpv6Addr* **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** } or [**peer**](cmdqueryname=peer+advertise+route-reoriginated) *peerGroupName* **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
   
   
   
   The device is enabled to re-originate the VPNv4 or VPNv6 routes received from UPEs into EVPN routes and advertise them to NPEs.
   
   The *peerIpv6Addr* parameter specifies the IP address of an NPE peer, and the *peerGroupName* parameter specifies the name of an NPE peer group.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on a UPE or NPE to check the VPN routing table. The command output shows the default routes or specific routes sent by the remote ends.
* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) **prefix-route** command on an NPE to check the EVPN IP prefix routing table. The command output shows the IP prefix routes sent from the remote ends.