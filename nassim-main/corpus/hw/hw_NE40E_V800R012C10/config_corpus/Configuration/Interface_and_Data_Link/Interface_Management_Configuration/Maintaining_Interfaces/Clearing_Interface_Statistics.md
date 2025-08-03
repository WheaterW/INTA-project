Clearing Interface Statistics
=============================

Before collecting traffic statistics within a specified period of time on an interface, you must clear existing statistics on the interface.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when running the following commands.



#### Procedure

* To clear the traffic statistics on an interface, run the [**reset counters interface**](cmdqueryname=reset+counters+interface) command in the user view.
* To clear the historical peak rate of an interface and obtain the peak rate in subsequent periods, run the [**reset counters peak-rate interface**](cmdqueryname=reset+counters+peak-rate+interface) command in the user view.