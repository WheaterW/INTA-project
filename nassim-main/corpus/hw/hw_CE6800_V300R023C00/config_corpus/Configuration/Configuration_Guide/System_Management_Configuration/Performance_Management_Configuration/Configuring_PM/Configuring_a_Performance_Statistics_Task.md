Configuring a Performance Statistics Task
=========================================

Configuring a Performance Statistics Task

#### Prerequisites

Reachable routes have been configured between the device and PM server.


#### Context

To collect and analyze performance statistics about system services, configure a performance statistics task and bind the task to one or more instances. In the performance statistics task, you can configure the performance statistics collection interval, sampling interval, and parameters for statistics file generation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the PM view.
   
   
   ```
   [pm](cmdqueryname=pm)
   ```
3. Enable the data statistics function.
   
   
   ```
   [statistics enable](cmdqueryname=statistics+enable)
   ```
4. Create a performance statistics task and enter the performance statistics task view.
   
   
   ```
   [statistics-task](cmdqueryname=statistics-task) task-name
   ```
5. Bind an instance to the performance statistics task.
   
   
   ```
   [binding](cmdqueryname=binding) instance-type instance-type { all | instance { vpn-instance-name } &<1-8> }
   ```
   
   After an instance is bound to the performance statistics task, the system immediately collects and records the performance statistics about the instance.
6. (Optional) Disable measurement for a statistics indicator of the bound instance.
   
   
   ```
   [measure disable instance-type](cmdqueryname=measure+disable+instance-type) instance-type { measure { measure-name } | all }
   ```
   
   
   
   By default, measurement is enabled for all statistics indicators of a bound instance.
   
   To view statistics indicators of a bound instance, run the [**display pm measure-info**](cmdqueryname=display+pm+measure-info) **instance-type** *instance-type-name* command.
7. (Optional) Configure a sampling interval.
   
   
   ```
   [sample-interval](cmdqueryname=sample-interval) interval
   ```
   
   By default:
   
   * If the performance statistics collection interval is 5 minutes, the default sampling interval is 1 minute.
   * If the performance statistics collection interval is 10 minutes, the default sampling interval is 2 minutes.
   * If the performance statistics collection interval is 15 minutes, the default sampling interval is 3 minutes.
   * If the performance statistics collection interval is 30 minutes, the default sampling interval is 5 minutes.
   * If the performance statistics collection interval is 60 minutes, the default sampling interval is 5 minutes.
   * If the performance statistics collection interval is 1440 minutes, the default sampling interval is 15 minutes.
8. (Optional) Configure a performance statistics collection interval.
   
   
   ```
   [statistics-cycle](cmdqueryname=statistics-cycle) cycle
   ```
   
   By default, the performance statistics collection interval is 15 minutes.
9. (Optional) Configure whether to generate performance statistics files.
   
   
   * Disable the function to generate performance statistics files.
     ```
     [record-file disable](cmdqueryname=record-file+disable)
     ```
     
     By default, performance statistics files are automatically generated and saved on a device.
     
     You can run this command to prevent performance statistics files from being generated, reducing memory resource consumption.
   
   
   * Set the number of performance statistics collection intervals when the function to generate performance statistics files is enabled.
     ```
     [record-interval](cmdqueryname=record-interval) interval
     ```
     By default:
     + If a short interval (5, 10, 15, 30, or 60 minutes) is set for collecting performance statistics, the system generates a performance statistics file for every four intervals.
     + If a long interval (1440 minutes) is set for collecting performance statistics, the system generates a performance statistics file for every interval.
     
     After the command is run, the system generates a performance statistics file at every *cycle* x *interval* minutes to automatically save the performance statistics.
     
     You can run the [**file-format**](cmdqueryname=file-format) { **text** | **xml** } command to set a format for performance statistics files.
10. Exit the PM view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```