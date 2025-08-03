Clearing RIPng
==============

To clear RIPng information, run the reset commands in the
user view.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

RIPng information cannot be restored
after you clear it. Therefore, exercise caution when running the reset
command.



#### Procedure

* Run the [**reset ripng**](cmdqueryname=reset+ripng) *process-id* **statistics** **interface** { **all** | *interface-type interface-number* [ **neighbor** *neighbor-ipv6-address* ]
  } command to clear the statistics of the counter that is maintained
  by a particular RIPng process. This command helps to re-collect statistics
  during debugging.