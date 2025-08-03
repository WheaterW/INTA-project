Creating a VPLS Connection
==========================

When configuring VPLS multi-homing, you need to create VSIs, configure BGP signaling, RDs, and VPN targets, and create VPLS connections.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is enabled, and its view is displayed.
3. (Optional) Run [**bgp-vpn label-block-size**](cmdqueryname=bgp-vpn+label-block-size) *size-value*
   
   
   
   The L2VPN label block size is configured.
4. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   A VSI is created.
5. Run [**pwsignal bgp multi-homing**](cmdqueryname=pwsignal+bgp+multi-homing)
   
   
   
   VPLS multi-homing is enabled.
6. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the VSI.
   
   
   
   After configuring multi-homing as the PW signaling protocol for a VSI, you must configure an RD before performing other configurations.
   
   Configuring different RDs for different PEs is recommended.
7. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-16> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   VPN targets are configured for the VSI.
   
   
   
   When using this command, note the mapping between the VPN target attribute on the local end and that on the remote end. Specifically:
   
   * **export-extcommunity** on the local end is the same as **import-extcommunity** on the peer end.
   * **import-extcommunity** on the local end is the same as **export-extcommunity** on the peer end.
8. Run [**site-range**](cmdqueryname=site-range) *site-range* [ **default-offset** { **0** | **1** } ]
   
   
   
   The multi-homing site range is configured.
9. Perform operations in either of the following scenario as needed:
   
   
   * In a VPLS multi-homing scenario where a CE is single-homed to a PE:
     1. Run the [**site default**](cmdqueryname=site+default) command to enter the default VSI-BGP-SITE view.
        
        After the [**pwsignal bgp multi-homing**](cmdqueryname=pwsignal+bgp+multi-homing) command is run, the system automatically generates a default multi-homing site for the single-homing PE. After the default multi-homing site is generated, run the [**site default**](cmdqueryname=site+default) command to enter the default VSI-BGP-SITE view.
     2. Run the [**site-id**](cmdqueryname=site-id) *site-id* command to configure the multi-homing site ID.
     3. (Optional) Run the [**preference**](cmdqueryname=preference) *preference* command to configure the multi-homing site preference.
   * In a VPLS multi-homing scenario where a CE is multi-homed to PEs:
     1. Run the [**site name**](cmdqueryname=site+name) *site-name* command to create a multi-homing site and enter the VSI-BGP-SITE view.
     2. Run the [**site-id**](cmdqueryname=site-id) *site-id* command to configure the multi-homing site ID.
     3. Run the [**best-site**](cmdqueryname=best-site) command to configure the multi-homing site as the optimal one.
        
        In a VPLS multi-homing scenario, the system selects a site for PW establishment based on the AC state (ACS), multi-homing site preference (PREF), and PE's router ID (PE-ID). However, the site selected may differ if the ACS, PREF, or PE-ID value changes, causing frequent PW changes. To prevent frequent PW changes, run the [**best-site**](cmdqueryname=best-site) command to specify an optimal multi-homing site so that the endpoint PEs will use the optimal site for PW establishment.
        
        This step is mutually exclusive with [9.e](#EN-US_TASK_0172370206__li_e) and [9.f](#EN-US_TASK_0172370206__li_f).
     4. (Optional) Run the [**preference**](cmdqueryname=preference) *preference* command to configure the multi-homing site preference.
     5. (Optional) Run the [**active delay-time**](cmdqueryname=active+delay-time) *delay-time* command to configure a time period during which an AC interface remains in the blocked state.
        
        This step is mutually exclusive with [9.c](#EN-US_TASK_0172370206__li_c).
     6. (Optional) Run the [**recover delay-time**](cmdqueryname=recover+delay-time) *delay-time* command to configure the delay time after which an AC interface becomes active upon device restart.
        
        This step is mutually exclusive with [9.c](#EN-US_TASK_0172370206__li_c).
10. (Optional) Run [**peer**](cmdqueryname=peer) *peer-address* **pw** *pw-name*
    
    
    
    A PW is created, and the VSI-BGP-PW view is displayed.
11. (Optional) Run [**pw**](cmdqueryname=pw) *pw-name*
    
    
    
    The VSI-BGP-PW view is displayed.
    
    
    
    After you create the PW in Step 10, you can run this command in the VSI-BGP-MH view to enter the VSI-BGP-PW view.
12. (Optional) Run one of the following commands to configure BUM traffic suppression for the BGP VPLS VSI:
    
    
    * To set the maximum rate of broadcast traffic that is allowed to pass, run the [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] command.
    * To set the maximum rate of multicast traffic that is allowed to pass, run the [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] command.
    * To set the maximum rate of unknown unicast traffic that is allowed to pass, run the [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] command.
    
    If the actual traffic rate reaches the configured maximum limit, excess packets are discarded.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.