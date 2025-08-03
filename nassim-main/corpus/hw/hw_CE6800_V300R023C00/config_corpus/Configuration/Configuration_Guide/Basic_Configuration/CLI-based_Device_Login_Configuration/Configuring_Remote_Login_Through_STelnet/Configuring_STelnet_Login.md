Configuring STelnet Login
=========================

Configuring STelnet Login

#### Prerequisites

Before configuring STelnet login, you have completed the following tasks:

* Ensure that there are reachable routes between the terminal and the device.
* Install the SSH client software on the terminal.

![](public_sys-resources/note_3.0-en-us.png) 

SSHv2 is more secure than SSHv1, and is therefore recommended for STelnet login.



#### Default Settings

**Table 1** Default settings for configuring STelnet login
| Parameter | Default Setting |
| --- | --- |
| STelnet server function | Disabled |



#### Procedure

1. **Enable the STelnet server function and configure related parameters.**
   
   
   
   For details, see [Configuring the SSH Server Function and Related Parameters](galaxy_ssh_cfg_0009.html) in Configuration Guide > Security Configuration.
2. **Configure the VTY user interface for SSH users to log in to the device.**
   
   
   
   For details, see [Configuring a VTY User Interface to Support SSH](galaxy_ssh_cfg_0010.html) in Configuration Guide > Security Configuration.
3. **Configure SSH user information.**
   
   
   
   For details, see [Configuring an SSH User](galaxy_ssh_cfg_0011.html) in Configuration Guide > Security Configuration.
4. **Log in to the device using STelnet.**
   
   
   
   Use the SSH client software to log in to the device using STelnet from a terminal. The third-party software OpenSSH and Windows CLI are used in the following example.
   
   Access the Windows CLI and run the OpenSSH commands to connect to the device. (The following information is for reference only.)
   
   ```
   C:\Users\User1>ssh admin@10.136.195.11
   admin@10.136.195.11's password:
   Info: The max number of VTY users is 21, the number of current VTY users online is 1, and total number of terminal users online is 1.
         The current login time is 2020-12-15 14:23:00.
   <HUAWEI>
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The Windows CLI can identify OpenSSH commands only when OpenSSH is installed on the terminal.
   * For details about how to install OpenSSH, see the OpenSSH installation guide.
   * To use OpenSSH to connect to the device using STelnet, run the OpenSSH commands. For details about OpenSSH commands, see the OpenSSH help.

#### Verifying the Configuration

* Run the [**display ssh user-information**](cmdqueryname=display+ssh+user-information) [ *username* ] command to check SSH user information on the SSH server. If no SSH user is specified, this command displays information about all SSH users on the SSH server.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **status** command to check global configuration information about the SSH server.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **session** command on the SSH server to check the sessions between the SSH server and the SSH clients.