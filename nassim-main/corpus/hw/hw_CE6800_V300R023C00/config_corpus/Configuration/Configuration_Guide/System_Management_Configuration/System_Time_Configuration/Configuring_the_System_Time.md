Configuring the System Time
===========================

Configuring the System Time

#### Context

System time is the current time that a device keeps track of and is recorded in timestamps of sent packets. Users in different regions can configure the system time according to their own country's or region's regulations.

System time = Coordinated Universal Time (UTC) + Time zone offset + Daylight saving time (DST) offset

The system time needs to be set correctly so that a device can coordinate properly with other devices. However, on networks that contain multiple devices, setting or adjusting the system time manually involves a heavy workload and may compromise the clock accuracy. To ensure clock synchronization among devices with clocks, you can configure the Network Time Protocol (NTP) feature. This allows devices to synchronize their clocks so that they can provide diverse applications based on consistent time.


#### Procedure

1. Configure the time zone in the user or system view.
   
   
   ```
   [clock timezone](cmdqueryname=clock+timezone) time-zone-name { add | minus } offset
   ```
   
   
   
   **add**: adds the specified time zone offset on the basis of the UTC time. The sum of the default UTC time zone and *offset* is the time in the time zone specified by *time-zone-name*.
   
   **minus**: subtracts the specified time zone offset from the UTC time. The remainder obtained by subtracting the time zone offset (*offset*) from the default system time (UTC time) is the time in the time zone specified by *time-zone-name*.
   
   After a time zone is configured, the device adds timestamps to the local log in the format of *original system time* ± *offset*. An example is Apr 27 2020 22:36:09+08:00.
2. Configure the current time in the user view.
   
   
   ```
   [clock datetime](cmdqueryname=clock+datetime) [ utc ] time date
   ```
   
   
   
   The time format is HH:MM:SS, and the date format is YYYY-MM-DD.
   
   If the configuration contains the keyword **utc**, the configured time is the UTC time. If the configuration does not contain the keyword **utc** and a time zone has been configured, the configured time is the system time.
   
   If the configuration does not contain the keyword **utc** and no time zone has been configured, the system saves the configured time (UTC time) based on time zone 0. In this case, the configured time is the system time. If a time zone is configured later, the current time plus the time zone offset is the system time.
3. (Optional) Configure the DST in the user or system view.
   
   
   ```
   [clock daylight-saving-time](cmdqueryname=clock+daylight-saving-time) dstname one-year start-time start-date end-time end-date offset
   ```
   
   or
   
   ```
   [clock daylight-saving-time](cmdqueryname=clock+daylight-saving-time) dstname repeating start-time { { first | second | third | fourth | last } startweekday startmonth end-time { first | second | third | fourth | last } endweekday endmonth } offset [ startyear [ endyear ] ]
   ```
   
   You can configure the start time and end time for periodic DST in one of the following modes: date+date, week+week, date+week, and week+date. For configuration details, see the [**clock daylight-saving-time**](cmdqueryname=clock+daylight-saving-time) command.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the current time is the DST time, you can set a time zone using the [**clock timezone**](cmdqueryname=clock+timezone) *time-zone-name* { **add** | **minus** } *offset* command. However, when the system time is within the DST, the time zone in the [**display clock**](cmdqueryname=display+clock) command output is the DST name. The system will display the configured time zone after the DST ends.
4. (Optional) Set the date format of the device in the user or system view.
   
   
   ```
   [clock date-format](cmdqueryname=clock+date-format) { YYYY-MM-DD | MM-DD-YYYY }
   ```
   
   By default, the date format of a device is *YYYY-MM-DD*.
   
   *YYYY-MM-DD* indicates year-month-day, and *MM-DD-YYYY* indicates month-day-year.

#### Verifying the Configuration

Run the [**display clock**](cmdqueryname=display+clock) [ **utc** ] command to check the configured system clock.


#### Follow-up Procedure

To automatically synchronize time from the NTP server, see "NTP Configuration" in Configuration Guide > System Management Configuration.