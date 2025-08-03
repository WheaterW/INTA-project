Maintaining NQA
===============

Maintaining NQA

#### Stopping a Test Instance

To modify test parameters of a test instance, you need to stop it first.

Run the following commands in the NQA view to stop an NQA test instance.

![](../public_sys-resources/notice_3.0-en-us.png) 

Stopping an NQA test instance will terminate the running test instance.


**Table 1** Commands used to stop an NQA test instance
| Operation | Command |
| --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) |
| Enter the view of a test instance. | [**nqa test-instance**](cmdqueryname=nqa+test-instance) *admin-name test-name* |
| Stop an NQA test instance. | [**stop**](cmdqueryname=stop) |
| Commit the configuration. | [**commit**](cmdqueryname=commit) |



#### Restarting an NQA Test Instance

Restarting an NQA test instance is to stop and then immediately start it.

Run the following commands in the NQA view to restart an NQA test instance.

![](../public_sys-resources/notice_3.0-en-us.png) 

Restarting an NQA test instance will terminate the running test instance.


**Table 2** Commands used to restart an NQA test instance
| Operation | Command |
| --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) |
| Enter the view of a test instance. | [**nqa test-instance**](cmdqueryname=nqa+test-instance) *admin-name test-name* |
| Restart an NQA test instance. | [**restart**](cmdqueryname=restart) |
| Commit the configuration. | [**commit**](cmdqueryname=commit) |



#### Deleting Records

Historical test records and test results can be deleted before the next test is performed.

Before running the [**clear-records**](cmdqueryname=clear-records) command, run the [**stop**](cmdqueryname=stop) and [**commit**](cmdqueryname=commit) commands to stop the NQA test instance first.

![](../public_sys-resources/notice_3.0-en-us.png) 

Deleted records cannot be restored. Exercise caution when running the commands.


**Table 3** Commands used to delete test records of an NQA test instance
| Operation | Command |
| --- | --- |
| Enter the system view. | [**system-view**](cmdqueryname=system-view) |
| Enter the view of a test instance. | [**nqa test-instance**](cmdqueryname=nqa+test-instance) *admin-name test-name* |
| Delete the historical test records and test results of an NQA test instance. | [**clear-records**](cmdqueryname=clear-records) |
| Commit the configuration. | [**commit**](cmdqueryname=commit) |



#### Checking Supported Test and Server Types

You can run the following commands to check the test and server types supported by the device.

* Run the [**display nqa support-test-type**](cmdqueryname=display+nqa+support-test-type) command to check the supported test types.
* Run the [**display nqa support-server-type**](cmdqueryname=display+nqa+support-server-type) command to check the supported server types.