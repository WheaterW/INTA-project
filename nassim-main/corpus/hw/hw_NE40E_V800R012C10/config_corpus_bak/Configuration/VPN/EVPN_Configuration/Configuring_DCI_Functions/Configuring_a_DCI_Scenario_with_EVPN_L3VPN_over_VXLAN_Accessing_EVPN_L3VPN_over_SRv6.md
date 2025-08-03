Configuring a DCI Scenario with EVPN L3VPN over VXLAN Accessing EVPN L3VPN over SRv6
====================================================================================

In a DCI scenario with EVPN L3VPN over VXLAN accessing EVPN L3VPN over SRv6, different cloud platforms are used for management. VXLAN tunnels are established to access the DCI backbone network, over which EVPN L3VPN over SRv6 is used to carry Layer 3 services.

#### Context

DC GWs and DCI-PEs are separately deployed, and EVPN is used as the control plane protocol to establish VXLAN tunnels. A DCI-PE runs EVPN to learn a VM's host IP route information from a DC and uses EVPN L3VPN over SRv6 to send received host IP routes to the peer DCI-PE, allowing VM host packets to be forwarded at Layer 3.

On the network shown in [Figure 1](#EN-US_TASK_0000001171403020__fig_dc_vrp_dci_cfg_000501), the DC GWs GW1 and GW2 are connected to the DCI backbone network with EVPN L3VPN over SRv6 configured. After EVPN and VXLAN tunnels are deployed between the DC GWs and DCI-PEs, host IP routes can be exchanged between different DCs, implementing communication between VMs in different DCs.

**Figure 1** Configuring a DCI scenario with EVPN L3VPN over VXLAN accessing EVPN L3VPN over SRv6  
![](figure/en-us_image_0000001216884345.png)

#### Procedure

1. Configure a VXLAN tunnel between each DCI-PE and the corresponding gateway. For configuration details, see [Configuring VXLAN](dc_vrp_vxlan_cfg_1216.html).
2. Configure basic EVPN L3VPN over SRv6 functions on the DCI backbone network. For configuration details, see [Configuring EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_evpn_cfg_0152_copy.html).
3. Configure each DCI-PE to advertise re-originated routes to its BGP EVPN peer.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is enabled to add a re-origination flag to EVPN routes received from the DC.
   4. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **ip** | **ipv6** }
      
      
      
      The device is configured to advertise re-originated routes to its BGP EVPN peer (remote PE).
      
      
      
      After this step is performed, the DCI-PE re-originates the VXLAN-encapsulated EVPN routes received from the DC and then advertises them as SRv6-encapsulated EVPN routes to its BGP EVPN peers on the DCI backbone network.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
4. Configure each DCI-PE to advertise re-originated routes to its DC-side BGP EVPN peers.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is enabled to add a re-origination flag to EVPN routes received from the peer DCI-PE.
   4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** | **mac-ipv6** | **ipv6** }
      
      
      
      The device is configured to advertise re-originated routes to its DC-side BGP EVPN peers.
      
      
      
      After this step is performed, if a DCI-PE receives SRv6-encapsulated EVPN routes from a BGP EVPN peer on the DCI backbone network, the DCI-PE re-originates the EVPN routes and advertises them as VXLAN-encapsulated EVPN routes to its DC-side BGP EVPN peers.
   5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise encap-type vxlan**
      
      
      
      The device is configured to advertise VXLAN-encapsulated EVPN routes to DC-side EVPN peers.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
5. Enable EVPN route advertisement in the BGP-VPN instance address family view.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**ipv4-family vpn-instance**](cmdqueryname=ipv4-family+vpn-instance) *vpn-instance-name* or [**ipv6-family vpn-instance**](cmdqueryname=ipv6-family+vpn-instance) *vpn-instance-name*
      
      
      
      The BGP VPN instance IPv4/IPv6 address family view is displayed.
   3. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
      
      
      
      The device is configured to advertise the host IPv4/IPv6 routes in the VPN instance as EVPN IPv4/IPv6 prefix routes.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.