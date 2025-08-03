Configuring PW OAM to Detect Public Network Link Faults
=======================================================

PW OAM includes Multiprotocol Label Switching Transport Profile (MPLS-TP) OAM and MPLS OAM. PW OAM can quickly detect PW faults, enabling speedy PW switching for service protection.

#### Context

PW OAM improves the reliability and maintainability of transport networks. Currently, PW OAM includes MPLS-TP OAM and MPLS OAM.

* MPLS-TP OAM can effectively detect, identify, and locate faults at the MPLS-TP user plane and quickly switch services away from faulty links or nodes. MPLS-TP OAM can detect faults on PWs carried over bidirectional LSPs and collect performance statistics.
* MPLS OAM is a detection mechanism intended for the MPLS user plane. It provides users with PW status information without relying on any network plane. In addition, MPLS OAM provides network administrators and maintenance engineers with a variety of diagnostic interfaces for them to measure network performance and maintain networks.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In a scenario with both PW APS and PW OAM, after PW OAM (MPLS OAM or MPLS-TP OAM) is deleted, PW APS will fail.




#### Procedure

* Configure MPLS-TP OAM to detect PW faults.
  
  
  
  Perform the following steps on the endpoint PEs of the primary and secondary PWs (the SPEs of MS-PWs do not need the following configurations):
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls-tp meg**](cmdqueryname=mpls-tp+meg) *meg-name* command to create a MEG and enter its view.
  3. Run the [**me l2vc**](cmdqueryname=me+l2vc) **peer-ip** *peer-ip-value* **vc-id** *vc-id**-value* **vc-type** *vc-type-value* [ **remote-peer-ip** *remote-peer-ip-value* | **ttl** *ttl-number* ] **mep-id** *mep-id-value* **remote-mep-id** *remote-mep-id-value* [ **gal** { **13** | **14** } ] command to configure an ME instance and bind it to an SS-PW or MS-PW.
  4. Run the [**cc send enable**](cmdqueryname=cc+send+enable) command to enable the local end to send CC/CV packets.
  5. Run the [**cc receive enable**](cmdqueryname=cc+receive+enable) command to enable the local end to receive CC/CV packets.
  6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure MPLS OAM to detect PW faults.
  
  
  
  Perform the following steps on the endpoint PEs of the primary and secondary PWs (the SPEs of MS-PWs do not need the following configurations):
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls**](cmdqueryname=mpls) command to enter the MPLS view.
  3. Run the [**mpls oam**](cmdqueryname=mpls+oam) command to enable MPLS OAM globally.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**mpls-oam**](cmdqueryname=mpls-oam) command to enter the MPLS OAM view.
  6. Run the [**mpls oam l2vc**](cmdqueryname=mpls+oam+l2vc) **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* [ **remote-peer-ip** *remote-peer-ip* **remote-vc-id** *remote-vc-id* **remote-vc-type** *remote-vc-type* ] **type** { **cv** | **ffd** **frequency** { **3** | **10** | **20** | **50** | **100** | **200** | **500** } } [ **auto-protocol** [ **overtime** *overtime* ] ] [ **compatibility-mode***compati-mode-val* ] [ **bdi-frequency***bdi-frep-val* ] [ **exp***exp-value* ] command to configure MPLS OAM parameters.
     
     
     
     The target PW can be either an SS-PW or an MS-PW. If the target PW is an MS-PW, you need to set **remote-peer-ip**, **remote-vc-id**, and **remote-vc-type**.
  7. (Optional) Run the [**mpls oam l2vc enable**](cmdqueryname=mpls+oam+l2vc+enable) { **send** | **receive** } **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* command to enable OAM.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If you want to manually send or receive CC/CV packets, do not configure the **auto-protocol** parameter in the [**mpls oam l2vc**](cmdqueryname=mpls+oam+l2vc) command. Instead, run the [**mpls oam l2vc enable**](cmdqueryname=mpls+oam+l2vc+enable) command to enable OAM on PW endpoints.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.