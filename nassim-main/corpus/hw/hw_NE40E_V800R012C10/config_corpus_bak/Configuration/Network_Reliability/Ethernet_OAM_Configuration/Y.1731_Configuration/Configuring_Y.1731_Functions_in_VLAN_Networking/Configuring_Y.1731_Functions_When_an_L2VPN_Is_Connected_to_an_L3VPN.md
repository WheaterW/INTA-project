Configuring Y.1731 Functions When an L2VPN Is Connected to an L3VPN
===================================================================

Single-ended frame loss measurement, dual-ended frame loss measurement, one-way frame delay measurement, and two-way frame delay measurement can be configured when an L2VPN is connected to an L3VPN.

#### Usage Scenario

In [Figure 1](#EN-US_TASK_0172362115__fig_dc_vrp_y1731_cfg_005301), an L2VPN is connected to an L3VPN. To collect performance statistics for a link between CE1 and PE3, use the following monitoring functions defined by Y.1731:

* Single-ended frame loss measurement
* Dual-ended frame loss measurement
* One-way frame delay measurement
* Two-way frame delay measurement

**Figure 1** L2VPN connected to an L3VPN  
![](images/fig_dc_vrp_y1731_cfg_005301.png)  


#### Pre-configuration Tasks

Before configuring Y.1731 functions when an L2VPN is connected to an L3VPN, complete the following tasks:

* Configure an L2VPN to connect to an L3VPN on MEPs.
* Configure CFM on MEPs, and set the MEP type to outward-facing.


[Single-ended Frame Loss Measurement When an L2VPN Is Connected to an L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0054.html)

When an L2VPN is connected to an L3VPN, single-ended frame loss measurement is enabled to monitor link quality. This helps prevent CCMs from overloading the network.

[Dual-ended Frame Loss Measurement When an L2VPN Is Connected to an L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0055.html)

When a CFM-enabled L2VPN is connected to an L3VPN, dual-ended frame loss measurement is enabled to collect detailed statistics and monitor link quality.

[One-Way Frame Delay Measurement When an L2VPN Is Connected to an L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0056.html)

One-way frame delay measurement can be configured when CFM is enabled for an L2VPN connected to an L3VPN to monitor link connectivity and a MEP has the time synchronized with that on an RMEP.

[Two-Way Frame Delay Measurement When an L2VPN Is Connected to an L3VPN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_y1731_cfg_0057.html)

Two-way frame delay measurement can be configured when CFM is enabled on an L2VPN connected to an L3VPN to monitor link connectivity and a MEP does not have the time synchronized with that on an RMEP.