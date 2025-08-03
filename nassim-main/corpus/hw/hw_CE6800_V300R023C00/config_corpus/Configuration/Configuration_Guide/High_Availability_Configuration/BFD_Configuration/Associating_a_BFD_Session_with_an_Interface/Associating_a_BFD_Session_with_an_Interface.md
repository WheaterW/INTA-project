Associating a BFD Session with an Interface
===========================================

Associating a BFD Session with an Interface

#### Prerequisites

Before associating a BFD session with an interface, you must create a BFD session.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OAM management view.
   
   
   ```
   [oam-mgr](cmdqueryname=oam-mgr)
   ```
3. Configure the BFD session to transmit fault notification messages to an interface.
   
   
   ```
   [oam-bind ingress bfd-session](cmdqueryname=oam-bind+ingress+bfd-session) { bfd-session-id | session-name bfd-session-name } trigger if-down egress interface interface-type interface-number
   ```
   
   The physical status of the interface bound to the BFD session becomes down after the BFD session detects a fault.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```