Clearing MLD Information
========================

Clearing MLD Information

#### Context

To clear MLD information, perform the following operations in the user view.

![](public_sys-resources/notice_3.0-en-us.png) 

After MLD group information is cleared, multicast members may not be able to receive multicast data. Therefore, exercise caution when performing this operation.

MLD statistics on an interface cannot be restored after they are cleared. Therefore, exercise caution when performing this operation.


**Table 1** Clearing MLD information
| Operation | Command |
| --- | --- |
| Clear the multicast groups that hosts dynamically join on an interface. | [**reset mld group**](cmdqueryname=reset+mld+group) **all**  [**reset mld group**](cmdqueryname=reset+mld+group) **interface** *interface-type* *interface-number* { **all** | *ipv6-group-address* [ *ipv6-group-mask-length* ] [ *ipv6-source-address* [ *ipv6-source-mask-length* ] ] } |
| Clear the multicast groups that hosts statically join on an interface. | [**undo mld static-group**](cmdqueryname=undo+mld+static-group) { **all** | *ipv6-group-address* [ **source** *ipv6-source-address* ] } |
| Clear the multicast groups established based on MLD SSM mapping rules. | [**reset mld group ssm-mapping**](cmdqueryname=reset+mld+group+ssm-mapping) **all**  [**reset mld group**](cmdqueryname=reset+mld+group) **ssm-mapping** **interface** *interface-type* *interface-number* { **all** | *ipv6-group-address* [ *ipv6-group-mask-length* ] } |
| Clear statistics about MLD control messages. | [**reset mld control-message counters**](cmdqueryname=reset+mld+control-message+counters) [ **interface** *interface-type* *interface-number* ] [ **message-type** { **query** | **report** } ] |