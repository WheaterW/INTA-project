Creating a Timestamp-Refresh Instance
=====================================

When you create a timestamp-refresh instance, the timestamp-refresh instance view is directly displayed. In this view, you can configure the update threshold, type, mode, and offset value for the instance. The purpose of creating a timestamp-refresh instance is to associate this instance with input multicast streams. This simplifies the timestamp-refresh configuration.

#### Context

Timestamp-refresh allows a device to refresh the timestamps of RTP packets to be synchronous with its local time.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**multicast timestamp-refresh instance**](cmdqueryname=multicast+timestamp-refresh+instance) *instance-name* command to create a timestamp-refresh instance and enter the timestamp-refresh instance view.
3. Run the [**mode**](cmdqueryname=mode) { **2022-7** | **common** } command to configure a mode for the timestamp-refresh instance.
   
   The purpose of setting a mode for the timestamp-refresh instance is to specify the method for the offset value to take effect.
   * If the 2022-7 mode is set for a timestamp-refresh instance, traffic is blocked. You can configure the device to deliver the global offset value for the timestamp-refresh instance to stop traffic blocking and make the timestamp-refresh function take effect.
   * In the common mode, the timestamp-refresh offset value updated by the main control board is automatically delivered, requiring no extra configuration.
4. Run the [**type**](cmdqueryname=type) {**video-stream** | **ancillary-data** } command to configure a type for the timestamp-refresh instance.
   
   
   
   The purpose of configuring a type for the timestamp-refresh instance is to determine the type of multicast data.
   
   
   
   * **video-stream:** video stream type
   * **ancillary-data**: ancillary data type
5. (Optional) Run the [**update-threshold**](cmdqueryname=update-threshold)**update-threshold-value** command to configure an update threshold for the timestamp-refresh instance.
   
   
   
   The purpose of configuring an update threshold for a timestamp-refresh instance is to specify the condition of updating the timestamp-refresh offset value. When the packet arrival time difference is less than the update threshold, the timestamp-refresh offset value is not updated.
6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
7. (Optional) Run the [**set multicast timestamp-refresh**](cmdqueryname=set+multicast+timestamp-refresh) **instance** *instance-name***timestamp-offset** *timestamp-offset-value* command to deliver the timestamp-refresh offset value.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This configuration applies only to the 2022-7 mode. In the common mode, the timestamp-refresh offset value updated by the main control board is automatically delivered, requiring no extra configuration.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.