Deleting LAD Neighbor Information
=================================

You can run the [**clear**](cmdqueryname=clear) command to delete Link Automatic Discovery (LAD) neighbor information.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

LAD neighbor information cannot be restored after it is deleted. Exercise caution when running the [**clear link neighbor**](cmdqueryname=clear+link+neighbor) command.



#### Procedure

1. Run the [**clear link neighbor**](cmdqueryname=clear+link+neighbor) [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ] { **sub-interface** | **all** } command in the user view to delete LAD neighbor information.