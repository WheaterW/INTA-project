(Optional) Manually Switching PWs in a PW Protection Group
==========================================================

In PW maintenance, you can manually switch services to the standby PW to facilitate maintenance operations.

#### Context

If you want to maintain the device where the active PW is configured in a VPLS PW redundancy scenario, you can switch services from the active PW to the standby PW and switches services back after the device stabilizes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the PWs that work in master/slave PW redundancy mode support manual switching.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The view of the created VSI is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
   
   
   
   The VSI-LDP view is displayed.
4. Run [**protect-group**](cmdqueryname=protect-group) *group-name*
   
   
   
   A PW protection group is created, and the PW protection group view is displayed.
5. Run [**protect-switch manual**](cmdqueryname=protect-switch+manual)
   
   
   
   An active/standby PW switching is performed in the PW protection group.
6. Run [**protect-switch clear**](cmdqueryname=protect-switch+clear)
   
   
   
   An active/standby PW switchback is performed in the PW protection group.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.