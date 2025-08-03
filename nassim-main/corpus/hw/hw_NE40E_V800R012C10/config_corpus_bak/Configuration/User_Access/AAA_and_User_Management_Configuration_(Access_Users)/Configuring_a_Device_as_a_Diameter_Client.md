Configuring a Device as a Diameter Client
=========================================

A Diameter client must be configured if service policies need to be delivered through the server.

#### Context

A Diameter server is used to deliver service policies for value-added services, such as BoD, DAA, and EDSG services.

Before configuring a Diameter server, familiarize yourself with the following basic concepts:

* Diameter client: local Router. Only one client can be configured on a device.
* Diameter server: is the remote policy server (RM9000). A maximum of eight servers can be specified for a Router.
* Diameter server group: is a Diameter server-client group that is uniquely identified by the client name and server name. A maximum of eight Diameter connection groups can exist on a Router because a maximum of eight servers can be specified on a Router.
* Diameter link: A Diameter link is established using TCP. The IP address and port number of the Diameter client and those of the Diameter server uniquely identify a Diameter link. A maximum of four Diameter links can be set up in the Diameter server group view.


[(Optional) Configuring Interfaces to Support EDSG Service Policies Delivered by Diameter Servers](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0051.html)

If Diameter needs to be used in EDSG service scenarios, configure Diameter interfaces to support EDSG service policies delivered by Diameter servers.

[Configuring Diameter Functions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0052.html)



[Configuring a Diameter Link](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0053.html)

This section describes how to configure a Diameter link to connect a Diameter client and a Diameter server.

[(Optional) Binding a Diameter Server Group to an AAA Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0054.html)

After a Diameter server group is configured, bind the server group to an AAA domain.

[Verifying the Diameter Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0055.html)

After configuring Diameter, check the configuration.