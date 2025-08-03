Configuring the Maximum Output SSM Quality Level of Clock Signals
=================================================================

Configuring the Maximum Output SSM Quality Level of Clock Signals

#### Context

By default, the clock signals transmitted to downstream devices use their actual SSM quality level. To reduce the probability of downstream devices synchronizing with poor-quality clock signals, you can set the maximum output SSM quality level of the clock signals transmitted to downstream devices to be lower than the actual SSM quality level.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the maximum output SSM quality level of clock signals.
   
   
   ```
   [clock](cmdqueryname=clock) max-out-ssm { prc | sec | ssua | ssub }
   ```
   
   
   
   By default, the maximum output SSM quality level of clock signals is not configured. That is, the clock signals transmitted to downstream devices use their actual SSM quality level.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```