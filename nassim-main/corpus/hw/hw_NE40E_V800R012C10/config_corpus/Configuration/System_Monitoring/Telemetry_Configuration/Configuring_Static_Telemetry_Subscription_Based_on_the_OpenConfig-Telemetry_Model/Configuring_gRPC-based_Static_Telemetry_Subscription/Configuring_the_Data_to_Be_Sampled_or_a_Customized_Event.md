Configuring the Data to Be Sampled or a Customized Event
========================================================

When configuring static telemetry subscription to the sampled data or a customized event, you need to create a sampling sensor group and specify a sampling path and filter criteria.

#### Context

A device functions as a client, and a collector functions as a server. To statically subscribe to the sampled data or a customized event, you need to configure a source from which to sample the data.

You can configure a telemetry customized event. If a performance indicator of a resource object that telemetry monitors exceeds the user-defined threshold, the customized event is reported to the collector in time for service policy determination.


#### Procedure

* Configure the data to be sampled.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**telemetry**](cmdqueryname=telemetry) [ **openconfig** ]
     
     
     
     The telemetry view is displayed.
  3. Run [**sensor-group**](cmdqueryname=sensor-group) *sensor-name*
     
     
     
     A sampling sensor group is created, and its view is displayed.
  4. Run [**sensor-path**](cmdqueryname=sensor-path) *path* 
     
     
     
     A sampling path is configured for a telemetry sensor.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + A maximum of 64 sampling paths can be configured for a sampling sensor group, including sampling paths configured using the [**sensor-path**](cmdqueryname=sensor-path) and [**sensor-path self-defined-event**](cmdqueryname=sensor-path+self-defined-event) commands. When the number of sampling paths reaches the upper limit, the device displays a message indicating that the maximum number of sampling paths is reached.
     + A sampling path name can be configured for up to 10 sampling sensor groups at the same time. When the number of sampling sensor groups for which a sampling path name is configured reaches the upper limit, the device displays a message indicating that the maximum number of sampling sensor groups is reached.
     + You can configure only the sampling paths for which you have the read permission.
  5. (Optional) Run [**sample-mode yang**](cmdqueryname=sample-mode+yang)
     
     
     
     The sampling mode is set to YANG model-based sampling.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the sampling mode is switched, some sampling content changes, and the sampling interval may change to an integer multiple of the minimum sampling interval under the new sampling mode.
  6. (Optional) Run [**depth**](cmdqueryname=depth) *depth-value*
     
     
     
     A data sampling depth is configured for the sampling path.
  7. (Optional) Run [**policy reset-when-start**](cmdqueryname=policy+reset-when-start)
     
     
     
     The sampling path is cleared during initial configuration.
     
     
     
     Currently, only the sampling path **huawei-qos:qos/global-query/default-queue-statisticss/default-queue-statistics** can be cleared during initial configuration.
  8. Run [**filter**](cmdqueryname=filter) *filter-name*
     
     
     
     A filter is configured for the sampling path, and its view is displayed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If a sampling sensor group is subscribed to and configured with redundancy suppression using the [**sensor-group**](cmdqueryname=sensor-group) command in the subscription view, filter conditions cannot be configured for the sampling path in this sampling sensor group.
  9. Run [**op-field**](cmdqueryname=op-field) *field* **op-type** { **eq** | **gt** | **ge** | **lt** | **le** } **op-value** *value*
     
     
     
     A filter criterion is configured.
  10. (Optional) Run [**condition-relation**](cmdqueryname=condition-relation) { **and** | **or** }
      
      
      
      The logical operation relationship between multiple filter conditions is configured.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure a customized event.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**telemetry**](cmdqueryname=telemetry) [ **openconfig** ]
     
     
     
     The telemetry view is displayed.
  3. Run [**sensor-group**](cmdqueryname=sensor-group) *sensor-name*
     
     
     
     A sampling sensor group is created, and its view is displayed.
  4. Run [**sensor-path**](cmdqueryname=sensor-path) *path* **self-defined-event**
     
     
     
     A customized telemetry event is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + A maximum of 64 sampling paths can be configured for a sampling sensor group, including sampling paths configured using the [**sensor-path self-defined-event**](cmdqueryname=sensor-path+self-defined-event) and [**sensor-path**](cmdqueryname=sensor-path) commands. When the number of sampling paths reaches the upper limit, the device displays a message indicating that the maximum number of sampling paths is reached.
     + A sampling path name can be configured for up to 10 sampling sensor groups at the same time. When the number of sampling sensor groups for which a sampling path name is configured reaches the upper limit, the device displays a message indicating that the maximum number of sampling sensor groups is reached.
     + You can configure only the sampling paths for which you have the read permission.
  5. (Optional) Run [**sample-mode yang**](cmdqueryname=sample-mode+yang)
     
     
     
     The sampling mode is set to YANG.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the sampling mode is switched, some sampling content changes, and the sampling interval may change to an integer multiple of the minimum sampling interval under the new sampling mode.
  6. (Optional) Run [**description**](cmdqueryname=description) *event-description*
     
     
     
     A description is configured for the customized event.
  7. (Optional) Run [**suppress-period**](cmdqueryname=suppress-period) *period*
     
     
     
     A suppression period is configured for the customized event.
  8. (Optional) Run [**level**](cmdqueryname=level) *level-value*
     
     
     
     The level of the customized telemetry event is set.
  9. (Optional) Run [**depth**](cmdqueryname=depth) *depth-value*
     
     
     
     A data sampling depth is configured for the sampling path.
  10. Run [**filter**](cmdqueryname=filter) *filter-name*
      
      
      
      A filter is configured for the sampling path, and its view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If a sampling sensor group is subscribed to and configured with redundancy suppression using the [**sensor-group**](cmdqueryname=sensor-group) command in the subscription view, filter conditions cannot be configured for the sampling path in this sampling sensor group.
  11. Run [**op-field**](cmdqueryname=op-field) *field* **op-type** { **eq** | **gt** | **ge** | **lt** | **le** } **op-value** *value*
      
      
      
      A filter criterion is configured.
  12. (Optional) Run [**condition-relation**](cmdqueryname=condition-relation) { **and** | **or** }
      
      
      
      The logical operation relationship between multiple filter conditions is configured.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.