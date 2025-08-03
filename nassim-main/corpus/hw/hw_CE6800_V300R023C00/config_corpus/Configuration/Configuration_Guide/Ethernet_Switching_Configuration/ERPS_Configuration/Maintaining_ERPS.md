Maintaining ERPS
================

Maintaining ERPS

#### Context

Before collecting ERPS statistics again, run the [**reset erps**](cmdqueryname=reset+erps) command to clear existing ERPS statistics.

![](public_sys-resources/notice_3.0-en-us.png) 

ERPS statistics cannot be restored after they are cleared. Exercise caution when running this command.



#### Procedure

1. Clear packet statistics in an ERPS ring in the user view.
   
   
   ```
   [reset erps](cmdqueryname=reset+erps) [ ring ring-id ] statistics
   ```