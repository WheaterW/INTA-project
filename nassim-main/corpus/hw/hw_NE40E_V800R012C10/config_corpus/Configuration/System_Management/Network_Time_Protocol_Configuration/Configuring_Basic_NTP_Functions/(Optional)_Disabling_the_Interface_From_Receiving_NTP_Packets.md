(Optional) Disabling the Interface From Receiving NTP Packets
=============================================================

To prevent a host on the LAN from synchronizing the clock on the specified server, you can disable the specified interface on the host from receiving NTP packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ntp-service**](cmdqueryname=ntp-service) **in-interface** **disable** or [**ntp-service**](cmdqueryname=ntp-service) **ipv6** **in-interface** **disable**
   
   
   
   The interface on the device is disabled from receiving NTP packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.