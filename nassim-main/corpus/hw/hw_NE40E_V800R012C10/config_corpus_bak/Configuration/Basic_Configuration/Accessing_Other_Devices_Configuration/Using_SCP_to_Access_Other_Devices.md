Using SCP to Access Other Devices
=================================

The Secure Copy Protocol (SCP) client sets up a secure connection to the SCP server so that the client can upload files to or download files from the server.

#### Usage Scenario

SCP is a secure file transfer method based on SSH2.0 that supports file upload or download in batches.

#### Pre-configuration Tasks

Before using SCP to access other devices, ensure that the route between the SCP client and server is reachable.


[Configuring the SCP Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0126.html)

This section describes how to configure the SCP server to establish a secure connection to the SCP client to implement secure remote access.

[Configuring an SCP Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0127.html)

After a secure connection is established between an SCP client and server through negotiation, the client can upload files to the server or download files from it.

[Verifying the Configuration of Using SCP to Access Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0128.html)

After completing the configuration for using SCP to access other devices, you can view the source IP address of the SCP client.