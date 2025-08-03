Disabling Rapid EBGP Connection Reset
=====================================

Disabling rapid EBGP connection reset can prevent frequent reestablishment and deletion of EBGP sessions if route flapping occurs. This speeds up BGP network convergence.

#### Context

With rapid EBGP connection reset, BGP can immediately respond to a fault on an interface and delete the direct EBGP sessions on the interface without waiting for the hold timer to expire, which speeds up BGP network convergence. Rapid EBGP connection reset is enabled by default.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Rapid EBGP connection reset enables BGP to quickly respond to interface faults, but not interface recovery. After the interface recovers, BGP uses its state machine to restore relevant sessions.

If the status of an interface used to establish an EBGP connection changes frequently, the EBGP session will be deleted and reestablished repeatedly, causing network flapping. To address this issue, disable rapid EBGP connection reset so that BGP will not delete direct EBGP sessions on the interface until the hold timer expires. Therefore, disabling rapid EBGP connection reset suppresses BGP network flapping, speed ups BGP network convergence, and reduces network bandwidth consumption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**undo ebgp-interface-sensitive**](cmdqueryname=undo+ebgp-interface-sensitive)
   
   
   
   Rapid EBGP connection reset is disabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Disable rapid EBGP connection reset only when the status of an interface used to establish an EBGP connection changes frequently. If the status of the interface becomes stable, run the [**ebgp-interface-sensitive**](cmdqueryname=ebgp-interface-sensitive) command to enable rapid EBGP connection reset.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.