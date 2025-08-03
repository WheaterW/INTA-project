Overview of User Login
======================

Users can manage or maintain a device only after logging in to the device successfully. You can log in to the device through the console port or using Telnet or STelnet.

You can configure, monitor, and maintain local or remote network devices only after configuring user interfaces, user management, and terminal services.

User interfaces provide the login portal, user management ensures login security, and terminal services offer login protocols.

[Table 1](#EN-US_CONCEPT_0172359754__tab_dc_vrp_basic_cfg_002501) describes user login modes.

**Table 1** User login modes
| Login Mode | Applicable Scenario | Remarks |
| --- | --- | --- |
| [Configuring Login Through a Console Port](dc_vrp_basic_cfg_0026.html) | When a device is powered on for the first time, you must log in to the device through the console port.  * If you cannot remotely access a device, you can locally log in to the device through the console port. * If a device fails to start, you can log in to the device to diagnose the fault through the console port. | By default, you can log in to a device directly through the console port. |
| [Configuring Telnet Login](dc_vrp_basic_cfg_0030.html) | You can log in to a device using Telnet to locally or remotely configure the device. The device authenticates users based on configured login parameters.  Telnet facilitates remote device maintenance but provides low security. | By default, you cannot log in to a device directly using Telnet. Before you use Telnet to log in to a device, you must locally log in to the device through the console port and perform the following configurations:  * Configure an IP address for the management network port on the device and ensure that a reachable route exists between the user terminal and the device. By default, the IP address of the management network port is 192.168.0.1/24. * Configure an authentication mode for the VTY user interface. * Set a user level for the VTY user interface. * Enable the Telnet service. |
| [Configuring STelnet Login](dc_vrp_basic_cfg_0037.html) | STelnet based on the Secure Shell (SSH) protocol provides information security and authentication, which protects devices against attacks, such as IP spoofing.  You can use STelnet to log in to a device to locally or remotely maintain the device. | By default, you can log in to a device directly using STelnet through the management network port (GigabitEthernet0/0/0). NOTE:  After the device is powered on, the system will automatically bind the management network port to the VPN for exclusive use (\_\_LOCAL\_OAM\_VPN\_\_) and assign the IP address 192.168.0.1/24 for the management network port.  You can configure any other IP address on the 192.168.0.0/24 network segment for the terminal and log in to the device through SSH (STelnet) to maintain the device on site. For details about the default account and password, see [List of Customized and Default Accounts and Passwords](../ne/dc_ne_sec_maintenance_0061.html).  After configuring services, change the user name and password immediately to ensure service security. The IP address of the management network port can be changed or deleted. You can shut down the management network port as required.   If you need to locally log in to the device through the console port first, perform the following configurations after login:   * Configure an IP address for the management network port on the device and ensure that a reachable route exists between the user terminal and the device. By default, the IP address of the management network port is 192.168.0.1/24. * Configure an authentication mode for the VTY user interface. * Set a user level for the VTY user interface. * Configure the VTY user interface to support SSH. * Configure an SSH user and specify STelnet as the service type. * Enable the STelnet service. |

When a user logs in to a device using one of the preceding methods, the device automatically executes a built-in batch processing file and records the execution information in the system log file.

#### Console Port

For information about a console port, see [Overview of Logging In to the System for the First Time](dc_vrp_first_login_cfg_0001.html).


#### Telnet

Telnet is an application layer protocol in the TCP/IP protocol suite and provides remote login and virtual terminal services. The NE40E provides the following Telnet services:

* Telnet server: A user runs the Telnet client program on a PC to log in to the device to configure and manage the device. The device functions as a Telnet server.
* Telnet client: After using the terminal emulator or Telnet client program on a PC to connect to the device, a user runs the [**telnet**](cmdqueryname=telnet) command to log in to another device for configuration and management. The device functions as a Telnet client. In [Figure 1](#EN-US_CONCEPT_0172359754__fig_dc_vrp_basic_cfg_002501), the CE functions as both a Telnet server and a Telnet client.
  
  **Figure 1** Telnet server providing the Telnet client service  
  ![](images/fig_dc_vrp_basic_cfg_002501.png)
* Telnet service interruption
  
  **Figure 2** Usage of Telnet shortcut keys  
  ![](images/fig_dc_vrp_basic_cfg_002503.png)
  Two types of shortcut keys can be used to interrupt Telnet connections. As shown in [Figure 2](#EN-US_CONCEPT_0172359754__fig_dc_vrp_basic_cfg_002503), P1 uses Telnet to log in to P2 and then to P3. P1 is the Telnet client of P2, and P2 is the Telnet client of P3. The usage of shortcut keys is described as follows:
  + **Ctrl\_]**: Instructs the server to disconnect a Telnet connection.
    
    When the network works properly, entering the shortcut key **Ctrl\_]** causes the Telnet server to interrupt the current Telnet connection.
    
    For example, after you enter **Ctrl\_]** on P3, the **<P2>** prompt is displayed.
    
    ```
    <P3> Select Ctrl_] to return to the prompt of P2
    ```
    ```
    The connection was closed by the remote host.
    ```
    ```
    <P2>
    ```
    
    After you enter **Ctrl\_]** on P2, the **<P1>** prompt is displayed.
    
    ```
    <P2> Ctrl_]
    ```
    ```
    The connection was closed by the remote host.
    ```
    ```
    <P1>
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If the network connection is disconnected, shortcut keys do not take effect.
  + **Ctrl\_K**: Instructs the client to disconnect the connection.
    
    When the server fails and the client is unaware of the failure, the server does not respond to the client's input. If you enter **Ctrl\_K**, the Telnet client interrupts and quits the Telnet connection.
    
    For example, enter **Ctrl\_K** on P3 to quit the Telnet connection.
    
    ```
    <P3> Ctrl_K
    ```
    ```
    <P1>
    ```
    ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
    
    When the number of remote login users reaches the maximum number of VTY user interfaces, the system prompts subsequent users with a message, indicating that all user interfaces are in use and no more Telnet connections are allowed.

#### STelnet

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, a device running SSH1 or SSH2 can function as an SSH server. Only devices running SSH2 can function as SSH clients. STelnet is based on SSH2. When the client and the server set up a secure connection after negotiation, the client can log in to the server in the same way as using Telnet.

Telnet access is not secure because there is no authentication method and the data transmitted across Transmission Control Protocol (TCP) connections is in plaintext. As a result, the system is vulnerable to denial of service (DoS), IP address spoofing, and route spoofing attacks.

SSH provides secure remote access on an insecure network by supporting the following functions:

* Supports key authentication. The public and private keys are generated according to the encryption principle of the asymmetric encryption system, which helps implement secure key exchange and ensures secure sessions.
* Encrypts transmitted data.
* When the SSH client communicates with the server, the user name and password are encrypted to prevent the password from being intercepted.

A device serving as an SSH server can accept connection requests from multiple SSH clients. The device can also serve as an SSH client, helping users establish SSH connections with an SSH server. This allows users to use SSH to log in to remote devices from the local device.

* Local connection
  
  As shown in [Figure 3](#EN-US_CONCEPT_0172359754__fig_dc_vrp_basic_cfg_002504), an SSH channel is established for a local connection.
  
  **Figure 3** Establishing an SSH channel on a local area network (LAN)  
  ![](images/fig_dc_vrp_basic_cfg_002504.png)
* Wide area network (WAN) connection
  
  As shown in [Figure 4](#EN-US_CONCEPT_0172359754__fig_dc_vrp_basic_cfg_002505), an SSH channel is established for a connection on a WAN.
  
  **Figure 4** Establishing an SSH channel on a WAN  
  ![](images/fig_dc_vrp_basic_cfg_002505.png)