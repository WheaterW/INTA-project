Clearing RIPng
==============

Clearing RIPng

#### Context

To clear RIPng information, run the reset commands in the user view.

![](public_sys-resources/notice_3.0-en-us.png) 

RIPng information cannot be restored after you clear it. Therefore, exercise caution when running the reset command.



#### Procedure

* Run the [**reset ripng**](cmdqueryname=reset+ripng) *process-id* **statistics** **interface** { **all** | *interface-type interface-number* [ **neighbor** *neighbor-ipv6-address* ] } command to clear the statistics of the counter maintained by a special RIPng process. This command allows you to repeatedly record statistics during debugging.