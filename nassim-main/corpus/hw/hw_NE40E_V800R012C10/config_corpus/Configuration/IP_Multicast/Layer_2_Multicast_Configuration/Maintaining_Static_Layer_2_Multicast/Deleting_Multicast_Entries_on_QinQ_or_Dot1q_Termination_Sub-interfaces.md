Deleting Multicast Entries on QinQ or Dot1q Termination Sub-interfaces
======================================================================

If multicast entries on a QinQ or dot1q termination sub-interface are unnecessary, delete them from the sub-interface.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Temporary service interruptions may occur after multicast entries are deleted from a QinQ or dot1q termination sub-interface. Therefore, exercise caution when running the following commands to delete multicast entries.



#### Procedure

* To delete multicast entries on QinQ or dot1q termination sub-interfaces, run either of the following commands:
  
  
  + To delete multicast entries on all QinQ or dot1q termination sub-interfaces, run the [**reset igmp-snooping qinq-group all**](cmdqueryname=reset+igmp-snooping+qinq-group+all) command.
  + To delete multicast entries on a specified QinQ or dot1q termination sub-interface, run the [**reset igmp-snooping qinq-group interface**](cmdqueryname=reset+igmp-snooping+qinq-group+interface) *interface-type* *interface-number* [ **pe-vid** *pe-vid* [ **ce-vid** *ce-vid* ] [ *group-address* [ **mask** { *group-mask* | *group-mask-length* } ] ] [ *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] ] ] command.