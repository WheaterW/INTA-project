Performing Configuration Rollback
=================================

Configuration rollback allows the system to roll back to a specified historical configuration state. This section describes how to roll back the system to the specified configuration state.

#### Context

If you have committed configurations but find unexpected results, roll the system back to a specified historical configuration state.


#### Procedure

1. (Optional) Select a validation mode and edit and commit configurations.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) The system supports two validation modes: immediate mode and two-phase validation mode.
   * In immediate validation mode, after you run a command and press **Enter**, the system checks whether the current configuration is different from the previous one. If they are different, the system commits the current configuration and generates a configuration rollback point. Multiple configuration rollback points may be created for a feature.
   * In two-phase validation mode, after you run a series of commands, the system checks the differences between the current configuration and the previous one and generates a configuration rollback point only when you run the [**commit**](cmdqueryname=commit) [ **description** *description* ] command. The configurations of multiple commands for a service take effect in batches. You can run the **description** *description* command to add a brief description for a configuration rollback point, allowing rapid locating of a desired configuration rollback point. The two-phase validation mode is recommended for configuration editing and committing.
   * Run the [**system-view**](cmdqueryname=system-view) **immediately** command to enter the system view in immediate validation mode. After you run commands to edit configurations, the new configurations take effect immediately.
   * Run the [**system-view**](cmdqueryname=system-view) command to enter the system view in two-phase validation mode.
     
     1. (Optional) Run the [**undo configuration checkpoint auto-save disable**](cmdqueryname=undo+configuration+checkpoint+auto-save+disable) command to enable the device to automatically generate a configuration rollback point.
     2. Edit configurations.
     3. Run the [**commit**](cmdqueryname=commit) [ **description** *description* | **label** *label* ] command to commit the new configurations for them to take effect.
2. Check the configuration rollback point list and configuration difference.
   
   
   1. Run the [**display configuration commit list**](cmdqueryname=display+configuration+commit+list) [ **verbose** ] [ *number-of-commits* | **label** ] command to check the configuration rollback point list, determine whether a configuration rollback point is generated, and view information about each configuration rollback point.
      
      To view information about the most recent configuration rollback points, specify *number-of-commits*.
   2. Run the [**display configuration commit changes**](cmdqueryname=display+configuration+commit+changes) [ **at** *commit-id* | **since** *commit-id* | **last** *number-of-commits* ] command to view configuration changes. Based on the configuration changes, you can determine whether to roll back system configurations and check the impact of the configuration rollback operation on system performance.
      
      To view configuration changes at all configuration rollback points, run this command with no parameter specified.
      
      To view the configuration changes at a configuration rollback point, specify **at** *commit-id*.
      
      To view configuration changes since a configuration rollback point, specify **since** *commit-id*.
      
      To view configuration changes at the most recent configuration rollback points, specify **last** *number-of-commits*.
3. Roll back system configurations as required.
   
   
   * If the historical configuration corresponding to a configuration rollback point meets user requirements, perform the following steps:
     
     1. Run the [**return**](cmdqueryname=return) command to return to the user view. This ensures that no additional configuration is committed after the configuration rollback operation begins.
     2. Run the [**rollback configuration**](cmdqueryname=rollback+configuration) { **to** **commit-id** *commit-id* | **last** *number-of-commits* | **to** **label** *label* | **to** **file** *file-name* } command to roll system configurations back to a previous configuration rollback point by specifying the desired configuration rollback point or the number of the configuration rollback points that the incoming configuration rollback operation is expected to undergo. All configurations that were in place at the rollback point are restored, regardless of any change executed after the rollback point was created. Configurations created after the point are deleted, deleted configurations are restored, and modified configurations are returned to what they were when the rollback point was created.
        
        To roll system configurations back to a specified configuration rollback point, specify **to** **commit-id** *commit-id*.
        
        To allow the configuration rollback operation to undergo the most recent configuration rollback points, specify **last** *number-of-commits*.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        After the configuration rollback operation is complete, you can run the [**display configuration rollback result**](cmdqueryname=display+configuration+rollback+result) command to view the result of the latest configuration rollback operation.
   * If the current configuration is incorrect or the configuration of the configuration rollback point meets user requirements, you can perform the following steps to load the configuration corresponding to the configuration rollback point, and then edit the required content:
     
     1. Run the [**return**](cmdqueryname=return) command to return to the user view. This ensures that no additional configuration is committed after the configuration rollback operation begins.
     2. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     3. Run the [**load configuration rollback changes**](cmdqueryname=load+configuration+rollback+changes){ **at****commit-id***at-commit-id* | **to****commit-id***commit-id* | **last***number-of-commits* | **to****label***user-label* } command to load the configuration of a specified configuration rollback point or the configuration with a specified user label.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        After the configuration rollback operation is complete, you can run the [**display configuration rollback changes load-result**](cmdqueryname=display+configuration+rollback+changes+load-result) command to view the result of the latest configuration rollback operation.

#### Checking the Configuration

* Run the [**display configuration commit list**](cmdqueryname=display+configuration+commit+list) [ **verbose** ] [ *number-of-commits* | **label** ] command to view the configuration rollback point list.
* Run the [**display configuration commit changes**](cmdqueryname=display+configuration+commit+changes) [ *commit-id* | **since** *commit-id* | **last** *number-of-commits* ] command to view information about configuration changes.
* Run the [**display configuration rollback result**](cmdqueryname=display+configuration+rollback+result) command to view information about the latest configuration rollback operation, including warning and failure messages if there is any.
* Run the [**display configuration rollback changes load-result**](cmdqueryname=display+configuration+rollback+changes+load-result) command to view the command that fails to be executed to load the configuration of the specified configuration rollback point or the configuration with a specified user label and the failure cause.