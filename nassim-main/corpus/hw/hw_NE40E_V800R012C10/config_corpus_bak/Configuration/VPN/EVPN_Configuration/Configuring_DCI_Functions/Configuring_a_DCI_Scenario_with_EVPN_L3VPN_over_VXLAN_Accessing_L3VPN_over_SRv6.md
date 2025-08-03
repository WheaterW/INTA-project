Configuring a DCI Scenario with EVPN L3VPN over VXLAN Accessing L3VPN over SRv6
===============================================================================

In a DCI scenario with EVPN L3VPN over VXLAN accessing L3VPN over SRv6, different cloud platforms are used for management. VXLAN tunnels are established to access the DCI backbone network, over which L3VPN over SRv6 is used to carry Layer 3 services.

#### Context

DC GWs and DCI-PEs are separately deployed, and EVPN is used as the control plane protocol to establish VXLAN tunnels. A DCI-PE runs EVPN to learn a VM's host IP route information from a DC and uses VPNv4/VPNv6 to send received host IP routes to the peer DCI-PE, allowing VM host packets to be forwarded at Layer 3.

On the network shown in [Figure 1](#EN-US_TASK_0000001171084526__fig_dc_vrp_dci_cfg_000501), the DC GWs GW1 and GW2 are connected to the DCI backbone network with L3VPN over SRv6 configured. After EVPN and VXLAN tunnels are deployed between the DC GWs and DCI-PEs, host IP routes can be exchanged between different DCs, implementing communication between VMs in different DCs.

**Figure 1** Configuring a DCI scenario with EVPN L3VPN over VXLAN accessing L3VPN over SRv6  
![](figure/en-us_image_0000001216642915.png)

#### Procedure

1. Configure a VXLAN tunnel between each DCI-PE and the corresponding gateway. For configuration details, see [Configuring VXLAN](dc_vrp_vxlan_cfg_1216.html).
2. Configure L3VPNv4/L3VPNv6 over SRv6 on the DCI backbone network. For configuration details, see [Configuring L3VPNv4 over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0012.html) or [Configuring L3VPNv6 over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0251.html).
3. Configure DCI-PEs to send routes re-originated in the EVPN address family to a VPNv4/VPNv6 peer.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from the BGP EVPN peer.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** or [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   6. Configure the device to advertise routes re-originated by the BGP-EVPN address family to the VPNv4/VPNv6 peer.
      
      
      * Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv6-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** } command in the BGP VPNv4 address family view to enable the device to advertise routes re-originated in the BGP-EVPN address family to VPNv4 peers.
      * Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv6-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ipv6** | **ipv6** } command in the BGP VPNv6 address family view to enable the device to advertise routes re-originated in the BGP-EVPN address family to VPNv6 peers.
      
      
      
      After this step is performed, the DCI-PE re-originates the VXLAN-encapsulated EVPN routes received from the DC and then advertises them as SRv6-encapsulated VPNv4/VPNv6 routes to its VPNv4/VPNv6 peers on the DCI backbone network.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
4. Configure the DCI-PE to advertise routes re-originated in the VPNv4/VPNv6 address family to a BGP EVPN peer.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** or [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv6-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from VPNv4/VPNv6 peers.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
      
      
      
      The device is configured to advertise routes re-originated in the VPNv4/VPNv6 address family to a BGP EVPN peer.
      
      
      
      After this step is performed, the DCI-PE re-originates SRv6-encapsulated VPNv4/VPNv6 routes received from the DCI backbone network and then advertises them as VXLAN-encapsulated EVPN routes to its BGP EVPN peers on the DC side.
   7. Run [**peer**](cmdqueryname=peer+advertise+encap-type) { *ipv4-address* | *group-name* } **advertise encap-type vxlan**
      
      
      
      The device is configured to advertise VXLAN-encapsulated EVPN routes to DC-side EVPN peers.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
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