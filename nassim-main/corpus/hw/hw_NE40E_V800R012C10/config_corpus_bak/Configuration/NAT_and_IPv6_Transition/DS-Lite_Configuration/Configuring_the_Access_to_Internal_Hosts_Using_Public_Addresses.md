Configuring the Access to Internal Hosts Using Public Addresses
===============================================================

A DS-Lite device can be configured to allow public network users to use a specified public IP address and port number to proactively access private network users.

#### Usage Scenario

You can deploy DS-Lite to allow intranet users of a private network to initiate a request for accessing public network services, whereas public network users cannot obtain information about the users of the private network and cannot access these users. The NE40E supports the DS-Lite internal server function and the port forwarding function. A user's private network IP address and port can be associated with a public network IP address and port, respectively, so that external users can access the public IP address and port of the user to access the private network user.

* DS-Lite internal server: Internal servers can be configured to associate a user's private IP address and port with a public IP address and port, respectively.
* Port forwarding: A user's private IP address and port can be dynamically associated with a public IP address and port, respectively.

#### Pre-configuration Tasks

Before configuring the access to internal hosts using public addresses, complete the following tasks:

* Configure basic DS-Lite functions.
* Configure DS-Lite translation for user traffic.
* Configure a DS-Lite device to properly interwork with a RADIUS server.
* (Optional) Configure DS-Lite user information.


[Configuring the DS-Lite Server Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0028.html)

This section describes how to configure the DS-Lite server function so that external users can proactively access the private network server.

[Configuring Port Forwarding](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0029.html)

When the IP addresses of internal servers frequently change, you can configure the port forwarding service to dynamically associate each internal server with a public IP address and port. 

[Verifying the Configuration of Access to Internal Hosts Using Public Addresses](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0030.html)

After the DS-Lite internal server function is configured, you can check the server mapping information of the internal server.