(Optional) Re-Encapsulating IRB (v6) Routes into the desired Routes
===================================================================

If you want to convert the IRB routes carrying the network segment address of a tenant host that are received by a device into host IP prefix routes or ARP routes, or convert the IRBv6 routes carrying the IPv6 network segment address of a tenant host that are received by a device into host IPv6 prefix routes or ND routes, you must enable the device to re-encapsulate IRB or IRBv6 routes into the desired routes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn**](cmdqueryname=evpn)
   
   
   
   The global EVPN configuration view is created and displayed.
3. Run [**irb-reoriginated compatible**](cmdqueryname=irb-reoriginated+compatible)
   
   
   
   The device is enabled to re-encapsulate IRB routes into IP prefix routes and ARP routes, or re-encapsulate IRBv6 routes into IPv6 prefix routes and ND routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.