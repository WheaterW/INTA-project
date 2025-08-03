Monitoring the NetStream Operating Status
=========================================

In routine maintenance, you can run the following command in any view to check the NetStream operating status.

#### Procedure

* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) **origin** **slot** *slot-id* command to check information about the NetStream flow buffer.
* Run the [**display ip netstream statistics**](cmdqueryname=display+ip+netstream+statistics) **slot** *slot-id* command to check statistics about NetStream packets.
* Run the [**display ip netstream statistics interface**](cmdqueryname=display+ip+netstream+statistics+interface) *interface-type interface-number* command to check statistics about the sampled packets on an interface.
* Run the [**display netstream**](cmdqueryname=display+netstream) { **all** | **global** | **interface** *interface-type interface-number* } command to check NetStream configurations in different views.
* Run the [**display ip netstream cache**](cmdqueryname=display+ip+netstream+cache) { **as** | **as-tos** | **bgp-nexthop-tos** | **destination-prefix** | **destination-prefix-tos** | **index-tos** | **mpls-label** | **prefix** | **prefix-tos** | **protocol-port** | **protocol-port-tos** | **source-prefix** | **source-prefix-tos** | **source-index-tos**  | **vni-sip-dip**  | **vlan-id** } **slot** *slot-id* command to check information about various aggregated flows in the buffer.
* Run the [**display ip netstream export option**](cmdqueryname=display+ip+netstream+export+option) command to check information about the output option template.
* Run the [**display ipv6 netstream cache**](cmdqueryname=display+ipv6+netstream+cache) { **origin** | **as** | **as-tos** | **bgp-nexthop-tos** | **destination-prefix** | **destination-prefix-tos** | **index-tos** | **prefix** | **prefix-tos** | **protocol-port** | **protocol-port-tos** | **source-prefix** | **source-prefix-tos** | **mpls-label** | **vlan-id** } **slot** *slot-id* command to check information about various aggregated flows in the buffer.
* Run the [**display ipv6 netstream statistics**](cmdqueryname=display+ipv6+netstream+statistics) **slot** *slot-id* command to check statistics about NetStream statistics.
* Run the [**display ip netstream sampler-id allocated-info**](cmdqueryname=display+ip+netstream+sampler-id+allocated-info) [ **slot** *slot-id* ] command to check the sampling ID allocation information on a specified interface board.