Configuring Automatic Clock Source Selection
============================================

Configuring Automatic Clock Source Selection

#### Context

A device supports three modes of clock source selection: automatic, manual, and forcible. By default, a device works in automatic clock source selection mode.

The factors for clock source selection include the priority and synchronous status message (SSM) quality level of a clock source.

* Priority
  
  By default, a clock source does not have a default priority. Such a clock source does not participate in clock source selection. A clock source can participate in clock source selection only if a priority is configured.
  
  A lower value indicates a higher priority.
* SSM quality level
  
  An SSM is a group of codes used to indicate the level of the clock quality on a synchronization network. SSMs reflect the level of synchronous timing signals transmitted on a synchronous timing link. A higher SSM quality level indicates a higher clock accuracy. A device can be configured to select a clock source according to the SSM quality level.
  
  The following SSM quality levels are used, listed in descending order of synchronization quality:
  
  + PRC: G.811 clock signal.
  + SSU-A: G.812 transit node clock signal.
  + SSU-B: G.812 local node clock signal.
  + SEC: SDH equipment clock source signal.
  + DNU: The clock source is not used for synchronization.
  + Unknown: The synchronization quality of the clock source is unknown.
  
  You can set a higher priority for a high-precision and high-reliability reference clock so that the reference clock can be preferentially selected.

When multiple clock sources exist on a network, the device selects a clock source in the following sequence:

1. If the device is not configured to select a clock source based on the SSM quality level, it selects a clock source to be synchronized with based on the priorities configured for these clock sources.
2. If the device is configured to select a clock source based on the SSM quality level:
   1. The device preferentially selects a clock source to be synchronized with based on the SSM levels of clock sources in descending order.
   2. If multiple clock sources have the same SSM quality level, the device selects the clock source to be synchronized with based on the priorities of these clock sources in descending order.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Restore the clock source selection mode to automatic.
   
   
   ```
   [clock clear](cmdqueryname=clock+clear)
   ```
   
   If a clock source has been selected manually or forcibly, run this command to restore the automatic mode.
3. (Optional) Enable clock source selection based on SSM quality levels.
   
   
   ```
   [clock ssm-control](cmdqueryname=clock+ssm-control) on
   ```
   
   By default, clock source selection based on SSM quality levels is not enabled.
4. Configure the working mode of the device clock as normal.
   
   
   ```
   [clock run-mode](cmdqueryname=clock+run-mode) normal
   ```
   
   By default, the device clock works in normal mode.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```