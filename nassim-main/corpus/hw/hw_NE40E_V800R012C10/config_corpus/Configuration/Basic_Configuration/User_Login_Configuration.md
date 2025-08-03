User Login Configuration
========================

You can log in to a device through a console port or using Telnet or SSH (STelnet) to maintain the device locally or remotely.

#### Context

If multiple users log in to a device through a console port, the following security risks occur:

* The device authenticates only the first user.
* The input information of a user is displayed for all users at the same time. For example, if a user runs a command to change the password, the input information is visible to all users at the same time.

Therefore, logging in to a device through the console port is not recommended. If this login mode is required, do not configure multiple users for simultaneous login.


[Overview of User Login](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0025.html)

Users can manage or maintain a device only after logging in to the device successfully. You can log in to the device through the console port or using Telnet or STelnet.

[Configuration Precautions for User Login](../../../../software/nev8r10_vrpv8r16/user/spec/User_Login_limitation.html)



[Configuring Login Through a Console Port](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0026.html)

To configure a router that is powered on for the first time or locally maintain the router, log in to the router through the console port.

[Configuring a User to Log In Through Telnet](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0030.html)

This section describes how to configure a user to remotely log in to devices through Telnet to perform management and maintenance.

[Configuring STelnet Login](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0037.html)

STelnet based on SSH2 provides secure remote access over an insecure network.

[Configuration Examples for User Login](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_basic_cfg_0045.html)

This section provides examples for configuring login through a console port, Telnet login, and STelnet login.