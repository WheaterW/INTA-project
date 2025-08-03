Configuring a Performance Statistics Task
=========================================

This section describes how to configure a performance statistics task. After the performance statistics collection interval is set and an instance is bound to a performance statistics task, the system starts collecting the performance statistics.

#### Context

A performance statistics task enables the system to periodically collect performance statistics for a service. In a performance statistics task, basic performance statistics functions are implemented, and performance statistics files can be generated.

Perform the following steps on the device:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pm**](cmdqueryname=pm)
   
   
   
   The PM view is displayed.
3. Run [**statistics enable**](cmdqueryname=statistics+enable)
   
   
   
   The performance statistics function is enabled.
4. Run [**statistics-task**](cmdqueryname=statistics-task) *task-name*
   
   
   
   A performance statistics task is created, and the performance statistics task view is displayed.
5. Run 
   
   
   
   The type of the performance statistics task is configured.
6. Run [**statistics-cycle**](cmdqueryname=statistics-cycle) *STATSCYCLE*
   
   
   
   The performance statistics collection interval is set.
7. Run [**binding**](cmdqueryname=binding) **instance-type** *instance-type* { **all** | **instance** { *ivpn-instance-name* } & <1-8> }
   
   
   
   An instance is bound to the performance statistics task.
   
   
   
   After an instance is bound to a performance statistics task, the system collects the performance statistics about the instance and generates a statistics file.
8. (Optional) Run [**measure disable**](cmdqueryname=measure+disable) **instance-type** *instance-type* **measure** *measure-name*
   
   
   
   Measurement is disabled for a statistics indicator of the instance bound to the performance statistics task.
   
   
   
   To view statistics indicators of the bound instance, run the [**display pm measure-info**](cmdqueryname=display+pm+measure-info) **instance-type** *instance-type-name* command. To disable measurement for a specific statistics indicator of the bound instance, run the [**measure disable**](cmdqueryname=measure+disable) **instance-type** *instance-type* **measure** *measure-name* command.
9. Run either of the following commands:
   
   
   * Run the [**record-file disable**](cmdqueryname=record-file+disable) command to disable the generation of a performance statistics file.
     
     Run this command when you do not want the system memory to be occupied by many performance statistics files.
   * If the performance statistics file generation function is left enabled, you can run the [**record-interval**](cmdqueryname=record-interval) *interval* command to set the number of intervals at which performance statistics are collected.
     
     After the command is run, the system generates performance statistics files every *cycle* x *interval* minutes and automatically saves the performance statistics in the files.
     
     Run the [**file-format**](cmdqueryname=file-format) { **text** | **xml** } command to set the format for performance statistics files.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.