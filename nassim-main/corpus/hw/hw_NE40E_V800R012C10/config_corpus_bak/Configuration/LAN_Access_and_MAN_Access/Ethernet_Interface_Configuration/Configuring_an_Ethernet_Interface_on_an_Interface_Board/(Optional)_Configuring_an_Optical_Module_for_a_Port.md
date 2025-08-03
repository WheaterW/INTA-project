(Optional) Configuring an Optical Module for a Port
===================================================

(Optional)_Configuring_an_Optical_Module_for_a_Port

#### Context

Wavelengths play a major role in the transmission quality and efficiency of an optical fiber. You can set the wavelength to enable an optical fiber to work in different transmission modes. Before setting the center wavelength for a wavelength-tunable optical module with a 50 GHz channel spacing, run the **display wavelength-map** command to view the channel corresponding to the center wavelength to be set. Then, run the [**wavelength-channel**](cmdqueryname=wavelength-channel) *channel-num* command to specify the channel number corresponding to the center wavelength of the optical module. For a wavelength-tunable optical module with channel spacing other than 50 GHz, you need to run three commands. Specifically, run the **display wavelength-capability** command to check the wavelength and frequency capabilities of the optical module on a specified interface, run the [**wavelength-channel**](cmdqueryname=wavelength-channel) [**frequency**](cmdqueryname=frequency) *frequency-number* command to set the frequency of the optical module, and run the [**wavelength-channel**](cmdqueryname=wavelength-channel) [**wavelength**](cmdqueryname=wavelength) *wave-number* command to set the wavelength of the optical module.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Set the optical module of the interface.
   
   
   * To configure the channel number corresponding to the center wavelength of the optical module, run the **wavelength-channel** *channel-num* [ **[**frequency-spacing**](cmdqueryname=frequency-spacing)** { **100GHz** | **75GHz** } ] command.
   * To configure the frequency and frequency spacing of the optical module, run the [**wavelength-channel**](cmdqueryname=wavelength-channel) [**frequency**](cmdqueryname=frequency) *frequency-number* [ **[**frequency-spacing**](cmdqueryname=frequency-spacing)** { **100GHz** | **75GHz** } ] command.
   * To configure the wavelength and frequency spacing of the optical module, run the [**wavelength-channel**](cmdqueryname=wavelength-channel) [**wavelength**](cmdqueryname=wavelength) *wave-number* [ **frequency-spacing** { **100GHz** | **75GHz** } ] command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.