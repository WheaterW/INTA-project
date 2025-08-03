Deleting Statistics About MLD Messages
======================================

If you need to re-collect the statistics about MLD messages, delete the existing statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Deleted statistics about MLD messages cannot be restored. Therefore, exercise caution when running the [**reset mld control-message counters**](cmdqueryname=reset+mld+control-message+counters) command.



#### Procedure

1. Run the [**reset mld control-message counters**](cmdqueryname=reset+mld+control-message+counters) [ **interface** *interface-type* *interface-number* ] [ **message-type** { **query** | **report** } ] command in the user view to delete statistics about MLD messages.