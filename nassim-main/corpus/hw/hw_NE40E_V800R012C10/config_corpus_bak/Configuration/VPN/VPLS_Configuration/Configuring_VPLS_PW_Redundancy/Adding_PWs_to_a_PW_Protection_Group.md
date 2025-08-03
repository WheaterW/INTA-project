Adding PWs to a PW Protection Group
===================================

After configuring PWs, add them to a PW protection group, specify PW priorities, and configure PW protection group parameters to implement PW redundancy.

#### Context

After configuring two VSI PWs on a UPE, add them to a PW protection group, specify their priorities, and configure PW protection group parameters for the two PWs to work in backup mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The view of the created VSI is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   The VSI-LDP view is displayed.
4. Run [**protect-group**](cmdqueryname=protect-group) *group-name*
   
   
   
   A PW protection group is created, and its view is displayed.
5. Run [**protect-mode pw-redundancy**](cmdqueryname=protect-mode+pw-redundancy) { **master** | **independent** }
   
   
   
   A PW redundancy mode is configured for the current PW protection group.
   
   
   
   The **master** mode must be configured in an HVPLS scenario. If the **master** mode is configured in a VPLS + VPWS interworking scenario, a bypass PW must be configured between NPEs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The PW redundancy mode of the PW protection group must be configured before you start the following configurations.
6. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **preference** *preference-value*
   
   
   
   A PW is added to the PW protection group, and the priority of the PW is specified. A smaller value indicates a higher priority. Of the two PWs added to a PW protection group, the one with a higher priority functions as the primary PW.
7. (Optional) Run [**stream-dual-receiving**](cmdqueryname=stream-dual-receiving)
   
   
   
   Both the primary and secondary PWs are configured to receive packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command helps prevent packet loss during traffic switchback, but may incur routing loops.
8. (Optional) Run [**holdoff**](cmdqueryname=holdoff) *holdoffTime*
   
   
   
   A switching delay is configured for the PW protection group with the master/slave PW redundancy mode.
   
   
   
   If a fault occurs on the primary PW, traffic immediately switches to the secondary PW. If the working path flaps or an error occurs in the detection mechanism, traffic frequently switches between the working and protection paths. To prevent this problem, configure a switching delay.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   On a VPLS network that uses BFD for fault detection, traffic immediately switches from the primary PW to the secondary PW after BFD detects a fault on the primary PW, irrespective of whether delayed switching is configured. It is recommended that you determine whether to use BFD or delayed switching based on your requirements.
   
   After you configure a switching delay (*holdoffTime*), traffic forwarded during the delay period will be interrupted if the primary PW fails to recover before the delay period expires.
9. (Optional) Run [**reroute**](cmdqueryname=reroute) { [**delay**](cmdqueryname=delay) *delay-time* | **immediately** | **never** }
   
   
   
   A revertive PW switching policy is configured.
   
   
   
   The [**reroute**](cmdqueryname=reroute) command can be used only for a PW protection group with the master/slave PW redundancy mode.
   * [**delay**](cmdqueryname=delay) *delay-time*: indicates delayed switchback, meaning that traffic is switched back to the primary PW after a delay.
   * **immediately**: indicates immediate switchback.
   * **never**: indicates non-switchback. Traffic is switched back only after the backup PW fails.
   
   The revertive switching policy for a PW protection group in independent PW redundancy mode can only be immediate switchback and cannot be changed.
   
   The revertive switching policy affects traffic switchback after the primary PW recovers.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.