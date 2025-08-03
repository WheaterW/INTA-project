Adding an Interface to an IS-IS Mesh Group
==========================================

Adding an Interface to an IS-IS Mesh Group

#### Context

After an interface on a device receives a new LSP, the device floods the LSP through other local interfaces. On a network with high connectivity and multiple P2P links, such processing causes repeated LSP flooding, wasting bandwidth. To prevent this problem, you can add some interfaces to a mesh group. Interfaces in a mesh group flood their received LSPs only to the interfaces that are not in this mesh group, and use the CSNP and PSNP mechanisms to synchronize the LSDBs in the entire network segment.


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
4. Add the interface to a mesh group.
   
   
   ```
   [isis mesh-group](cmdqueryname=isis+mesh-group) { mesh-group-number | mesh-blocked }
   ```
   
   
   
   If **mesh-blocked** is specified, the interface is blocked and cannot flood LSPs. All the interfaces in a mesh group ensure the synchronization of the LSDBs in the entire network segment using the CSNP and PSNP mechanisms.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis mesh-group**](cmdqueryname=display+isis+mesh-group) [ *process-id* | **vpn-instance** *vpn-instance-name*] command to check IS-IS mesh group configurations.