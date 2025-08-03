Verifying the Configuration
===========================

In routine maintenance or after NetStream configurations are complete, you can run the display commands in any view to check whether NetStream is enabled on the device.

#### Context

Run the following command to check the previous configuration.


#### Procedure

* Run the [**display ipv6 netstream cache**](cmdqueryname=display+ipv6+netstream+cache) { **as** | **as-tos** | **bgp-nexthop-tos** | **destination-prefix** | **destination-prefix-tos** | **index-tos** | **prefix** | **prefix-tos** | **protocol-port** | **protocol-port-tos** | **source-prefix** | **source-prefix-tos** | **mpls-label** | **vlan-id** | **flexflowtpl** *record-name* } **slot** *slot-id* command to check various aggregated flows in the buffer.
* Run the [**display ipv6 netstream statistics**](cmdqueryname=display+ipv6+netstream+statistics) **slot** *slot-id* command to check statistics about NetStream packets.
* Run the [**display ip netstream statistics interface**](cmdqueryname=display+ip+netstream+statistics+interface) { *interface-name* | *interface-type* *interface-number* } command to check statistics about sampled packets on an interface.
* Run the [**display netstream**](cmdqueryname=display+netstream) { **all** | **global** | **interface** *interface-type interface-number* } command to check NetStream configurations in different views.
* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) **aggregation** **statistics** **slot** *slot-id* command to check aggregation flow table specifications and the number of current flows of a specific board.