Configuring Interworking Between EVPN VPLS over MPLS and Static VXLAN
=====================================================================

In MetroFabric scenarios with CU separation deployed, interworking between EVPN VPLS over MPLS and static VXLAN must be deployed on metro edge function (MEF) devices.

#### Context

In a MetroFabric scenario with CU separation deployed (as shown in [Figure 1](#EN-US_TASK_0172370530__fig_dc_vrp_evpn_cfg_015401)), MPLS EVPN runs on the metro network, and static VXLAN tunnels are established between the MEF devices and vBRAS-UPs. Therefore, the MEF1 and MEF2 devices must support interworking between EVPN VPLS over MPLS and static VXLAN to establish E2E forwarding paths for traffic.

**Figure 1** Interworking between EVPN VPLS over MPLS and static VXLAN  
![](images/fig_dc_vrp_evpn_cfg_015401.png)

This interworking scenario supports the following key functions:

* MEF1 and MEF2 learn MAC routes on the static VXLAN tunnel side.
* A VXLAN EVPN peer relationship is established between MEF1 and MEF2. Both MEF1 and MEF2 can re-originate the MAC routes learned on the static VXLAN tunnel side and flood the MAC routes through BGP EVPN.
* An MPLS EVPN peer relationship is established between MEF1 and MEF2. MEF1 and MEF2 flood ES routes to each other and support DF election.
* MEF1 and MEF2 advertise the MAC routes (maybe the re-originated MAC routes) learned on the static VXLAN tunnel side to MEF3 (the BGP EVPN peer on the MPLS EVPN side) through EVPN. MAC load balancing is implemented on MEF3.
* MAC mobility is supported between MEF1 and MEF2.

#### Pre-configuration Tasks

Before configuring interworking between EVPN VPLS over MPLS and static VXLAN, complete the following tasks:

* Configure [EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html) between MEF1 and MEF3 and between MEF2 and MEF3.
* Configure BD MPLS EVPN. To allow MEF1 and MEF2 to implement load balancing, configure the same ESI in the BDs on MEF1 and MEF2.
* Configure VXLAN tunnels between MEF1, MEF2, and vBRAS-UPs. MEF1 and MEF2 function as aggregation devices, and vBRAS-UPs function as BRASs. Currently, only static VXLAN tunnels can be established.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  MEF1 and MEF2 form the anycast relationship. Therefore, the same source VTEP IP address must be configured for MEF1 and MEF2.

After the pre-configuration tasks are complete, perform the following operations.


#### Procedure

1. Configure a BGP EVPN peer relationship between MEF1 and MEF2.
   1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enable BGP and enter its view.
   2. (Optional) Run the [**router-id**](cmdqueryname=router-id) *ipv4-address* command to configure a BGP router ID.
   3. Run the [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number* command to configure the remote device as a peer.
   4. (Optional) Run the [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* **connect-interface** *interface-type* *interface-number* [ *ipv4-source-address* ] command to specify the source interface and source address for the setup of a TCP connection with the BGP peer.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If loopback interfaces are used to establish a BGP connection, it is recommended that the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command be run on both ends to ensure correct connection. If this command is run on only one end, the BGP connection may fail to be established.
   5. (Optional) Run the [**peer**](cmdqueryname=peer+ebgp-max-hop) *ipv4-address* [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ] command to set the maximum number of hops allowed for an EBGP EVPN connection.
      
      
      
      Generally, EBGP EVPN peers are directly connected. If they are not directly connected, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to allow the EBGP EVPN peers to establish a multi-hop TCP connection.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If loopback interfaces are used for an EBGP EVPN connection, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command must be run, with the *hop-count* value greater than or equal to 2. If this configuration is absent, the EBGP EVPN connection fails to be established.
   6. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP EVPN address family view.
   7. Run the [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable** command to enable the function to exchange EVPN routes with a specified peer or peer group.
   8. Run the [**peer**](cmdqueryname=peer+advertise+encap-type) { *ipv4-address* | *group-name* } **advertise encap-type vxlan** command to configure the function to advertise EVPN routes carrying the VXLAN encapsulation attribute to peers.
   9. (Optional) Run the [**peer**](cmdqueryname=peer+route-policy) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* { **import** | **export** } command to specify a route-policy for the routes received from or to be advertised to a BGP EVPN peer or peer group.
      
      
      
      After the route-policy is applied, the routes received from or to be advertised to a specified BGP EVPN peer or peer group will be filtered, ensuring that only desired routes are imported or advertised. This configuration helps manage routes and reduce required routing entries and system resources.
   10. (Optional) Run the [**peer**](cmdqueryname=peer+next-hop-invariable) { *group-name* | *ipv4-address* } **next-hop-invariable** command to enable the device to advertise routes to an EBGP EVPN peer without changing the next hop. If an EBGP EVPN peer relationship has been established between a spine node and a gateway, run the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command on the spine node to ensure that the next hop of the routes received by this gateway is another gateway
   11. (Optional) Run the [**peer**](cmdqueryname=peer+mac-limit) { *group-name* | *ipv4-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ] command to configure the maximum number of MAC advertisement routes that can be received from a peer.
       
       
       
       If an EVPN instance imports many invalid MAC advertisement routes from peers and these routes account for a large proportion of the total MAC advertisement routes, run the command to configure the maximum number of MAC advertisement routes that can be received from each peer. If the number of received MAC advertisement routes exceeds the specified maximum number, the system displays an alarm, instructing users to check the validity of the MAC advertisement routes received in the EVPN instance.
2. Configure the function to re-originate EVPN routes between MEF1 and MEF2.
   1. Run the [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate** command to configure the device to add a re-origination flag to routes received from the BGP EVPN peer.
   2. Run the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** **mac** command to configure the function to re-originate MAC routes through EVPN and send the re-originated MAC routes to a specified BGP EVPN peer.
   3. Run the [**quit**](cmdqueryname=quit) command to exit the BGP EVPN address family view.
   4. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view.
3. Enable MEF1 and MEF2 to advertise the MAC routes (maybe the re-originated MAC routes) learned on the static VXLAN tunnel side to the BGP EVPN peer on the MPLS EVPN side through EVPN.
   1. Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
   2. Run the [**advertise vxlan-tunnel mac**](cmdqueryname=advertise+vxlan-tunnel+mac) command to enable the device to advertise the MAC routes on the static VXLAN tunnel side to the BGP EVPN peers on the MPLS EVPN side through EVPN.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) **mac-route** [ *prefix* ] command on MEF1, MEF2, and MEF3 to view details about EVPN MAC routes.