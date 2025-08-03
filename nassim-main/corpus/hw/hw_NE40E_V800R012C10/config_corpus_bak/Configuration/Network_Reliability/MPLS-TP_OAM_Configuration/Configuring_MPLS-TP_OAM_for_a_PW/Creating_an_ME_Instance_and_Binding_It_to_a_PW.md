Creating an ME Instance and Binding It to a PW
==============================================

This section describes how to create an ME instance and bind it to a PW.

#### Context

Create an ME instance and bind it to the PW to use MPLS-TP OAM to monitor a PW over a bidirectional LSP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls-tp mode**](cmdqueryname=mpls-tp+mode) { **standard** | **private** }
   
   
   
   A detection mode is configured for MPLS-TP OAM.
3. (Optional) Run [**mpls-tp channel-type**](cmdqueryname=mpls-tp+channel-type) {**0x7ffa** | **0x8902** }
   
   
   
   An ACH label value is specified.
4. Run [**mpls-tp meg**](cmdqueryname=mpls-tp+meg) *meg-name*
   
   
   
   A MEG is created, and the MEG view is displayed.
5. Create an ME instance and bind it to a single- or multi-segment PW.
   
   
   * If the PW is a single-segment PW, the configuration steps are as follows:
     + On the local MEP, run the [**me l2vc**](cmdqueryname=me+l2vc) **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* **mep-id** *mep-id* **remote-mep-id** *remote-mep-id* command to create an ME instance and bound it to a single-segment PWE3 PW.
     + On the RMEP, run the [**me l2vc**](cmdqueryname=me+l2vc) **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* **mep-id** *mep-id* **remote-mep-id** *remote-mep-id* command to create an ME instance and bound it to the same single-segment PWE3 PW.
   * If the PW is a multi-segment PW, the **ttl** parameter must be specified:
     + On the local MEP, run the [**me l2vc**](cmdqueryname=me+l2vc) **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* [ **remote-peer-ip** *remote-peer-ip* | **ttl** *ttl-number* ] **mep-id** *mep-id* **remote-mep-id** *remote-mep-id* [ **gal** { **13** | **14** } ] command to create an ME instance and bound it to a multi-segment PWE3 static PW.
     + On the RMEP, run the [**me l2vc**](cmdqueryname=me+l2vc) **peer-ip** *peer-ip* **vc-id** *vc-id* **vc-type** *vc-type* [ **remote-peer-ip** *remote-peer-ip* | **ttl** *ttl-number* ] **mep-id** *mep-id* **remote-mep-id** *remote-mep-id* [ **gal** { **13** | **14** } ] command to create an ME instance and bound it to the same multi-segment PWE3 static PW.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.