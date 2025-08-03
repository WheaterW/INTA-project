Using Telnet to Log In to Other Devices
=======================================

Telnet is a client/server application that allows you to log in to remote devices to manage and maintain the devices.

#### Usage Scenario

Large numbers of devices need to be managed and maintained on a network. You cannot connect each device to a terminal. When no reachable route exists between remote devices and a terminal, you can use Telnet to log in to the remote devices from the device that you have logged in to.

As shown in [Figure 1](#EN-US_TASK_0172360068__fig_dc_vrp_basic_cfg_013901), you can use Telnet on the PC to log in to the Telnet client. Because the PC does not have a reachable route to the Telnet server, you cannot remotely manage the Telnet server. To remotely manage the Telnet server, use Telnet on the Telnet client to log in to the Telnet server.

**Figure 1** Using Telnet on the Telnet client to log in to the Telnet server  
![](images/fig_dc_vrp_basic_cfg_013901.png)

#### Pre-configuration Tasks

Before using Telnet on the Telnet client to log in to the Telnet server, complete the following task:

* [Configure Telnet login](dc_vrp_basic_cfg_0030.html).
* Ensure that the route between the Telnet client and server is reachable.


[(Optional) Configuring a Source Address for the Telnet Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0140.html)

You can configure a source address for the Telnet client and use the source address to establish a Telnet connection, ensuring file transfer security.

[Using Telnet to Log In to Other Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0141.html)

Telnet is a client/server application that allows you to log in to remote devices to manage and maintain the devices.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0142.html)

After logging in to another device from the current device through Telnet, you can check information about the established TCP connection.