Deleting MLD Group Information
==============================

If MLD group information is unnecessary, delete it in the user view.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The [**reset mld group**](cmdqueryname=reset+mld+group) or [**reset mld group ssm-mapping**](cmdqueryname=reset+mld+group+ssm-mapping) command deletes information about the MLD groups that an interface dynamically joins, which may cause receivers to fail to receive multicast data. Exercise caution when running this command.



#### Procedure

* To delete information about the MLD groups (excluding the MLDv1 groups in the SSM group address range) that an interface dynamically joins, run the following commands in the user view:
  
  
  + [**reset mld group**](cmdqueryname=reset+mld+group) **all**
  + [**reset mld group**](cmdqueryname=reset+mld+group) **interface** *interface-type* *interface-number* { **all** | *ipv6-group-address* [ *ipv6-group-mask-length* ] [ *ipv6-source-address* [ *ipv6-source-mask-length* ] ] }
* To delete information about the MLDv1 groups in the SSM group address range, run the following commands in the user view:
  
  
  + [**reset mld group ssm-mapping**](cmdqueryname=reset+mld+group+ssm-mapping) **all**
  + [**reset mld group ssm-mapping**](cmdqueryname=reset+mld+group+ssm-mapping) **interface** *interface-type* *interface-number* { **all** | *ipv6-group-address* [ *ipv6-group-mask-length* ] }
* To delete information about the MLD groups that an interface statically joins, run the [**undo mld static-group**](cmdqueryname=undo+mld+static-group) { **all** | *ipv6-group-address* [ **source** *ipv6-source-address* ] } command in the user view.