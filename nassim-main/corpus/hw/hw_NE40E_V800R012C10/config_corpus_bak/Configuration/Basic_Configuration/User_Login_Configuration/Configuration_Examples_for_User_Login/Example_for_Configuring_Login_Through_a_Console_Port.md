Example for Configuring Login Through a Console Port
====================================================

In this example, configure login parameters on a PC to implement login through a console port.

#### Networking Requirements

If you have changed the default parameter values for a device's console user interface, you must accordingly change the login parameter values on a PC before you log in to the device through the console port next time.

**Figure 1** Login through a console port  
![](images/fig_dc_vrp_basic_cfg_004601.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Connect the PC to the console port on the Router.
2. Set login parameters on the PC.
3. Log in to the Router.

#### Data Preparation

Login parameters need to be configured based on the physical attributes of the console port on the router. The physical attributes include Bits per second, Data bits, Parity, Stop bits, and Flow control. For the first login, the default values of the parameters are used.

The PuTTY.exe software must have been installed on the client.


#### Procedure

1. Start the PuTTY.exe program. In the PuTTY configuration page (shown in [Figure 2](#EN-US_TASK_0172359858__en-us_task_0172359668_fig819804711612)), set the connection type to **Serial**.
   
   **Figure 2** PuTTY configuration page  
   ![](figure/en-us_image_0195774881.png)
2. Choose **Serial** in the Category navigation tree on the left of the PuTTY configuration page. In the port connection configuration page (shown in [Figure 3](#EN-US_TASK_0172359858__en-us_task_0172359668_fig175289125185)), set the communication parameters of the port to the default values of the device. (The following figure is for reference only. Use the default settings during configuration.)
   
   **Figure 3** Port connection configuration page  
   ![](figure/en-us_image_0295091930.png)
3. Click **Open**. Then the system prompts you to set an authentication password, as shown in [Figure 4](#EN-US_TASK_0172359858__en-us_task_0172359668_fig11372143315617). After the confirm the password, the system automatically saves it.
   
   **Figure 4** Login page  
   ![](figure/en-us_image_0194852587.png "Click to enlarge")
   
   After the password is set, the command prompt (for example, **<HUAWEI>**) of the user view is displayed, which indicates that you have entered the user view and can perform configurations.
   
   You can enter commands to configure the device or view its running status. Enter a question mark (?) when you need help.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The password must meet the following requirements:
   
   * The password is entered in man-machine interaction mode. The system does not display the entered password.
   * A password is a string of 8 to 16 case-sensitive characters and must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
   * Special characters exclude question marks (?) and spaces. However, spaces are allowed in the password if the password is enclosed in quotation marks.
     + Double quotation marks cannot contain double quotation marks if spaces are used in a password.
     + Double quotation marks can contain double quotation marks if no space is used in a password.
     
     For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
   
   The configured password is displayed in ciphertext in the configuration file.