Filtering a Port Number and a Port Range
========================================

To secure networks from virus, configure the port filter function on a CGN service board to prevent an unwanted port from being translated to a filtered port and resulting in a packet forwarding failure.

#### Context

The port filter function may cause the core router (CR) to discard returned packets. A NAT64 service board translates a private source port into a filtered port used to forward packets from a private network to a public network. After packets are returned from the public network to the private network, the CR finds that the packets' destination port is within a range of filtered ports and unexpectedly discards the packets, which interrupts user services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
   
   
   
   The NAT64 instance view is displayed.
3. Run [**exclude-port**](cmdqueryname=exclude-port) { *start-port* [ **to** *end-port* ] } & <1â10>
   
   
   
   A port number and a port range to be filtered are specified.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.