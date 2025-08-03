Verifying DHCP-based ZTP with a Controller
==========================================

Verifying DHCP-based ZTP with a Controller

#### Context

During DHCP-based ZTP with a controller, you can perform the following operations to check whether ZTP is complete:

* Configure a Syslog server to upload user logs recorded during the ZTP process to the NMS.
* Check the device management status on the controller.

#### Procedure

1. The device completes the ZTP process in about 15 minutes after it is powered on. You can then log in to the device to check whether the startup files are the required ones.
   
   
   ```
   [display startup](cmdqueryname=display+startup)
   ```

#### Follow-up Procedure

If deployment fails, analyze ZTP logs on the device to determine the cause. ZTP logs are saved in the file named **ztp\_*YYYYMMHHMMSS*.log** in the **flash:/** directory.