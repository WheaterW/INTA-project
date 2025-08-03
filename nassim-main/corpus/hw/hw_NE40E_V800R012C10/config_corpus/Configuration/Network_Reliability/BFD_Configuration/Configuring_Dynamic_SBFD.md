Configuring Dynamic SBFD
========================

Seamless Bidirectional Forwarding Detection (SBFD) can be configured to implement rapid link fault detection.

#### Usage Scenario

BFD techniques are mature. However, when a large number of BFD sessions are configured to detect links, the negotiation time of the existing BFD state machine is lengthened. In this situation, SBFD can be configured. It is a simplified BFD state machine that shortens the negotiation time and improves network-wide flexibility.


#### Pre-configuration Tasks

Before configuring SBFD, complete the following tasks:

* Connect interfaces.
* Assign an IP address to each Layer 3 interface.


[Configuring an SBFD Reflector Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0046.html)

This section describes how to configure a Seamless Bidirectional Forwarding Detection (SBFD) reflector function. An SBFD reflector can work with an initiator to quickly detect link faults.

[Configuring the SBFD Initiator Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0047.html)

The functions of the Seamless Bidirectional Forwarding Detection (SBFD) initiator can be configured, in addition to the reflector functions, implementing rapid SBFD link detection.

[(Optional) Configuring SBFD Session Authentication Information](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0068.html)

You can configure SBFD session authentication information, such as the authentication algorithm, authentication key, and authentication encryption password, to improve network security.

[(Optional) Configuring Association Between an SBFD Session and a Session Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_2021.html)

You can associate the BFD session status with the session group status to implement fast switching upon multiple points of failure on a segmented cascaded network.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bfd_cfg_0050.html)

After configuring an SBFD Session, verify the configuration.