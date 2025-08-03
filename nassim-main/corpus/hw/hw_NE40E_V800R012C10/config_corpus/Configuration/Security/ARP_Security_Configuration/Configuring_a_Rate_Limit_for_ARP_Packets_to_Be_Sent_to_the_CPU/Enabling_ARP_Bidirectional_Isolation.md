Enabling ARP Bidirectional Isolation
====================================

Address Resolution Protocol (ARP) bidirectional isolation
enables the Router to process ARP request and reply packets separately, improving the
fault locating efficiency when a large number of ARP packets are received
in a short period.

#### Context

Configure ARP bidirectional isolation on interfaces of
the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view
   is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*sub-interface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**arp-safeguard enable**](cmdqueryname=arp-safeguard+enable)
   
   
   
   ARP bidirectional
   isolation is enabled.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   ARP bidirectional isolation is
   mutually exclusive to of L2VPN and proxy ARP. Before configuring ARP
   bidirectional isolation, delete L2VPN and proxy ARP configurations,
   if present.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.