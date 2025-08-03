Configuring a Clock Source
==========================

Configuring a Clock Source

#### Prerequisites

* Devices on which SyncE needs to be performed are connected through Ethernet interfaces to form a clock synchronization network.
* A clock source is connected to the clock synchronization network through Ethernet interfaces.

#### Context

Before configuring clock synchronization on a device, you need to configure the device with either a PTP clock source or a line clock source. The configuration varies according to the type of clock source. Perform the corresponding procedure according to the clock source used on the clock synchronization network.


#### Procedure

* Configure a PTP clock source.
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
     
     By default, no priority is configured for a PTP clock source, indicating that the clock source can participate in clock source selection only if a priority is configured. A smaller value indicates a higher priority.
  4. (Optional) Configure the SSM quality level of the PTP clock source.
     
     
     ```
     [clock source](cmdqueryname=clock+source) ptp ssm { dnu | prc | sec | ssua | ssub | unk }
     ```
     
     By default, the SSM quality level of a PTP clock source is DNU, indicating that the clock source is not used for synchronization.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a line clock source.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the Ethernet interface connected to the line clock source.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Enable clock synchronization for the line clock source.
     
     
     ```
     [clock synchronization enable](cmdqueryname=clock+synchronization+enable)
     ```
     
     
     
     By default, clock synchronization is not enabled for a line clock source.
  4. Configure a priority for the line clock source.
     
     
     ```
     [clock](cmdqueryname=clock) priority priority-value
     ```
     
     By default, no priority is configured for a line clock source, indicating that the clock source does not participate in clock source selection. A smaller value indicates a higher priority.
  5. (Optional) Configure the SSM quality level of the line clock source.
     
     
     ```
     [clock source](cmdqueryname=clock+source) ptp ssm { prc | ssua | ssub | sec | dnu | unk }
     ```
     
     By default, the SSM quality level of a line clock source is that of the clock signals transmitted from the peer device.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```