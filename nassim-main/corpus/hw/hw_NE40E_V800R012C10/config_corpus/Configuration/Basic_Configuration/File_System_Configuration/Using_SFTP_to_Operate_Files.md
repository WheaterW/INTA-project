Using SFTP to Operate Files
===========================

SFTP enables you to log in to a remote device securely to manage files. SFTP improves data transmission security.

#### Usage Scenario

As the device deployment scale increases, more and more devices need to be maintained and upgraded remotely. Online software upgrade, a new upgrade method by loading software packages remotely, facilitates remote upgrades, reduces upgrade costs, shortens the time that customers wait for upgrades, and improves customers' satisfaction. FTP is usually used to transmit data for online upgrades. FTP transmits data and even user names and passwords in plaintext, bringing security risks.

SFTP resolves the security issue. It enables you to securely log in to a remote device for file management, improving data transmission security. You can use SFTP to log in to a remote device from a device functioning as a client for secure file transfer and online upgrades.


#### Pre-configuration Tasks

Before using SFTP to operate files, configure a reachable route between a terminal and a device.


[Configuring an SSH User and Specifying a Service Type](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0016.html)

To allow users to log in to a device through SFTP, configure an SSH user, generate a local key pair, configure a user authentication mode, and specify a service type for the SSH user.

[Enabling the SFTP Service](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0017.html)

Before using SFTP to access a device, enable the SFTP service on the device.

[Configuring SFTP Server Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0018.html)

You can configure a device to support the SSH protocol of earlier versions, configure or change the listening port number of an SFTP server, and set an interval at which key pairs are updated.

[(Optional) Configuring Session-CAR for Whitelisted SSH Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_login_cfg_0002_1.html)

You can configure Session-CAR for whitelisted SSH sessions to limit the rate at which packets of the whitelisted SSH sessions are sent to the SSH server. This configuration prevents non-whitelisted SSH sessions from preempting bandwidth if the SSH server encounters a traffic burst.

[Configuring an Authorized SFTP Server Directory](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0028.html)

This topic describes how to configure an authorized SFTP server directory for SSH users.

[Using SFTP to Log In to the System](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0019.html)

After the configuration is complete, you can use SFTP to log in to the device for file management.

[Using SFTP Commands to Operate Files](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0020.html)

After logging in to the SFTP server, you can manage directories and files on the server.

[Verifying the Configuration of SFTP-based File Operations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vfm_cfg_0021.html)

After completing the configuration of SFTP-based file operations, view information about SSH users and the configuration of the SSH server.