Configuring the Sampling Path and Filter Criteria
=================================================

Configuring the Sampling Path and Filter Criteria

#### Context

When configuring static subscription to collect sampled data, you need to create a sampling sensor group and specify a sampling path and filter criteria. You can configure a customized event. If a performance indicator of a resource object that the telemetry-enabled device monitors meets the filter criteria, the corresponding customized event will be reported to the collector in a timely manner for service policy determination.

You can configure the sampling path and filter criteria using either of the following methods as required:

* Configure the sampling path and filter criteria for a non-customized event.
* Configure the sampling path and filter criteria for a customized event. This method is more flexible.

#### Procedure

* Configure the sampling path and filter criteria for a non-customized event.
  1. Create a sampling sensor group.
     
     
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Enter the telemetry view.
        ```
        [telemetry](cmdqueryname=telemetry) [ openconfig ]
        ```
     3. Create a sampling sensor group, and enter the sensor group view.
        ```
        [sensor-group](cmdqueryname=sensor-group) sensor-name
        ```
  2. Configure a non-customized event for the sampling sensor group, including the sampling path and filter criteria.
     
     
     1. Configure a sampling path for the non-customized event.
        ```
        [sensor-path](cmdqueryname=sensor-path) path
        ```
        ![](public_sys-resources/note_3.0-en-us.png) 
        
        You can configure only the sampling paths on which you have the read permission.
        
        A maximum of 64 sampling paths can be configured for a sampling sensor group, including sampling paths configured using the [**sensor-path**](cmdqueryname=sensor-path) and [**sensor-path self-defined-event**](cmdqueryname=sensor-path+self-defined-event) commands. When the number of sampling paths reaches the upper limit, the device displays a message indicating that the maximum number of paths is reached.
        
        A sampling path name can be configured in a maximum of 10 sampling sensor groups. When the number of sampling sensor groups for which the same sampling path name is configured reaches the upper limit, a message indicating this will be displayed.
        
        If the sampling sensor group is subscribed and configured with redundancy suppression, sampling paths with filter criteria specified cannot be configured in this sampling sensor group.
     2. (Optional) Configure the data sampling depth for the non-customized event.
        ```
        [depth](cmdqueryname=depth) depth-value
        ```
     3. Create a filter for the sampling path.
        1. Create a filter and enter the filter view.
           ```
           [filter](cmdqueryname=filter) filter-name
           ```
        2. Configure filter criteria.
           ```
           [op-field](cmdqueryname=op-field) field op-type { eq | gt | ge | lt | le } op-value value
           ```
        3. Configure the logical operation mode between filter criteria.
           ```
           [condition-relation](cmdqueryname=condition-relation) { and | or }
           ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the sampling path and filter criteria for a customized event.
  1. Create a sampling sensor group.
     
     
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Enter the telemetry view.
        ```
        [telemetry](cmdqueryname=telemetry) [ openconfig ]
        ```
     3. Create a sampling sensor group, and enter the sensor group view.
        ```
        [sensor-group](cmdqueryname=sensor-group) sensor-name
        ```
  2. Configure a customized event for the sampling sensor group, including the sampling path and filter criteria.
     
     
     1. Configure a sampling path for the customized event and enter the customized event view.
        ```
        [sensor-path](cmdqueryname=sensor-path) path  self-defined-event
        ```
        ![](public_sys-resources/note_3.0-en-us.png) 
        
        You can configure only the sampling paths on which you have the read permission.
        
        A maximum of 64 sampling paths can be configured for a sampling sensor group, including sampling paths configured using the [**sensor-path**](cmdqueryname=sensor-path) and [**sensor-path self-defined-event**](cmdqueryname=sensor-path+self-defined-event) commands. When the number of sampling paths reaches the upper limit, the device displays a message indicating that the maximum number of paths is reached.
        
        A sampling path name can be configured in a maximum of 10 sampling sensor groups. When the number of sampling sensor groups for which the same sampling path name is configured reaches the upper limit, a message indicating this will be displayed.
        
        If the sampling sensor group is subscribed and configured with redundancy suppression, sampling paths with filter criteria specified cannot be configured in this sampling sensor group.
     2. (Optional) Configure the description, suppression period, level, and data sampling depth of the customized event based on actual requirements.
        + Configure a description for the customized event.
          ```
          [description](cmdqueryname=description) event-description
          ```
        + Configure a suppression period for the customized event.
          ```
          [suppress-period](cmdqueryname=suppress-period) period
          ```
        + Configure a level for the customized event.
          ```
          [level](cmdqueryname=level) level-value
          ```
        + Configure a data sampling depth for the sampling path.
          ```
          [depth](cmdqueryname=depth) depth-value
          ```
     3. Create a filter for the sampling path.
        1. Create a filter and enter the filter view.
           ```
           [filter](cmdqueryname=filter) filter-name
           ```
        2. Configure filter criteria.
           ```
           [op-field](cmdqueryname=op-field) field op-type { eq | gt | ge | lt | le } op-value value
           ```
        3. Configure the logical operation mode between filter criteria.
           ```
           [condition-relation](cmdqueryname=condition-relation) { and | or }
           ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display telemetry sensor**](cmdqueryname=display+telemetry+sensor) [ *sensor-name* ] command to check the sensor group information.
* Run the [**display telemetry sensor-path**](cmdqueryname=display+telemetry+sensor-path) command to check the sampling paths of the sensor.