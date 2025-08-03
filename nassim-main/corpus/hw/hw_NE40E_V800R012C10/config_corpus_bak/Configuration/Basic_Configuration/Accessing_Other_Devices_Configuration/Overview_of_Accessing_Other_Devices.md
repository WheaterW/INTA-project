Overview of Accessing Other Devices
===================================

You can log in to one device and access another device using Telnet, FTP, TFTP, SCP, STelnet or SFTP.

As shown in [Figure 1](#EN-US_CONCEPT_0172360033__fig_dc_vrp_basic_cfg_007801), after you use the terminal emulator or Telnet program on a PC to connect to the Router, you can use Telnet, FTP, TFTP, SCP, STelnet or SFTP to access other devices from the Router functioning as a client.

**Figure 1** Accessing other devices  
![](images/fig_dc_vrp_basic_cfg_007801.png)
#### Telnet

Telnet is an application layer protocol in the TCP/IP protocol suite and provides remote login and virtual terminal services. The NE40E provides the following Telnet services:

* Telnet server: A user runs the Telnet client program on a PC to log in to the device to configure and manage the device. The device functions as a Telnet server.
* Telnet client: After using the terminal emulator or Telnet client program on a PC to connect to the device, a user runs the [**telnet**](cmdqueryname=telnet) command to log in to another device for configuration and management. The device functions as a Telnet client. In [Figure 2](#EN-US_CONCEPT_0172360033__en-us_concept_0172359754_fig_dc_vrp_basic_cfg_002501), the CE functions as both a Telnet server and a Telnet client.
  
  **Figure 2** Telnet server providing the Telnet client service  
  ![](images/fig_dc_vrp_basic_cfg_002501.png)
* Telnet service interruption
  
  **Figure 3** Usage of Telnet shortcut keys  
  ![](images/fig_dc_vrp_basic_cfg_002503.png)
  Two types of shortcut keys can be used to interrupt Telnet connections. As shown in [Figure 3](#EN-US_CONCEPT_0172360033__en-us_concept_0172359754_fig_dc_vrp_basic_cfg_002503), P1 uses Telnet to log in to P2 and then to P3. P1 is the Telnet client of P2, and P2 is the Telnet client of P3. The usage of shortcut keys is described as follows:
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

#### FTP

FTP is a standard application protocol based on the TCP/IP protocol suite. It is used to transfer files between local clients and remote servers. FTP uses two TCP connections to copy a file from one system to another. The TCP connections are usually established in client-server mode, one for control (the server port number is 21) and the other for data transmission (the server port number is 20).

* Control connection: issues commands from the client to the server and transmits replies from the server to the client, minimizing the transmission delay.
* Data connection: transmits data between the client and server, maximizing the throughput.

FTP has two file transfer modes:

* Binary mode: is used to transfer program files, such as .app, .bin, and .btm files.
* ASCII mode: is used to transfer text files, such as .txt, .bat, and .cfg files.

The device provides the following FTP functions:

* FTP client: Users can use the terminal emulator or the Telnet program to connect PCs to the device, and run the [**ftp**](cmdqueryname=ftp) command to establish a connection between the device and a remote FTP server to access and operate files on the server.
* FTP server: Users can use the FTP client program to log in to the device and operate files on the device.
  
  Before users log in, the network administrator must configure an IP address for the FTP server.


#### TFTP

TFTP is an application protocol based on User Datagram Protocol (UDP) connections. It uses the UDP port number 69 to transfer files between local hosts and remote servers. Unlike FTP, TFTP is simple, providing no authentication. It is applicable to scenarios where complicated interactions between clients and the server are not required.

TFTP supports both binary and ASCII file transfer modes, which are also supported by FTP.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Currently, the HUAWEI NE40E-M2 series supports only the binary mode for TFTP.
* Currently, the HUAWEI NE40E-M2 series can function only as a TFTP client but not a TFTP server.

TFTP transfer requests are initiated by clients:

* When a TFTP client needs to download files from the server, the client sends a read request to the TFTP server. The server sends data packets to the client, and the client acknowledges the data packets.
* When a TFTP client needs to upload a file to the server, the client sends a write request and then data to the server, and receives acknowledgments from the server.


#### STelnet

STelnet is based on SSH2.0. The client and server set up a secure connection through negotiation. STelnet enables the client to log in to the server.

* Support for both STelnet client and server functions
  
  A device can function as either an STelnet server or a client that accesses other STelnet servers.
* Enabling or disabling of the STelnet server function
  
  When the STelnet server function is not required, you can disable it globally.

#### SCP

The Secure Copy Protocol (SCP) is derived from Secure Shell version 2 (SSH2.0). A user on an SCP client must enter a correct user name, password, and private key for authentication before establishing a connection with an SCP server. After being authenticated, the client can remotely manage file transfer using SCP. The system encrypts user data using a negotiated session key.

An attacker does not have the correct private key or password and therefore fails to be authenticated. In addition, the attacker cannot decrypt data or obtain a session key even though the attacker intercepts data exchanged between clients and the server. Only specified clients and the server can decrypt data exchanged between one another, ensuring secure data transmission on the network.

* Support for both SCP client and server functions
  
  The device can function as either an SCP server or an SCP client that accesses other SCP servers.
* Enabling or disabling of the SCP server function (disabled by default)
  
  Disable the SCP server function if you do not need it. This function is configured globally.
* Supports client and server using the transparent file system. For all file operations, a unified file system is used to access files on remote boards.
* Support for recursive transfer of multiple files
  
  For example, a directory contains multiple files and sub-directories. SCP can be used to transfer all files in the directory in a batch without changing the hierarchical directory structure.

#### SFTP

SFTP uses SSH to ensure secure file transfer. On one hand, SFTP allows remote users to securely log in to the device to manage and transfer files. On the other hand, users can use the device functioning as a client to log in to a remote server and transfer files securely.

When the SFTP server or the connection between the server and the client fails, the client needs to detect the fault in time and removes the connection proactively. To address this need when the client logs in to the server through SFTP, configure an interval at which Keepalive packets are sent if no packet is received and the maximum number of times that the server does not respond to the client.

* If the client does not receive any packet within the specified period, the client sends a Keepalive packet to the server.
* If the maximum number of times that the server does not respond exceeds the specified value, the client proactively releases the connection.