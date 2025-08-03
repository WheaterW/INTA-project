Configuring the Center Wavelength of a WDM Optical Module
=========================================================

Configuring the Center Wavelength of a WDM Optical Module

#### Context

A wavelength determines transmission quality and efficiency of an optical fiber, and it can be set for optical transmission as required to enable optical fibers to work in different transmission modes. The system has 80 channels, each corresponding to a wavelength and frequency. You can set the center wavelength of a WDM optical module by setting the channel ID, frequency, or wavelength.

![](public_sys-resources/note_3.0-en-us.png) 

This function can be configured only on ports where WDM optical modules are installed or pre-configured.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Set the center wavelength of the WDM optical module.
   
   
   * By setting the channel ID
     ```
     [wavelength-channel](cmdqueryname=wavelength-channel) channel-number
     ```
     
     Run the [**display wavelength-map**](cmdqueryname=display+wavelength-map) command to check the mapping between the channel ID and center wavelength of the WDM optical module, and then set the corresponding channel ID.
   * By setting the frequency
     ```
     [wavelength-channel](cmdqueryname=wavelength-channel) frequency frequency_value
     ```
   * By setting the wavelength
     ```
     [wavelength-channel](cmdqueryname=wavelength-channel) wavelength wavelength_value
     ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display wavelength-map**](cmdqueryname=display+wavelength-map) command to check the mapping between the channel ID and center wavelength of the WDM optical module.