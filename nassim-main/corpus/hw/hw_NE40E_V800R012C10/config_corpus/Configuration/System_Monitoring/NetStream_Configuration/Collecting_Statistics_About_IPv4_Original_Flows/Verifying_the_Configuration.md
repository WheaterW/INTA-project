Verifying the Configuration
===========================

In routine maintenance or after NetStream configurations are complete, you can run the display commands in any view to check the running status of NetStream functions.

#### Procedure

* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) **origin** [ **source-ip** *source-ip* ] [ **source-port** *source-port* ] [ **destination-ip** *destination-ip* ] [ **destination-port** *destination-port* ] [ **protocol** { **udp** | **tcp** | *protocol-number* } ] [ **time-range from** *start-time* **to** *end-time* ] [ **source-interface** { *source-interface-type* *source-interface-num* | *source-interface-name* } ] [ **destination-interface** { *destination-interface-type* *destination-interface-num* | *destination-interface-name* } ] **slot** *slot-id* command to check information about the NetStream buffer.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If NetStream sampling is configured on the logical interface in the downstream direction, running this command can only display information about the NetStream buffer of the physical interface where the logical interface resides.
* Run the [**display ip netstream statistics**](cmdqueryname=display+ip+netstream+statistics) **slot** *slot-id* command to check statistics about NetStream packets.
* Run the [**display ip netstream statistics interface**](cmdqueryname=display+ip+netstream+statistics+interface) { *interface-name* | *interface-type* *interface-number* } command to check statistics about sampled packets on an interface.
* Run the [**display netstream**](cmdqueryname=display+netstream) { **all** | **global** | **interface** *interface-type interface-number* } command to check NetStream configurations in different views.
* Run the [**display ip netstream monitor**](cmdqueryname=display+ip+netstream+monitor) { **all** | *monitor-name* } command to check the monitoring information about IPv4 original flows.
* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) **origin** **statistics** **slot** *slot-id* command to check original flow table specifications and the number of current flows on a specific board.
* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) [ **source-ip** *source-ip* ] [ **source-port** *source-port* ] [ **destination-ip** *destination-ip* ] [ **destination-port** *destination-port* ] [ **protocol** { **tcp** | **udp** | *protocol-number* } ] [ **time-range** **from** *start-time* **to** *end-time* ] [ **interface** { *interface-name* | *interface-type* *interface-num* } ] [ **type** { **ipv4** | **mpls** } ] **slot** *slot-id* command to check original flow sampling information in the NetStream IPv4 or MPLS buffer based on 5-tuple information.