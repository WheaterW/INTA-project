Enabling Routed Proxy ARP
=========================

To allow subnets on the same IP network to communicate, enable routed proxy ARP.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**arp-proxy enable**](cmdqueryname=arp-proxy+enable)
   
   
   
   Routed proxy ARP is enabled on the interface.
   
   
   
   After routed proxy ARP is enabled on a Router, you must reduce the aging time of ARP entries on the Router so that the number of packets received but cannot be forwarded by the Router is decreased.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.