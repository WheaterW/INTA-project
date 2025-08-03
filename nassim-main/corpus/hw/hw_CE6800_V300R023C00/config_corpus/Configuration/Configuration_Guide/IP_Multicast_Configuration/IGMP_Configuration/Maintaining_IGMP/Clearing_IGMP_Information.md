Clearing IGMP Information
=========================

Clearing IGMP Information

#### Context

To clear IGMP information, perform the following operations in the user view.

![](public_sys-resources/notice_3.0-en-us.png) 

After IGMP group information is cleared, multicast members may not be able to receive multicast data. Therefore, exercise caution when performing this operation.

IGMP statistics on an interface cannot be restored after they are cleared. Therefore, exercise caution when performing this operation.


**Table 1** Clearing IGMP information
| Operation | Command |
| --- | --- |
| Clear the multicast groups that hosts dynamically join on an interface. | [**reset igmp**](cmdqueryname=reset+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **group** { **all** | **interface** *interface-type* *interface-number* { **all** | *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] [ *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] ] } } |
| Clear the multicast groups that hosts statically join on an interface. | [**undo igmp static-group**](cmdqueryname=undo+igmp+static-group) { **all** | *group-address* [ **inc-step-mask** { *group-mask* | *group-mask-length* } **number** *group-number* ] [ **source** *source-address* ] } |
| Clear the multicast groups established based on IGMP SSM mapping rules. | [**reset igmp**](cmdqueryname=reset+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **group** **ssm-mapping** { **all** | **interface** *interface-type* *interface-number* { **all** | *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] } } |
| Clear statistics about IGMP control messages. | [**reset igmp**](cmdqueryname=reset+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message counters** [ **interface** *interface-type* *interface-number* ] [ **message-type** { **query** | **report** } ] |