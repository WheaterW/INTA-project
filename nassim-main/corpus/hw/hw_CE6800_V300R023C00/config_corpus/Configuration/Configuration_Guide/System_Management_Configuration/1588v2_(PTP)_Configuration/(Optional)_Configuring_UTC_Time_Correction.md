(Optional) Configuring UTC Time Correction
==========================================

(Optional) Configuring UTC Time Correction

#### Context

Universal Coordinated Time (UTC) is Greenwich Mean Time (GMT) which is displayed on a 1588v2 device. There is a fixed time offset between UTC and International Atomic Time (TAI), and the International Earth Rotation Service (IERS) advertises this offset on a regular basis.

When tracking an external clock source, a 1588v2 device uses the time offset provided by the external clock source by default. If the external clock signals are lost, the 1588v2 device continues to use the previous time offset, which may change, leading to inaccurate time signals on a 1588v2 network.

You only need to configure the time offset between UTC and TAI on the grandmaster clock of a 1588v2 network, as the time on other 1588v2 devices will remain consistent with that of the grandmaster clock.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an accumulative offset between UTC and TAI.
   
   
   ```
   [ptp utc-offset](cmdqueryname=ptp+utc-offset) utc-offset
   ```
   
   
   
   By default, the accumulated offset between UTC and TAI is 0.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```