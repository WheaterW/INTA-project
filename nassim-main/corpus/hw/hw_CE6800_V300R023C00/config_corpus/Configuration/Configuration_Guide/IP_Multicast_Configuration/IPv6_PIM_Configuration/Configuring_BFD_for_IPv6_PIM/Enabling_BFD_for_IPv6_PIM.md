Enabling BFD for IPv6 PIM
=========================

Enabling BFD for IPv6 PIM

#### Context

You can enable BFD for IPv6 PIM on the interfaces that connect PIM neighbors. This function applies only to non-broadcast multiple access (NBMA) and broadcast interfaces, not to MTunnel interfaces.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable IPv6 PIM-SM.
   
   
   ```
   [pim ipv6 sm](cmdqueryname=pim+ipv6+sm)
   ```
5. Enable BFD for IPv6 PIM.
   
   
   ```
   [pim ipv6 bfd enable](cmdqueryname=pim+ipv6+bfd+enable)
   ```
   
   
   
   By default, BFD for IPv6 PIM is disabled.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```