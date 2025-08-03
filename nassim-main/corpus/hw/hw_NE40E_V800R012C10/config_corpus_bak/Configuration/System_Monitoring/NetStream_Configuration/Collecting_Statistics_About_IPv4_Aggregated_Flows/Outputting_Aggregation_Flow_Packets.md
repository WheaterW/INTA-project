Outputting Aggregation Flow Packets
===================================

To ensure that aggregation flow packets are correctly output to the NMS, specify the aging time, output format, and source and destination addresses for aggregation flows.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip netstream export host**](cmdqueryname=ip+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ]
   
   
   
   A destination IP address and a UDP port number are configured for outputting statistics.
   
   
   
   If the destination IP addresses are specified in both the system and the aggregation views, the configuration in the aggregation view takes effect.
3. Run [**ip netstream aggregation**](cmdqueryname=ip+netstream+aggregation) { **as** | **as-tos** | **bgp-nexthop-tos** | **destination-prefix** | **destination-prefix-tos** | **index-tos** | **mpls-label** | **prefix** | **prefix-tos** | **protocol-port** | **protocol-port-tos** | **source-prefix** | **source-prefix-tos** | **source-index-tos** | **vlan-id** | **bgp-community** | **vni-sip-dip** }
   
   
   
   The IPv4 aggregation configuration mode view is displayed.
4. Run [**enable**](cmdqueryname=enable)
   
   
   
   The NetStream aggregation mode is enabled.
5. (Optional) Run [**export version**](cmdqueryname=export+version) { **8** | **9** | **ipfix** }
   
   
   
   The format for outputting aggregation flow packets is set.
   
   
   
   Flows aggregated in **as**, **as-tos**, **destination-prefix**, **destination-prefix-tos**, **prefix**, **prefix-tos**, **protocol-port**, **protocol-port-tos**, **source-prefix**, or **source-prefix-tos** mode are output in the V8 format by default. You can specify the output format for aggregation flows as needed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For the **vlan-id**, **bgp-nhp-tos**, **vni-sip-dip**, and **index-tos** aggregation modes, aggregation flows are output in the V9 format by default. You can change the format to IPFIX using the [**export version**](cmdqueryname=export+version) command.
6. (Optional) Run [**template timeout-rate**](cmdqueryname=template+timeout-rate) *timeout-interval*
   
   
   
   The interval at which the template for outputting aggregation flows in the V9 or IPFIX format is refreshed is set.
7. Run [**ip netstream export source**](cmdqueryname=ip+netstream+export+source) { *ip-address* | **ipv6** *ipv6-address* } [ *port* ]
   
   
   
   The source IP address and source port are specified for aggregation flows.
   
   The source IP address and source port specified in the aggregation view take precedence over that specified in the system view. If no source IP address or source port is specified in the aggregation view, the source IP address and source port specified in the system view take effect.
8. Run [**ip netstream export host**](cmdqueryname=ip+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ]
   
   
   
   A destination IP address and a UDP port number are configured for outputting statistics.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The destination IP address configured in the system view takes precedence over that configured in the aggregation view.
   * NetStream packets are output to the NSC through the service interface instead of the management interface.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. (Optional) Configure NetStream packets to carry the flow sequence field.
    
    
    1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the slot in which the interface board for NetStream sampling resides.
    2. Run the [**ip netstream export sequence-mode flow**](cmdqueryname=ip+netstream+export+sequence-mode+flow) command to configure NetStream packets to carry the flow sequence field.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The command applies to the V9 format only.
    3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
11. (Optional) Set parameters for aging aggregation flows as required:
    
    
    * Run the [**ip netstream aggregation timeout**](cmdqueryname=ip+netstream+aggregation+timeout) **active** { *active-interval* | **interval-second** *active-interval-second* } command to set the active aging time for NetStream aggregation flows.
    * Run the [**ip netstream aggregation timeout**](cmdqueryname=ip+netstream+aggregation+timeout) **inactive** *inactive-interval* command to set the inactive aging time for NetStream aggregation flows.
12. (Optional) Exit the IPv4 aggregated configuration mode view. In the system view, run [**ip netstream export template sequence-number fixed**](cmdqueryname=ip+netstream+export+template+sequence-number+fixed)
    
    
    
    The sequence numbers of template packets and option template packets in IPFIX format are configured to remain unchanged, but data packets and option data packets in IPFIX format are still consecutively numbered.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.