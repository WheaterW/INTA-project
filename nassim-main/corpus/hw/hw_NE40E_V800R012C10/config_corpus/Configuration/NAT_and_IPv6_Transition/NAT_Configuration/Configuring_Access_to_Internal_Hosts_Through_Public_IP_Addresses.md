Configuring Access to Internal Hosts Through Public IP Addresses
================================================================

Configuring access to internal hosts through public IP addresses allows external users to communicate with intranet users using a public IP address and port number.

#### Usage Scenario

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only dedicated boards support this configuration.

NAT can be configured to allow private network users to initiate access connections to public network services, whereas public network users cannot access intranet users because they cannot obtain information about intranet users. The NE40E supports NAT server and port forwarding. The private IP address and port of a user are bound to a public IP address and port so that the external user can visit the private network user through the public IP address and port.

* NAT server: A server can be configured to associate a user's private IP address and port with a public IP address and port, respectively.
* Port forwarding: A user's private IP address and port can be dynamically associated with a public IP address and port, respectively.

#### Pre-configuration Tasks

Before you configure access to internal hosts using public addresses, complete the following tasks:

* Configure basic NAT functions.
* (Optional) Configure NAT user information.
* Configure NAT for user traffic.
* Ensure that the device can properly interwork with the RADIUS server.


[Configuring the NAT Server Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0067.html)

The NAT Server function can be configured on a private network so that external users can access the server through a NAT device.

[Configuring the Port Forwarding Service](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0074_m2.html)

If the IP addresses of internal servers frequently change, you can configure the port forwarding service to dynamically associate each internal server with a public IP address and a public port.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0075.html)

After configuring the NAT server function, you can check the server mapping entry information of the NAT server.