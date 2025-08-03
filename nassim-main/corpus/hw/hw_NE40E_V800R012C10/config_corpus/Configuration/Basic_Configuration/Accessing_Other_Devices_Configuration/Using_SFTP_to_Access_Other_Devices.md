Using SFTP to Access Other Devices
==================================

SFTP provides secure FTP services. After a device is configured as an SFTP client, the SFTP server authenticates the client and encrypts data in both directions to provide secure file transfer.

#### Usage Scenario

Based on SSH, SFTP ensures that users log in to a remote device securely to manage and transfer files, enhancing secure file transfer. Because the device can function as an SFTP client, you can log in to a remote SSH server from the device to transfer files securely.

#### Pre-configuration Tasks

Before using SFTP to access other devices, complete the following tasks:

1. [Configure an SSH user and specify a service type.](dc_vrp_vfm_cfg_0016.html)
2. [Enable the SFTP server function.](dc_vrp_vfm_cfg_0017.html)
3. [(Optional) Configure SFTP server parameters.](dc_vrp_vfm_cfg_0018.html)



[(Optional) Configuring a Source Address for the SFTP Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0102.html)

You can configure a source address for an SFTP client and use the source address to establish an SFTP connection, ensuring file transfer security.

[Configuring First Login to the SSH Server (Enabling First Login on the SSH Client)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0103.html)

After first login is enabled on an SSH client (SFTP client in this case), the client does not check the validity of the RSA, DSA, SM2, ECC public key for the SSH server when logging in to the SSH server for the first time.

[Configuring First-Time Login to Another Device Functioning as an SSH Server (with a Public Key Assigned from an SSH Client)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0104.html)

To allow an SSH client (SFTP client in this case) with first-time authentication disabled to successfully log in to an SSH server for the first time, configure the SSH client to assign an RSA, DSA, SM2, or ECC public key to the SSH server before the login.

[Using SFTP to Log In to Another Device Functioning as an SSH Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0105.html)

You can log in to an SSH server from an SSH client through SFTP.

[Using SFTP Commands to Operate Files](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0106.html)

You can manage directories and files of the SSH server through the SFTP client and view help for all SFTP commands on the SFTP client.

[Verifying the Configuration of Using SFTP to Access Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0107.html)

After completing the configuration of using SFTP to access other devices, you can view the source address of the SSH client, mappings between SSH servers and RSA or ECC public keys on the client, global configurations of the SSH servers, and sessions between the SSH servers and the client.