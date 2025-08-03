Configuring the License Function
================================

The license function is a prerequisite for configuring DS-Lite functions. The license function allows you to adjust DS-Lite bandwidth and session table resources.

#### Usage Scenario

DS-Lite bandwidth and session table resources are controlled using a license. A device is assigned no DS-Lite bandwidth or session table resources by default. Before you configure DS-Lite functions, adjust DS-Lite bandwidth and session table resources.


#### Pre-configuration Tasks

Before configuring the license function, load a license to a device and ensure that a service board is working properly.


[Enabling the DS-Lite Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0062.html)

DS-Lite must be enabled before DS-Lite functions are configured.

[Configuring Session Resources](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0007.html)

Configuring session resources is a prerequisite for configuring DS-Lite functions on a service board. If no session resources are configured, DS-Lite services become unavailable.

[Configuring Bandwidth Resources](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0006.html)

To improve DS-Lite forwarding performance on a dedicated board, configure DS-Lite bandwidth resources to increase bandwidth on the dedicated board.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0008.html)

After configuring the license function on a service board, you can view information about the DS-Lite bandwidth allocated by the license.