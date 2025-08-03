Deleting IGMP Group Information
===============================

If IGMP group information is unnecessary, delete it in the user view.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The [**reset igmp group**](cmdqueryname=reset+igmp+group) command deletes information about the IGMP groups that an interface dynamically joins, which may cause receivers to fail to receive multicast data. Exercise caution when running this command.



#### Procedure

* To delete information about the IGMP groups that an interface dynamically joins, run the following commands in the user view.
  
  
  + [**reset igmp**](cmdqueryname=reset+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **group** { **all** | **interface** *interface-type* *interface-number* { **all** | *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] [ *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] ] } }
  + [**reset igmp**](cmdqueryname=reset+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **group** **ssm-mapping** { **all** | **interface** *interface-type* *interface-number* { **all** | *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] } }
* To delete information about the IGMP groups that an interface statically joins, run the [**undo igmp static-group**](cmdqueryname=undo+igmp+static-group) { **all** | *group-address* [ **inc-step-mask** { *group-mask* | *group-mask-length* } **number** *group-number* ] [ **source** *source-address* ] } command in the interface view.