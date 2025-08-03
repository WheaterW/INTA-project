Configuring TWAMP
=================

This section describes how to configure TWAMP, including configuring the server and session-reflector.

#### Context

TWAMP applies to scenarios where statistics on IP network performance, such as the packet loss rate, jitter, and delay, need to be quickly obtained but not necessarily be highly accurate.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, a Huawei device can function either as the server or session-reflector. To implement TWAMP, ensure that devices that can function as the control-client and session-sender exist on the network.




#### Pre-configuration Tasks

Before configuring TWAMP, complete the following tasks:

* Ensure that some devices on the live network can function as the control-client and session-sender and comply with relevant standards.
* Ensure that the control-client and server are routable and the IP link between them works properly.


#### Data Preparation

To configure TWAMP, you need the following data.

| No. | Data |
| --- | --- |
| 1 | (Optional) TCP port number and inactive interval for a control session |
| 2 | (Optional) Inactive interval for a test session |



[Configuring the Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_twamp_cfg_0006.html)

This section describes how to configure the TWAMP server, which responds to the control-client's request for establishing, starting, or stopping a TWAMP session.

[Configuring the Session-Reflector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_twamp_cfg_0007.html)

This section describes how to configure the Session-Reflector. The Session-Reflector replies to the probes sent by the Session-Sender after being notified by the Server. 

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_twamp_cfg_0008.html)

After configuring TWAMP, verify the configuration.