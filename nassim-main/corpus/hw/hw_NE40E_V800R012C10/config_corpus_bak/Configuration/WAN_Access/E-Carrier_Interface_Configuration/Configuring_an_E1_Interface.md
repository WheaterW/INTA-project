Configuring an E1 Interface
===========================

Configuring_an_E1_Interface

#### Precautions

Before you use an E1 interface to carry upper-layer services, configure the E1 interface. Note that:

* If a physical interface has no cable connected, run the [**shutdown**](cmdqueryname=shutdown) command to disable this interface to prevent interference with the interface.
* After you configure services on an interface, run the [**shutdown**](cmdqueryname=shutdown) and then [**undo shutdown**](cmdqueryname=undo+shutdown) commands in the current interface view to ensure that the configured services are loaded onto the interface.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Running the [**shutdown**](cmdqueryname=shutdown) command in an E1 interface view will disable the E1 interface and may affect the normal operation of its channel-sets.



#### Pre-configuration Tasks

Before configuring an E1 interface, power on the device and ensure that it is working properly.


[Configuring the Working Mode for an E1 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ce1_cfg_0006.html)

This section describes how to configure the working mode of a channelized E1 interface. E1 interfaces can work in either clear channel mode or channelized mode.

[Configuring the Clock Mode for a CE1 Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ce1_cfg_5001.html)

A CE1 interface works in either master clock mode or slave clock mode. When two CE1 interfaces are directly connected, you must configure one to work in master clock mode and the other in slave clock mode. When a CE1 interface is connected to a transmission device, the CE1 interface must work in slave clock mode.

[Configuring the Frame Format for a CE1 Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ce1_cfg_5003.html)

You can configure a CE1 interface to use a 4-bit CRC code to check physical frames.

[Configuring the Loopback Function for an E1 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ce1_cfg_0007.html)

This section describes how to configure the loopback function on a channelized E1 interface. The loopback function is used to check the interface or cable status. In normal situations, the loopback function is disabled.

[Configuring ES-TCA Alarm Thresholds on a CE1 Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ce1_cfg_5006.html)

If the threshold for triggering an ES-TCA alarm is set and the number of E1 code errors exceeds the threshold, an alarm will be generated.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ce1_cfg_0008.html)

After you configure an E1 interface, verify the configurations and status of the interface.