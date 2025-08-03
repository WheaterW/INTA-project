Configuring the SOC
===================

This section describes how to configure the Security Operating
Center (SOC).

#### Applicable Environment

When an exception
occurs, for example, services are interrupted, the system performance
deteriorates, or service flapping occurs, maintenance personnel can
use the SOC to quickly determine if the exception has been caused
by a security attack. Maintenance personnel can also use the SOC to
perform routine maintenance and management to check if any security
attack has occurred and take immediate measures.


#### Pre-configuration Tasks

None


[Enabling the SOC](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_soc_cfg_0007.html)

You can enable the Security Operating Center (SOC) by enabling attack detection, attack source tracing, and attack defense.

[Analyzing Attack Events](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_soc_cfg_0008.html)

The SOC determines whether an attack event has occurred by analyzing attack event reports and statistics. If attack defense is enabled, you can also check packet loss statistics of the interface under attack.

[(Optional) Configuring a User-Defined Group for Which Attack Defense Is Enabled](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_soc_cfg_0013.html)

You can determine whether an attack event or source exists by checking alarm information and attack event reports. After an attack source is confirmed, you can configure a user-defined group for which attack defense is enabled to isolate the attack source.

[(Optional) Configuring Attack Source Tracing Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_soc_cfg_0009.html)

If attack event reports present incorrect or missing decisions on attack events, adjust attack source tracing parameters to allow attack source tracing to function precisely.

[(Optional) Configuring Attack Detection Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_soc_cfg_0014.html)

If attack event reports present incorrect or missing decisions on attack events, adjust attack detection parameters to allow attack detection to function precisely.

[Verifying the SOC Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_soc_cfg_0010.html)

After configuring attack source tracing parameters, check the configurations. If some parameters are not configured, their default values are displayed.