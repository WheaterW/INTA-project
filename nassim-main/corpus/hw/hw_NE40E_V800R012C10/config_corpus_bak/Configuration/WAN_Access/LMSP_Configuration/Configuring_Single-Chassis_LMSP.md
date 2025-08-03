Configuring Single-Chassis LMSP
===============================

Two devices that support LMSP can be connected using two links. Link reliability can be improved by configuring single-chassis LMSP.

#### Usage Scenario

Linear multiplex section protection (LMSP) needs to be configured when the Router is connected to a Radio Network Controller (RNC). As shown in [Figure 1](#EN-US_CONCEPT_0172364382__fig_dc_ne_lmsp_cfg_000501), PE2 and BSC (RNC) are connected using two CPOS links. You can configure interface 1 as a working interface, and interface 3 as a protection interface.

**Figure 1** Typical networking diagram of single-chassis LMSP  
![](images/fig_dc_ne_lmsp_cfg_002001.png)

#### Pre-configuration Task

Before configuring LMSP, configure an interface on the Router and ensure that the data link layer protocol run between the Router and the RNC is Up.


[Specifying a Working Interface and a Protection Interface for an LMSP Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0006.html)

A working interface and a protection interface must be specified and added to an LMSP group before other LMSP configurations are performed.

[Configuring a Working Mode for an LMSP Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0007.html)

A working mode can be configured for an LMSP group. The NE40E supports LMSP working modes, including automatic LMSP switching and a delayed switchback with the wait to restore (WTR) time configured. An LMSP working mode must be configured on a protection interface.

[Adding Interfaces of an LMSP Group to a Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0008.html)

The working and protection interfaces in an LMSP group must be added to the same trunk interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_lmsp_cfg_0009.html)

After configuring a single-chassis LMSP group, the LMSP group's working mode, working interface, WTR time, and interface status can be viewed.