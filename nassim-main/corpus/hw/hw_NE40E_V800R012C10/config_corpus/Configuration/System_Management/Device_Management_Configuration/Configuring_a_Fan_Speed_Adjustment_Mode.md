Configuring a Fan Speed Adjustment Mode
=======================================

Configuring a Fan Speed Adjustment Mode

#### Context

You can configure a fan speed adjustment mode based on the number of working boards on a device or the board temperature.

A device supports the following fan speed adjustment modes:

* auto: The system automatically adjusts the fan speed based on the ambient temperature reported by the temperature sensor of the associated board.
* full: Fans work at the highest speed.
* minimum-percent: The minimum fan speed percentage is specified. In this mode, the system automatically adjusts the fan speed based on the ambient temperature reported by the temperature sensor of the associated board. However, the fan speed never drops below the specified minimum speed percentage.
* silent: The fan speed is automatically adjusted. However, fans work with a small speed adjustment step to control the automatically adjusted fan speed, preventing the noise from being abruptly increased due to a great fan gear change.
* denoise: The fan speed is automatically adjusted to a lower one to reduce noises generated during fan running under the same ambient temperature. Compared with the silent mode, the denoise mode achieves fast adjustment of the fan speed to the target speed.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform any of the following operations based on the device's heat dissipation requirements:
   
   
   1. Run the [**fan speed**](cmdqueryname=fan+speed) { **auto** | **full** } command to set the fan speed adjustment mode to **auto** or **full**.
   2. Run the [**fan speed**](cmdqueryname=fan+speed) **minimum-percent** *minimum-value* command to set the fan speed adjustment mode to **minimum-percent**.
   3. Run the [**fan speed**](cmdqueryname=fan+speed) **silent** command to set the fan speed adjustment mode to **silent**.
   4. Run the [**fan speed**](cmdqueryname=fan+speed) **denoise** command to set the fan speed adjustment mode to **denoise**.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Run the [**display fan**](cmdqueryname=display+fan) command to check the fan status.