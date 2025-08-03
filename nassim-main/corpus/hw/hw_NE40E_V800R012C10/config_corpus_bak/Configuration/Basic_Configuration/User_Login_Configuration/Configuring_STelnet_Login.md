Configuring STelnet Login
=========================

STelnet based on SSH2 provides secure remote access over an insecure network.

#### Usage Scenario

Large numbers of devices need to be managed and maintained on a network. You cannot connect each device to a terminal. When no reachable route exists between remote devices and a terminal, you can use Telnet to log in to the remote devices from the device that you have logged in to. Telnet provides no secure authentication mode, and data is transmitted in simple mode over TCP, which brings security risks.

STelnet is a secure Telnet service based on SSH connections. SSH provides encryption and authentication and protects devices against attacks, such as IP spoofing.

If the authentication, encryption, and key exchange algorithms used by an SSH client to log in to a device through STelnet are weak security algorithms, the device displays a message indicating that these algorithms are insecure and asking users to use more secure algorithms or upgrade the client.

You can run the [**display ssh client session**](cmdqueryname=display+ssh+client+session) command to check the authentication and encryption algorithms used by the SSH client or the [**display security risk**](cmdqueryname=display+security+risk) **feature ssh\_client** command to check the risk information and handling suggestions for the SSH client.


#### Pre-configuration Tasks

Before configuring a user to log in to devices through STelnet, you can log in to the devices through the console port and change the default configurations of the devices so that the user can remotely log in to the devices through STelnet to perform management and maintenance. To change the default configurations, complete the following tasks:

* Configure IP addresses for the management network interfaces of the devices to ensure that the routes between the user terminal and devices are reachable.
* [Configure an authentication mode and user level for VTY user interfaces](dc_vrp_basic_cfg_0038.html) to achieve remote device management and maintenance.
* [Configure VTY user interfaces to support SSH](dc_vrp_basic_cfg_0039.html), [configure an SSH user and specify a service type](dc_vrp_basic_cfg_0040.html), and [enable the STelnet server function](dc_vrp_basic_cfg_0041.html) so that the user can remotely log in to the device through STelnet.


[Configuring a User Level and Authentication Mode for VTY User Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0038.html)



[Configuring VTY User Interfaces to Support SSH](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0039.html)

STelnet is based on SSH2. When the client and the server set up a secure connection after negotiation, the client can log in to the server in the same way as using Telnet.

[Configuring an SSH User and Specifying a Service Type](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0040.html)

To use STelnet to log in to a device, configure an SSH user, configure the device to generate a local key pair, configure an authentication mode, and specify a service type for the SSH user.

[Enabling the STelnet Server Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0041.html)



[Using STelnet to Log In to a Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0135.html)

After you log in to a device through a console port and configure the device, you can use STelnet to log in to and remotely maintain the device.

[Configuring STelnet Server Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0042.html)

You can configure STelnet server parameters to ensure server reliability. STelnet server parameters include the interval at which key pairs are updated, the timeout period for SSH authentication, number of SSH authentication retries, compatibility with earlier SSH versions, and listening port number of an SSH server.

[(Optional) Configuring Session-CAR for Whitelisted SSH Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_login_cfg_0002.html)

You can configure Session-CAR for whitelisted SSH sessions to limit the rate at which packets of the whitelisted SSH sessions are sent to the SSH server. This configuration prevents non-whitelisted SSH sessions from preempting bandwidth if the SSH server encounters a traffic burst.

[(Optional) Configuring Alarm Generation and Clearance Thresholds for SSH Server Login Failures](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0146.html)

This section describes how to configure alarm generation and clearance thresholds for SSH server login failures within a specified period. This configuration facilitates user login management.

[(Optional) Configuring the Maximum Number of Connections for SSH Login to the Server Using a Single IP Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_login_cfg_0004.html)

You can configure the maximum number of SSH connections established using a single IP address. This prevents the situation where other IP addresses fail in login because an IP address has been used to establish too many connections to a server.

[(Optional) Configuring the Local Port Forwarding Service for the SSH Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0147.html)

After the local port forwarding service is enabled on the SSH server, a forwarding channel can be established between the SSH server and a host with a specified IP address and port number.

[Configuring the Keyboard-Interactive Authentication Mode for an SSH Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0150.html)

If an SSH user logs in to a device using password card authentication, keyboard-interactive authentication must be enabled for this user.

[Setting Criteria for SSH Session Key Re-negotiation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0160.html)



[Verifying the Configuration of User Login to the System Using STelnet](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0044.html)

After using STelnet to log in to a device, verify the configuration.