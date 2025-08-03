Configuring the Static VXLAN Active-Active Scenario
===================================================

In the scenario where a DC is interconnected with an enterprise site, a CE is dual-homed to a VXLAN network. In this way, carriers can enhance VXLAN access reliability to improve the stability of user services so that rapid convergence can be implemented in case of a fault.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172363815__fig_dc_vrp_dci_cfg_000801), CE1 is dual-homed to PE1 and PE2. PE1 and PE2 use a virtual address as an NVE interface address at the network side, namely, an Anycast VTEP address. In this way, the CPE is aware of only one remote NVE interface. A VTEP address is configured on the CPE to establish a VXLAN tunnel with the Anycast VTEP address so that PE1, PE2, and the CPE can communicate.

The packets from the CPE can reach CE1 through either PE1 or PE2. However, single-homed CEs may exist, such as CE2 and CE3. As a result, after reaching a PE, the packets from the CPE may need to be forwarded by the other PE to a single-homed CE. Therefore, a bypass VXLAN tunnel needs to be established between PE1 and PE2.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before an IPv6 network is used to transmit traffic between a CPE and PE, an IPv4 over IPv6 tunnel must be configured between them. To enable a VXLAN tunnel to recurse routes to the IPv4 over IPv6 tunnel, static routes must be configured on the CPE and PE, and the outbound interface of the route destined for the VXLAN tunnel's destination IP address must be set to the IPv4 over IPv6 tunnel interface.


**Figure 1** Network diagram of configuring the static VXLAN active-active scenario  
![](images/fig_feature_image_0036023208.png)  


#### Procedure

1. Configure AC-side service access.
   1. Configure an Eth-Trunk interface on CE1 to dual-home CE1 to PE1 and PE2.
   2. Configure VXLAN service access points. For detailed configurations, see [Configuring a VXLAN Service Access Point](dc_vrp_vxlan6_cfg_0018b.html).
   3. Configure the same Ethernet Segment Identifier (ESI) for the links connecting CE1 to PE1 and PE2.
      
      
      1. Run the [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) command to enter the Eth-Trunk interface view.
      2. Run the [**esi**](cmdqueryname=esi) command to configure an ESI.
      3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure static VXLAN tunnels between the CPE and PEs. For detailed configurations, see [Configuring a VXLAN Tunnel](dc_vrp_vxlan_cfg_1214.html).
3. Configure a bypass VXLAN tunnel between PE1 and PE2.
   1. Configure a BGP EVPN peer relationship.
      
      
      1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enable BGP and enter the BGP view.
      2. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the peer device as a peer.
      3. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view.
      4. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **enable** command to enable the device to exchange EVPN routes with a specified peer or peer group.
      5. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise encap-type vxlan** command to advertise EVPN routes that carry the VXLAN encapsulation attribute to the peer.
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
        2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) [ **unicast** ] command to enable the IPv4 address family for a VPN instance.
        3. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the VPN instance.
        4. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] [ **evpn** ] command to configure VPN target for the EVPN instance.![](../../../../public_sys-resources/note_3.0-en-us.png) 
           
           The export VPN target of the local end must be the same as the import VPN target of the remote end, and the import VPN target of the local end must be the same as the export VPN target of the remote end.
        5. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance ipv4-family view.
        6. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
        7. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
        8. Run the [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode** command to create a VNI, associate the VNI with the BD, and apply split horizon to the BD.
        9. Run the [**quit**](cmdqueryname=quit) command to exit the BD view.
        10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   3. Enable the inter-chassis VXLAN function on PE1 and PE2.
      
      
      1. Run the [**evpn**](cmdqueryname=evpn) command to enter the EVPN view.
      2. Run the [**bypass-vxlan enable**](cmdqueryname=bypass-vxlan+enable) command to enable the inter-chassis VXLAN function.
      3. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN view.
      4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Configure ingress replication.
      
      
      1. Run the [**interface nve**](cmdqueryname=interface+nve) *nve-number* command to enter the NVE interface view.
      2. Run the [**source**](cmdqueryname=source) *ip-address* command to configure an IP address for the source VTEP.
      3. Run the [**vni**](cmdqueryname=vni) *vni-id* **head-end peer-list protocol bgp** command to enable ingress replication.
      4. Run the [**bypass source**](cmdqueryname=bypass+source) *ip-address* command to configure a source VTEP address for the bypass VXLAN tunnel.
      5. Run the [**mac-address**](cmdqueryname=mac-address) *mac-address* command to configure a VTEP MAC address.
      6. Run the [**quit**](cmdqueryname=quit) command to exit the NVE interface view.
      7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Configure FRR on the PEs.
   
   
   * Layer 2 communication
     
     1. Run the [**evpn**](cmdqueryname=evpn) command to enter the EVPN view.
     2. Run the [**vlan-extend private**](cmdqueryname=vlan-extend+private) **enable** command to enable the routes to be advertised to a peer to carry the newly added VLAN extended community attribute.
     3. Run the [**vlan-extend redirect**](cmdqueryname=vlan-extend+redirect) **enable** command to enable the function of redirecting the received routes that carry the VLAN private extended community attribute.
     4. Run the [**local-remote frr enable**](cmdqueryname=local-remote+frr+enable) command to enable FRR for MAC routes between the local and remote ends.â
     5. Run the [**quit**](cmdqueryname=quit) command to exit the EVPN view.
     6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Layer 3 communication
     
     1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
     2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enable the BGP-VPN instance IPv4 address family and enter the address family view.
     3. Run the [**auto-frr**](cmdqueryname=auto-frr) command to enable BGP auto FRR.
     4. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **as-number** *as-number* command to enable the function of exchanging EVPN routes with a specified peer or peer group. The IP address is a CE address.
     5. Run the [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) command to enable the VPN instance to advertise EVPN IP prefix routes.
     6. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-VPN instance IPv4 address family view.
     7. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
     8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. (Optional) Configure a UDP port on the PEs to prevent the receiving of duplicate packets.
   1. Run the [**evpn enhancement port**](cmdqueryname=evpn+enhancement+port) *port-id* command to configure a UDP port.
      
      
      
      The same UDP port number must be set for the PEs in the active state.
   2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
6. (Optional) Configure a VXLAN over IPsec tunnel between the CPE and PE to enhance the security for packets traversing an insecure network.
   
   
   
   For detailed configurations, see [Example for Configuring VXLAN over IPsec](dc_vrp_ipsec_cfg_0036.html).

#### Verifying the Configuration

After configuring the VXLAN active-active scenario, check information on the VXLAN tunnel, VNI status, and VBDIF. For detailed configurations, see [Verifying the Configuration of VXLAN in Distributed Gateway Mode Using BGP EVPN](dc_vrp_vxlan_cfg_1053.html).