Outputting Flexible Flow Packets
================================

To ensure that flexible flow packets can be correctly output to the NMS, specify the related parameters for flexible flows.

#### Context

IPv6 flexible flow packets can be output only in the V9 format.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 netstream export version**](cmdqueryname=ipv6+netstream+export+version) **9** [ **origin-as** | **peer-as** ] [ **bgp-nexthop** ]
   
   
   
   The output version number and AS option of flexible flow packets are specified.
3. (Optional) Configure NetStream packets to carry the flow sequence field.
   
   
   1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the slot in which the interface board for NetStream sampling resides.
   2. Run the [**ip netstream export sequence-mode flow**](cmdqueryname=ip+netstream+export+sequence-mode+flow) command to configure NetStream packets to carry the flow sequence field.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The command applies to the V9 format only.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. Run [**ipv6 netstream apply record**](cmdqueryname=ipv6+netstream+apply+record) *record-name*
   
   
   
   Flexible flows are applied in the system view.
   
   
   
   Flexible flow packets can be output only in the V9 format. If the version of the packets to be output is set to **ipfix** using the [**ipv6 netstream export version**](cmdqueryname=ipv6+netstream+export+version) command in the system view, the [**ipv6 netstream apply record**](cmdqueryname=ipv6+netstream+apply+record) command does not take effect.
5. (Optional) Run [**ipv6 netstream export template timeout-rate**](cmdqueryname=ipv6+netstream+export+template+timeout-rate) *timeout-interval*
   
   
   
   The interval at which the template for outputting original flows in the V9 format is refreshed is configured.
6. Run [**ipv6 netstream export source**](cmdqueryname=ipv6+netstream+export+source) { *ip-address* | **ipv6** *ipv6-address* } [ *port* ]
   
   
   
   The source IP address and source port are specified for flexible flows.
7. Configure a destination IP address and a UDP port number for outputting statistics in the system or slot view.
   
   
   * In the system view:
     
     Run the [**ipv6 netstream export host**](cmdqueryname=ipv6+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **version** { **9** | **ipfix** } ] [ **dscp** *dscp-value* ] command to configure a destination IP address and a UDP port number for outputting statistics.
   * In the slot view:
     
     1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the slot in which the interface board for NetStream sampling resides.
     2. Run the [**ipv6 netstream export host**](cmdqueryname=ipv6+netstream+export+host) [ **ipv6** ] *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **version** { **9** | **ipfix** } ] [ **dscp** *dscp-value* ] command to configure a destination IP address and a UDP port number for outputting statistics.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream packets are output to the NSC through the service interface instead of the management interface.
8. (Optional) Set parameters for aging flexible flows as needed:
   
   
   * Run the [**ipv6 netstream aggregation timeout**](cmdqueryname=ipv6+netstream+aggregation+timeout) **active** { *active-interval* | **interval-second** *active-interval-second* } command to set the active aging time for NetStream aggregation flows.
   * Run the [**ipv6 netstream aggregation timeout**](cmdqueryname=ipv6+netstream+aggregation+timeout) **inactive** *inactive-interval* command to set the inactive aging time for NetStream flexible flows.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.