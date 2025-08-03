Enabling or Disabling the Forwarding Chip Alarm-First Function
==============================================================

Enabling or Disabling the Forwarding Chip Alarm-First Function

#### Context

You can enable or disable the forwarding chip alarm-first function as required to perform different actions when a forwarding chip fault occurs.

* If the alarm-first function is disabled, an alarm is reported and the board on which the forwarding chip resides is restarted when a major fault occurs on the forwarding chip.
* If the alarm-first function is enabled, only an alarm is reported and the board on which the forwarding chip resides is not restarted when a major fault occurs on the forwarding chip.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the forwarding chip alarm-first function.
   
   
   ```
   [set system forwarding-engine alarm-first](cmdqueryname=set+system+forwarding-engine+alarm-first)
   ```
   
   By default, the forwarding chip alarm-first function is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```