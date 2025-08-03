Outputting Original Flow Packets
================================

To ensure that original flow packets can be correctly output to the NMS, configure the aging time, output format, and source and destination addresses for original flows.

#### Context

IPv6 original flows can be output only in the V9 or IPFIX format.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 netstream export version**](cmdqueryname=ipv6+netstream+export+version) { **9** [ **origin-as** | **peer-as** ] [ **bgp-nexthop** ] [ **ttl** ] [ **route-distinguisher** ] | **ipfix** [ **origin-as** | **peer-as** ] [ **bgp-nexthop** ] [ **ttl** ] [ **route-distinguisher** ] }
   
   
   
   The format of output packets is configured.
3. (Optional) Configure NetStream packets to carry the flow sequence field.
   
   
   1. Run [**slot**](cmdqueryname=slot) *slot-id*
      
      The view of the slot in which the interface board for NetStream sampling resides is displayed.
   2. Run [**ip netstream export sequence-mode flow**](cmdqueryname=ip+netstream+export+sequence-mode+flow)
      
      NetStream packets are configured to carry the flow sequence field.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The command applies to the V9 format only.
   3. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
4. (Optional) Run [**ipv6 netstream export template sequence-number fixed**](cmdqueryname=ipv6+netstream+export+template+sequence-number+fixed)
   
   
   
   The device is configured to keep the sequence numbers of template packets and option template packets in the IPFIX format unchanged and to consecutively number data packets and option data packets in the IPFIX format.
5. (Optional) Run [**ipv6 netstream export template timeout-rate**](cmdqueryname=ipv6+netstream+export+template+timeout-rate) *timeout-interval*
   
   
   
   The interval at which the template is refreshed when original flows are output in the V9 or IPFIX format is set.
6. Run [**ipv6 netstream export source**](cmdqueryname=ipv6+netstream+export+source) { *ip-address* | **ipv6** *ipv6-address* } [ *port* ]
   
   
   
   The source address and source port for outputting statistics are configured.
7. In the system or slot view, specify a destination address and a UDP port number for outputting statistics.
   
   
   * In the system view:
     
     Run [**ipv6 netstream export host**](cmdqueryname=ipv6+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ]
     
     A destination IP address and a UDP port number are configured for outputting statistics.
   * In the slot view:
     
     1. Run [**slot**](cmdqueryname=slot) *slot-id*
        
        The view of the slot in which the interface board for NetStream sampling resides is displayed.
     2. Run [**ipv6 netstream export host**](cmdqueryname=ipv6+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ]
        
        A destination IP address and a UDP port number are configured for outputting statistics.
     3. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream packets are output to the NSC through the service interface instead of the management interface.
8. (Optional) Set parameters for aging original flows as required:
   
   
   * To configure the active aging time for NetStream original flows, run the [**ipv6 netstream timeout**](cmdqueryname=ipv6+netstream+timeout) **active** { *active-interval* | **interval-second** *active-interval-second* } command.
   * To configure the inactive aging time for NetStream original flows, run the [**ipv6 netstream timeout**](cmdqueryname=ipv6+netstream+timeout) **inactive** *inactive-interval* command.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.