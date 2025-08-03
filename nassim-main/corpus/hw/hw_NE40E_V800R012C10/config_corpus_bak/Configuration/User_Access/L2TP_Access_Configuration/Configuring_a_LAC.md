Configuring a LAC
=================

To establish an L2TP tunnel between a LAC and an LNS, configuring
the LAC, including starting an L2TP connection and setting tunnel
parameters and an authentication mode for the LAC.

#### Usage Scenario

When an L2TP user goes online,
a LAC sets up a tunnel with a remote LNS and sends the user packets
to the LNS through the tunnel.

[Figure 1](#EN-US_TASK_0172374233__fig_dc_ne_l2tp_cfg_01369001) shows
how an NE40E that functions as a LAC initiates an L2TP connection to
an LNS when a user goes online.

**Figure 1** Process of initiating an L2TP connection
  
![](images/fig_dc_ne_l2tp_cfg_01369001.png)  

| (1) The NE40E reads the domain name contained in the username. |
| --- |
| (2) The NE40E reads the L2TP group name specified for the domain. |
| (3) The NE40E reads a specified LNS address in the L2TP group. |
| (4) The NE40E initiates a connection to the specified LNS. |




#### Pre-configuration Tasks

Before configuring
a LAC, [configure AAA schemes](dc_ne_aaa_cfg_0515.html).


[Enabling L2TP](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013687.html)

To set up an L2TP tunnel between a LAC and an LNS, L2TP must be first enabled.

[Configuring an L2TP Connection on the LAC Side](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013691.html)

Configuring an L2TP connection on the LAC side is the prerequisite for establishing an L2TP tunnel.

[Configuring L2TP Tunnel Authentication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013693.html)

An L2TP tunnel can be successfully established only after L2TP tunnel authentication succeeds.

[Configuring L2TP Attributes for Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013692.html)

The L2TP attributes of a user include the tunnel type, LAC source address, LNS address, tunnel name, tunnel password, and tunnel ID. The L2TP attributes delivered by the RADIUS server have a higher priority than those configured locally.

[Configuring LAC-Side User Access](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppoe_cfg_00055.html)

This section describes how to configure LAC-side user access to implement control and accounting for each access host.

[(Optional) Configuring URPF for L2TP Users](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pppoe_cfg_000551.html)

To prevent source address spoofing attacks, enable URPF for L2TP users.

[Verifying the LAC Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013696.html)

This section describes how to verify the configurations of the L2TP group, session information, and the tunnel on the LAC after the LAC is configured and users go online.