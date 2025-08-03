(Optional) Configuring PW APS
=============================

This section describes how to configure PW APS, so that an active/standby PW switchover can be performed if a PW fails.

#### Usage Scenario

On a network where a PW protection group is configured, you can configure PW APS to ensure that if one PW in the protection group fails, the other PW takes over to forward traffic. To accelerate PW fault detection, configure [MPLS OAM](dc_vrp_mplsoam_cfg_0001.html) or [MPLS-TP OAM](dc_vrp_mpls-tp_oam_cfg_0001.html).

Perform the following steps on the PEs at both ends of a PW:


#### Procedure

1. Configure PW APS.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**pw-aps**](cmdqueryname=pw-aps) *apsId* command to create a PW APS instance.
   3. (Optional) Run the [**description**](cmdqueryname=description) *text* command to configure a description for the PW APS instance.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of the AC interface configured with a PW protection group.
   6. Run the [**mpls l2vpn pw-aps**](cmdqueryname=mpls+l2vpn+pw-aps) *apsId* { **admin** | **reference** } command to bind the PW protection group to the PW APS instance.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure PW OAM to detect PW faults.
   
   
   * Configure MPLS OAM to detect PW faults.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**mpls**](cmdqueryname=mpls) command to enter the MPLS view.
     3. Run the [**mpls oam**](cmdqueryname=mpls+oam) command to enable MPLS OAM globally.
     4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     5. Run the [**mpls-oam**](cmdqueryname=mpls-oam) command to enter the MPLS OAM view.
     6. Run the [**mpls oam l2vc peer-ip**](cmdqueryname=mpls+oam+l2vc) *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* [ **remote-peer-ip** *remote-peer-ip* **remote-vc-id** *remote-vc-id* **remote-vc-type** *remote-vc-type* ] **type** { **cv** | **ffd** **frequency** { **3** | **10** | **20** | **50** | **100** | **200** | **500** } } [ **auto-protocol** [ **overtime** *overtime* ] ] [ **compatibility-mode** *compati-mode-val* ] [ **bdi-frequency** *bdi-frep-val* ] [ **exp** *exp-value* ] command to configure MPLS OAM parameters at both ends of the PW.
     7. Run the [**mpls oam l2vc enable**](cmdqueryname=mpls+oam+l2vc+enable) { **send** | **receive** } **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* command to enable OAM on the PW endpoint.
     8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * Configure MPLS-TP OAM to detect PW faults.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**mpls-tp meg**](cmdqueryname=mpls-tp+meg) *meg-name* command to create a MEG and enter its view.
     3. Run the [**me l2vc**](cmdqueryname=me+l2vc) **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* [ **remote-peer-ip** *remote-peer-ip* | **ttl** *ttl-number* ] **mep-id** *mep-id* **remote-mep-id** *remote-mep-id* command to configure an ME instance and bind it to the PW.
     4. Run the [**cc send enable**](cmdqueryname=cc+send+enable) command to enable the local end to send CC/CV packets.
     5. Run the [**cc receive enable**](cmdqueryname=cc+receive+enable) command to enable the local end to receive CC/CV packets.
     6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.