Configuring a Minimum Fan Speed for the Power Module
====================================================

Configuring a Minimum Fan Speed for the Power Module

#### Context

The fan speed affects the power module temperature. By default, the system automatically adjusts the fan speed to keep the power module temperature proper. You can set a minimum fan speed for the power module so that the fan speed never falls below the minimum speed.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration takes effect only for power modules with fans. You can run the [**display device power**](cmdqueryname=display+device+power) command to check whether a power module has fans.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a minimum fan speed for the power module.
   
   
   ```
   
   [device power fan-speed min-value](cmdqueryname=device+power+fan-speed+min-value) percent percent-num
   ```
   
   By default, the minimum fan speed of the power module is 20% of the full speed.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```