Configuring PPP as the Link Layer Protocol of an Interface
==========================================================

Configure PPP as the link layer protocol of an interface for the interface to implement P2P traffic transmission.

#### Context

PPP is a data link layer protocol used to transmit network layer packets on P2P links. It is extensible and supports both synchronous and asynchronous communication. Before configuring PPP parameters of an interface, configure PPP as the link layer protocol of the interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**link-protocol ppp**](cmdqueryname=link-protocol+ppp)
   
   
   
   PPP is configured as the link layer protocol of the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.