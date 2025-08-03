(Optional) Disabling an Interface from Dynamically Establishing BFD Sessions
============================================================================

(Optional) Disabling an Interface from Dynamically Establishing BFD Sessions

#### Context

If the [**bfd all-interfaces enable**](cmdqueryname=bfd+all-interfaces+enable) command is run for an IS-IS process on a P2P network, all IS-IS interfaces whose neighbors are up establish dynamic BFD sessions. If the command is run for an IS-IS process on a broadcast network, all IS-IS interfaces whose neighbors are up in this process establish dynamic BFD sessions between the DIS and non-DISs. To disable an interface from dynamically establishing BFD sessions, perform the following operations.


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
4. Disable the interface from dynamically establishing BFD sessions.
   
   
   ```
   [isis bfd block](cmdqueryname=isis+bfd+block)
   ```
   
   By default, an IS-IS interface can dynamically establish BFD sessions.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```