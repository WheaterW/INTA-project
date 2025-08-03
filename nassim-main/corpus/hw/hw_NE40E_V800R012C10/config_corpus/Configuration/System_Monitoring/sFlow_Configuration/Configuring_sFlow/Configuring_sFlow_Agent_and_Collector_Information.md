Configuring sFlow Agent and Collector Information
=================================================

Configuring sFlow Agent and Collector Information

#### Prerequisites

Before configuring sFlow, you have completed the following tasks:

* Ensure that there are reachable routes between the sFlow agent and collector.
* Create a VPN instance if the sFlow agent and collector are deployed on a private network.

#### Context

During sFlow configuration, you must create an sFlow collector and specify its address as the destination address for sFlow packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**sflow**](cmdqueryname=sflow)
   
   
   
   The sFlow view is displayed.
3. Run [**sflow agent**](cmdqueryname=sflow+agent) { **ip** *ip-address* | **ipv6** *ipv6-address* }
   
   
   
   An IP address is configured for the sFlow agent.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The address specified by *ip-address* must be a valid unicast address that has been configured on an interface of the device. The address specified by *ipv6-address* must be a global unicast address (it cannot be a link-local address).
4. (Optional) Run [**sflow export extended-route-data disable**](cmdqueryname=sflow+export+extended-route-data+disable)
   
   
   
   The sFlow agent is disabled from collecting routing information.
5. Run [**sflow collector**](cmdqueryname=sflow+collector) *collector-id*
   
   
   
   An sFlow collector is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Up to two sFlow collectors can be configured in each VS.
6. Run [**sflow server**](cmdqueryname=sflow+server) { **ip** *ip-address* | **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-name* ] [ **udp-port** *port* ]
   
   
   
   The destination IP address of sFlow packets is specified. sFlow packets must be sent through the service interface instead of the out-of-band management interface.
7. (Optional) Run [**sflow max-packet-length**](cmdqueryname=sflow+max-packet-length) *length*
   
   
   
   The maximum length of sFlow packets is set.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.