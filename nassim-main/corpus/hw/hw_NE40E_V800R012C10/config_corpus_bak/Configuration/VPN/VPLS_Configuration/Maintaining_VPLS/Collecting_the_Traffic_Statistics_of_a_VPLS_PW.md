Collecting the Traffic Statistics of a VPLS PW
==============================================

After configuring the function to collect VPLS traffic statistics, check information about the traffic on VPLS PWs.

#### Context

If a carrier needs to build a model of traffic between metro networks (such as IP/MPLS core metro networks) to provide reference for DiffServ TE deployment and maintenance, or the carrier needs to charge non-monthly rental subscribers by traffic, the function to collect traffic statistics of a specified PW can be configured.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** | **auto** ] command to enter the VSI view.
3. Run the following commands based on the VPLS type:
   
   
   * LDP VPLS
     1. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to configure LDP as the PW signaling protocol and enter the VSI-LDP view.
     2. Run the [**traffic-statistics peer**](cmdqueryname=traffic-statistics+peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **enable** or [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable) command to enable traffic statistics collection for an LDP VPLS PW.
   * BGP VPLS
     1. Run the [**pwsignal**](cmdqueryname=pwsignal) **bgp** command to configure BGP as the PW signaling protocol and enter the VSI-BGP view.
     2. Run the [**traffic-statistics peer**](cmdqueryname=traffic-statistics+peer) *peer-address* **remote-site** *site-id* **enable** command to enable traffic statistics collection for a BGP VPLS PW.
   * BGP AD VPLS
     1. Run the [**bgp-ad**](cmdqueryname=bgp-ad) command to enter the VSI-BGP AD view.
     2. Run the [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable) or [**traffic-statistics peer**](cmdqueryname=traffic-statistics+peer) *peer-address* **enable** command to enable traffic statistics collection for BGP AD VPLS PWs.
   * BGP multi-homing VPLS
     1. Run the [**pwsignal bgp multi-homing**](cmdqueryname=pwsignal+bgp+multi-homing) command to enable VPLS multi-homing.
     2. Run the [**traffic-statistics peer**](cmdqueryname=traffic-statistics+peer) *peer-address* **enable** command to enable traffic statistics collection for a specified PW.
4. Run the [**quit**](cmdqueryname=quit) command to return to the VSI view.
5. Run the [**traffic-statistics packet-type enable**](cmdqueryname=traffic-statistics+packet-type+enable) command to enable packet-type-based traffic statistics collection for VPLS PWs.
   
   
   
   This command can take effect only after traffic statistics collection is enabled for VPLS PWs using the [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable) command.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.