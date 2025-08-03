Verifying the Configuration
===========================

In routine maintenance or after pertaining configurations of NetStream are complete, you can run the display commands in any view to check whether NetStream is enabled on the device.

#### Procedure

* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) { **as** | **as-tos** | **bgp-nexthop-tos** | **bgp-community** | **destination-prefix** | **destination-prefix-tos** | **index-tos** | **mpls-label** | **prefix** | **prefix-tos** | **protocol-port** | **protocol-port-tos** | **source-prefix** | **source-prefix-tos** | **source-index-tos** | **vni-sip-dip** | **vlan-id** | **flexflowtpl** *record-name* } **slot** *slot-id* command to check information about flows aggregated in different modes in the buffer.
* Run the [**display ip netstream statistics**](cmdqueryname=display++ip+netstream+statistics) **slot** *slot-id* command to check statistics about NetStream flows.
* Run the [**display ip netstream statistics interface**](cmdqueryname=display+ip+netstream+statistics+interface) { *interface-name* | *interface-type* *interface-number* } command to check statistics about sampled packets on an interface.
* Run the [**display netstream**](cmdqueryname=display+netstream) { **all** | **global** | **interface** *interface-type interface-number* } command to check NetStream configurations in different views.
* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) **aggregation** **statistics** **slot** *slot-id* command to check aggregation flow table specifications and the number of current flows of a specific board.