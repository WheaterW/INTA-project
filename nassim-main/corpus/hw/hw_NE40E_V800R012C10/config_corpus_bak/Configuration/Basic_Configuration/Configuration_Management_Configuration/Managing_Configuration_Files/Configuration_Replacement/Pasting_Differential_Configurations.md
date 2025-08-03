Pasting Differential Configurations
===================================

If multiple devices share the same source but have different configurations, use this function to paste differential configurations to desired devices so that the configurations on the devices are the same.

#### Usage Scenario

If one of the devices with the same configurations encounters a configuration change, the configurations of other devices must be changed accordingly to keep configuration consistency. In this case, you can query the configuration differences and use the configuration replacement function to paste the differential configurations to those devices. This ensures that the configurations on all the devices are the same.

This function is supported only in the two-phase configuration validation mode.


#### Prerequisites

The system has been configured, and configuration rollback points have been generated. The list of configuration rollback points can be viewed using the [**display configuration commit list**](cmdqueryname=display+configuration+commit+list) [ **verbose** ] [ *number-of-commits* | **label** ] command.


#### Procedure

1. View configuration differences.
   * View the differential configurations (with the specified tag) between the configurations in a specified configuration file on the device and the current running configurations.
     
     + Run the [**display configuration changes**](cmdqueryname=display+configuration+changes) **running file** *file-name* **with-tag** command to view the current running configurations that are different from the configurations in the specified configuration file.
     + Run the [**display configuration changes**](cmdqueryname=display+configuration+changes) **file** *file-name* **running** **with-tag** command to view the specified configuration file's configurations that are different from the current running configurations.
     + Run the [**display configuration changes**](cmdqueryname=display+configuration+changes) **running label** *label* **with-tag** command to view the current running configurations that are different from the configurations with a specified tag.
     + Run the [**display configuration changes**](cmdqueryname=display+configuration+changes) **label** *label* **running** **with-tag** command to view the configurations (with a specified tag) that are different from the current running configurations.
   * View the configuration change information (with the specified tag) recorded at specified configuration rollback points.
     + Run the [**display configuration commit changes**](cmdqueryname=display+configuration+commit+changes) [ **at** *commit-id* | **since** *commit-id* | **last**  *number-of-commits* ] **with-tag** command to check the configuration change information (with the specified tag) recorded at specified configuration rollback points.
2. Copy the differential configurations and paste them to the local device to replace the current running configurations of the device.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**load configuration terminal**](cmdqueryname=load+configuration+terminal)
      
      
      
      The configuration difference pasting view is displayed.
      
      
      
      To paste
      the differential configurations in the configuration difference pasting
      view, perform the following steps:
      1. After entering the configuration difference pasting view, copy
         and paste the queried differential configurations to the current device.
      2. After pasting differential configurations, enter **end-diff** or **abort**.
         
         * **end-diff**: Ends the pasting and exits from the
           configuration difference pasting view.
         * **abort**: Cancels the pasting and exits from the
           configuration difference pasting view.
   3. (Optional) Run [**display configuration candidate**](cmdqueryname=display+configuration+candidate)
      
      
      
      Check whether the post-replacement configurations meet the expectation.
      
      
      
      * If the configurations meet the expectation, go to Step d.
      * If the configurations do not meet the expectation, run the [**clear configuration candidate**](cmdqueryname=clear+configuration+candidate) command to clear the configurations and perform Step b to paste differential configurations.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.