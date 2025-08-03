Viewing the Difference Between the Candidate Configuration and Current Running Configuration
============================================================================================

This section describes how to view the difference between the candidate configuration and current running configuration before the candidate configuration is committed. If a configuration conflict is found, resolve the conflict before viewing the configuration difference.

#### Context

Before committing a set of configuration, you can view the difference between the modified configuration and current running configuration. If the running configuration is changed during the period from configuration modification to configuration difference viewing, a configuration conflict occurs. In addition, an error message is displayed when you view the configuration difference. In this case, resolve the configuration conflict so that you can continue to view the configuration difference.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This operation can be performed only in two-phase validation mode.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**display configuration candidate changes**](cmdqueryname=display+configuration+candidate+changes)
   
   
   
   The difference between the candidate configuration and current running configuration is displayed.
   
   
   
   If the system displays a message indicating that the current configuration is changed, go to [Step 3](#EN-US_TASK_0139427561__s_3) to resolve the configuration conflict and then perform this step to view the configuration difference.
3. (Optional) Run [**refresh configuration candidate**](cmdqueryname=refresh+configuration+candidate)
   
   
   
   The candidate configuration is updated to resolve the configuration conflict.
   
   
   
   If a configuration conflict occurs, perform this step to resolve the conflict.