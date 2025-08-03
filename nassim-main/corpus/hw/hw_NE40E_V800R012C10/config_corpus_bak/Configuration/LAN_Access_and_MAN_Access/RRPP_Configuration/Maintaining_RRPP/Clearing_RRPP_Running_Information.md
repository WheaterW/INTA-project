Clearing RRPP Running Information
=================================

You can run the **reset** command to clear existing RRPP statistics before recollecting RRPP statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

RRPP statistics cannot be restored once cleared. Therefore, confirm the action before you use the command.



#### Procedure

1. In any view, to check packet statistics on the interface where RRPP snooping is enabled, run the [**display rrpp snooping statistics**](cmdqueryname=display+rrpp+snooping+statistics) { **all** | **interface** *{ interface-name | interface-type interface-number}* } command.
2. In the user view, to clear packet statistics on the interface where RRPP snooping is enabled, run the [**reset rrpp snooping statistics**](cmdqueryname=reset+rrpp+snooping+statistics) { **all** | **interface** *{ interface-name | interface-type interface-number}* } command.