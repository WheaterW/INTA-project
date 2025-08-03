Stopping a Test Instance
========================

This section describes how to stop a test instance when its test parameters need to be changed.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nqa**](cmdqueryname=nqa) **test-instance** *admin-name test-name*
   
   
   
   An NQA test instance is created, and the test instance view is displayed.
3. Run [**stop**](cmdqueryname=stop)
   
   
   
   The NQA test instance is stopped.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.