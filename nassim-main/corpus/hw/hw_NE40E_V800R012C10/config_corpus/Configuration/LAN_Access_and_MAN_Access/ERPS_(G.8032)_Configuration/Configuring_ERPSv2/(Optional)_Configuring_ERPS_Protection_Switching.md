(Optional) Configuring ERPS Protection Switching
================================================

To ensure that ERPS rings function normally when a device or link fails, you can set ERPS protection switching functions, such as revertive and non-revertive switching, port blocking modes, and timers.

#### Context

* [Revertive and non-revertive switching](dc_vrp_erps_cfg_0002.html#EN-US_CONCEPT_0172363431__li_dc_vrp_erps_cfg_0002_03)
  
  After link faults are rectified, whether to re-block the RPL owner port depends on the switching mode.
* [Port blocking mode](dc_vrp_erps_cfg_0002.html#EN-US_CONCEPT_0172363431__li_dc_vrp_erps_cfg_0002_04)
  
  In case the RPL has high bandwidth, blocking a link with low bandwidth and unblocking the RPL allow traffic to use the RPL and have more bandwidth. ERPS supports two manual port blocking modes: FS and MS. FS takes precedence over MS. An existing FS or MS operation can be cleared using the [**clear**](cmdqueryname=clear) command. The [**clear**](cmdqueryname=clear) command also has the following functions:
  + Triggers revertive switching before the WTR or WTB timer expires in the case of revertive operations.
  + Triggers revertive switching in the case of non-revertive operations.
* [Timer](dc_vrp_erps_cfg_0002.html#EN-US_CONCEPT_0172363431__li_dc_vrp_erps_cfg_0002_02)
  
  ERPS defines four timers: guard timer, hold-off timer, WTR timer, and WTB timer. The WTB timer value cannot be configured. Its value is the guard timer value plus 5. The default WTB timer value is 7s.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**erps ring**](cmdqueryname=erps+ring) *ring-id*
   
   
   
   The ERPS ring view is displayed.
3. Run [**revertive**](cmdqueryname=revertive) { **enable** | **disable** }
   
   
   
   The protection switching mode is specified.
4. Perform either of the following operations to configure a port blocking mode:
   
   
   * To configure a port blocking mode for a port in the ERPS ring view, run the [**port**](cmdqueryname=port) *interface-type interface-number* **protect-switch** { **force** | **manual** } command.
   * To configure a port blocking mode in the interface view, perform the following steps:
     
     1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view.
     3. Run the [**erps**](cmdqueryname=erps) **ring** *ring-id* [**protect-switch**](cmdqueryname=protect-switch) { **force** | **manual** } command to configure a port blocking mode for the port.
        
        The ERPS ring specified by **ring** *ring-id* must be the one to which the port belongs.
     4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   
   To clear the specified port blocking mode, run the [**clear**](cmdqueryname=clear) command in the ERPS ring view.
5. Run the following commands to configure one or more timers for the ERPS ring:
   
   
   * To configure the WTR timer, run the [**wtr-timer**](cmdqueryname=wtr-timer) *time-value* command.
   * To configure the guard timer, run the [**guard-timer**](cmdqueryname=guard-timer) *time-value* command.
   * To configure the hold-off timer, run the [**holdoff-timer**](cmdqueryname=holdoff-timer) *time-value* command.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.