Configuring AAA
===============

Before configuring AAA, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the data required for the configuration. This will help you complete the configuration task quickly and efficiently.

#### Usage Scenario

* Local authentication and authorization
  
  If user authentication or authorization is required when no RADIUS or HWTACACS server is deployed on the network, local authentication or authorization mode can be used. Local authentication and authorization feature fast processing and low operation cost, whereas the amount of information that can be stored is limited by the hardware capacity of the device.
  
  Local authentication and authorization are often used for administrators. Local authentication is a backup of RADIUS authentication and HWTACACS authentication; local authorization is a backup of HWTACACS authorization.
* HWTACACS authentication, authorization, and accounting: The authentication, authorization, and accounting in HWTACACS mode can prevent unauthorized users from attacking the network. In addition, the HWTACACS mode supports the authorization of command lines. Compared with RADIUS, HWTACACS is more reliable in transmission and encryption and is more suitable for security control.
* RADIUS authentication and accounting: The authentication and accounting in RADIUS mode can prevent unauthorized users from attacking the network. The RADIUS mode is often used in network environments requiring high security and remote access control.

#### Pre-configuration Tasks

Before configuring AAA, complete the following tasks:

* Power on the router or switch and ensuring that the self-test is successful.
* Ensure that the device is accessible.

#### Configuration Procedures

**Figure 1** AAA configuration flowchart  
![](images/fig_dc_vrp_aaa_cfg_100301.png)  


[Configuring AAA Schemes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1004.html)

This section describes how to configure authentication, authorization, and accounting (AAA) schemes.

[(Optional) Configuring Local Users](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1005.html)

When the authentication and authorization are implemented in local mode, the authentication and authorization information (such as the username, password, level, maximum number of connections, and maximum number of continuous authentication failures).

[(Optional) Configuring an HWTACACS Server Template](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1006.html)

When configuring an HWTACACS server template, you must specify the IP address, port number, and shared key of a specified HWTACACS server. Other configurations, such as whether the HWTACACS username carries the domain name and the time for the primary server to switch to the active state, have default settings and can be modified as required.

[(Optional) Configuring a RADIUS Server Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_aaa_cfg_0555.html)



[Configuring AAA Schemes for the Domain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1008.html)

Associate the remote authentication, authorization, and accounting schemes of the domain user with the server template by configuring a domain. Then, corresponding authentication, authorization, and accounting will be implemented for the users accessing the domain.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_aaa_cfg_1031.html)

After AAA is configured, you can view the configurations of authentication, authorization, and accounting schemes.