(Optional) Binding IP FRR and BFD
=================================

(Optional) Binding IP FRR and BFD

#### Context

Binding IP FRR and BFD is implemented by associating the status of BFD sessions with the link status of interfaces. This ensures that a link fault can be detected immediately and traffic can be quickly switched to the backup link.

* IP FRR and BFD can be bound in an OSPF process so that the binding takes effect for all interfaces in the OSPF process.
* Alternatively, IP FRR and BFD can be bound on specified interfaces.

Perform the following steps on the device where IP FRR and BFD need to be bound.


#### Procedure

* Bind IP FRR and BFD in an OSPF process.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the OSPF view.
     
     
     ```
     [ospf](cmdqueryname=ospf) [ process-id ]
     ```
     
     The *process-id* parameter specifies the ID of a process, and the default value is 1.
  3. Bind IP FRR and BFD in the OSPF process.
     
     
     ```
     [bfd all-interfaces](cmdqueryname=bfd+all-interfaces) frr-binding
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Bind IP FRR and BFD on a specified OSPF interface.
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
     [ospf bfd](cmdqueryname=ospf+bfd) frr-binding
     ```
     
     The BFD configuration on an interface takes precedence over that in the OSPF process.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```