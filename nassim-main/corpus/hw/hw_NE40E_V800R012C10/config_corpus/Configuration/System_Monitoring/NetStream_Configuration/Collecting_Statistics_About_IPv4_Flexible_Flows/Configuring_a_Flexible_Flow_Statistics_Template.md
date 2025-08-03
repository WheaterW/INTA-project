Configuring a Flexible Flow Statistics Template
===============================================

When configuring the flexible flow statistics output function, configure a flexible flow statistics template, customize matching and collected fields, and apply the template to an interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip netstream record**](cmdqueryname=ip+netstream+record) *record-name*
   
   
   
   An IPv4 flexible flow statistics template is created, and the recording view is displayed.
3. Run [**match**](cmdqueryname=match) { { **source** | **destination** } { **vlan** | **as** | **port** | **address** | **mask** } | **mpls** **top-label** **ip-address** | **mpls** **label** *position* | { **protocol** | **tos** | **direction** | **tcp-flag** } | { **input** | **output** } **interface** | **next-hop** [ **bgp** ] }
   
   
   
   Aggregation keywords are configured for the flexible flow statistics template.
4. (Optional) Run [**collect**](cmdqueryname=collect) {{ **first** | **last** } **switched** | **input** { **packets** | **bytes** } *length* | **flow-end-reason** }
   
   
   
   The device is configured to add the number of packets, number of bytes, flow aging reasons, and first and last forwarding time to the flexible flow statistics sent to the NSC.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.