Configuring the Dynamic IPv6 VXLAN Active-Active Scenario
=========================================================

In scenarios where an IPv6-based DC is interconnected with an enterprise site, a CE can be dual-homed to an IPv6 VXLAN to implement rapid convergence if a fault occurs, thereby enhancing access reliability and improving service stability.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0229407978__fig_dc_vrp_dci_cfg_000801), CE1 is dual-homed to PE1 and PE2. Both PEs use the same virtual address as an NVE interface address (namely, an Anycast VTEP address) at the network side. In this way, the CPE is aware of only one remote VTEP address. To allow the CPE to communicate with PE1 and PE2, a VTEP address must be configured on the CPE to establish an IPv6 VXLAN tunnel with the anycast VTEP address.

The packets from the CPE can reach CE1 through either PE1 or PE2. However, when a single-homed CE (CE2 and CE3 in this example) exists on the network, the packets from the CPE to the single-homed CE may need to detour to the other PE after reaching one PE. To ensure PE1-PE2 reachability, a bypass VXLAN tunnel must be established between PE1 and PE2.

**Figure 1** Network diagram of configuring the dynamic IPv6 VXLAN active-active scenario  
![](figure/en-us_image_0229675116.png)  


#### Procedure

1. Configure AC-side service access. 
   1. Configure an Eth-Trunk interface on CE1 to dual-home CE1 to PE1 and PE2.
   2. Configure VXLAN service access points. For detailed configurations, see [Configuring a VXLAN Service Access Point](dc_vrp_vxlan6_cfg_0007.html).
   3. Configure the same Ethernet Segment Identifier (ESI) for the links connecting PE1 and PE2 to CE1. 
      
      
      1. Run the [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) command to enter the Eth-Trunk interface view.
      2. Run the [**esi**](cmdqueryname=esi)*esi* command to configure an ESI.
      3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure an IPv6 VXLAN tunnel between the CPE and each PE using BGP EVPN. For detailed configurations, see [Configuring an IPv6 VXLAN Tunnel](dc_vrp_vxlan6_cfg_0008.html).
3. Configure a bypass VXLAN tunnel between PE1 and PE2.
   1. Configure a BGP EVPN peer relationship.
      
      
      1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enable BGP and enter the BGP view.
      2. Run the [**peer**](cmdqueryname=peer+as-number+%28BGP+view%29+%28IPv6%29) *ipv6-address* **as-number** *as-number* command to specify an IPv6 peer.
      3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view.
      4. Run the [**peer**](cmdqueryname=peer+enable+%28BGP-EVPN+address+family+view%29+%28IPv6%29) { *group-name* | *ipv6-address* } **enable** command to enable the device to exchange EVPN routes with a specified peer or peer group.
      5. Run the [**peer**](cmdqueryname=peer+advertise+encap-type) { *group-name* | *ipv6-address* } **advertise encap-type vxlan** command to enable the device to advertise EVPN routes that carry the VXLAN encapsulation attribute to the peer or peer group.
      6. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-EVPN address family view.
      7. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
      8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   2. Configure a VPN instance or EVPN instance.
      
      
      * Layer 2 communication (Configure an EVPN instance.)
        
        1. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to create a BD EVPN instance and enter the EVPN instance view.
        2. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the EVPN instance.
        3. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the EVPN instance.![](../../../../public_sys-resources/note_3.0-en-us.png) 
           
           The export VPN target of the local end must be the same as the import VPN target of the remote end, and the import VPN target of the local end must be the same as the export VPN target of the remote end.
        4. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN instance view.
        5. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
        6. Run the [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode** command to create a VNI, associate the VNI with the BD, and specify split horizon for packet forwarding.
        7. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* [ **bd-tag** *bd-tag* ] command to bind a specified EVPN instance to the BD. By specifying different *bd-tag* values, you can bind multiple BDs to the same EVPN instance. In this way, VLAN services of different BDs can access the same EVPN instance while being isolated.
        8. Run the [**quit**](cmdqueryname=quit) command to exit the BD view.
        9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
      * Layer 3 communication (Configure a VPN instance.)
        
        1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter the VPN instance view.
        2. Run the [**ipv6-family**](cmdqueryname=ipv6-family) [ **unicast** ] command to enable the IPv6 address family for a VPN instance.
        3. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the VPN instance.
        4. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] [ **evpn** ] command to configure VPN target for the EVPN instance.![](../../../../public_sys-resources/note_3.0-en-us.png) 
           
           The import and export VPN targets of the local end must be the same as the export and import VPN targets of the remote end, respectively.
        5. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance ipv4-family view.
        6. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
        7. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
        8. Run the [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode** command to create a VNI, associate the VNI with the BD, and apply split horizon to the BD.
        9. Run the [**quit**](cmdqueryname=quit) command to exit the BD view.
        10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   3. Configure an EVPN instance.
      
      
      1. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to create a BD EVPN instance and enter its view.
      2. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the EVPN instance.
      3. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the EVPN instance. The import and export VPN targets of the local end must be the same as the export and import VPN targets of the remote end, respectively.
      4. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN instance view.
      5. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
      6. Run the [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode** command to create a VNI, associate the VNI with the BD, and apply split horizon to the BD.
      7. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* [ **bd-tag** *bd-tag* ] command to bind a specified EVPN instance to the BD. By specifying different *bd-tag* values, you can bind multiple BDs to the same EVPN instance. In this way, VLAN services of different BDs can access the same EVPN instance while being isolated.
      8. Run the [**quit**](cmdqueryname=quit) command to exit the BD view.
      9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Enable the inter-chassis VXLAN function on PE1 and PE2. 
      
      
      1. Run the [**evpn**](cmdqueryname=evpn) command to enter the EVPN view.
      2. Run the [**bypass-vxlan enable**](cmdqueryname=bypass-vxlan+enable) command to enable the inter-chassis VXLAN function.
      3. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN view.
      4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   5. Configure ingress replication.
      
      
      1. Run the [**interface nve**](cmdqueryname=interface+nve) *nve-number* command to enter the NVE interface view.
      2. Run the [**source**](cmdqueryname=source+%28NVE+interface+view%29+%28IPv6%29) *ipv6-address* command to configure an IPv6 address for the source VTEP.
      3. Run the [**vni**](cmdqueryname=vni) *vni-id* **head-end peer-list protocol bgp** command to enable ingress replication.
      4. Run the [**bypass source**](cmdqueryname=bypass+source+%28ipv6-address%29) *ipv6-address* command to configure a source VTEP IPv6 address for the bypass VXLAN tunnel.
      5. Run the [**mac-address**](cmdqueryname=mac-address) *mac-address* command to configure a MAC address for the VTEP.
      6. Run the [**quit**](cmdqueryname=quit) command to exit the NVE interface view.
      7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Configure FRR on each PE. 
   
   
   * For Layer 2 communication:
     
     1. Run the [**evpn**](cmdqueryname=evpn) command to enter the EVPN view.
     2. Run the [**vlan-extend private enable**](cmdqueryname=vlan-extend+private+enable) command to enable the routes to be sent to a peer to carry the VLAN private extended community attribute.
     3. Run the [**vlan-extend redirect enable**](cmdqueryname=vlan-extend+redirect+enable) command to enable the function of redirecting the received routes that carry the VLAN private extended community attribute.
     4. Run the [**local-remote frr enable**](cmdqueryname=local-remote+frr+enable) command to enable FRR for MAC routes between the local and remote ends.â
     5. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN view.
     6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * For Layer 3 communication:
     
     1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     2. Run the [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv6 address family view.
     3. Run the [**auto-frr**](cmdqueryname=auto-frr) command to enable BGP auto FRR.
     4. Run the [**peer**](cmdqueryname=peer+as-number+%28BGP-VPN+instance+IPv6+address+family+view%29+%28IPv6%29) { *ipv6-address* | *group-name* } **as-number** *as-number* command to specify a peer IP address and the number of the AS where the peer resides.
     5. Run the [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) command to enable the VPN instance to advertise EVPN IP prefix routes.
     6. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPN instance IPv6 address family view.
     7. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
     8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring a dynamic IPv6 VXLAN active-active scenario, verify the configuration.

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | [ *bd-id* [ **brief** | **verbose** | **binding-info** ] ] ] command to check BD configurations.
* Run the [**display interface nve**](cmdqueryname=display+interface+nve) [ *nve-number* | **main** ] command to check NVE interface information.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) command to check EVPN instance information.
* Run the [**display bgp**](cmdqueryname=display+bgp) **evpn peer** [ [ *ipv6-address* ] **verbose** ] command to check information about BGP EVPN peers.
* Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) [ **vni** *vni-id* ] command to check the ingress replication lists of all VNIs or a specified one.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check IPv6 VXLAN tunnel information.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) [ *vni-id* [ **verbose** ] ] command to check IPv6 VXLAN configurations and the VNI status.