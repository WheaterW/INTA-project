Configuring Multicast NAT on an Outbound Interface
==================================================

This section describes how to configure multicast NAT on an outbound interface of multicast streams and specify a source IP address, destination IP address, and destination port number for post-translation multicast streams.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the outbound interface of multicast streams is displayed.
3. Run [**multicast-nat outbound**](cmdqueryname=multicast-nat+outbound) **id** *outbound-id* [ **name** *outbound-name* ] [ **src-mac auto-translate** ] [ **src-ip** *source-address* ] [ **dst-ip** *destination-address* ] [ **src-udp-port** *source-port* ] [ **dst-udp-port**  *port* ] [ **rtp-ssrc auto-translate** ] [ **rtp-sn auto-translate** [ **rtp-ext-sn auto-translate** ] ]
   
   
   
   The source IP address, destination IP address, and destination port number are specified for post-translation multicast streams.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.