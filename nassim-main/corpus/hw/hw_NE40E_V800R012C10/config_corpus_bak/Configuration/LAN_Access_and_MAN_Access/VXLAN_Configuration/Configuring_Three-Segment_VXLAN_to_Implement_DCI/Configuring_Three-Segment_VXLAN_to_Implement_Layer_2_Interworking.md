Configuring Three-Segment VXLAN to Implement Layer 2 Interworking
=================================================================

Three-segment VXLAN tunnels can be configured to enable communication between VMs that belong to the same subnet but different DCs.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172363813__fig_dc_vrp_vxlan_cfg_120201), VXLAN tunnels are configured both within DC A and DC B and between transit leaf nodes in both DCs. To enable communication between VM1 and VM2, implement Layer 2 communication between DC A and DC B. If the VXLAN tunnels within DC A and DC B use the same VXLAN Network Identifier (VNI), this VNI can also be used to establish a VXLAN tunnel between Transit Leaf1 and Transit Leaf2. In practice, however, different DCs have their own VNI spaces, and therefore the VXLAN tunnels within DC A and DC B mostly likely use different VNIs. To configure a VXLAN tunnel between Transit Leaf1 and Transit Leaf2 in such cases, perform a VNI conversion.

For example, in [Figure 1](#EN-US_TASK_0172363813__fig_dc_vrp_vxlan_cfg_120201), the VXLAN tunnel in DC A uses the VNI 10, and that in DC B uses the VNI 20. Transit Leaf2's VNI (20) must be configured as the outbound VNI on Transit Leaf1, and Transit Leaf1's VNI (10) as the outbound VNI on Transit Leaf2. After the configuration is complete, Layer 2 packets can be forwarded properly. Take DC A sending packets to DC B as an example. After receiving VXLAN packets within DC A, Transit Leaf1 decapsulates the packets and then uses the outbound VNI 20 to re-encapsulate the packets before sending them to Transit Leaf2. Upon receipt, Transit Leaf2 forwards them as normal VXLAN packets.

**Figure 1** Network diagram of configuring three-segment VXLAN to implement Layer 2 interworking  
![](images/fig_dc_vrp_vxlan_cfg_120201.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Layer 2 communication between VMs in different DCs is implemented here, therefore avoiding the need to configure a Layer 3 gateway.
* If DC A and DC B belong to the same AS, configure an RR on the edge device. If DC A and DC B do not belong to the same AS, establish an EBGP EVPN peer relationship between edge devices.


#### Procedure

1. Configure BGP EVPN within DC A and DC B to establish VXLAN tunnels. For detailed configurations, see [Configuring VXLAN in Centralized Gateway Mode Using BGP EVPN](dc_vrp_vxlan_cfg_0017b.html). There is no need to configure a Layer 3 VXLAN gateway.
2. Configure BGP EVPN on Transit Leaf1 and Transit Leaf2 to establish a VXLAN tunnel between them. For detailed configurations, see [Configuring VXLAN in Centralized Gateway Mode Using BGP EVPN](dc_vrp_vxlan_cfg_0017b.html). There is no need to configure a Layer 3 VXLAN gateway.
3. Configure Transit Leaf1 and Transit Leaf2 to advertise routes that are re-originated by the EVPN address family to BGP EVPN peers.
   
   
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      The BGP view is displayed.
   2. Run [**l2vpn-family**](cmdqueryname=l2vpn-family) **evpn**
      
      The BGP-EVPN address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **split-group** *split-group-name*
      
      A split horizon group (SHG) to which BGP EVPN peers (or peer groups) belong is configured.
      
      In Layer 2 interworking scenarios, to prevent forwarding BUM traffic from causing a loop, an SHG must be configured. Separately specify the name of the SHG between Transit Leaf1 and Transit Leaf2 on each, so that devices within DC A and DC B belong to the default SHG and Transit Leaf1 and Transit Leaf2 belong to the specified SHG. In this manner, when a transit leaf node receives BUM traffic, it does not forward traffic to a device belonging to the same SHG, therefore preventing loops.
   4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **import** **reoriginate**
      
      The function to re-originate routes received from BGP EVPN peers is enabled.
      
      Enable on transit leaf nodes the function to re-originate routes received from BGP EVPN peers within DCs and between the DCs (between transit leaf nodes).
   5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** **mac**
      
      The function to advertise re-originated EVPN routes to BGP EVPN peers is enabled.
      
      In Layer 2 interworking scenarios, configure the function to advertise only re-originated MAC routes to BGP EVPN peers. Enable on transit leaf nodes the function to advertise re-originated MAC routes to BGP EVPN peers within DCs and between the DCs (between transit leaf nodes).
   6. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.