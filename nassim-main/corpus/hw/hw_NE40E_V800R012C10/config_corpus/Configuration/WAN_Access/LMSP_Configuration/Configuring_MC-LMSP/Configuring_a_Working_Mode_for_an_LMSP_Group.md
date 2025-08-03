Configuring a Working Mode for an LMSP Group
============================================

A working mode can be configured for an LMSP group. The NE40E supports LMSP working modes, including automatic LMSP switching and a delayed switchback with the wait to restore (WTR) time configured. An LMSP working mode must be configured on a protection interface.

#### Context

Automatic LMSP switching modes are classified as 1:1 bidirectional or 1+1 unidirectional.

After a fault in the working link is rectified, services automatically switch from the protection link to the working link. During the switchback, some service traffic is dropped because some resources related to the working link or NE40E are being restored. To prevent service loss, the WTR time can be set on the NE40E to delay a switchback. Services can automatically switch from the protection link back to the working link in the specified WTR time after the working link becomes available.

Perform the following steps on a protection interface in an LMSP group:


#### Procedure

* Configure an automatic protection switching mode for an LMSP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run the following commands to display the interface view:
     
     
     ```
     [controller cpos](cmdqueryname=controller+cpos) cpos-number
     ```
  3. Run [**aps mode**](cmdqueryname=aps+mode) { **one2one bidirection** | **one-plus-one** { **bidirection** | **unidirection** } }
     
     
     
     A working mode is configured for the LMSP group. One of the following parameter combinations can be configured:
     
     + **one2one bidirection**:
       - 1:1 mode: Only the working link transmits traffic. The protection link takes over traffic only if the working link fails.
       - Bidirectional mode: The transmit end sends traffic along and the receive end receives traffic from the protection link if a fault occurs on the working link.
     + **one-plus-one unidirection**:
       - 1+1 mode: Both the working and protection links transmit traffic.
       - Unidirectional mode: Only the receive end receives traffic from the protection link if a fault occurs on the optical fiber to an interface.
     + **one-plus-one bidirection**:
       - 1+1 mode: Both the working and protection links transmit traffic.
       - Bidirectional mode: The transmit end sends traffic along and the receive end receives traffic from the protection link if a fault occurs on the working link.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Set the WTR time for an LMSP group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run the following commands:
     
     
     ```
     [controller cpos](cmdqueryname=controller+cpos) cpos-number
     ```
     
     The protection interface view of the LMSP group is displayed.
  3. Run [**aps revert**](cmdqueryname=aps+revert) *wtr-time*
     
     
     
     The WTR time is set for the LMSP group.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If two different switchback delays are set on two protection interfaces in LMSP groups on two ends of a link, the effective switchback delay depends on one of the following situations:
     
     + If **one-plus-one** **unidirection** is configured, the switchback delays on both protection interfaces take effect after the working interfaces recover.
     + If **one2one bidirection** or **one-plus-one** **bidirection** is configured, the switchback delay on the protection interface of the device with the working interface recovering later than the other working interface takes effect on both protection interfaces.
     + In an MC-LMSP scenario, the switchback time must be the same on two LMSP devices on the RNC side and slave RSG side.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.