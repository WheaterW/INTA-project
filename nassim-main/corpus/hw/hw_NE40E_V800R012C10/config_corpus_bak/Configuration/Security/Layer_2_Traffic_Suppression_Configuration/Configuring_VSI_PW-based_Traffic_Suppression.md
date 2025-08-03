Configuring VSI PW-based Traffic Suppression
============================================

This section describes how to configure VSI PW-based traffic suppression in order to reduce the traffic burden on a network.

#### Usage Scenario

In addition to user traffic management and bandwidth allocation, an Ethernet requires broadcast, multicast, and unknown unicast traffic to be suppressed to ensure the secure transmission of unicast traffic and properly utilize bandwidth resources.

Most networks require unicast traffic to be much heavier than broadcast, multicast, and unknown unicast traffic. If broadcast, multicast, and unknown unicast traffic is not suppressed, forwarding a large volume of such traffic consumes numerous bandwidth resources, reducing network performance and even causing a communication interruption. If interface-based traffic suppression is configured, the broadcast, multicast, and unknown unicast traffic of all PWs created on the interface is suppressed. To implement more convenient and flexible traffic suppression, you can configure VSI PW-based suppression for broadcast, multicast, and unknown unicast traffic.


#### Pre-configuration Tasks

Before configuring Layer 2 traffic suppression, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.
* Enable the MPLS L2VPN function.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   The VSI view is displayed.
3. Run [**suppression**](cmdqueryname=suppression) { **inbound** | **outbound** } **enable**
   
   
   
   Traffic suppression is enabled for the VSI.
4. Configure VSI PW-based LDP interface traffic suppression in the VSI-LDP-PW view, VSI PW-based BGP interface traffic suppression in the VSI-BGP-PW view, or VSI PW-based BGPAD interface traffic suppression in the VSI-BGPAD-PW view.
   
   
   * Configure VSI PW-based LDP interface traffic suppression in the VSI-LDP-PW view.
     1. Run [**pwsignal ldp**](cmdqueryname=pwsignal+ldp)
        
        The VSI-LDP view is displayed.
     2. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
        
        A VSI ID is configured.
     3. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
        
        A PW is created, and the VSI-LDP-PW view is displayed.
   * Configure VSI PW-based BGP interface traffic suppression in the VSI-BGP-PW view.
     1. Run [**pwsignal bgp**](cmdqueryname=pwsignal+bgp)
        
        The VSI-BGP view is displayed.
     2. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
        
        An RD is configured for the current VSI.
     3. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* **both**
        
        The current VSI is associated with the specified VPN target.
     4. Run [**peer**](cmdqueryname=peer) *peer-address* **remote-site** *remote-site-id* **pw** *pw-name*
        
        A PW is created, and the VSI-BGP-PW view is displayed.
   * Configure VSI PW-based BGPAD interface traffic suppression in the VSI-BGPAD-PW view.
     1. Run [**bgp-ad**](cmdqueryname=bgp-ad)
        
        The BGP AD view is displayed.
     2. Run [**vpls-id**](cmdqueryname=vpls-id) *vplsIdValue*
        
        The ID of the VPLS domain to which the VSI belongs is specified.
     3. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* **both**
        
        The current VSI is associated with the specified VPN target.
     4. Run [**peer**](cmdqueryname=peer) *peer-address* **pw** *pw-name*
        
        A PW is created, and the VSI-BGPAD-PW view is displayed.
5. Run [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ]
   
   
   
   VSI PW-based broadcast traffic suppression is implemented.
6. Run [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ]
   
   
   
   VSI PW-based multicast traffic suppression is implemented.
7. Run [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cirVal* [ **cbs** *cbsVal* ]
   
   
   
   VSI PW-based unknown unicast traffic suppression is implemented.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

After the configuration is complete, perform the following operation to verify the configuration:

Run the [**display interface**](cmdqueryname=display+interface) { *interface-name* | *interface-type interface-num* } **suppression vsi** *vsi-name* or [**display traffic-statistics suppression interface**](cmdqueryname=display+traffic-statistics+suppression+interface) { *interface-name | interface-type interface-num* } **vsi** *vsi-name* command to check Layer 2 traffic suppression statistics about specified VPLS services on the specified interface.