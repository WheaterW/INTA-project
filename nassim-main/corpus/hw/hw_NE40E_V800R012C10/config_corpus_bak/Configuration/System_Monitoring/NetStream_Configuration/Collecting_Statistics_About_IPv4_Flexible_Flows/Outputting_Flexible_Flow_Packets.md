Outputting Flexible Flow Packets
================================

To ensure that flexible flow packets can be correctly output to the NMS, specify the related parameters for flexible flows.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip netstream export version**](cmdqueryname=ip+netstream+export+version) **9** [ **origin-as** | **peer-as** ] [ **bgp-nexthop** ]
   
   
   
   The output version number and AS option of flexible flow packets are specified.
   
   
   
   NetStream flexible flow packets support only the V9 format.
3. (Optional) Configure NetStream packets to carry the flow sequence field.
   
   
   1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the slot in which the interface board for NetStream sampling resides.
   2. Run the [**ip netstream export sequence-mode flow**](cmdqueryname=ip+netstream+export+sequence-mode+flow) command to configure NetStream packets to carry the flow sequence field.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      This command applies to the V9 format only.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
4. Run [**ip netstream apply record**](cmdqueryname=ip+netstream+apply+record) *record-name*
   
   
   
   Apply a flexible flow in the system view.
   
   
   
   Flexible flow packets can be output only in the V9 format. If the version of the packets to be output is set to **5** or **ipfix** using the [**ip netstream export version**](cmdqueryname=ip+netstream+export+version) command in the system view, the [**ip netstream apply record**](cmdqueryname=ip+netstream+apply+record) command does not take effect.
5. (Optional) Run [**ip netstream export template timeout-rate**](cmdqueryname=ip+netstream+export+template+timeout-rate) *timeout-interval*
   
   
   
   The interval at which the template for outputting flexible flows in the V9 format is refreshed is configured.
6. Run [**ip netstream export source**](cmdqueryname=ip+netstream+export+source) *ip-address* [ *port* ]
   
   
   
   The source IP address and source port are specified for flexible flows.
7. Specify the destination IP address and UDP port number of the peer NSC for NetStream flexible flows to be output in the system or slot view.
   
   
   * In the system view:
     
     Run the [**ip netstream export host**](cmdqueryname=ip+netstream+export+host) *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ] command to configure a destination IP address and a UDP port number for outputting statistics.
   * In the slot view:
     
     1. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the slot in which the interface board for NetStream sampling resides.
     2. Run the [**ip netstream export host**](cmdqueryname=ip+netstream+export+host) *ip-address* *port* [ **vpn-instance** *vpn-instance-name* ] [ **dscp** *dscp-value* ] command to configure a destination IP address and a UDP port number for outputting statistics.
     3. Run the [**quit**](cmdqueryname=quit) command to enter the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   NetStream packets are output to the NSC through the service interface instead of the management interface.
8. (Optional) Set parameters for aging flexible flows as needed:
   
   
   * Run the [**ip netstream aggregation timeout**](cmdqueryname=ip+netstream+aggregation+timeout) **active** { *active-interval* | **interval-second** *active-interval-second* } command to set the active aging time for NetStream aggregation flows.
   * Run the [**ip netstream aggregation timeout**](cmdqueryname=ip+netstream+aggregation+timeout) **inactive** *inactive-interval* command to set the inactive aging time for NetStream flexible flows.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.