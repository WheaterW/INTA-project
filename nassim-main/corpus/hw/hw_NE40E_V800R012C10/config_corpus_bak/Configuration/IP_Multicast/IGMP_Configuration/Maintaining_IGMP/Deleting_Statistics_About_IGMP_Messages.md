Deleting Statistics About IGMP Messages
=======================================

If you need to re-collect the statistics about IGMP messages, delete the existing statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Deleted statistics about IGMP messages cannot be restored. Therefore, exercise caution when running the [**reset igmp**](cmdqueryname=reset+igmp) command.



#### Procedure

1. Run the [**reset igmp**](cmdqueryname=reset+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message counters** [ **interface** *interface-type* *interface-number* ] [ **message-type** { **query** | **report** } ] command in the user view to delete statistics about IGMP messages.