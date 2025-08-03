Maintaining 1588v2
==================

Maintaining 1588v2

#### Monitoring the 1588v2 Operating Status

You can run the following command in any view to check the 1588v2 operating status during routine maintenance.

**Table 1** Checking the 1588v2 operating status
| Operation | Command |
| --- | --- |
| Check the 1588v2 operating status. | [**display ptp**](cmdqueryname=display+ptp) { **all** [ **config** | **state** ] | **interface** *interface-type* *interface-number* } |



#### Clearing 1588v2 Message Statistics

![](public_sys-resources/notice_3.0-en-us.png) 

Statistics cannot be restored after being deleted. Exercise caution when running the commands.

You can run the following commands to clear 1588v2 message statistics.

**Table 2** Clearing 1588v2 message statistics
| Operation | Command |
| --- | --- |
| Clear 1588v2 message statistics. | [**reset ptp statistics**](cmdqueryname=reset+ptp+statistics) { **all** | **interface** *interface-type* *interface-number* } |