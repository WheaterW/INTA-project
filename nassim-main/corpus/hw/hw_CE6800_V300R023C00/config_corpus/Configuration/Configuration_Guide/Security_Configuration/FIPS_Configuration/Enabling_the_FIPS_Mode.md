Enabling the FIPS Mode
======================

Enabling the FIPS Mode

#### Context

With FIPS mode enabled, the device has stricter security requirements and checks whether the algorithms used by cryptographic modules comply with FIPS. This ensures the proper running of cryptographic modules.

![](public_sys-resources/note_3.0-en-us.png) 

Enabling the FIPS mode on the device will clear the configuration file for next startup and immediately restart the device. Therefore, exercise caution when enabling the FIPS mode.

After the FIPS mode is enabled, the weak security algorithm/protocol feature package can be installed on the device, but does not take effect. That is, the weak security algorithm/protocol cannot be used.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the FIPS mode.
   
   
   ```
   [fips-mode enable](cmdqueryname=fips-mode+enable)
   ```
   
   By default, the FIPS mode is disabled on the device.

#### Verifying the Configuration

* Run the [**display fips-mode**](cmdqueryname=display+fips-mode) command in the system view to check whether the FIPS mode is enabled on the device.
* Run the [**display fips-mode algorithm self-check**](cmdqueryname=display+fips-mode+algorithm+self-check) command in the system view to check whether the algorithms provided by cryptographic modules of the device comply with FIPS.
* Run the [**display fips-mode finite-state**](cmdqueryname=display+fips-mode+finite-state) command in the system view to check the historical records of FIPS mode status changes.