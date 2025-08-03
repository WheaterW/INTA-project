Assigning an IP Address to an Interface
=======================================

You can assign an IP address to an interface or configure
IP address unnumbered.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface
   view is displayed.
3. Run either of the following commands.
   
   
   * To assign an IP address to the interface, run:
     
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
     ```
   * To configure IP address unnumbered, run:
     
     ```
     [ip address unnumbered](cmdqueryname=ip+address+unnumbered)  interface interface-type interface-number
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before configuring IP address unnumbered on an interface
     on which HDLC runs as a data link layer protocol, ensure that the
     interface borrowing an IP address can learn a route to the peer; otherwise,
     data cannot be transmitted to the peer.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.