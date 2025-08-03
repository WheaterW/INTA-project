Using Ping/Tracert to Test a Layer 2 Network
============================================

Ping/Tracert can be used to diagnose faults on a Layer 2 Ethernet network.

#### Context

To manually monitor the connectivity between two devices, you can send test packets and wait for a reply to test whether the destination device is reachable.

* To check the connectivity of the link between two devices on a network without MDs, MAs, and MEPs configured, use GMAC ping.
* To check the connectivity of the link between MEPs or between a MEP and a MIP in the same MA on a network with MDs, MAs, and MEPs configured, use 802.1ag MAC ping.

#### Pre-configuration Tasks

No pre-configuration task is required for GMAC ping.

Before performing 802.1ag MAC ping, complete the following task:

* Configure basic CFM functions.


[Using GMAC Ping to Check Link Connectivity on a Layer 2 Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ping_cfg_0014.html)

Generic MAC (GMAC) ping applies to a part of or a whole network for monitoring connectivity without configuring a maintenance domain (MD), maintenance association (MA), or maintenance association end point (MEP).

[Using GMAC Trace to Check a Path on a Layer 2 Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ping_cfg_0015.html)

Generic MAC (GMAC) trace can be used to monitor paths and locate faults in a part of or a whole network without configuring an MD, MA, or MEP.

[Using 802.1ag MAC Ping to Check Link Connectivity on a Layer 2 Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ping_cfg_0025.html)

802.1ag MAC ping monitors connectivity between MEPs or between MEPs and MIPs within an MA.

[Using 802.1ag MAC Trace to Check a Path on a Layer 2 Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ping_cfg_0026.html)

802.1ag MAC trace monitors the connectivity between MEPs or between MEPs and MIPs within an MA and provides information used to locate faults.