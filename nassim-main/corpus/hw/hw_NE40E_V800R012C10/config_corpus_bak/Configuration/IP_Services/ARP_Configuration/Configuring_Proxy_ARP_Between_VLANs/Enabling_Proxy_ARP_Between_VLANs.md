Enabling Proxy ARP Between VLANs
================================

To enable communication between devices in different VLANs, proxy ARP between VLANs is required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ] 
   
   
   
   The sub-interface view is displayed.
3. Run [**arp-proxy inter-sub-vlan-proxy enable**](cmdqueryname=arp-proxy+inter-sub-vlan-proxy+enable)
   
   
   
   Proxy ARP between VLANs is enabled on the sub-interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.