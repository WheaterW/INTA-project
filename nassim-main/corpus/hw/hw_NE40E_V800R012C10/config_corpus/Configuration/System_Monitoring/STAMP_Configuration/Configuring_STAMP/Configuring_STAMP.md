Configuring STAMP
=================

This section describes how to configure STAMP to collect packet loss and delay statistics of a device.

#### Context

STAMP uses a simplified configuration model, eliminating the need to differentiate between the Session-Sender and Session-Reflector roles during configuration.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa stamp**](cmdqueryname=nqa+stamp)
   
   
   
   STAMP is enabled globally, and its view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The interface view is displayed.
5. Run [**stamp**](cmdqueryname=stamp) { **ipv4** | **ipv6** } [**enable**](cmdqueryname=enable)[ **period***periodValue* | **time-out***time-outValue* | **dscp***dscp-value* | **nexthop-ip***ip-addr* | **dest-port***udp-port* ] \*
   
   
   
   IPv4/IPv6 STAMP is enabled on the interface as required.
   
   
   
   You can set *ip-addr* to an IPv4 or IPv6 address based on the service type.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.