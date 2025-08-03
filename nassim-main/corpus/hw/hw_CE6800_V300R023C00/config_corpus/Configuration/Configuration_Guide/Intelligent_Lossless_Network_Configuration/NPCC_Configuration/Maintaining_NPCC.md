Maintaining NPCC
================

Maintaining NPCC

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after they are cleared. Exercise caution when clearing the statistics.



#### Procedure

* Clear statistics about CNPs proactively sent by an NPCC-enabled forwarding device.
  
  
  ```
  [reset npcc statistics](cmdqueryname=reset+npcc+statistics) [ interface { interface-name | interface-type interface-number } ]
  ```
  
  If no interface is specified, CNP statistics on the chip and all interfaces are cleared.