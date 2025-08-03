Configuring an E3 Interface
===========================

This section describes how to configure an E3 interface
to carry upper-layer services.

#### Precautions

When configuring E3 interfaces
to carry upper-layer services, note the following:

* If an E3 interface on the device is idle (no cable is connected
  to the interface), run the [**shutdown**](cmdqueryname=shutdown) command to shut down the E3 interface to prevent it from
  being interfered.
* After configuring services on an E3 interface, run the **shutdown** and then **undo shutdown** commands in the interface view for
  the services to take effect.
* The **shutdown** and **undo shutdown** commands run on an
  E3 interface also take effect with the serial interface created on
  the E3 interface. However, the **shutdown** and **undo shutdown** commands run on a serial interface takes effect only with the serial
  interface.


#### Pre-configuration Tasks

Before configuring
an E3 interface, power on the device and ensure that the self-check
succeeds.


[Creating a Synchronous Serial Interface on an E3 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_e3_cfg_0002.html)

Before using an E3 interface to transmit data, you must create a synchronous serial interface on the E3 interface.

[Configuring Loopback on an E3 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_e3_cfg_0003.html)

To monitor the status of an E3 interface or the cable connected to the E3 interface, configure loopback on the E3 interface.

[Configuring a Clock Mode for an E3 Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_e3_cfg_0004.html)

An E3 interface works either in master clock mode or slave clock mode.

[Verifying the E3 Interface Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_e3_cfg_0005.html)

After configuring an E3 interface, verify its status and clock configuration.