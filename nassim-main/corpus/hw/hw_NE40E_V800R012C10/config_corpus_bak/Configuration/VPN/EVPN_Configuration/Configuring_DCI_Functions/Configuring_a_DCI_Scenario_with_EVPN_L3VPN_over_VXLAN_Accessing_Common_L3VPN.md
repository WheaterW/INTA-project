Configuring a DCI Scenario with EVPN L3VPN over VXLAN Accessing Common L3VPN
============================================================================

The DCI scenario with EVPN L3VPN over VXLAN accessing common L3VPN involves different cloud management platforms, and a VXLAN tunnel is used to access the DCI backbone network.

#### Context

Gateways and DCI-PEs are separately deployed. EVPN is used as the control plane protocol to dynamically establish VXLAN tunnels. A DCI-PE runs EVPN to learn a VM's host IP route information from a DC and uses VPNv4/VPNv6 to send received host IP routes to the peer DCI-PE, allowing VM host packets to be forwarded at Layer 3.

In [Figure 1](#EN-US_TASK_0172363953__fig_dc_vrp_dci_cfg_000501), DC gateways GW1 and GW2 connect to the DCI backbone network. To enable inter-DC VM communication, BGP/MPLS IPv4/IPv6 VPN functions are deployed on the DCI backbone network, and EVPN and VXLAN tunnels are deployed between the gateways and DCI-PEs to transmit VM host IP routes.

**Figure 1** Configuring a DCI scenario with EVPN L3VPN over VXLAN accessing common L3VPN  
![](images/fig_dc_vrp_dci_cfg_000501.png)

#### Procedure

1. Configure a VXLAN tunnel between each DCI-PE and the corresponding gateway. For detailed configurations, see [Configuring VXLAN](dc_vrp_vxlan_cfg_1216.html).
2. Configure basic L3VPN functions on the DCI backbone network. For detailed configurations, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) or [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).
3. Configure DCI-PEs to send routes re-originated in the EVPN address family to a VPNv4/VPNv6 peer.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from a BGP EVPN peer.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   5. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** or [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** | **mac-ipv6** | **ipv6** }
      
      
      
      The device is configured to send routes re-originated in the EVPN address family to a VPNv4/VPNv6 peer.
      
      After the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** | **mac-ipv6** | **ipv6** } command is run and EVPN routes received from the DC side and carrying the VXLAN encapsulation attribute are re-originated on the DCI-PE, the DCI-PE advertises VPNv4/VPNv6 routes that carry the MPLS encapsulation attribute to the VPNv4/VPNv6 peer on the DCI backbone network.
4. Configure the DCI-PE to send routes re-originated in the VPNv4/VPNv6 address family to a BGP EVPN peer.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** or [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
      
      
      
      The BGP-VPNv4/VPNv6 address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from a VPNv4/VPNv6 peer.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
   5. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   6. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
      
      
      
      The device is configured to send routes re-originated in the VPNv4/VPNv6 address family to a BGP EVPN peer.
      
      
      
      After the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** } command is run and VPNv4/VPNv6 routes received from the DCI backbone network and carrying the MPLS encapsulation attribute are re-originated on the DCI-PE, the DCI-PE advertises EVPN routes that carry the VXLAN encapsulation attribute to the BGP EVPN peer in the DC.
   7. Run [**peer**](cmdqueryname=peer+advertise+encap-type) { *ipv4-address* | *group-name* } **advertise encap-type vxlan**
      
      
      
      EVPN routes that carry the VXLAN encapsulation attribute are sent to the EVPN peer on the DC side.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
5. (Optional) Configure AC access to the DCI backbone network on the DCI-PE. This enables flexible device deployment on the network.
   1. Run [**evpn**](cmdqueryname=evpn)
      
      
      
      The EVPN global configuration view is displayed.
   2. Run [**dci local-route advertise-to-mpls**](cmdqueryname=dci+local-route+advertise-to-mpls)
      
      
      
      The device is enabled to advertise local routes carrying the VXLAN attribute based on the encapsulation type on the peer end.
   3. Run [**advertise vxlan-tunnel mac**](cmdqueryname=advertise+vxlan-tunnel+mac)
      
      
      
      The function to advertise MAC routes learned from the static VXLAN side based on the encapsulation type on the peer end is enabled.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the EVPN global configuration view.
   5. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
      
      
      
      The view of the BD to be bound to the EVPN instance is displayed.
   6. Run [**vxlan vni vni-id split-horizon-mode**](cmdqueryname=vxlan+vni+vni-id+split-horizon-mode)
      
      
      
      A VNI is created and bound to a BD, and split horizon is configured for packet forwarding.
   7. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* [ **bd-tag** *bd-tag* ]
      
      
      
      The BD is bound to an EVPN instance. By specifying different **bd-tag** values, you can bind multiple BDs to the same EVPN instance. In this way, VLAN services of different BDs can access the same EVPN instance while remaining isolated.
   8. Run [**evpn-dci support ac-access**](cmdqueryname=evpn-dci+support+ac-access)
      
      
      
      AC access is configured on the interworking node.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BD view.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.