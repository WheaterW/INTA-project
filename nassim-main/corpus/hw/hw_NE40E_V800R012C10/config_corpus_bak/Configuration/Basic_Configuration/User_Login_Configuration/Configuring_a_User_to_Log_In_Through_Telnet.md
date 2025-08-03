Configuring a User to Log In Through Telnet
===========================================

This section describes how to configure a user to remotely log in to devices through Telnet to perform management and maintenance.

#### Usage Scenario

If one or more devices need to be configured and managed, you do not need to connect each of the devices to the user terminal for local maintenance. If you have obtained the IP addresses of the devices and it is not the first time for you to log in to the devices, use Telnet to log in to the devices from the user terminal and perform remote device configuration. This method allows you to maintain multiple devices using a single user terminal, greatly facilitating operations.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Device IP addresses must be preconfigured through the console port.

You are advised to use STelnet because Telnet is insecure.



#### Pre-configuration Tasks

Before configuring a user to log in to devices through Telnet, log in to the devices through the console port and change the default configurations of the devices so that the user can remotely log in to the devices through Telnet to perform management and maintenance. To change the default configurations, complete the following tasks:

* Configure IP addresses for the management network interfaces of the devices to ensure that the routes between the user terminal and devices are reachable.
* [Configure an authentication mode and user level for VTY user interfaces](dc_vrp_basic_cfg_0031.html) to achieve remote device management and maintenance.
* [Enable the Telnet server function](dc_vrp_basic_cfg_0033.html) so that users can remotely log in to devices through Telnet.


[Configuring a User Level and Authentication Mode for the VTY User Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0031.html)

To use Telnet to log in to a device for remote management and maintenance, you must first log in to the device through the console port and change the user level and authentication mode.

[Enabling the Telnet Server Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0033.html)

Before a user terminal establishes a Telnet connection with a device, log in to the device through the console port to enable the Telnet server function on the device. You can then use Telnet to remotely log in to the device.

[Using Telnet to Log In to the System](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0035.html)

After you log in to a device through a console port and configure the device, you can use Telnet to log in to and remotely maintain the device.

[Configuring Telnet Server Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0034.html)

Properly setting parameters for a Telnet server improves network security. Telnet server parameters include a listening port number and source interface.

[(Optional) Configuring Whitelist Session-CAR for Telnet](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_login_cfg_0001.html)

You can configure whitelist session-CAR for Telnet to limit the rate of Telnet packets based on sessions. This configuration prevents Telnet server sessions from preempting bandwidth if the Telnet server encounters a traffic burst.

[(Optional) Configuring Telnet Access Control](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0122.html)

An ACL can be configured to allow only specified clients to access a Telnet server.

[(Optional) Enabling the IP Address Blocking Function for Telnet Connections](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0143.html)

The IP address blocking function for Telnet connections prevents IP addresses that fail to be authenticated from logging in to a device through Telnet. If this function is disabled, the device is vulnerable to network attacks.

[(Optional) Configuring Alarm Generation and Clearance Thresholds for Telnet Server Login Failures](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0145.html)

This section describes how to configure alarm generation and clearance thresholds for Telnet server login failures within a specified period. This configuration facilitates user login management.

[(Optional) Configuring the Maximum Number of Connections for Telnet Login to the Server Using a Single IP Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_login_cfg_0003.html)

You can configure the maximum number of Telnet connections established using a single IP address. This prevents the situation where other IP addresses fail in login because an IP address has been used to establish too many connections to a server.

[Verifying the Configuration of User Login to the System Using Telnet](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0036.html)

After using Telnet to log in to a device, you can view information about the current user interface, every user interface, and established TCP connections.