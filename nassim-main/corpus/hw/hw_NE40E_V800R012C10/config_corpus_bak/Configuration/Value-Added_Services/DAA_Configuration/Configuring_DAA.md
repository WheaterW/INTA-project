Configuring DAA
===============

Before configuring DAA, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

Typical DAA usage scenarios are as follows:

* In some regions, small local carriers need to rent backbone carriers' lines to provide Internet access services to users. The local carriers also need to pay the backbone carriers for traffic over the backbone networks. Low fees are charged for traffic over a local network, whereas high fees are charged for traffic over a backbone network. To increase revenues, local carriers need a solution that can distinguish the two types of traffic and perform accounting based on tariff levels. DAA meets this requirement and is capable of performing differentiated accounting on traffic over both local and backbone networks.
* When campus users access a campus network, the carrier does not charge any fees or charges low fees, and the carrier does not limit their access rates. However, when campus users access an external network, the carrier charges high fees and limits their access rates. DAA is capable of performing differentiated accounting and rate limit on traffic over the campus and external networks, increasing carrier revenues.
* Many Internet services, such as gaming, File Transfer Protocol (FTP), video on demand (VOD), and news services, have different costs and bandwidth requirements. Carriers need to perform differentiated accounting and rate limit on different services. When network congestion occurs, the quality of the services is guaranteed based on their priorities. For example, if the priority of gaming services is higher than that of news services, the quality of the gaming services is preferentially guaranteed during network congestion. DAA can also meet this requirement. Carriers deploy various services on different servers. When users access these servers, DAA distinguishes services based on the network segments on which the servers reside and performs differentiated accounting, rate limit, and priority scheduling.


#### Pre-configuration Tasks

Before configuring DAA, complete the following tasks:

* Run the [**license active**](cmdqueryname=license+active) command to load the BRAS and DAA licenses.
* Configure an authentication scheme, an accounting scheme, and a RADIUS server group for a DAA service policy (for details, see [AAA and User Management Configuration (Access Users)](dc_ne_aaa_cfg_0035.html)).
* Configure an address pool (for details, see [Configuring an IPv4 Address Pool and an Address Pool Group](dc_ne_ipv4_address_cfg_0048.html)).
* Configure a domain and bind the authentication scheme, accounting scheme, address pool, and RADIUS server group to the domain (for details, see [Configuring a Domain](dc_ne_aaa_cfg_0111.html)).
* Configure a BAS interface (for details, see [IPoE Access Configuration](dc_ne_ipox_cfg_0031.html) and [PPPoE Access Configuration](dc_ne_pppoe_cfg_0001.html)).


[Enabling the Value-added Service Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0004.html)

DAA can be configured only after the value-added service function is enabled.

[Configuring the Policy Server](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0005.html)

This section describes the methods and procedures for configuring the policy server.

[Configuring an Accounting Mode for Value-added Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0006.html)

Carriers can configure differentiated services and tariff policies for different users.

[Configuring a DAA Service Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0007.html)

This section describes how to configure a DAA service policy.

[Applying a Value-added Service Policy to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0009.html)

If a policy server does not deliver any service policy, the service policy configured in a domain is used.

[Binding a Policy Server to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0010.html)

Bind a policy server to a domain so that users are authenticated and accounted by the server.

[Applying a DAA Service Policy to a BAS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0015.html)

Applying a DAA service policy to a BAS interface allows access control between users in an enterprise as well as policy sharing between users in different enterprises.

[Configuring PUPP](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0020.html)



[(Optional) Configuring Accounting Packet Merging for Value-added Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0011.html)

To reduce the number of packets sent to a RADIUS accounting server, configure accounting packet merging for value-added services.

[(Optional) Enabling the Device to Report Statistics About Dropped DAA Service Traffic](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0021.html)

You can enable the device to report statistics about dropped DAA service traffic. This allows you to query information about users with such traffic.

[Verifying the DAA Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_daa_cfg_0012.html)

After configuring DAA, verify the DAA configuration.