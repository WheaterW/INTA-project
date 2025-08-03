Setting the MTU Value for DS-Lite Services
==========================================

You can change the MTU value so that the packets for DS-Lite are not fragmented, improving DS-Lite translation efficiency.

#### Context

When the link MTU is small, DS-Lite packet fragments may be generated. You can change the MTU value so that the packets for DS-Lite are not fragmented, improving DS-Lite translation efficiency.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* **id** *id*
   
   
   
   The DS-Lite instance view is displayed.
3. Run [**ds-lite mtu**](cmdqueryname=ds-lite+mtu) *mtu-value*
   
   
   
   The IPv6 MTU for packets of a DS-Lite instance is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.