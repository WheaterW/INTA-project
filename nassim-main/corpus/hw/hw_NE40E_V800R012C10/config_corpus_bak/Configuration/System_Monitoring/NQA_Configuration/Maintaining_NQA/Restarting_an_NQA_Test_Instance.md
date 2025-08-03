Restarting an NQA Test Instance
===============================

This section describes how to restart (namely, to stop and then immediately start) an NQA test instance.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Restarting an NQA test instance terminates the running test instance.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name*
   
   
   
   An NQA test instance is created, and the test instance view is displayed.
3. Run [**restart**](cmdqueryname=restart)
   
   
   
   The NQA test instance is restarted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.