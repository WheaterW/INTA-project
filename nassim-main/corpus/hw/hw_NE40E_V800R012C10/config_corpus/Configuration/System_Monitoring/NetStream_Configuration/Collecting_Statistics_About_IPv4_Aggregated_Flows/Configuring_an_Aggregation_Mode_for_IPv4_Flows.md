Configuring an Aggregation Mode for IPv4 Flows
==============================================

Configuring an aggregation mode is to specify an attribute type for original flows to be aggregated. An aggregation mode must be specified before original flows with the same attributes are aggregated as one flow and output to the NetStream Collector (NSC).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip netstream aggregation**](cmdqueryname=ip+netstream+aggregation) { **as** | **as-tos** | **bgp-nexthop-tos** | **destination-prefix** | **destination-prefix-tos** | **index-tos** | **mpls-label** | **prefix** | **prefix-tos** | **protocol-port** | **protocol-port-tos** | **source-prefix** | **source-prefix-tos** | **source-index-tos** | **vlan-id** | **bgp-community** | **vni-sip-dip** }
   
   
   
   The aggregation configuration mode view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the NetStream flow aggregation function is enabled on a device, the device classifies and aggregates original flows based on specified rules and sends the aggregated flows to the NetStream Data Analyzer (NDA) for analysis. Aggregating original flows can significantly reduce the consumption of network bandwidth, CPU, and memory resources. Flow attributes based on which flows are aggregated vary according to flow aggregation modes.
   
   
   **Table 1** Mapping between aggregation modes and flow attributes
   | Aggregation mode | Description |
   | --- | --- |
   | as | NetStream combines flows with the same source AS number, destination AS number, inbound interface index, and outbound interface index into an aggregated flow and generates one aggregation record. |
   | as-tos | NetStream combines flows with the same source AS number, destination AS number, inbound interface index, outbound interface index, and type of service (ToS) into an aggregated flow and generates one aggregation record. |
   | bgp-nexthop-tos | NetStream combines flows with the same destination AS number, source AS number, BGP next hop, inbound interface index, and outbound interface index into an aggregated flow and generates one aggregation record. |
   | destination-prefix | NetStream combines flows with the same destination AS number, destination mask length, destination prefix, and outbound interface index into an aggregated flow and generates one aggregation record. |
   | destination-prefix-tos | NetStream combines flows with the same destination AS number, destination mask length, destination prefix, ToS, and outbound interface index into an aggregated flow and generates one aggregation record. |
   | index-tos | NetStream combines flows with the same inbound interface index, outbound interface index, and ToS into an aggregated flow and generates one aggregation record. |
   | mpls-label | Indicates the MPLS label aggregation, which aggregates flows with the same first layer label, second layer label, third layer label, TopLabelIpAddress, stack bottom symbol of the first layer label, and the EXP value of the first layer label. |
   | prefix | NetStream combines flows with the same source AS number, destination AS number, source mask length, destination mask length, source prefix, destination prefix, inbound interface index, and outbound interface index into an aggregated flow and generates one aggregation record. |
   | prefix-tos | NetStream combines flows with the same source AS number, destination AS number, source mask length, destination mask length, source prefix, destination prefix, ToS, inbound interface index, and outbound interface index into an aggregated flow and generates one aggregation record. |
   | protocol-port | NetStream combines flows with the same protocol number, source port, and destination port into an aggregated flow and generates one aggregation record. |
   | protocol-port-tos | NetStream combines flows with the same protocol number, source port, destination port, ToS, inbound interface index, and outbound interface index into an aggregated flow and generates one aggregation record. |
   | source-prefix | NetStream combines flows with the same source AS number, source mask length, source prefix, and inbound interface index into an aggregated flow and generates one aggregation record. |
   | source-prefix-tos | NetStream combines flows with the same source AS number, source mask length, source prefix, ToS, and inbound interface index into an aggregated flow and generates one aggregation record. |
   | source-index-tos | NetStream combines flows with the same inbound interface index, ToS and BGP next hop into an aggregated flow and generates one aggregation record. |
   | vlan-id | NetStream combines flows with the same VLAN ID and inbound interface index into an aggregated flow and generates one aggregation record. |
   | bgp-community | NetStream combines flows with the same inbound and outbound interface indexes and BGP community into an aggregated flow generates one aggregation record. |
   | vni-sip-dip | Indicates a VNI aggregation mode. NetStream combines flows with the same VNI ID and the same source and destination IP addresses of tenants into an aggregated flow and generates one aggregation record. |
3. Run [**enable**](cmdqueryname=enable)
   
   
   
   Statistics collection of flows aggregated in a specified aggregation mode is enabled.
4. (Optional) Run [**mask**](cmdqueryname=mask) { **source** | **destination** } **minimum** *mask-length*
   
   
   
   The length of the aggregate mask is set. The effective mask is the greater one between the mask in the FIB table and the configured mask. If no aggregate mask is set, the system uses the mask in the FIB table for flow aggregation.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The aggregate mask takes effect only on flows aggregated in the following modes: destination-prefix, destination-prefix-tos, prefix, prefix-tos, source-prefix, and source-prefix-tos.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.