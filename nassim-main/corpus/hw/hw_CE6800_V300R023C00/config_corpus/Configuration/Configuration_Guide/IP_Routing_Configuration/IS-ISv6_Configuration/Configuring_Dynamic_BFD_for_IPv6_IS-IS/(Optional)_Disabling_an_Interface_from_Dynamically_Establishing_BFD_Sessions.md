(Optional) Disabling an Interface from Dynamically Establishing BFD Sessions
============================================================================

(Optional) Disabling an Interface from Dynamically Establishing BFD Sessions

#### Context

If the [**ipv6 bfd all-interfaces enable**](cmdqueryname=ipv6+bfd+all-interfaces+enable) command is run for an IS-IS process on a P2P network, all IS-IS interfaces whose neighbors are up establish IPv6 BFD sessions. If the command is run for an IS-IS process on a broadcast network, all IS-IS interfaces whose neighbors are up in this process establish IPv6 BFD sessions between the DIS and non-DISs. To disable an interface from establishing IPv6 BFD sessions, perform the following operations.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Disable the interface from dynamically establishing IPv6 BFD sessions.
   
   
   ```
   [isis ipv6 bfd block](cmdqueryname=isis+ipv6+bfd+block)
   ```
   
   By default, an IS-IS interface can dynamically establish IPv6 BFD sessions.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```