Using STelnet to Log In to Other Devices
========================================

STelnet provides secure Telnet services. You can use STelnet to log in to and manage other devices from the device that you have logged in to.

#### Usage Scenario

Large numbers of devices need to be managed and maintained on a network. You cannot connect each device to a terminal. When no reachable route exists between remote devices and a terminal, you can use Telnet to log in to the remote devices from the device that you have logged in to. Telnet provides no secure authentication mode, and data is transmitted in simple mode over TCP, which brings security risks.

STelnet is a secure Telnet service over SSH connections. SSH provides encryption and authentication and protects devices against attacks, such as IP spoofing. As shown in [Figure 1](#EN-US_TASK_0172360076__fig_dc_vrp_basic_cfg_008301), the device supports the SSH function. You can log in to a remote device in SSH mode to manage and maintain the device. The device that you have logged in functions as an SSH client, and the remote device functions as an SSH server.

**Figure 1** Using STelnet to log in to the SSH server  
![](images/fig_dc_vrp_basic_cfg_008301.png)

#### Pre-configuration Tasks

Before using STelnet to log in to other devices, complete the following task:

* [Configure STelnet login](dc_vrp_basic_cfg_0037.html).


[Configuring First Login to the SSH Server (Enabling First Login on the SSH Client)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0084.html)

After first login is enabled on the SSH client (STelnet client in this case), the client does not check the validity of the RSA, DSA, SM2, or ECC public key for the SSH server when logging in to the SSH server for the first time.

[Configuring First-Time Login to Another Device Functioning as an SSH Server (with a Public Key Assigned from an SSH Client)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0085.html)

To allow an SSH client (STelnet client in this case) with first-time authentication disabled to successfully log in to an SSH server for the first time, configure the SSH client to assign an RSA, DSA, SM2, or ECC public key to the SSH server before the login.

[(Optional) Configuring the Keepalive Feature on the SSH Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0116.html)

After the keepalive feature is configured on the SSH client, the client sends keepalive packets at the configured interval to the SSH server to check whether the connection between them is normal. The keepalive feature implements fast fault detection.

[Using STelnet to Log In to Another Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0086.html)

You can use STelnet to log in to an SSH server from an SSH client to configure and manage the server.

[Verifying the Configuration of Using STelnet to Log In to Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0087.html)

After completing the configuration for using STelnet to log in to other devices, you can view mappings between SSH servers and RSA or ECC public keys on the SSH client, global configuration of SSH servers, and sessions between SSH servers and the client.