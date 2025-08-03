Configuring MSTP Parameters on an Interface
===========================================

Multiple Spanning Tree Protocol (MSTP) implements Rapid Spanning Tree Protocol (RSTP) rapid convergence. To achieve rapid convergence, you need to configure proper MSTP parameters.

#### Applicable Environment

In some specific networks, MSTP parameters will affect the speed of network convergence. Configuring proper MSTP parameters is required.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The default parameters also can be used to complete MSTP rapid convergence. Therefore, the configuration procedures and steps in this command task are all optional.



#### Pre-configuration Tasks

Before configuring MSTP parameters, complete the following task:

* Configuring basic MSTP functions


[Configuring System Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0023.html)

Multiple Spanning Tree Protocol (MSTP) parameters that may affect network convergence include the network diameter, hello time, and timeout period for waiting for Bridge Protocol Data Units (BPDUs) from the upstream (3 x hello time x time factor). Configure proper MSTP parameters to implement rapid network convergence.

[Configuring Port Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0024.html)

Port parameters that may affect Multiple Spanning Tree Protocol (MSTP) topology convergence include the link type and maximum number of sent Bridge Protocol Data Units (BPDUs). Configure proper port parameters to implement rapid topology convergence.

[Verifying the MSTP Parameter Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0025.html)

After Multiple Spanning Tree Protocol (MSTP) parameters are configured, verify the configuration.