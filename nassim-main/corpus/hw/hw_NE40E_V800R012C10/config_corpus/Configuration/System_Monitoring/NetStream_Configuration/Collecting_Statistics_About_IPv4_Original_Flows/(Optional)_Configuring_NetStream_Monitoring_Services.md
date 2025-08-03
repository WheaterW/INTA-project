(Optional) Configuring NetStream Monitoring Services
====================================================

NetStream monitoring services can be configured on the NetStream Data Exporter (NDE), enabling carriers to implement more delicate traffic statistics collection and management over IPv4 original flows.

#### Context

Increasing types of services and applications on networks urge carriers to provide more delicate management and accounting services.

If NetStream is configured on multiple interfaces on an NDE, all interfaces send traffic statistics to a single NetStream Collector (NSC). The NSC cannot distinguish interfaces, and therefore, cannot manage or analyze traffic statistics based on interfaces. In addition, the NSC will be overloaded due to a great amount of information.

NetStream monitoring configured on an NDE allows the NDE to send traffic statistics collected on specified interfaces to specified NSCs for analysis, achieving interface-specific service monitoring. Traffic statistics can be balanced among these NSCs to reduce the load on a single NSC.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip netstream monitor**](cmdqueryname=ip+netstream+monitor) *monitor-name*
   
   
   
   A NetStream monitoring service view is created and displayed, or an existing NetStream monitoring service view is directly displayed.
3. (Optional) Run [**ip netstream export source**](cmdqueryname=ip+netstream+export+source) { *ip-address* | [**ipv6**](cmdqueryname=ipv6) *ipv6-address* } [ port ]
   
   
   
   A source IP address and a source port are configured for outputting NetStream flows.
4. Run [**ip netstream export host**](cmdqueryname=ip+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **version** { **5** | **9** | **ipfix** } ] [ **dscp** *dscp-value* ]
   
   
   
   The destination IP address for outputting statistics and the UDP port number of the peer NSC are configured.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
7. Run [**ip netstream monitor**](cmdqueryname=ip+netstream+monitor) *monitor-name* { **inbound** | **outbound** }
   
   
   
   NetStream monitoring services are deployed in the inbound or outbound direction of the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When configuring NetStream monitoring services, you need to run the [**ip netstream**](cmdqueryname=ip+netstream) { **inbound** | **outbound** } command in the interface view. Otherwise, the [**ip netstream monitor**](cmdqueryname=ip+netstream+monitor) *monitor-name* { **inbound** | **outbound** } command does not take effect.
   
   If NetStream monitoring services have been configured on the interface, statistics about original flows are sent to the destination IP address specified in the NetStream monitoring service view, not that specified in the system view. Similarly, the source address and source port configured in the NetStream monitoring service view are used for outputting statistics.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.