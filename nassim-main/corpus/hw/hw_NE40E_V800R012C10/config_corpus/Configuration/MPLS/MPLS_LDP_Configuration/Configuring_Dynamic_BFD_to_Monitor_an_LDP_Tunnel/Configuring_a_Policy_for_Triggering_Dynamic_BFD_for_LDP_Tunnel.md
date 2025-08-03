Configuring a Policy for Triggering Dynamic BFD for LDP Tunnel
==============================================================

Either the host address-based policy or FEC list-based policy can be used to dynamically establish BFD sessions to monitor LDP tunnels.

#### Context

One of the following trigger policies can be used to establish BFD sessions to monitor LDP tunnels:

* Host address-based policy: used when all host addresses are available to trigger the creation of BFD sessions.
* IP address prefix-based policy: used when only FEC entries that match a specified IP address prefix can be used to trigger the creation of BFD sessions.
* FEC list-based policy: used when only some host addresses are available to establish BFD sessions. The FEC list contains specified host addresses.

Perform the following steps on the ingress on which an LDP tunnel to be monitored is established:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls bfd-trigger-tunnel**](cmdqueryname=mpls+bfd-trigger-tunnel+host+ip-prefix+fec-list) { **host** | **ip-prefix** *ip-prefix-name* | **fec-list** *list-name* }
   
   
   
   The policy for establishing a session of dynamic BFD for LDP LSP is configured.
   
   
   
   A BFD session can be created only after this command is executed.
   
   If no parameter is specified, the host address-based policy is used by default.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.