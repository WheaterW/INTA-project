Maintaining IM
==============

Maintaining IM includes clearing IM statistics and monitoring IM.

#### Clearing Statistics

To delete statistics and information in the buffer, perform the following operations in the user view:

![](public_sys-resources/caution_3.0-en-us.png) 

Statistics and buffer information cannot be restored after being cleared. Therefore, exercise caution when performing this operation.


**Table 1** Clearing statistics
| Operation | Command |
| --- | --- |
| Clear IM statistics. | [**reset info-center statistics**](cmdqueryname=reset+info-center+statistics) |
| Clear information in the log buffer. | [**reset logbuffer**](cmdqueryname=reset+logbuffer) |
| Delete traps in the trap buffer. | [**reset trapbuffer**](cmdqueryname=reset+trapbuffer) |



#### Monitoring IM

During routine maintenance, you can run the following commands in any view to display the desired device information.

**Table 2** Monitoring IM
| Operation | Command |
| --- | --- |
| View information in IM records. | [**display info-center**](cmdqueryname=display+info-center) [ **statistics** ] |
| View information in the log buffer. | [**display logbuffer**](cmdqueryname=display+logbuffer)  [**display logbuffer brief**](cmdqueryname=display+logbuffer+brief) |
| View traps in the trap buffer. | [**display trapbuffer**](cmdqueryname=display+trapbuffer) [ **size** *buffersize* ]  [**display trapbuffer brief**](cmdqueryname=display+trapbuffer+brief) |
| View information recorded in the log file. | [**display logfile**](cmdqueryname=display+logfile) *path* [ *offset* ] |
| View the list of log files generated in a specified period. | [**display logfile**](cmdqueryname=display+logfile) [ **log** | **diagnose** ] **list** **starttime** *starttime-value* **endtime** *endtime-value* |



#### Checking Security Log Files

![](public_sys-resources/note_3.0-en-us.png) 

Currently, the command applies only to xxx.log and xxx.log.zip files.

To check whether a specified security log file has been tampered with, run the following command.

**Table 3** Checking Security Log Files
| Operation | Command |
| --- | --- |
| Check whether the specified security log file is tampered with. | [**check logfile**](cmdqueryname=check+logfile) *filepath* |