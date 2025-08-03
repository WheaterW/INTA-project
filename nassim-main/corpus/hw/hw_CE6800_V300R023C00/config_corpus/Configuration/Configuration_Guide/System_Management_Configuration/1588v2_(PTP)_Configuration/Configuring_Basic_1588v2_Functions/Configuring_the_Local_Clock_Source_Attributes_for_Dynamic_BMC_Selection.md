Configuring the Local Clock Source Attributes for Dynamic BMC Selection
=======================================================================

Configuring the Local Clock Source Attributes for Dynamic BMC Selection

#### Context

After multiple 1588v2 devices are configured to import time signals from an external clock, their local clocks can participate in BMC selection. A grandmaster clock can be dynamically determined based on the BMC algorithm and provides time signals to the entire 1588v2 network. 1588v2 devices obtain clock synchronization information from the grandmaster clock through 1588v2.

During implementation of the dynamic BMC algorithm, 1588v2 devices select the grandmaster clock based on the following sequence of priorities: **priority1** > **clock-class** > **clock-accuracy** > **priority2**. Specifically, the **priority1** values of 1588v2 devices are compared first. If the **priority1** values are the same, the **clock-class** values are compared, and the process continues in this manner. The clock with the highest priority is elected as the grandmaster clock.

Perform the following steps on each 1588v2 device connected to an external clock source:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure clock source attributes for BMC selection as required.
   
   
   
   **Table 1** Configuring clock source attributes for BMC selection
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the level of a clock source. | [**ptp clock-source**](cmdqueryname=ptp+clock-source) **local** **clock-class** *clock-class-value* | By default, the level of the local clock source is 187.  NOTE:  If the value of *clock-class-value* is less than 128, the device cannot function as a slave clock. |
   | Configure the clock accuracy of a clock source. | [**ptp clock-source**](cmdqueryname=ptp+clock-source) **local** **clock-accuracy** *clock-accuracy-value* | By default, the accuracy of the local clock source is 0x31. |
   | Configure priority1 for a clock source. | [**ptp clock-source**](cmdqueryname=ptp+clock-source) **local** **priority1** *priority1-value* | By default, the priority1 value of the local clock source is 128. |
   | Configure priority2 for a clock source. | [**ptp clock-source**](cmdqueryname=ptp+clock-source) **local** **priority2** *priority2-value* | By default, the priority2 value of the local clock source is 128. |
3. (Optional) Configure the type of the clock source traced by devices.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) local time-source time-source-value
   ```
   
   By default, the type value of the local clock source is 8, indicating that the clock type is INTERNAL\_OSCILLATOR.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```