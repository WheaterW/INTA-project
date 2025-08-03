Improving DCN Security
======================

To improve DCN security, you can configure an alarm threshold for the number of NEs connected to a GNE, SSL authentication, and OSPF interface authentication, and optimize DCN routes on all NEs.

#### Usage Scenario

You can improve DCN security through the following methods:

* Configure an alarm threshold for the number of NEs connected to the GNE to prevent the GNE from being overloaded with NEs. When the number of NEs connected to the GNE reaches the alarm threshold, the GNE will send a trap to its interworking NMSs.
* Configure Secure Sockets Layer (SSL) authentication and OSPF interface authentication to improve DCN network security through the encryption and authentication mechanisms.
* Configure OSPF parameters as required to optimize DCN routes.
* Adjust the forwarding priority of DCN packets as required to improve network stability.
* Configure an ACL-based DCN policy to be used to filter DCN packets.

#### Pre-configuration Tasks

Before configuring related functions to improve DCN security, enable DCN globally.


[Configuring an Alarm Threshold for the Number of NEs Connected to a GNE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0047.html)

To prevent a GNE from being overloaded with NEs, configure an alarm threshold for the number of NEs connected to the GNE. When the number of NEs connected to the GNE reaches the alarm threshold, the GNE will send a trap to its interworking NMSs.

[Configuring SSL Authentication on a GNE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0048.html)

After Secure Sockets Layer (SSL) authentication is configured on a GNE, the GNE can communicate with its interworking NMSs only when the exchanged packets are authenticated.

[Binding a DTLS Policy to a GNE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0111.html)

After a DTLS policy is bound to a GNE in the DCN view, the NMS can communicate with the GNE only after the policy is authenticated.

[Configuring OSPF Interface Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0049.html)

A DCN runs OSPF and supports packet authentication. After an authentication mode is specified, NEs accept only the OSPF packets that have been authenticated. If packets fail to be authenticated, neighbor relationships cannot be established.

[Optimizing DCN Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0050.html)

To improve DCN performance, configure OSPF functions.

[Configuring a Forwarding Priority for DCN Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0054.html)

If DCN packets are carried by IP packets, the forwarding priority of the DCN packets is lower than other packets. In this scenario, configure a forwarding priority, based on which a GNE forwards the DCN packets.

[Configuring an ACL-based DCN Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0056.html)

An ACL-based DCN policy can be used to filter DCN packets. The DCN packets that fail to match the ACL rule are discarded, improving DCN network security.

[Disabling Fast DCN Session Restart Triggered by DCN PPPoE Terminate Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0058.html)

Disabling fast DCN session restart triggered by DCN PPPoE Terminate packets prevents such packets from being used to launch an attack, which improves device reliability.

[Configuring Encryption for the Channel Between a GNE and an NE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0059.html)

To prevent malicious attacks and improve security, configure encryption for the channel between the specified GNE and NE.

[(Optional) Configuring Whitelist Session-CAR for QX TCP Connections](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0065.html)

You can configure whitelist session-CAR for QX TCP Connections to limit the rate of sessions. This configuration prevents bandwidth preemption among QX TCP sessions if traffic bursts occur.

[(Optional) Configuring Whitelist Session-CAR for QX UDP Connections](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0066.html)

You can configure whitelist session-CAR for QX UDP Connections to limit the rate of sessions. This configuration prevents bandwidth preemption among QX UDP sessions if traffic bursts occur.

[Verifying the DCN Security Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0051.html)

After configuring related functions to improve DCN security, verify the configuration.