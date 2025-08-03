Deleting Test Records
=====================

This section describes how to delete test records before the next test is conducted.

#### Prerequisites

The NQA test instance has been stopped.


#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Test records cannot be restored after being deleted. Exercise caution when running the [**clear-records**](cmdqueryname=clear-records) command.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name*
   
   
   
   An NQA test instance is created, and the test instance view is displayed.
3. Run [**clear-records**](cmdqueryname=clear-records)
   
   
   
   Historical records and result records of the NQA test instance are deleted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.