Clearing Error Statistics and Alarm Status Information on an E1 Interface or on a CPOS Interface's E1 Channels
==============================================================================================================

Clearing Error Statistics and Alarm Status Information on an E1 Interface or on a CPOS Interface's E1 Channels

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.

This section describes how to clear error statistics and alarm status information on an E1 interface or on a CPOS interface's E1 channels.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**reset e1 counters controller cpos**](cmdqueryname=reset+e1+counters+controller+cpos) *controller-number* **e1** *e1-number* command to clear error statistics and alarm status information on a CPOS interface's E1 channels or run the [**reset e1 counters controller e1**](cmdqueryname=reset+e1+counters+controller+e1) *controller-number* command to clear error statistics and alarm status information on an E1 interface.