Logging In to a Device Through the Management Network Port
==========================================================

If a device is powered on for the first time, you can use the management network port to log in to it in SSH mode.

#### Context

On a network with low security, you can use a terminal to connect to a device through SSH, which provides secure information guarantee and a powerful authentication function to protect the device against attacks such as IP spoofing. By default, you can log in to a device directly through the management network port.

The following procedure is based on the condition that PuTTY has been installed on the client.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After a device is powered on, the management network port (GigabitEthernet0/0/0) is automatically bound to a reserved VPN (**\_\_LOCAL\_OAM\_VPN\_\_**) and assigned the IP address 192.168.0.1/24.

You can configure another IP address on the 192.168.0.0/24 network segment for the terminal and log in to the device through SSH for local device maintenance.

If the device has been connected to the DHCP server before startup, the default address of the management network port may be overwritten or lost.

After configuring services on the device, change the username and password immediately to ensure service security. The IP address of the management network port can be changed or deleted, and the port can be shut down as required.



#### Procedure

1. Configure an SSH client.
   
   
   
   Start PuTTY. The client configuration page is displayed, as shown in [Figure 1](#EN-US_TASK_0267354676__fig_dc_vrp_basic_cfg_013512). In the **Host Name (or IP address)** text box, enter the IP address of the SSH server.
   
   **Figure 1** SSH client configuration page  
   ![](figure/en-us_image_0288275851.png)
2. Click **Open**. If the connection is normal, the system prompts you to enter the username and password, as shown in [Figure 2](#EN-US_TASK_0267354676__fig1361613567216).
   
   **Figure 2** Login authentication page for the SSH client  
   ![](figure/en-us_image_0288263265.png)
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Enter the default username and password of the device. For details, see [List of Customized and Default Accounts and Passwords](../ne/dc_ne_sec_maintenance_0061.html).
   
   For details about how to log in to the device through STelnet by configuring the console port, see [Configuring STelnet Login](dc_vrp_basic_cfg_0037.html).
3. If an unconfigured device starts and the .defcfg file does not contain any preset account, the first-login process is triggered during STelnet login. In this case, the system prompts you to create a username and set a password, as shown in [Figure 3](#EN-US_TASK_0267354676__fig17311138192816).
   
   
   
   The [**user-security-policy first-login-linkage enable**](cmdqueryname=user-security-policy+first-login-linkage+enable) command can be used to restrict the creation of users during the first-login process to only the console port or STelnet mode (not both). This command can take effect only if it has been added to the configuration file. It is delivered during device startup and cannot be executed by users who have logged in to the device.
   
   
   
   **Figure 3** First-login process page  
   ![](figure/en-us_image_0288272338.png "Click to enlarge")
   
   
   
   After the user is created, the connection is torn down. You need to log in to the device as the new user.