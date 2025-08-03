Verifying DHCP-based ZTP Without a Controller
=============================================

Verifying DHCP-based ZTP Without a Controller

#### Procedure

1. The device completes the ZTP process in about 15 minutes after it is powered on. You can then log in to the device to check whether the startup files are the required ones.
   
   
   ```
   [display startup](cmdqueryname=display+startup)
   ```

#### Follow-up Procedure

If deployment fails, analyze ZTP logs on the device to determine the cause. ZTP logs are saved in the file named **ztp\_*YYYYMMHHMMSS*.log** in the **flash:/** directory.