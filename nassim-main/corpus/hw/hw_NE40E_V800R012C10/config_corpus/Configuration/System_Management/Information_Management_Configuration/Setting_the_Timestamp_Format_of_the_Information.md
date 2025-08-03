Setting the Timestamp Format of the Information
===============================================

This section describes how to set the timestamp format of the information.

#### Usage Scenario

The timestamp format of the information can be set to meet different time requirements in different places. After the configuration is complete, new information is generated according to the set timestamp format.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this document, timestamp formats of logs, traps, and debugging information are set.

Only physical systems (PSs) support setting the timestamp format of the Information.



#### Pre-configuration Tasks

Before setting the timestamp format in the information, ensure that the device is powered on correctly and the self-test is successful.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run any of the following commands to set the timestamp format of the information:
   
   
   * To set the timestamp format of the log information, run the [**info-center timestamp**](cmdqueryname=info-center+timestamp) **log** { **boot** | { **date** | **short-date** | **format-date** | **rfc-3339** } [ **precision-time** { **tenth-second** | **millisecond** | **second** } ] } [ **without-timezone** ] command.
   * To set the timestamp format of the trap, run the [**info-center timestamp**](cmdqueryname=info-center+timestamp) **trap** { **boot** | { **date** | **short-date** | **format-date** | **rfc-3339** } [ **precision-time** { **tenth-second** | **millisecond** | **second** } ] } [ **without-timezone** ] command.
   * To set the timestamp format of the debugging information, run the [**info-center timestamp**](cmdqueryname=info-center+timestamp) **debugging** { **boot** | { **date** | **short-date** | **format-date** | **rfc-3339** } [ **precision-time** { **tenth-second** | **second** | **millisecond** } ] } [ **without-timezone** ] command.
   
   The following table describes the elements of the timestamp in **date** format.
   
   **Table 1** Elements of the timestamp in date format
   | Field | Description | Value |
   | --- | --- | --- |
   | yyyy | Year | 4 digits |
   | mm | Month | Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, or Dec |
   | dd | Date | If the date value (such as 7) is smaller than 10, a blank is added before the date. |
   | hh:mm:ss | Local time in hh:mm:ss format | The hour (hh) is expressed in 24-hour system, ranging from 00 to 23. The minute (mm) and second (ss) are values ranging from 00 to 59. |
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display logbuffer**](cmdqueryname=display+logbuffer) command to check whether the timestamp format in the log information is configured successfully.