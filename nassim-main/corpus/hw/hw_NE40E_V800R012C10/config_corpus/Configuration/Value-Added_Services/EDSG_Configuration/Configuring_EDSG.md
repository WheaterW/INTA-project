Configuring EDSG
================

Before configuring EDSG, familiarize yourself with the
usage scenario, complete the pre-configuration tasks, and obtain the
data required for the configuration.

#### Usage Scenarios

Typical EDSG usage scenarios
are as follows:

* In some regions, small local carriers need to rent backbone
  carriers' lines to provide Internet access services to users. The
  local carriers also need to pay the backbone carriers for traffic
  over the backbone networks. Low fees are charged for traffic over
  a local network, whereas high fees are charged for traffic over a
  backbone network. To increase revenues, local carriers need a solution
  that can distinguish the two types of traffic and perform accounting
  based on network types. EDSG meets this requirement. Two EDSG services
  can be configured for the local and backbone networks based on destination
  addresses to implement differentiated accounting on traffic over both
  the local and backbone networks.
* When campus users access a campus network, the carrier does
  not charge any fees or charges low fees, and the access rate is unlimited.
  However, when campus users access an external network, the carrier
  charges high fees and limits their access rates. To increase the carrier's
  revenues, configure two EDSG services for the campus and external
  networks based on destination addresses to implement differentiated
  accounting and rate limit on traffic over both the campus and external
  networks.
* Many Internet services, such as gaming, File Transfer Protocol
  (FTP), video on demand (VOD), and news services, have different costs
  and bandwidth requirements. To implement differentiated accounting
  and rate limit on various services, configure these services as different
  EDSG services.

As shown in [Figure 1](#EN-US_TASK_0172375050__fig_dc_ne_cfg_edsg_000201), Point-to-Point Protocol over Ethernet (PPPoE) users access networks
1 and 2. Different fees need to be charged for traffic over networks
1 and 2. The users have different bandwidth requirements for networks
1 and 2. To meet these requirements, configure two EDSG services on
the broadband remote access server (BRAS) to perform differentiated
accounting and rate limit on traffic over networks 1 and 2. EDSG allows
carriers to provide flexible service and accounting policies for different
user requirements.

![](../../../../public_sys-resources/note_3.0-en-us.png) The BRAS can work with
the AAA server, policy server, and portal server to implement differentiated
accounting and rate limit based on destination addresses.

* AAA server: provides user authentication, authorization, and
  accounting. Generally, a RADIUS server is used as a AAA server.
* Policy server: delivers EDSG service policies. Only a RADIUS
  server can be used as a policy server.
* Portal server: provides user interfaces. Users can log in to
  a portal server and select EDSG services as required. A portal server
  is generally integrated into a AAA or policy server.



**Figure 1** EDSG networking
  
![](images/fig_dc_ne_cfg_edsg_0001.png)

#### Pre-configuration Tasks

Before configuring
EDSG, complete the following tasks:

* Load the BRAS license and the EDSG license.
* Configure an authentication scheme, an accounting scheme, and
  a RADIUS server group for an EDSG service policy (for details, see [AAA and User Management Configuration (Access Users)](dc_ne_aaa_cfg_0035.html)).
* Configure an address pool (for details, see [Configuring an IPv4 Address Pool and an Address Pool Group](dc_ne_ipv4_address_cfg_0048.html)).
* Configure a domain and bind the authentication scheme, accounting
  scheme, address pool, and RADIUS server group to the domain (for details,
  see [Configuring a Domain](dc_ne_aaa_cfg_0111.html)).
* Configure a BAS interface (for details, see [IPoE Access Configuration](dc_ne_ipox_cfg_0031.html) and [PPPoE Access Configuration](dc_ne_pppoe_cfg_0001.html)).


[Enabling the Value-added Service Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0004.html)

EDSG can be configured only after the value-added service function is enabled.

[Configuring a Policy Server](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0005.html)

This section describes how to configure a policy server.

[Configuring an EDSG Traffic Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0006.html)

To distinguish user traffic over networks 1 and 2, create two service groups and configure an EDSG traffic policy for each service group. This section describes how to configure an EDSG traffic policy.

[Configuring an EDSG Service Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0007.html)

You can configure different EDSG service policies to implement differentiated accounting and rate limiting for user access to different networks.

[(Optional) Applying an EDSG Service Policy to a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0032.html)

If no EDSG service policy is delivered from the policy server, use the service policy group configured in the AAA domain.

[(Optional) Configuring a Mapping Between a Time Range Template and Service Bandwidth](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_edsg_0015.html)

This section describes how to configure a mapping between a time range template and EDSG service bandwidth. After the configuration is complete, the EDSG service bandwidth is adjusted when the time range changes.

[(Optional) Configuring the Prepaid Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0009.html)

The prepaid function allows the RADIUS server to deliver an EDSG service with a specified time or traffic volume quota in advance. After the quota is exhausted, the BRAS reapplies for an EDSG service quota from the RADIUS server. When the RADIUS server returns a zero quota, the BRAS executes a deactivation or redirection policy. If a carrier wants users to pay in advance and reserve the time or volume quota, the carrier can configure the prepaid function. This section describes how to configure the prepaid function.

[Configuring a Mode in Which an EDSG Service Policy Is Obtained](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0010.html)

An EDSG service policy can be downloaded from local configurations or a RADIUS server.

[(Optional) Configuring a Rate Limit Mode for Services in a Domain](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0011.html)



[(Optional) Configuring EDSG Service Rate Limiting and Traffic Statistics Collection Policies](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0060.html)



[(Optional) Enabling EDSG Services to Support HQoS Scheduling for Home Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0022.html)

This section describes how to enable EDSG services to support HQoS scheduling for home users in a AAA domain.

[(Optional) Configuring EDSG Service Traffic to Match a User Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0021.html)

This section describes how to configure EDSG service traffic to match a user group in load-balancing scenarios.

[(Optional) Configuring Accounting Copy for EDSG Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_edsg_0026.html)

This section describes how to enable the copy function for EDSG service accounting packets in a user access domain.

[(Optional) Configuring Accounting Packet Merging for Value-added Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_edsg_0027.html)

This section describes how to configure accounting packet merging for value-added services to reduce the number of packets sent to a RADIUS accounting server.

[(Optional) Enabling the Captive Portal Function Based on EDSG Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0023.html)

After an HTTP redirection profile is bound to a service policy, the captive portal function based on EDSG services is enabled. When users visit HTTP web pages matching service traffic, the service traffic is redirected to a specified page.

[(Optional) Configuring the Device to Use the Inner IPv4 Address of Each IPv4-in-IPv6 Packet to Match IPv4 UCLs of EDSG Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0028.html)

You can configure this function to allow IPv4-in-IPv6 packets to use inner IPv4 addresses to match IPv4 UCLs of EDSG services.

[(Optional) Configuring RADIUS Attributes](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_edsg_0013.html)

To enable attributes delivered by a RADIUS server through CoA packets or RADIUS to take effect, you must configure these attributes on the NE40E.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_edsg_cfg_0012.html)

After configuring EDSG services successfully, check information about the configured service policies and users' value-added services and ensure that EDSG services run properly.