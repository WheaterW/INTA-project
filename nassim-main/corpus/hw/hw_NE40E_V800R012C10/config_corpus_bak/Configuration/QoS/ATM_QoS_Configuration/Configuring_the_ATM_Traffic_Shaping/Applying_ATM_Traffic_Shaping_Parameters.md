Applying ATM Traffic Shaping Parameters
=======================================

ATM traffic shaping parameters are applied to ATM interfaces
or ATM sub-interfaces.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **atm** *interface-number*[.*subinterface* ]
   
   
   
   The ATM interface
   view or sub-interface view is displayed.
3. Run the following command as required:
   
   
   * To create PVP and display the PVP view, run:
     
     ```
     [pvp](cmdqueryname=pvp) vpi
     ```
   * To create PVC and display the PVC view, run:
     
     ```
     [pvc](cmdqueryname=pvc) { pvc-name vpi/vci | vpi/vci }
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + PVP can be configured on ATM sub-interfaces only.
     + PVP and PVC should not coexist on the same ATM sub-interface.
4. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The PVC or PVP is shut down.
5. Run [**service**](cmdqueryname=service)
   { **input** | **output** } *service-name*
   
   
   
   The service type of
   PVC or PVP is specified and the traffic shaping parameters are applied
   to the PVC or PVP.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) To specify
   a service type of PVC or PVP with the [**service**](cmdqueryname=service) **output** command, you need to run the [**shutdown**](cmdqueryname=shutdown) command to shut down the PVC or PVC and then run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to re-enable the PVC or PVP. In this manner, the
   configuration can be ensured to take effect.
6. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   
   
   Traffic shaping is enabled on the PVC or PVP.