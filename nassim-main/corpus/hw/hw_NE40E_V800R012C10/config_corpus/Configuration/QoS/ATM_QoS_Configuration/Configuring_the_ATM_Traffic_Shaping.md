Configuring the ATM Traffic Shaping
===================================

Configuring ATM traffic shaping limits the volume of outgoing
traffic on an ATM network within a reasonable range, preventing a
large number of burst data that from affecting normal operation of
the network.

#### Usage Scenario

To keep the traffic over
an ATM network within a reasonable scope to avoid abnormal operation
of the network in the case of heavy and bursting traffic, you can
configure ATM traffic shaping to limit the outgoing traffic rate.
The configuration can better utilize the network resources.


#### Pre-configuration Tasks

Before configuring
the ATM traffic shaping, complete the following tasks:

* Configuring the physical parameters of ATM interfaces to ensure
  normal operation of the interfaces
* Configuring IP addresses for the ATM interfaces

#### Configuration Procedures

**Figure 1** Flowchart for Configuring the ATM Traffic Shaping
  
![](images/fig_dc_ne_qos_cfg_01239501.png)


[Configuring ATM Traffic Shaping Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012397.html)

You must specify the service type and parameters related to the service type for PVCs or PVPs to limit the volume of outgoing traffic on an ATM network.

[Applying ATM Traffic Shaping Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012398.html)

ATM traffic shaping parameters are applied to ATM interfaces or ATM sub-interfaces.

[Verifying the Configuration of ATM Traffic Shaping](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012399.html)

After ATM traffic shaping is configured, you can view traffic shaping parameters.