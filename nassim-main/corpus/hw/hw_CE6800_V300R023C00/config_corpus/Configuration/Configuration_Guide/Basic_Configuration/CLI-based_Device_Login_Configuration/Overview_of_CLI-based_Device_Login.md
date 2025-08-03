Overview of CLI-based Device Login
==================================

When a device functions as a server, you can log in to the device through the console port, Telnet, or STelnet. When a device functions as a client, you can log in to a server from the device through Telnet or STelnet.

To manage and maintain the device either locally or remotely, you need to configure the user interface, user management information, and terminal services before login.

* User interface: provides the login entry.
* User management information: ensures login security.
* Terminal services: support login protocols.

You can log in to the device using one of the modes described in [Table 1](#EN-US_CONCEPT_0000001513173038__tab_dc_cfg_login_000101) to configure and manage the device.

**Table 1** User login modes
| Login Mode | Advantage | Disadvantage | Application Scenario | Description |
| --- | --- | --- | --- | --- |
| [Configuring Local Login Through a Console Port](vrp_login_cfg_0005.html) | A dedicated console cable is used for device control. | You cannot remotely log in to the device. | * The device is configured for the first time. * Remote login to the device is unavailable. * If the device fails to start, you can access the BootLoader menu for device diagnosis or upgrade. | Login through a console port is the basis for other login modes.  By default, you can log in to the device through a console port and use command at privilege level 3. |
| [Configuring Remote Login Through Telnet](vrp_login_cfg_0008.html) | You can log in to devices remotely using Telnet for management and maintenance without the need to connect a terminal to each device, thereby facilitating operations. | Data is transmitted using TCP in plain text, posing potential security risks. | If you need to configure the device remotely after connecting a terminal to the network, log in to the device using Telnet. Login using Telnet is typically used on networks that do not have high security requirements. | This login mode is disabled by default. Before logging in to a device through Telnet, you can log in through the console port and perform the following operations:  * Configure a reachable route between the user terminal and device. (By default, no IP address is configured on the device.) * Enable the Telnet server function and configure related parameters. * Configure a user interface for Telnet login. * Configure a local Telnet user. |
| [Configuring Remote Login Through STelnet](vrp_login_cfg_0013.html) | The STelnet protocol provides secure remote login on insecure networks to ensure secure data transmission as well as data integrity and reliability. | The configuration is complex. | You can log in to the device using STelnet on networks with high security requirements. STelnet, based on the SSH protocol, provides powerful authentication functions to ensure information security and protect the device against attacks, such as IP spoofing attacks. | This login mode is disabled by default. Before logging in to a device through STelnet, you can log in through the console port or Telnet and perform the following operations:  * Configure a reachable route between the user terminal and device. (By default, no IP address is configured on the device.) * Enable the STelnet server function and configure related parameters. * Configure a user interface for SSH login. * Configure SSH user information. |


#### Console Port

The console port is an EIA/TIA-232 DCE port provided by a device. You can directly connect the serial port of a user terminal to the console port of the device to log in to the device and configure the device locally.


#### Telnet

Telnet is an application layer protocol in the TCP/IP protocol stack. It provides remote login and virtual terminal services, and uses the client/server model. That is, the Telnet client sends a request to the Telnet server, and the Telnet server provides the Telnet service. The devices support the Telnet client and server functions.

As shown in [Figure 1](#EN-US_CONCEPT_0000001513173038__fig_dc_cfg_login_000101), DeviceA functions as both a Telnet server and a Telnet client. If there is no reachable route between the PC and DeviceB, you can remotely log in to DeviceB through DeviceA. In this case, DeviceB functions as the Telnet server for DeviceA.

**Figure 1** Telnet client/server model  
![](figure/en-us_image_0000001512693920.png)

#### STelnet

Telnet uses the TCP protocol to transmit data in plain text. It does not have a secure authentication mode and is vulnerable to Denial of Service (DoS), IP address spoofing, and route spoofing attacks.

STelnet is based on SSH2.0. The STelnet client and server establish a secure connection through negotiation, and the client can then access the server.