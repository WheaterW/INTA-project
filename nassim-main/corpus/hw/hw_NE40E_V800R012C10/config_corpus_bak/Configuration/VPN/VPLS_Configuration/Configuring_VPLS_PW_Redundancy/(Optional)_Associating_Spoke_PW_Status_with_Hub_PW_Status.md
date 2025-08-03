(Optional) Associating Spoke PW Status with Hub PW Status
=========================================================

After spoke PW status is associated with hub PW status, a spoke PW will go down if the associated hub PWs all go down, triggering a primary/secondary spoke PW switchover.

#### Context

In a VPLS PW redundancy scenario: If all the hub PWs of an SPE where the primary spoke PW resides go down but the primary spoke PW is still up, traffic still travels along the primary spoke PW to the SPE. Because all hub PWs of the SPE are down, the SPE discards received traffic. To prevent this situation, associate spoke PW status with hub PW status on the SPE where the primary spoke PW resides. Then, after all the hub PWs of the SPE where the primary spoke PW resides go down, the SPE instructs the UPE to switch traffic to the secondary spoke PW.

**Figure 1** VPLS PW redundancy networking  
![](figure/en-us_image_0192710678.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The view of the created VSI is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   The VSI-LDP view is displayed.
4. Run [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name*
   
   
   
   A PW is created, and its view is displayed.
5. Run [**track hub-pw**](cmdqueryname=track+hub-pw)
   
   
   
   Spoke PW status is associated with hub PW status.
   
   
   
   This command applies only to spoke PWs. Ensure that spoke PWs have been created using the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] [ **tnl-policy** *policy-name* ] [ [ **endpoint** *endpoint4-address* ] **color** *color-value* ] **upe** command.
   
   After this command is run, SPE1 instructs the UPE to switch traffic to the secondary spoke PW after detecting that all connected hub PWs are down. The [**protect-group**](cmdqueryname=protect-group) *group-name* and [**protect-mode pw-redundancy**](cmdqueryname=protect-mode+pw-redundancy) **master** commands must have been run to create a PW protection group with the master/slave PW redundancy mode, and the primary and secondary PWs must have been added to the group.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.