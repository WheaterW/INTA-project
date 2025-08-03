(Optional) Configuring the Priority of an ATM PVC
=================================================

By setting priorities for ATM PVC traffic, you can schedule traffic on the PVCs with different priorities.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **atm** *interface-number.sub-interface*
   
   
   
   The ATM sub-interface view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To configure the priorities of all PVCs in the interface view, you can run the [**service output priority**](cmdqueryname=service+output+priority) command on the interface.
3. Run [**pvc**](cmdqueryname=pvc) *pvc-name* [ *vpi*/*vci* ]
   
   
   
   The PVC view is displayed.
4. Run [**service output priority**](cmdqueryname=service+output+priority) *priority-value*
   
   
   
   The priority of the PVC is specified.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can use this command to configure priorities of UBR and UBR-plus type PVCs. Therefore, the system can schedule the traffic in the PVCs with different priorities.