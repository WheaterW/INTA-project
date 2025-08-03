(Optional) Binding IP FRR and BFD
=================================

(Optional) Binding IP FRR and BFD

#### Context

Binding IP FRR and BFD is implemented by associating the status of BFD sessions with the link status of interfaces. This ensures that a link fault can be detected immediately and traffic can be quickly switched to the backup link.

* IP FRR and BFD can be bound in an OSPFv3 process so that the binding takes effect for all interfaces in the OSPFv3 process.
* Alternatively, IP FRR and BFD can be bound on specified interfaces.

Perform the following steps on the device where IP FRR and BFD need to be bound.


#### Procedure

* Bind IP FRR and BFD in an OSPFv3 process.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the OSPFv3 view.
     
     
     ```
     [ospfv3](cmdqueryname=ospfv3) [ process-id ]
     ```
  3. Bind IP FRR and BFD in the OSPFv3 process.
     
     
     ```
     [bfd all-interfaces](cmdqueryname=bfd+all-interfaces) frr-binding
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Bind IP FRR and BFD on a specified interface.
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
  4. Bind IP FRR and BFD on the interface.
     
     
     ```
     [ospfv3 bfd](cmdqueryname=ospfv3+bfd) frr-binding
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```