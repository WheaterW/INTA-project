Verifying the Configuration
===========================

In routine maintenance or after NetStream configurations are complete, you can run the display commands in any view to check the running status of NetStream functions.

#### Prerequisites

NetStream statistics collection configurations are complete.


#### Procedure

* Run the [**display ipv6 netstream cache**](cmdqueryname=display+ipv6+netstream+cache) **origin** [ **source-ipv6** *source-ip* ] [ **source-port** *source-port* ] [ **destination-ipv6** *destination-ip* ] [ **destination-port** *destination-port* ] [ **protocol** { **udp** | **tcp** | *protocol-number* } ] [ **time-range from** *start-time* **to** *end-time* ] [ **source-interface** { *source-interface-type* *source-interface-num* | *source-interface-name* } ] [ **destination-interface** { *destination-interface-type* *destination-interface-num* | *destination-interface-name* } ] **slot** *slot-id* command to check information about the NetStream buffer.
* Run the [**display ipv6 netstream statistics**](cmdqueryname=display+ipv6+netstream+statistics) **slot** *slot-id* command to check statistics about NetStream packets.
* Run the [**display ip netstream statistics interface**](cmdqueryname=display+ip+netstream+statistics+interface) { *interface-name* | *interface-type* *interface-number* } command to check statistics about sampled packets on an interface.
* Run the [**display netstream**](cmdqueryname=display+netstream) { **all** | **global** | **interface** *interface-type interface-number* } command to check NetStream configurations in different views.
* Run the [**display ipv6 netstream monitor**](cmdqueryname=display+ipv6+netstream+monitor) { **all** | *monitor-name* } command to check monitoring information about IPv6 original flows.
* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) **origin** **statistics** **slot** *slot-id* command to check original flow table specifications and the number of current flows of a specific board.
* Run the [**display ipv6 netstream cache**](cmdqueryname=display+ipv6+netstream+cache) [ **source-ipv6** *source-ipv6* ] [ **source-port** *source-port* ] [ **destination-ipv6** *destination-ipv6* ] [ **destination-port** *destination-port* ] [ **protocol** { **tcp** | **udp** | *protocol-number* } ] [ **time-range from** *start-time* **to** *end-time* ] [ **interface** { *interface-name* | *interface-type* *interface-num* } ] [ **type** { **ipv6** | **mpls** } ] **slot** *slot-id* command to check original flow sampling information in the NetStream IPv6 or MPLS buffer based on 5-tuple information.