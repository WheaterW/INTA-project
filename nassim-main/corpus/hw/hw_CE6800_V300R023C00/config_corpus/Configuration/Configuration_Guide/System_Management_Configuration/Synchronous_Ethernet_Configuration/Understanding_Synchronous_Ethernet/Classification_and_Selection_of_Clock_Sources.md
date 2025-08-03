Classification and Selection of Clock Sources
=============================================

Classification and Selection of Clock Sources

#### Clock Sources

A device that provides clock signals for local devices is called a clock source. A local device can have multiple clock sources, which are classified as follows:

* External clock source
  
  An external clock source is connected to a clock device at a higher stratum through Ethernet interfaces.
* PTP clock source
  
  A PTP clock source extracts clock signals through 1588v2 messages.
* Line clock source
  
  A line clock source extracts clock signals over Ethernet bit streams through Ethernet interfaces.
* System clock source
  
  A system clock source is a device's internal clock (such as the clock provided by the device's clock chip).

Among these clock sources, the typical order of clock accuracy is as follows: external clock source > PTP clock source > line clock source > system clock source.


#### Factors in Clock Source Selection

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


#### Priority of Clock Source Selection

When multiple clock sources exist on a network, the device selects a clock source in the following sequence:

1. If the device is not configured to select a clock source based on the SSM quality level, it selects a clock source to be synchronized with based on the priorities configured for these clock sources.
2. If the device is configured to select a clock source based on the SSM quality level:
   1. The device preferentially selects a clock source to be synchronized with based on the SSM levels of clock sources in descending order.
   2. If multiple clock sources have the same SSM quality level, the device selects the clock source to be synchronized with based on the priorities of these clock sources in descending order.


#### Clock Source Selection Modes

A device supports three modes of clock source selection: automatic, manual, and forcible.

* Automatic mode: The system uses the automatic clock source selection algorithm to determine the clock source to be synchronized with based on the priorities and SSM quality levels of clock sources.
* Manual mode: The clock source to be synchronized with is manually specified using commands. Such a clock source must have the highest SSM quality level.
* Forcible mode: The clock source to be synchronized with is forcibly specified using commands. Such a clock source can be any clock source.

For details about protection switching when a clock source fails in each mode, see [Protection Switching](galaxy_synce_cfg_0009.html).

![](public_sys-resources/note_3.0-en-us.png) 

Using the automatic mode is recommended. In this mode, a device can dynamically select the optimal clock source to be synchronized with based on the priority.