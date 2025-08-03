Configuring an EVC to Transmit Multicast Services
=================================================

To improve network resource usage and implement on-demand multicast data forwarding in an EVC scenario, configure an EVC to transmit multicast services.

#### Usage Scenario

* Configure an EVC to transmit Layer 2 multicast services.
  
  After a multicast data message is received on an interface in a broadcast domain (BD), the message is broadcast to all the other interfaces in the same BD, including the interfaces not connected to multicast data receivers. Such data broadcasting wastes bandwidth resources and may result in security issues. To resolve these issues, configure an EVC to implement on-demand Layer 2 multicast service transmission in a specific BD.
* Configure an EVC to transmit Layer 3 multicast services.
  
  An EVC applies to Layer 2 interfaces and does not support IP address configuration. To enable an EVC-capable BD to communicate with Layer 3 interfaces, configure a logical VBDIF interface for the BD. A VBDIF interface is a network-layer interface and supports IP address configuration. By configuring a VBDIF interface for a BD, you can enable an EVC to transmit Layer 3 multicast services, which simplifies network planning and management.

#### Pre-configuration Tasks

Before configuring an EVC to transmit multicast services, complete the following tasks:

* [Establishing the EVC Model](dc_vrp_evc_cfg_0003.html)
* Configure a routing protocol so that devices can communicate at the network layer.


[Configuring an EVC to Transmit Layer 3 Multicast Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0035.html)

To enable an EVC-capable BD to communicate with a Layer 3 multicast network, configure a VBDIF interface for the BD, so that the EVC can transmit Layer 3 multicast services and implement on-demand data forwarding.

[Configuring an EVC to Transmit Layer 2 Multicast Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0036.html)

To improve network resource usage and implement on-demand multicast data forwarding in an EVC scenario, configure an EVC to transmit Layer 2 multicast services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evc_cfg_0037.html)

After configuring an EVC to transmit multicast services, you can check the status of multicast services.