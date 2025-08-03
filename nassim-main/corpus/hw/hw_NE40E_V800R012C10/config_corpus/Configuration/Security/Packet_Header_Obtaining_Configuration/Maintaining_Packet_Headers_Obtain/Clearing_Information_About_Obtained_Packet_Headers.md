Clearing Information About Obtained Packet Headers
==================================================

If packet header getting instances saved on the main control board's memory need to be cleared, run the [**capture-packet free**](cmdqueryname=capture-packet+free) command.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Cleared packet header getting instances cannot be restored. Therefore, exercise caution when running this command.



#### Procedure

1. Run the [**capture-packet free**](cmdqueryname=capture-packet+free) { **all** | **instance-id** *instance-id* } command to clear the information about packet header getting instances.