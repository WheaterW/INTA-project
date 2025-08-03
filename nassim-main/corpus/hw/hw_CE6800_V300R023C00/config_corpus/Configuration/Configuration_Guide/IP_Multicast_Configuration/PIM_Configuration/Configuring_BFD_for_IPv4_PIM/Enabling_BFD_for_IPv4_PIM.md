Enabling BFD for IPv4 PIM
=========================

Enabling BFD for IPv4 PIM

#### Context

Enable BFD for IPv4 PIM on the interfaces that connect PIM neighbors. This function applies only to non-broadcast multiple access (NBMA) and broadcast interfaces and cannot be enabled on MTunnel interfaces.


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
4. Enable BFD for IPv4 PIM.
   
   
   ```
   [pim bfd enable](cmdqueryname=pim+bfd+enable)
   ```
   
   
   
   By default, BFD for IPv4 PIM is disabled.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```