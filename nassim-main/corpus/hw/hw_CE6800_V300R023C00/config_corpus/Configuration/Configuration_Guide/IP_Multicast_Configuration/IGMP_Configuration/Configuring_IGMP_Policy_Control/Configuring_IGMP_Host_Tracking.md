Configuring IGMP Host Tracking
==============================

Configuring IGMP Host Tracking

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface connected to the user network segment.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable IGMP.
   
   
   ```
   [igmp enable](cmdqueryname=igmp+enable)
   ```
5. Set the IGMP version to IGMPv3 on the interface.
   
   
   ```
   [igmp version](cmdqueryname=igmp+version) 3
   ```
6. Configure the host tracking function.
   
   
   ```
   [igmp explicit-tracking](cmdqueryname=igmp+explicit-tracking)
   ```
   
   The host tracking function can be used only in IGMPv3 scenarios.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```