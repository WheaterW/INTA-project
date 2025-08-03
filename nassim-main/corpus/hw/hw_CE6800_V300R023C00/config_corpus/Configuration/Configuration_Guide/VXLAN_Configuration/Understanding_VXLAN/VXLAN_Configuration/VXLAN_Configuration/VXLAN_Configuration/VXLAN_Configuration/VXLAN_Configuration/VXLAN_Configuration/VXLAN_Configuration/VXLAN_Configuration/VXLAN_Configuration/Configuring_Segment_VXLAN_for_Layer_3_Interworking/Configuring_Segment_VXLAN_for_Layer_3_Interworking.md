Configuring Segment VXLAN for Layer 3 Interworking
==================================================

Configuring Segment VXLAN for Layer 3 Interworking

#### Prerequisites

Before configuring segment VXLAN for Layer 3 interworking, you have completed the following tasks:

* Configure BGP EVPN to establish one VXLAN tunnel in DC A and another one in DC B.
  + If the underlay network is an IPv4 network, see [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1066.html).
  + If the underlay network is an IPv6 network, see [Establishing IPv6 VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan6_cfg_1066.html).
* Configure BGP EVPN between border leaf nodes in DCs to establish an inter-DC VXLAN tunnel.
  + If the underlay network is an IPv4 network, see [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan_cfg_1066.html).
  + If the underlay network is an IPv6 network, see [Establishing IPv6 VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](../dc/dc_vrp_vxlan6_cfg_1066.html).![](../public_sys-resources/note_3.0-en-us.png) 
  
  When configuring a VXLAN tunnel between border leaf nodes in DCs, you do not need to create a BD or perform BD-related configurations. This does not affect the establishment of the VXLAN tunnel between the border leaf nodes. However, in this scenario, VMs attached to border leaf nodes cannot access the network through Layer 2 sub-interfaces associated with a BD.

#### Context

In [Figure 1](#EN-US_TASK_0000001560704188__fig_dc_vrp_vxlan_cfg_108501), BGP EVPN is configured between distributed gateways in DC A and DC B to create VXLAN tunnels and configured between Leaf2 and Leaf3 to create another VXLAN tunnel. To implement Layer 3 interworking between VMs on different subnets in DC A and DC B, you need to configure segment VXLAN on Leaf2 and Leaf3 at the edge.

**Figure 1** Configuring segment VXLAN for Layer 3 interworking  
![](figure/en-us_image_0000001611502917.png)

#### Procedure

1. Configure Leaf2 and Leaf3 to advertise re-originated EVPN routes to their BGP EVPN peers.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
   3. Enter the BGP EVPN address family view.
      
      
      ```
      [l2vpn-family](cmdqueryname=l2vpn-family) evpn
      ```
   4. Configure the device to add a re-origination flag to routes received from BGP EVPN peers or peer groups.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | ipv6-address | group-name } import reoriginate
      ```
   5. Configure the device to advertise re-originated EVPN routes to BGP EVPN peers or peer groups on one end.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | ipv6-address | group-name } advertise route-reoriginated evpn { mac | mac-ip | ip | mac-ipv6 | ipv6 }
      ```
      
      After this step is performed, Leaf2 or Leaf3 changes the next hop of a received EVPN route to itself, replaces the router MAC address in the gateway MAC address attribute with its own router MAC address, and replaces the L3VNI with its local VPN instance's L3VNI.
   6. (Optional) Configure the device to advertise the MED attribute to its EBGP EVPN peer or peer group.
      
      
      ```
      [peer](cmdqueryname=peer) { peerIpv4Addr  | peerGroupName } transit-med-to-ebgp
      ```
      
      By default, the MED attribute of EVPN routes is not advertised to EBGP EVPN peers. If the VXLAN gateways in a DC work in active/standby mode and an active/standby service switchover needs to be implemented by changing the cost value, perform this step so that the device can advertise the MED attribute of the local EVPN route to its EBGP EVPN peer.
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
2. (Optional) Enable the asymmetric mode for IRB/IRBv6 routes on Leaf2 and Leaf3.
   1. Enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
   2. Enter the BGP VPN instance's IPv4/IPv6 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name or [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
      ```
   3. Enable the asymmetric mode for IRB/IRBv6 routes.
      
      
      ```
      [irb asymmetric](cmdqueryname=irb+asymmetric) route-policy route-policy-name
      ```
      
      Before running this command, you need to create a route-policy to filter out the IRB/IRBv6 routes received by Leaf2 from Leaf1.
      
      If you want the Leaf4-to-Leaf1 traffic to be forwarded to other devices (such as firewalls) after reaching Leaf2 instead of being directly sent to Leaf1, enable the asymmetric mode for IRB/IRBv6 routes on Leaf2. In this manner, forwarding entries are not delivered for the IRB/IRBv6 routes received by Leaf2 from Leaf1, but the routes received by Leaf2 from Leaf3 are not affected.
   4. Return to the BGP view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
3. (Optional) Disable Leaf2 and Leaf3 from re-originating IRB routes when no BD is configured.
   1. Enter the global EVPN configuration view.
      
      
      ```
      [evpn](cmdqueryname=evpn)
      ```
   2. The function to re-originate IRB routes when no BD is configured is disabled.
      
      
      ```
      [irb-reoriginated without-bridge-domain disable](cmdqueryname=irb-reoriginated+without-bridge-domain+disable)
      ```
      
      By default, when no BD is configured, Leaf2 and Leaf3 can re-originate IRB routes for inter-DC VXLAN tunnel creation. To prevent IRB routes from being re-originated again after a BD is configured for Leaf2 and Leaf3, perform this step.
   3. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
4. (Optional) Disable on Leaf2 and Leaf3 the function to advertise re-originated IRB routes without being restricted by a split horizon group (SHG).
   1. Enter the global EVPN configuration view.
      
      
      ```
      [evpn](cmdqueryname=evpn)
      ```
   2. Disable the function to advertise re-originated IRB routes without being restricted by an SHG.
      
      
      ```
      [irb-reoriginated without-split-group disable](cmdqueryname=irb-reoriginated+without-split-group+disable)
      ```
      
      By default, re-originated IRB routes are advertised without being restricted by an SHG.
      
      In scenarios where segment VXLAN tunnels are used for DCI, BGP EVPN peer-based SHGs are introduced to prevent BUM traffic forwarding from causing loops during Layer 2 interconnection. If no BGP EVPN peer-based SHGs are specified on transit leaf nodes (edge devices interconnecting DCs), all BGP EVPN peers belong to the default system SHG. In this case, after a transit leaf node re-originates IRB routes received from an intra-DC device, the node cannot advertise the re-originated IRB routes to the peer DC's transit leaf node. This is because both of the transit leaf nodes belong to the default system SHG. As a result, Layer 3 traffic forwarding is affected.
      
      To prevent this problem, a device advertises re-originated IRB routes without being restricted by an SHG by default. If SHGs are specified for all BGP EVPN peers on transit leaf nodes, perform this step to disable the function to advertise re-originated IRB routes without being restricted by an SHG.
   3. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
5. (Optional) Configure Leaf2 and Leaf3 to re-originate IRB/IRBv6 routes as IP prefix routes.
   1. Enter the VPN instance view.
      
      
      ```
      [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
      ```
   2. Enter the VPN instance's IPv4 or IPv6 address family view.
      
      
      ```
      [ipv4-family](cmdqueryname=ipv4-family) or [ipv6-family](cmdqueryname=ipv6-family)
      ```
   3. Configure IRB/IRBv6 routes to be re-originated as IP prefix routes.
      
      
      ```
      [irb-reoriginate irb2ip](cmdqueryname=irb-reoriginate+irb2ip) enable
      ```
      
      If you want Leaf2 and Leaf3 to communicate through IP prefix routes, enable the function to re-originate IRB/IRBv6 routes as IP prefix routes.
   4. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

After completing the configuration, run the following commands to verify it.

* Run the [**display bgp evpn peer**](cmdqueryname=display+bgp+evpn+peer) command to check BGP EVPN peer information.
* Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) [ **vni** *vni-id* ] command to check the ingress replication lists of all VNIs or a specified VNI.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check VXLAN tunnel information.
* Run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) [ *vni-id* [ **verbose** ] ] command to check VXLAN configuration and VNI state information.