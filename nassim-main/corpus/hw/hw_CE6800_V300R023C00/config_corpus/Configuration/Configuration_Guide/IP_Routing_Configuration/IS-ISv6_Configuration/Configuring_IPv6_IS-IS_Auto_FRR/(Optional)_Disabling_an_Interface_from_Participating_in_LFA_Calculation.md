(Optional) Disabling an Interface from Participating in LFA Calculation
=======================================================================

(Optional) Disabling an Interface from Participating in LFA Calculation

#### Context

By default, IPv6 IS-IS interfaces can participate in LFA calculation. In cases where the primary link fails and a backup link is also at risk of failure, you can disable the interface corresponding to the backup link from participating in LFA calculation to control the traffic forwarding path.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Disable the interface from participating in LFA calculation.
   
   
   ```
   [undo isis ipv6 lfa-backup](cmdqueryname=undo+isis+ipv6+lfa-backup) [ level-1 | level-2 | level-1-2 ] 
   ```
   
   
   
   By default, IPv6 IS-IS interfaces can participate in LFA calculation.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```