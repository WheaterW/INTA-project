Clearing Statistics
===================

Clearing Statistics

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

Be aware that statistics cannot be restored after being deleted. Exercise caution when clearing the statistics.


![](public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported on the CE6885-LL (low latency mode).



#### Procedure

1. Clear 5-tuple-based interface traffic statistics.
   
   
   ```
   [reset port forwarding-path path-id](cmdqueryname=reset+port+forwarding-path+path-id) pathnum statistics
   ```