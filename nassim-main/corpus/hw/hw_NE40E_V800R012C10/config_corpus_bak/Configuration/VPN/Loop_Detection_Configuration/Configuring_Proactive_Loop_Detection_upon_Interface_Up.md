Configuring Proactive Loop Detection upon Interface Up
======================================================

Proactive loop detection upon interface up takes effect only after being enabled in both the system and interface views.

#### Context

Perform the following steps on PEs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the VS mode is used, this configuration task is supported only by the admin VS.


![](../../../../public_sys-resources/notice_3.0-en-us.png) 

It is therefore recommended that you disable this function on devices that are operating normally. If it is used to detect link connectivity during the site deployment stage, disable it after this stage is complete.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**loop-detect trigger enable**](cmdqueryname=loop-detect+trigger+enable)
   
   
   
   Proactive loop detection upon interface up is enabled globally.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After proactive loop detection upon interface up is enabled globally, it must also be enabled on specific interfaces. Otherwise, it cannot work.
   * After proactive loop detection upon interface up is disabled globally, it stops working.
3. (Optional) Enable proactive loop detection upon interface up.
   1. Run the [**interface**](cmdqueryname=interface) { **gigabitethernet** | **eth-trunk** } *interface-number* command to enter the view of an interface.
   2. Run the [**undo loop-detect trigger disable**](cmdqueryname=undo+loop-detect+trigger+disable) command to enable proactive loop detection on the interface.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The interface must be an AC interface.
      * Proactive loop detection upon interface up takes effect only after being enabled in both the system and interface views.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. (Optional) Run [**loop-detect trigger min-slot-uptime**](cmdqueryname=loop-detect+trigger+min-slot-uptime) *min-slot-uptime*
   
   
   
   The minimum delay before proactive loop detection starts to take effect after an interface board is started is configured.
5. (Optional) Run [**loop-detect trigger min-port-uptime**](cmdqueryname=loop-detect+trigger+min-port-uptime)*min-port-uptime*
   
   
   
   The minimum delay before proactive loop detection starts to take effect after an interface goes up is configured.
6. (Optional) Specify the range of VLANs to which the main interface sends proactive loop detection packets.
   1. Run the [**interface**](cmdqueryname=interface) { **gigabitethernet** | **eth-trunk** } *interface-number* command to enter the interface view.
   2. Run the [**loop-detect trigger detection vid**](cmdqueryname=loop-detect+trigger+detection+vid) *low-vid* [ **to** *high-vid* ] command to specify the range of VLANs to which the main interface sends proactive loop detection packets.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.