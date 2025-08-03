(Optional) Configuring Link Monitoring
======================================

You can configure errored frame, errored code, or errored frame second detection to detect link-layer faults.

#### Usage Scenario

Ethernet fault detection is quite difficult to implement, especially when the physical communication is not interrupted but network performance slowly deteriorates.

EFM OAM provides the link monitoring function, which is used to detect and locate link-layer faults in different scenarios. In link monitoring, when a link fault occurs, the local device reports the fault to the remote device by sending OAM PDUs. Fault types are as follows:

* Link fault: If link signals of the remote device are lost, an OAM PDU is sent every second.
* Critical event: If an uncertain urgent event occurs, OAM PDUs are sent immediately and continuously.


#### Pre-configuration Tasks

Before configuring link monitoring, [configure basic EFM OAM functions](dc_vrp_efm_cfg_2003.html).


[(Optional) Configuring Errored Frame Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2012.html)

If the number of errored frames detected on the local interface reaches or exceeds a configured threshold within a specified interval, the local device reports the fault to the remote device.

[(Optional) Configuring Errored Code Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2013.html)

If the number of errored codes detected on the local interface reaches or exceeds a configured threshold within a specified interval, the local device reports the fault to the remote device.

[(Optional) Configuring Errored Frame Second Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2014.html)

If the number of errored frame seconds detected on the local interface reaches or exceeds a configured threshold within a specified interval, the local device reports the fault to the remote device.

[(Optional) Configuring Periodic EFM Errored Frame Detection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2036.html)

If the number of errored frames that an EFM-enabled interface detects within a configured detection period reaches or exceeds a configured threshold, the interface notifies its peer interface of the errored frame fault.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2016.html)

After configuring link monitoring, verify the configurations.