Using FTP to Operate Files
==========================

FTP is used to transfer files between local clients and remote servers.

#### Usage Scenario

As devices operate stably and are deployed on a large scale, more and more devices need to be maintained and upgraded remotely. Online software upgrade, a new upgrade method by loading software packages remotely, facilitates remote online upgrades, reduces upgrade expenditures, shortens the time that customers wait for upgrades, and improves customers' satisfaction. The delay, packet loss, and jitter affect data transmission on networks. To ensure the quality of online upgrade and data transmission, use FTP to perform online upgrades and transfer files based on TCP connections.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Use the SFTP protocol because this protocol is not secure.



#### Pre-configuration Tasks

Before using FTP to operate files, configure a reachable route between a terminal and a device.


[Configuring a Local FTP User](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0007.html)

You can configure authentication information, authorization mode, and authorized directory to prevent unauthorized FTP users from accessing a specified directory.

[(Optional) Specifying a Listening Port Number for the FTP Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0008.html)

After a listening port number is specified for the FTP server, only users who know the new port number can access the server, ensuring security.

[Enabling the FTP Server Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0009.html)

Before using FTP to operate files, enable the FTP server function on a device.

[Configuring FTP Server Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0010.html)

Configuring proper parameters for the FTP server ensures device security and maximizes resource usage efficiency.

[(Optional) Configuring Session-CAR for Whitelisted FTP Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0029.html)

You can configure Session-CAR for whitelisted FTP sessions to limit the rate at which packets of the whitelisted FTP sessions are sent to the FTP server. This configuration prevents non-whitelisted FTP sessions from preempting bandwidth if the FTP server encounters a traffic burst.

[(Optional) Configuring FTP Access Control](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0011.html)

An ACL can be configured to allow only specified clients to access an FTP server.

[(Optional) Configuring the IP Address Locking Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ftp_cfg_0147.html)

To improve device security and protect user passwords against attacks, configure the FTP-based IP address locking function.

[Using FTP to Access a Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0012.html)

After an FTP server is configured, you can access the server from a PC by using FTP to manage files on the server.

[Using FTP Commands to Operate Files](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0013.html)

After logging in to a device that functions as an FTP server by using FTP, you can upload files to or download files from the device, and manage device directories.

[Verifying the Configuration of Using FTP to Operate Files](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0014.html)

After completing the configuration of using FTP to operate files, you can view the configuration and status of the FTP server as well as information about logged-in FTP users.