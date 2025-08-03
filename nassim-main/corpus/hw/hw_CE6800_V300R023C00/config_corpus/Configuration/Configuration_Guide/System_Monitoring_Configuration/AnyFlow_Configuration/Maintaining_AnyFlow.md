Maintaining AnyFlow
===================

Maintaining AnyFlow

#### Context

During routine maintenance, you can run commands to view details about AnyFlow tables or clear the flow table on the chip built in the CPU to release the CPU resources.


#### Procedure

**Table 1** Maintaining AnyFlow
| To... | Run... |
| --- | --- |
| Check all information about the AnyFlow tables. | [**display any-flow flow-cache**](cmdqueryname=display+any-flow+flow-cache) { **ipv4** | **ipv6** } ****slot******slot-id** |
| Check information about the AnyFlow tables that meet specified conditions. | **[**display any-flow flow-cache**](cmdqueryname=display+any-flow+flow-cache)** { **sip** *ipv4-sip-address* **dip** *ipv4-dip-address* | **ipv6** **sip** *ipv6-sip-address* **ipv6** **dip** *ipv6-dip-address* } [ **srcport** *srcport-number* | **dstport** *dstport-number* | **protocol** *protocol-number* | **vpn-instance** *vpn-instance-name* | **vlan** *vlan-id* | **vni** *vni-id* | **rocev2** [ **dest-qp** *dest-qp-value* ] ] \* **slot** *slot-id* |
| Check information about hardware flow entry resources. | [**display any-flow flow-cache resource**](cmdqueryname=display+any-flow+flow-cache+resource) [ ****slot**** **slot-id**] |
| View the flow table statistics on the chip built in the CPU for AnyFlow. | [**display any-flow flow-cache statistics**](cmdqueryname=display+any-flow+flow-cache+statistics) [ **slot** *slot-id* ] |
| Clear the flow table on the chip built in the CPU. | [**reset any-flow flow-cache**](cmdqueryname=reset+any-flow+flow-cache) |