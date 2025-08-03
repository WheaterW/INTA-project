Configuring the System Clock
============================

You need to correctly set the system clock to ensure synchronization with other devices.

#### Usage Scenario

NTP provides the provision for configuring the system datetime, timezone and daylight saving time information.

In the application environment where absolute time is strictly required, the current date and clock of the Router must be set.


#### Pre-configuration Tasks

None


#### Procedure

1. Run [**clock datetime**](cmdqueryname=clock+datetime) *time* *date*
   
   
   
   The current time is set.
2. (Optional) Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
3. Run [**clock timezone**](cmdqueryname=clock+timezone) *time-zone-name* { **add** | **minus** } *offset*
   
   
   
   The local time zone is set.
4. Run [**clock daylight-saving-time**](cmdqueryname=clock+daylight-saving-time) *dstname* **one-year** *start-time start-date end-time end-date offset*
   
   
   
   Or, [**clock daylight-saving-time**](cmdqueryname=clock+daylight-saving-time) *dstname* **repeating** *start-time* { { **first** | **second** | **third** | **fourth** | **last** } *weekday month* } *end-time* { { **first** | **second** | **third** | **fourth** | **last** } *weekday month* | *end-date* } *offset* [ *start-year* [ *end-year* ] ]
   
   The daylight saving time is set.

#### Checking the Configurations

After completing the configuration, run the following command to verify the configuration.

Run the [**display clock**](cmdqueryname=display+clock) command to display the system time.