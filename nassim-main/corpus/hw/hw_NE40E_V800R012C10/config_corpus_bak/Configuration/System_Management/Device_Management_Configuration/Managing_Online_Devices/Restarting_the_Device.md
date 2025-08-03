Restarting the Device
=====================

After the software of a device is upgraded, restart the device to validate the configurations.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Be cautious to use the [**reboot**](cmdqueryname=reboot) command because it can break down the entire network for a short period. In addition, check whether configuration files need be saved before restarting the device.

In VS mode, this section applies only to the admin VS.


#### Procedure

1. Run the [**reboot**](cmdqueryname=reboot) command to start the device immediately.
   
   
   
   After the [**reboot**](cmdqueryname=reboot) command is run, the system checks whether the current configuration is consistent with the configuration saved in the configuration file. If the configuration is inconsistent with the configuration saved in the configuration file, the system prompts you to save the current configuration. The system then prompts you to confirm whether to save the current configuration in the configuration file to be activated next time.