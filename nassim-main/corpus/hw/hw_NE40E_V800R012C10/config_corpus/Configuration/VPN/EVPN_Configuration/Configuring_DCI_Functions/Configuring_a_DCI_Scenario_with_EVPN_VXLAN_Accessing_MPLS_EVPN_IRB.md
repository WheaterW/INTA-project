Configuring a DCI Scenario with EVPN VXLAN Accessing MPLS EVPN IRB
==================================================================

In a DCI scenario with EVPN VXLAN accessing MPLS EVPN IRB, different cloud platforms are used for management. VXLAN tunnels are established to access the DCI backbone network, over which EVPN MPLS is used to carry Layer 3 services.

#### Context

DCGWs and DCI-PEs are separately deployed, and EVPN is used as the control plane protocol to establish VXLAN tunnels. A DCI-PE runs EVPN to learn a VM's IP route from a DC and sends the learned host IP route to the peer DCI-PE through a BGP EVPN peer relationship to implement Layer 3 service forwarding between VMs.

On the network shown in [Figure 1](#EN-US_TASK_0172370573__fig_dc_vrp_dci_cfg_002701), the DCGWs GW1 and GW2 are connected to the DCI backbone network with BGP EVPN configured. After BGP EVPN peer relationships and VXLAN tunnels are established between the DCGWs and the DCI-PEs, host IP routes can be exchanged between different DCs, implementing communication between VMs in different DCs.

**Figure 1** Configuring a DCI scenario with EVPN VXLAN accessing MPLS EVPN IRB  
![](images/fig_dc_vrp_dci_cfg_000501.png)

#### Pre-configuration Tasks

Before configuring a DCI scenario with VXLAN EVPN accessing MPLS EVPN IRB, ensure Layer 3 route reachability on the IPv4 network.


#### Procedure

1. Configure IGP on the DCI backbone network to ensure IP connectivity.
2. Configure a VXLAN tunnel between each DCI-PE and the corresponding gateway. For detailed configurations, see [Configuring VXLAN](dc_vrp_vxlan_cfg_1216.html).
3. Configure VPN instances to exchange routes with EVPN instances.
   
   
   
   For IPv4 services, configure an IPv4 L3VPN instance.
   
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      A VPN instance is created, and its view is displayed.
   2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      The VPN instance IPv4 address family is enabled, and its view is displayed.
   3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      An RD is configured for the VPN instance IPv4 address family.
   4. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      VPN targets are configured for the VPN instance IPv4 address family to exchange routes with the remote PE's L3VPN instance.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      VPN targets are configured for the VPN instance IPv4 address family to exchange routes with the local EVPN instance.
   6. Run [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable)
      
      EVPN is enabled to generate and advertise IP prefix and IRB routes.
   7. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
      
      EVPN routes that can be imported into the VPN instance IPv4 address family are associated with a tunnel policy.
   8. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance IPv4 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance view.
   
   For IPv6 services, configure an IPv6 L3VPN instance.
   
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      A VPN instance is created, and its view is displayed.
   2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      The VPN instance IPv6 address family is enabled, and its view is displayed.
   3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      An RD is configured for the VPN instance IPv6 address family.
   4. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      VPN targets are configured for the VPN instance IPv6 address family to exchange routes with the remote PE's L3VPN instance.
   5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      VPN targets are configured for the VPN instance IPv6 address family to exchange routes with the local EVPN instance.
   6. Run [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable)
      
      EVPN is enabled to generate and advertise IP prefix and IRB routes.
   7. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
      
      EVPN routes that can be imported into the VPN instance IPv6 address family are associated with a tunnel policy.
   8. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance IPv6 address family view.
   9. Run [**quit**](cmdqueryname=quit)
      
      Exit the VPN instance view.
4. Establish on the local DCI-PE a BGP EVPN peer relationship with the remote DCI-PE, and enable the local DCI-PE to advertise routes re-originated by the EVPN address family to the BGP EVPN peer.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      BGP is enabled, and its view is displayed.
   3. (Optional) Run [**router-id**](cmdqueryname=router-id) *ipv4-address*
      
      
      
      A BGP router ID is configured.
   4. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      The remote device is configured as a peer.
   5. (Optional) Run [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* **connect-interface** *interface-type* *interface-number* [ *ipv4-source-address* ]
      
      
      
      A source interface and a source IP address are specified to set up a TCP connection between the BGP peers.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If loopback interfaces are used to establish a BGP connection, it is recommended that the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command be run on both ends to ensure correct connection. If this command is run on only one end, the BGP connection may fail to be established.
   6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
      
      
      
      The device is enabled to exchange EVPN routes with a specified peer or peer group.
   8. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      
      
      The device is configured to add a re-origination flag to routes received from the BGP EVPN peer.
   9. Configure types of routes to be advertised:
      
      
      * If you want the network to carry only Layer 2 services, perform the following configurations:
        1. Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **mac** } command to configure the device to re-originate EVPN routes and advertise them to the BGP EVPN peer.
        2. Run the [**peer**](cmdqueryname=peer+advertise) { *ipv4-address* | *group-name* } **advertise** { **arp** | **nd** } command to configure the device to advertise ARP (ND) routes.
      * If you want the network to carry only Layer 3 services, perform the following configurations:
        1. Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** | **mac-ipv6** | **ipv6** } command to configure the device to re-originate EVPN routes and advertise them to the BGP EVPN peer.
        2. Run the [**peer**](cmdqueryname=peer+advertise) { *ipv4-address* | *group-name* } **advertise** { **irb** | **irbv6** } command to configure the device to advertise IRB/IRBv6 routes.
      * If you want the network to carry both Layer 2 and Layer 3 services, perform the following configurations:
        1. Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac** | **mac-ip** | **ip** | **mac-ipv6** | **ipv6** } command to configure the device to re-originate EVPN routes and advertise them to the BGP EVPN peer.
        2. Run the [**peer**](cmdqueryname=peer+advertise) { *ipv4-address* | *group-name* } **advertise** { **irb** | **irbv6** } command to configure the device to advertise IRB/IRBv6 routes.
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