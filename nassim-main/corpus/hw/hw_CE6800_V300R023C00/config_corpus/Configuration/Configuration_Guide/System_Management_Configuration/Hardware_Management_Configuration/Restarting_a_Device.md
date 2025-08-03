Restarting a Device
===================

Restarting a Device

#### Context

You can restart a device either immediately or at scheduled time:

* Restart the device immediately: The device can be restarted immediately after you run the related command.
* Restart the device at scheduled time: The device can be restarted at a specified time. After the software package for next startup is configured, you can configure the device to restart at the time when the service volume is light to minimize the impact of device restart on services.

After the device restarts, it uses the software package specified for the next startup:

* If the software package specified for the next startup is damaged, the software package specified for the previous normal startup is used.
* If the software package specified for the previous normal startup does not exist on the device, the device searches the storage device for a valid software package.

![](public_sys-resources/notice_3.0-en-us.png) 

* Restarting the device will interrupt services. Only restart the device when absolutely necessary.
* If you need the current configuration to take effect after restarting the device, save the current configuration before restarting.


#### Procedure

* Restart the device immediately.
  
  
  ```
  [reboot](cmdqueryname=reboot) [ fast | save diagnostic-information ]
  ```
  
  **fast**: The device is rapidly restarted and does not prompt you to save the configuration file. If this parameter is set, unsaved configuration information will be lost.
  
  **save** **diagnostic-information**: The system will save the diagnostic information to the root directory of the storage device before it restarts.
* Restart the device at a scheduled time.
  
  
  ```
  [schedule reboot](cmdqueryname=schedule+reboot) { at exact-time [ date ] | delay interval [ force ] }
  ```
  
  **at** *exact-time*: specifies the time to restart the device.
  
  **delay** *interval*: specifies the time to wait before restarting the device. **force**: If this parameter is not specified in the command, the system compares the current configuration with the configuration file. If it detects differences, the system asks you whether you want to save the current configuration. After you have responded, the system asks you to confirm the configured restart time. Enter **Y** or **y** to make the configured restart time take effect. If this parameter is specified in the command, the system does not display any message, and the restart time takes effect. In this case, the current configuration is not compared or saved.

#### Verifying the Configuration

Run the [**display schedule reboot**](cmdqueryname=display+schedule+reboot) command to check configurations about scheduled device restart.