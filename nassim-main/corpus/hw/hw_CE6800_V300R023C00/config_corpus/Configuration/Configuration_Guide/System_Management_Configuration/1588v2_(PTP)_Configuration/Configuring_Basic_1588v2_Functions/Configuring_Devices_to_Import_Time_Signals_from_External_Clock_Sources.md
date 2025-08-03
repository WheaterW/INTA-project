Configuring Devices to Import Time Signals from External Clock Sources
======================================================================

Configuring Devices to Import Time Signals from External Clock Sources

#### Context

An external clock source can be used to provide reference time signals for devices. Currently, devices can import time signals from PTP clock sources and external clock sources. This section describes how to configure a device to import time signals from PTP clock sources. For details about configuring line clock sources, see [Configuring a Clock Source](galaxy_synce_cfg_0012.html).

When the dynamic BMC algorithm is used, multiple 1588v2 devices can be configured to import time signals from external clock sources so that these 1588v2 devices can take part in dynamic determination of the grandmaster clock through the BMC algorithm. The determined grandmaster clock provides time signals for all devices on the 1588v2 network, and these devices use 1588v2 to obtain clock synchronization information from the grandmaster clock.

Perform the following steps on each 1588v2 device connected to an external clock source:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable clock synchronization for the PTP clock source.
   
   
   ```
   [clock](cmdqueryname=clock) source ptp synchronization enable
   ```
   
   
   
   By default, clock synchronization is not enabled for a PTP clock source.
3. Configure a priority for the PTP clock source.
   
   
   ```
   [clock](cmdqueryname=clock) source ptp priority priority-value
   ```
   
   
   
   By default, no priority is set for a PTP clock source, indicating that it cannot participate in BMC selection. A smaller value indicates a higher priority.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

To enable 1588v2 on an interface to which time signals are imported from a PTP clock source, refer to [Enabling 1588v2 on an Interface](galaxy_1588v2_cfg_0016.html). Time signals can then be successfully imported from the PTP clock source.