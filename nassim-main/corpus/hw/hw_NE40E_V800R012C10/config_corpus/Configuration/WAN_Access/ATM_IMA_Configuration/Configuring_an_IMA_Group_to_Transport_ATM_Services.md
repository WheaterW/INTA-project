Configuring an IMA Group to Transport ATM Services
==================================================

Before configuring an IMA group to transport ATM services, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Context

An IMA group can be considered a logical link that aggregates several low-speed physical links (member links) to provide higher bandwidth. The rate of the logical link is approximately the sum of the rate of the member links in the IMA group.


#### Pre-configuration Tasks

Before configuring an IMA group interface, connect interfaces and set their physical parameters to ensure that the physical status of the interfaces can go Up.


[Creating an IMA Group Interface and Adding an Interface to It](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_atm_cfg_0006.html)

To increase bandwidth, create an IMA group and bundle several links in the IMA group.

[(Optional) Configuring IMA Group Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_atm_cfg_0007.html)

Configure IMA group parameters as required.

[Configuring a Service Type for a PVC](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_atm_cfg_0008.html)

To implement ATM traffic shaping, configure a service type for a PVC.

[(Optional) Configuring Continuity Check on ATM Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_atm_0002.html)

After ATM cell relay has been configured on an ATM interface or a logical interface whose link layer protocol is ATM, you can perform a continuity check on the ATM services.

[Configuring the Alarm threshold of ATM Module](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_atm_0001.html)

After configuring the ATM module to report alarms to the NMS, you can monitor the alarm status of the ATM module on the NMS interface.

[Verifying the IMA Group Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_atm_cfg_0009.html)

After completing configurations on an IMA group interface, verify the configuration.