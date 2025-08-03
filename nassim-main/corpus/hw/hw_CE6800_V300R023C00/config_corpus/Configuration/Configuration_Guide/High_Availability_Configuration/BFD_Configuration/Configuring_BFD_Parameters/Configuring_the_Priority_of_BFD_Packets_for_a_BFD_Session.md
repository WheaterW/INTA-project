Configuring the Priority of BFD Packets for a BFD Session
=========================================================

Configuring the Priority of BFD Packets for a BFD Session

#### Context

You can change the priority of BFD packets to implement the following functions:

* Check whether packets with different priorities on a link can be properly forwarded.
* Preferentially forward high-priority BFD packets.

#### Procedure

* To configure the priority of BFD packets for dynamic or static BFD sessions in batches, perform the following steps:
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BFD view.
     
     ```
     [bfd](cmdqueryname=bfd)
     ```
  3. Configure the priority of BFD packets for all dynamic or static BFD sessions.
     
     ```
     [tos-exp](cmdqueryname=tos-exp) tos-value { dynamic | static }
     ```
     
     The default priority of BFD packets is 7. The value 0 indicates the lowest priority, whereas the value 7 indicates the highest priority.
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```
* To configure the priority of BFD packets for a single static BFD session, perform the following steps:
  
  1. Enter the system view.
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BFD session view.
     ```
     [bfd](cmdqueryname=bfd) session-name
     ```
  3. Configure the priority of BFD packets for the specified BFD session.
     ```
     [tos-exp](cmdqueryname=tos-exp) tos-value
     ```
     
     The default priority of BFD packets is 7. The value 0 indicates the lowest priority, whereas the value 7 indicates the highest priority.
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```