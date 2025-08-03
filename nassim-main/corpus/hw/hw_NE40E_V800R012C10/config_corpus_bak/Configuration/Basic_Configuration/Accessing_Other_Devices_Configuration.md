Accessing Other Devices Configuration
=====================================

A device can function as a client to access other devices on the network.

#### Context

To perform management, configuration, or file operations on other devices, access them using Telnet, FTP, TFTP, STelnet, SCP, or SFTP from the current device.


[Overview of Accessing Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0078.html)

You can log in to one device and access another device using Telnet, FTP, TFTP, SCP, STelnet or SFTP.

[Configuration Precautions for Access to Other Devices](../../../../software/nev8r10_vrpv8r16/user/spec/Access_to_Other_Devices_limitation.html)



[Using Telnet to Log In to Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0139.html)

Telnet is a client/server application that allows you to log in to remote devices to manage and maintain the devices.

[Using STelnet to Log In to Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0083.html)

STelnet provides secure Telnet services. You can use STelnet to log in to and manage other devices from the device that you have logged in to.

[Using TFTP to Access Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0088.html)

TFTP is used to transfer files between remote servers and local hosts. Unlike FTP, TFTP is simple and provides no authentication. TFTP applies when no complex interaction is required between clients and the server.

[Using FTP to Access Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0094.html)

You can log in to an FTP server from the device that functions as an FTP client to upload files to or download files from the server.

[Using SFTP to Access Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0101.html)

SFTP provides secure FTP services. After a device is configured as an SFTP client, the SFTP server authenticates the client and encrypts data in both directions to provide secure file transfer.

[Configuring the SFTP Client to Use the One-click File Operation Command to Perform File Operations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0203.html)

The device functions as an SFTP client and uses the one-click file operation command to upload files from the SFTP client to the SFTP server or download files from the SFTP server to the SFTP client.

[Using SCP to Access Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0125.html)

The Secure Copy Protocol (SCP) client sets up a secure connection to the SCP server so that the client can upload files to or download files from the server.

[Configuring an SSL Cipher Suite](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0063.html)

During authentication between the client and server, an encryption algorithm list is provided for SSL algorithm negotiation. This section describes how to configure an SSL cipher suite with supported encryption algorithms. Using secure algorithms enhances system security.

[Configuring and Binding an SSL Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0055.html)

SSL policies can be used to protect transmitted data from being tampered with, improving security.

[Using HTTP to Log In to Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_http_cfg_0010.html)

Hypertext Transfer Protocol (HTTP) is an application-layer protocol that transports hypertext from WWW servers to local browsers. It uses the client/server model in which requests and replies are exchanged.

[Configuring a DSCP Value for Telnet/SSH Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0162.html)

This section describes how to configure a DSCP value for Telnet/SSH packets.

[Configuration Examples for Accessing Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0108.html)

This section provides examples for configuring one device to access other devices.