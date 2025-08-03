Outputting Aggregation Flow Packets
===================================

To ensure that aggregation flow packets are correctly output to the NMS, configure the aging time, source address, and destination address for aggregated flows.

#### Context

IPv6 aggregation flow packets can be output only in the V9 or IPFIX format.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 netstream export host**](cmdqueryname=ipv6+netstream+export+host) *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ]
   
   
   
   The destination IP address of the output packets carrying statistics is configured.
   
   
   
   The destination IP address specified in the system view takes precedence over that specified in the aggregation view.
3. Run [**ipv6 netstream aggregation**](cmdqueryname=ipv6+netstream+aggregation) { **as** | **as-tos** | **bgp-nexthop-tos** | **destination-prefix** | **destination-prefix-tos** | **index-tos** | **mpls-label** | **prefix** | **prefix-tos** | **protocol-port** | **protocol-port-tos** | **source-prefix** | **source-prefix-tos** | **vlan-id** }
   
   
   
   The IPv6 NetStream aggregation view is displayed.
4. Run [**enable**](cmdqueryname=enable)
   
   
   
   The NetStream aggregation mode is enabled.
5. (Optional) Run [**export version**](cmdqueryname=export+version) { **9** | **ipfix** }
   
   
   
   The output format of aggregation flows is configured.
6. (Optional) Run [**template timeout-rate**](cmdqueryname=template+timeout-rate) *timeout-interval*
   
   
   
   The interval at which the template is refreshed when aggregation flows are exported in the V9 or IPFIX format is set.
7. Run [**ipv6 netstream export source**](cmdqueryname=ipv6+netstream+export+source) { *ip-address* | **ipv6** *ipv6-address* } [ *port* ]
   
   
   
   The source address and source port for exporting statistics are configured.
   
   
   
   The source IP address and the source port configured in the aggregation view take precedence over that configured in the system view. If no source IP address and source port are configured in the aggregation view, the source IP address and the source port configured in the system view are used.
8. Run [**ipv6 netstream export host**](cmdqueryname=ipv6+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ]
   
   
   
   A destination IP address and a UDP port number are configured for outputting statistics.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * You can specify eight destination IP addresses in the system view, IPv4 aggregation view, and IPv6 aggregation view.
   * The destination IP address specified in the system view takes precedence over that specified in the aggregation view.
   * NetStream packets are output to the NSC through the service interface instead of the management interface.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. (Optional) Set parameters for aging aggregated flows as needed:
    
    
    * Run the [**ipv6 netstream aggregation timeout**](cmdqueryname=ipv6+netstream+aggregation+timeout) **active** { *active-interval* | **interval-second** *active-interval-second* } command to set the active aging time for NetStream aggregation flows.
    * Run the [**ipv6 netstream aggregation timeout**](cmdqueryname=ipv6+netstream+aggregation+timeout) **inactive** *inactive-interval* command to set the inactive aging time for NetStream aggregation flows.
11. (Optional) Run [**ipv6 netstream export template sequence-number fixed**](cmdqueryname=ipv6+netstream+export+template+sequence-number+fixed)
    
    
    
    The device is configured to keep the sequence numbers of template packets and option template packets in the IPFIX format unchanged and to consecutively number data packets and option data packets in the IPFIX format.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.