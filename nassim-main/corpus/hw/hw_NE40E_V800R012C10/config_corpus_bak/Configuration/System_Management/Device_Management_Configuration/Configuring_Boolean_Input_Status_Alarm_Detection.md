Configuring Boolean Input Status Alarm Detection
================================================

Configuring_Boolean_Input_Status_Alarm_Detection

#### Context

The device receives the status of the external sensor through its Boolean input channel as a Boolean value. You can set the normal input status and the name of the Boolean alarm to be reported to the NMS. This allows the device to report a Boolean alarm to the NMS if the status of the external sensor differs from the normal input status.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K-B supports this function.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**io-alarm slot**](cmdqueryname=io-alarm+slot) *slot-id* **index** *index-id* [ **name** *alarm-name* ] **default-status** { **open** | **close** } command to configure the normal input status and the name of the Boolean alarm to be reported to the NMS.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Result

Run the [**display io-alarm**](cmdqueryname=display+io-alarm) command to check the current Boolean input status.