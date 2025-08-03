Enabling Proxy ARP Anyway
=========================

This section describes how to enable proxy ARP anyway on a gateway to interconnect different subnets of an IP network when the gateways connected to VMs have the same IP address.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**arp-proxy anyway enable**](cmdqueryname=arp-proxy+anyway+enable)
   
   
   
   Proxy ARP anyway is enabled on the interface.
   
   
   
   After proxy ARP anyway is enabled on a device, you need to shorten the aging time of dynamic ARP entries to make them invalid as soon as possible. This can reduce the number of received packets that cannot be forwarded on the device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.