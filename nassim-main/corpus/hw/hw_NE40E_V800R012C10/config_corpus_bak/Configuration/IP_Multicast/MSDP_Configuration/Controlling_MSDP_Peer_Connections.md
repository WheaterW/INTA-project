Controlling MSDP Peer Connections
=================================

MSDP peers communicate through TCP connections. You can flexibly control the sessions set up between MSDP peers by ending or reestablishing TCP connections. In addition, you can also adjust the interval for retrying to set up MSDP peer connections and configure MSDP peer authentication to improve the security of TCP connections.

#### Usage Scenario

A Router can work normally with default control parameters. You are allowed to adjust the interval for retrying to set up MSDP peer connections if the default interval does not fit your network requirements.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Pre-configuration Tasks

Before configuring MSDP peer connection control, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM inter-domain multicast](dc_vrp_multicast_cfg_0045.html) or [configure Anycast-RP](dc_vrp_multicast_cfg_0050.html).


[Ending an MSDP Peer Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0057.html)

After the connection between MSDP peers is ended, the MSDP peers no longer exchange Source Active (SA) messages and do not retry to set up a new connection. You can reestablish the connection between MSDP peers as required.

[Adjusting the Interval for Retrying to Set Up an MSDP Peer Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0058.html)

A TCP connection needs to be immediately set up between the MSDP peers when a new MSDP peer relationship is created, an ended MSDP peer connection is restarted, or a faulty MSDP peer recovers. You can flexibly adjust the interval for retrying to set up a TCP connection between MSDP peers.

[Configuring MSDP Peer Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0059.html)



[Adjusting the Keepalive Time and Entry Holdtime of an MSDP Peer Relationship](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0111.html)

You can adjust the keepalive time and entry holdtime of an MSDP peer relationship, so that the device will delete the relationship in time when it is not needed.

[Verifying the Configuration of MSDP Peer Relationship Control Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0060.html)

After configuring MSDP peer relationship control parameters, verify information about MSDP peers.