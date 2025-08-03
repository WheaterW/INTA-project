Enabling Proxy ARP Within a VLAN
================================

To enable communication between isolated devices within the same VLAN, proxy ARP within the VLAN is required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ] 
   
   
   
   The sub-interface view is displayed.
3. Run [**arp-proxy inner-sub-vlan-proxy enable**](cmdqueryname=arp-proxy+inner-sub-vlan-proxy+enable)
   
   
   
   Proxy ARP within a VLAN is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.