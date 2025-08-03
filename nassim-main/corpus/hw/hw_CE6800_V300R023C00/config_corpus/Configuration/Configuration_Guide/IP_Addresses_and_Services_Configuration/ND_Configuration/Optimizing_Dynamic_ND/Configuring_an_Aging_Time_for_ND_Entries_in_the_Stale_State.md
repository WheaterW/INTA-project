Configuring an Aging Time for ND Entries in the Stale State
===========================================================

Configuring an Aging Time for ND Entries in the Stale State

#### Context

You can configure a shorter aging time for ND entries in the Stale state to speed up their aging.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an aging time for ND entries in the Stale state.
   
   
   ```
   [ipv6 nd stale-timeout](cmdqueryname=ipv6+nd+stale-timeout) seconds
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
5. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
6. Configure an aging time for ND entries in the Stale state for the interface.
   
   
   ```
   [ipv6 nd stale-timeout](cmdqueryname=ipv6+nd+stale-timeout) seconds
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```