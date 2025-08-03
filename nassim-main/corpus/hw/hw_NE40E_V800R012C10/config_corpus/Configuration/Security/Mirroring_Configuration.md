Mirroring Configuration
=======================

Mirroring helps you monitor a network and troubleshoot
faults.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The mirroring feature may be used to analyze the communication information of terminal customers for a maintenance purpose. Before enabling the mirroring function, ensure that it is performed within the boundaries permitted by applicable laws and regulations. Effective measures must be taken to ensure that information is securely protected.



[Overview of Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0001.html)

With the mirroring function, you can observe the traffic on a specific interface for locating faults on the network by obtaining packets sent to or received by the interface.

[Configuration Precautions for Mirroring](../../../../software/nev8r10_vrpv8r16/user/spec/Mirroring_limitation.html)



[Configuring Port Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0003.html)

Port mirroring enables a device to copy the traffic on a specified port (mirrored port) to an observing port for analysis, so that you can determine the traffic status of the mirrored port.

[Configuring Flow Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0009.html)

You can configure flow mirroring to copy the traffic of a specified type on the mirrored port to the observing port for analysis, thereby learning about the status of such traffic on the mirrored port.

[Configuring Flow Mirroring Based on the Option 82 Information of User Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0029.html)

This section describes how to configure flow mirroring based on the Option 82 information of user packets. This configuration enables a device to copy user packets carrying specified Option 82 information to the specified observing port for analysis. You can then determine the traffic status.

[Maintaining Mirroring Statistics](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0034.html)



[Configuration Examples for Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0018.html)

This section provides examples for configuring port mirroring and flow mirroring in typical scenarios. It covers networking requirements, configuration roadmaps, data preparations, and corresponding configuration files.