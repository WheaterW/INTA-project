Outputting Original Flow Packets
================================

To ensure that original flow packets can be correctly output to the NMS, configure the aging time, output format, and source and destination addresses for original flows.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ip netstream export version**](cmdqueryname=ip+netstream+export+version) { **5** [ **origin-as** | **peer-as** ] | **9** [ **origin-as** | **peer-as** ] [ **bgp-nexthop** ] [ **ttl** ] [ **route-distinguisher** ] | **ipfix** [ **origin-as** | **peer-as** ] [ **bgp-nexthop** ] [ **ttl** ] [ **route-distinguisher** ] }
   
   
   
   The format of output packets is configured.
   
   
   
   NetStream original flow packets can be output in V5, V9, or IPFIX format. V5, V9, and IPFIX formats are mutually exclusive.
   
   Using a template to output original flow packets, V9 allows statistics to be output more flexibly, newly defined flow elements to be extended more easily, and new records to be generated more easily.
   
   Compared with the V9 format, the IPFIX format improves packet extensibility and compatibility, security, and reliability. In addition, the IPFIX format has an enterprise identifier field added. When setting this field, you must use the IPFIX format for outputting NetStream IPv4 original flow packets.
   
   The V5 format is fixed, and the system cost is low. In most cases, NetStream original flow packets can be output in V5 format. In the following cases, however, NetStream original flow packets must be output in V9 or IPFIX format.
   * The output NetStream packets need to carry BGP next-hop information.
   * Interface indexes carried in the output NetStream packets need to be extended from 16 bits to 32 bits.
3. (Optional) Configure NetStream packets to carry the flow sequence field.
   
   
   1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the slot in which the interface board for NetStream sampling resides.
   2. Run the [**ip netstream export sequence-mode flow**](cmdqueryname=ip+netstream+export+sequence-mode+flow) command to configure NetStream packets to carry the flow sequence field.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This command applies to the V9 format only.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. (Optional) Run [**ip netstream export template sequence-number fixed**](cmdqueryname=ip+netstream+export+template+sequence-number+fixed)
   
   
   
   The sequence numbers of template packets and option template packets in the IPFIX format are configured to remain unchanged, but data packets and option data packets in the IPFIX format are still consecutively numbered.
5. (Optional) Run [**ip netstream export template timeout-rate**](cmdqueryname=ip+netstream+export+template+timeout-rate) *timeout-interval*
   
   
   
   The interval at which the template is refreshed when original flows are output in the V9 or IPFIX format is set.
6. Run [**ip netstream export source**](cmdqueryname=ip+netstream+export+source) { *ip-address* | **ipv6** *ipv6-address* } [ *port* ]
   
   
   
   The source IP address and source port are specified for original flows to be output.
7. In the system or slot view: specify the destination IP address and UDP port number of the peer NetStream Collector (NSC) for the statistics to be output.
   
   
   * In the system view:
     
     Run the [**ip netstream export host**](cmdqueryname=ip+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ] command to configure a destination IP address and a UDP port number for outputting statistics.
   * In the slot view:
     
     1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the slot in which the interface board for NetStream sampling resides.
     2. Run the [**ip netstream export host**](cmdqueryname=ip+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ] command to configure a destination IP address and a UDP port number for outputting statistics.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream packets are output to the NSC through the service interface instead of the management interface.
8. (Optional) Set parameters for aging original flows as needed:
   
   
   * Run the [**ip netstream timeout**](cmdqueryname=ip+netstream+timeout) **active** { *active-interval* | **interval-second** *active-interval-second* } to set the active aging time for NetStream original flows.
   * Run the [**ip netstream timeout**](cmdqueryname=ip+netstream+timeout) **inactive** *inactive-interval* command to set the inactive aging time for NetStream original flows.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.