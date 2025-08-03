(Optional) Configuring Power Locking and Gain Locking for an Optical Amplifier Module
=====================================================================================

You can configure power locking and gain locking for an optical amplifier module to amplify the optical power.

#### Context

Perform the following steps on the Router where power locking and gain locking need to be configured for an optical amplifier module.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following configurations as required.
   
   
   * Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of a specified interface.
3. Run [**work-mode**](cmdqueryname=work-mode) { **agc** *agc-value* |**apc** *apc-value* }
   
   
   
   Automatic gain control and automatic power control values are configured for channels of the optical amplifier module.
   
   If the optical amplifier module has only one optical amplifier, channel 0 can be configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When configuring an OA at the transmit end, run the [**work-mode apc**](cmdqueryname=work-mode+apc) *apc-value* command to configure an automatic power control (APC) value for the optical module of the OA. In this case, the transmit optical power of the OA is locked at the APC value configured using *apc-value*.
   
   When configuring an OA at the receive end, run the [**work-mode agc**](cmdqueryname=work-mode+agc) *agc-value* command to configure an automatic gain control (AGC) value for the optical module of the OA. In this case, the transmit optical power of the OA is equal to the sum of the receive optical power of the OA and the AGC value configured using *agc-value*.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.