Configuring TWAMP Light Functions
=================================

This section describes how to configure TWAMP Light functions, including configuring the Controller and Responder.

#### Usage Scenario

As TWAMP Light simplifies deployment and supports plug-and-play, you can use TWAMP Light to rapidly and flexibly measure the round-trip performance of an IP network, such as the two-way packet loss rate, jitter, and delay.


#### Pre-configuration Tasks

Before configuring TWAMP Light functions, complete the following tasks:

* Ensure that devices on the live network support TWAMP Light and comply with standard protocols.
* Ensure that the Controller and Responder are routable and IP links between them work properly.


[Configuring the TWAMP Light Responder](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_twamp-light_0012.html)

The TWAMP Light Responder responds to TWAMP test packets sent by the TWAMP Light Controller.

[Configuring the TWAMP Light Controller](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_twamp-light_0013.html)

The TWAMP Light Controller integrates the Control-Client and Session-Sender functions in the standard model. The TWAMP Light Control-Client establishes, starts, and stops a test session. The TWAMP Light Session-Sender starts performance tests and sends test packets to the Responder, or stops performance tests.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_twamp-light_cfg_0016.html)

After configuring the TWAMP Light statistics collection function, verify the configurations.