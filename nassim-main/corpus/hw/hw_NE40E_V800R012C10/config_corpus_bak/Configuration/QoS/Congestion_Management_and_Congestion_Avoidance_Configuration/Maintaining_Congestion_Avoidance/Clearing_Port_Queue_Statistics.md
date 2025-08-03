Clearing Port Queue Statistics
==============================

This section describes how to clear port queue statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being cleared. Exercise caution when clearing statistics.

To clear port queue statistics, run the following reset command in the user view.


#### Procedure

* Run the [**reset port-queue statistics**](cmdqueryname=reset+port-queue+statistics) [ **slot** *slot-id* | **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *cos-value* ] **outbound** [ **default** ] command to clear port queue statistics on a specified interface.
  
  
  
  In VS mode, the parameter **slot** is supported only by the admin VS.
* Run the [**reset port-queue statistics slot**](cmdqueryname=reset+port-queue+statistics+slot) *slot-id* [ *cos-value* ] **outbound** **bind** **mtunnel** command to clear statistics about all port queues or a specified priority queue on the MTunnel interface of distributed multicast VPN.
  
  
  
  In VS mode, this command is supported only by the admin VS.