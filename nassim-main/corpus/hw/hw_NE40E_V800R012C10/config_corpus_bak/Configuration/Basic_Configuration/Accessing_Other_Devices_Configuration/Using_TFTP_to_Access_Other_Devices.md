Using TFTP to Access Other Devices
==================================

TFTP is used to transfer files between remote servers and local hosts. Unlike FTP, TFTP is simple and provides no authentication. TFTP applies when no complex interaction is required between clients and the server.

#### Usage Scenario

In the TCP/IP protocol suite, FTP is most commonly used to transfer files. However, FTP brings complex interactions between terminals and servers, which is hard to implement on terminals that do not run advanced operating systems. TFTP is designed for file transfer that does not require complex interactions between terminals and servers. It is simple, requiring a few costs. TFTP can be used only for simple file transfer without authentication.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The HUAWEI NE40E-M2 series can function only as a TFTP client.



#### Pre-configuration Tasks

Before using TFTP to access other devices, [configure user login](dc_vrp_basic_cfg_0024.html).


[Configuring a Source Address for a TFTP Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0089.html)

You can configure a source address for a TFTP client and use the source address to establish a TFTP connection, ensuring file transfer security.

[Configuring TFTP Access Control](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0090.html)

An ACL can be configured to allow the TFTP client to access specified TFTP servers.

[Using TFTP to Download Files from Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0091.html)

You can run the **tftp** command to download files from a remote server to the local device.

[Using TFTP to Upload Files to Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0092.html)

You can run the **tftp** command to upload files from the local device to a remote server.

[Verifying the Configuration of Using TFTP to Access Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0093.html)

After completing the configuration for using TFTP to access other devices, you can view the source address of the TFTP client and configured ACL rules.