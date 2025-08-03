Configuring the Fan Speed
=========================

Configuring the Fan Speed

#### Context

The fan speed can be adjusted to reduce either the device temperature or the fan noise.

Two modes are available for fan speed adjustment:

* Manual mode: The fan speed is adjusted through the CLI.
* Automatic mode: The fan speed is automatically adjusted based on the device temperature. This mode is enabled by default or after the fan speed configuration is removed.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration does not take effect for the power module. To configure a minimum fan speed for the power module, run the **device power fan-speed min-value** command in the system view.




#### Procedure

* Manual mode
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Manually configure the fan speed.
     
     
     ```
     [device fan speed](cmdqueryname=device+fan+speed) percent percent-number 
     ```
     
     By default, fans work in automatic speed adjustment mode.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Automatic mode
  
  
  
  In automatic mode, you can set a minimum fan speed so that the fan speed will not be lower than the minimum speed.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the minimum fan speed.
     
     
     ```
     [device fan speed min-value](cmdqueryname=device+fan+speed+min-value) percent percent-number 
     ```
     
     By default, the minimum fan speed is not set.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display device fan**](cmdqueryname=display+device+fan) command to check the **Speed** field, which indicates the current fan speed.