Configuring Segment VXLAN to Implement Layer 2 Interworking (Mapping VNI Mode)
==============================================================================

Configuring Segment VXLAN to Implement Layer 2 Interworking (Mapping VNI Mode)

#### Prerequisites

Before configuring segment VXLAN for Layer 2 interworking (mapping VNI mode), you have completed the following tasks:

* Configure BGP EVPN to establish one VXLAN tunnel in DC A and another one in DC B.
  + If the underlay network is an IPv4 network, see [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1066.html).
  + If the underlay network is an IPv6 network, see [Establishing IPv6 VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan6_cfg_1066.html).
* Enable EVPN as the VXLAN control plane on DC border leaf nodes, configure BGP EVPN peer relationships, and configure EVPN instances.
  + If the underlay network is an IPv4 network, see [Configuring a VXLAN Tunnel](../dc/dc_vrp_vxlan_cfg_1090.html).
  + If the underlay network is an IPv6 network, see [Configuring an IPv6 VXLAN Tunnel](../dc/dc_vrp_vxlan6_cfg_1090.html).

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001259707903__fig_dc_vrp_vxlan_cfg_120301), one VXLAN tunnel needs to be configured within DC A, one within DC B, and one between the transit leaf nodes in the two DCs. To enable communication between VM1 and VM2, Layer 2 connectivity must be established between DC A and DC B. Because different DCs typically have their own VNI spaces, the VXLAN tunnels within DC A and DC B tend to use different VNIs. To configure a VXLAN tunnel between Transit Leaf1 and Transit Leaf2 in such cases, perform a VNI conversion.

[Figure 1](#EN-US_TASK_0000001259707903__fig_dc_vrp_vxlan_cfg_120301) shows segment VXLAN in mapping VNI mode. The VXLAN tunnel in DC A uses VNI 10, and that in DC B uses VNI 20. A VNI mapping table must be configured on Transit Leaf1 to map local VNI 10 to mapping VNI 30. Similarly, a VNI mapping table must also be configured on Transit Leaf2 to map local VNI 20 to mapping VNI 30. After the configuration is complete, Layer 2 packets can be forwarded properly. The following uses DC A sending packets to DC B as an example. After receiving VXLAN packets within DC A, Transit Leaf1 decapsulates the packets, searches the VNI mapping table for mapping VNI 30, and then uses the mapping VNI to re-encapsulate the packets before sending them to Transit Leaf2. Upon receipt, Transit Leaf2 decapsulates the VXLAN packets, searches the VNI mapping table for local VNI 20, and then uses the local VNI to re-encapsulate the packets before forwarding them within the DC.

**Figure 1** Configuring segment VXLAN for Layer 2 interworking  
![](figure/en-us_image_0000001259788159.png)

#### Procedure

1. Configure route re-origination on Transit Leaf1 and Transit Leaf2.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
   3. Enter the BGP-EVPN address family view.
      
      
      ```
      [l2vpn-family](cmdqueryname=l2vpn-family) evpn
      ```
   4. Configure a split horizon group to which BGP EVPN peers (or peer groups) belong.
      
      
      ```
      [peer](cmdqueryname=peer) { group-name | ipv6-address | ipv4-address } split-group split-group-name
      ```
      
      On Transit Leaf1 and Transit Leaf2, specify the name of the split horizon group between them. This ensures that devices within DC A and DC B belong to the default split horizon group and Transit Leaf1 and Transit Leaf2 belong to the specified split horizon group. After this configuration is complete, when a transit leaf node receives BUM traffic, it does not forward traffic to a device belonging to the same split horizon group, thereby preventing loops from occurring.
   5. Configure the device to add a re-origination flag to routes received from BGP EVPN peers or peer groups.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | ipv6-address | group-name } import reoriginate
      ```
      
      On transit leaf nodes, enable the function to add a re-origination flag to the routes received from a BGP EVPN peer in the local DC and to the routes received from a BGP EVPN peer (transit leaf node) in the other DC.
   6. Configure the device to advertise re-originated EVPN routes to BGP EVPN peers or peer groups.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | ipv6-address | group-name } advertise route-reoriginated evpn mac
      ```
      
      In Layer 2 interworking scenarios, configure the function to advertise only re-originated MAC routes to BGP EVPN peers. On transit leaf nodes, enable the function to advertise re-originated MAC routes to a BGP EVPN peer in the local DC and to a BGP EVPN peer (transit leaf node) in the other DC.
   7. Return to the BGP view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   8. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   9. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Configure the mapping VNI function on Transit Leaf1 and Transit Leaf2.
   1. Enter the BD view.
      
      
      ```
      [bridge-domain](cmdqueryname=bridge-domain) bd-id
      ```
   2. Configure a mapping VNI associated with a BD, and specify the split horizon group to which the mapping VNI belongs.
      
      
      ```
      [vxlan vni](cmdqueryname=vxlan+vni) map-vni-id split-group split-group-name
      ```
      
      The mapping VNI is used for the VXLAN tunnel between the DCs. After this configuration is complete, a transit leaf node replaces the VNI in VXLAN packets received from the local DC with the mapping VNI. This configuration decouples a DCN's VNI space from a DCI network's VNI space and isolates faults. Additionally, to prevent loops from occurring when a transit leaf node forwards BUM traffic, specify the split horizon group to which the mapping VNI belongs. The group name must be the one configured using the [**peer split-group**](cmdqueryname=peer+split-group) command in Step 1.
   3. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
3. Configure ingress replication for the mapping VNI on Transit Leaf1 and Transit Leaf2.
   1. Enter the NVE interface view.
      
      
      ```
      [interface nve](cmdqueryname=interface+nve) nve-number
      ```
   2. Configure ingress replication for the mapping VNI.
      
      
      ```
      [vni](cmdqueryname=vni) map-vni-id head-end peer-list protocol bgp
      ```
   3. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```