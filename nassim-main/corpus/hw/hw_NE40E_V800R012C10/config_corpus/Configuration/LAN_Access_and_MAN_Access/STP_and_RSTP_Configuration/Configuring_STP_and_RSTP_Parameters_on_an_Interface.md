Configuring STP/RSTP Parameters on an Interface
===============================================

A feedback mechanism is provided to confirm topology convergence. Thus, rapid convergence is implemented for Rapid Spanning Tree Protocol (RSTP).

#### Applicable Environment

On some specific networks, RSTP parameters will affect the speed of network convergence. Configuring proper RSTP parameters is required.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The default configurations of the parameters described in this section help implement RSTP rapid convergence. Therefore, the configuration process and all involved procedures described in this section are optional. You can perform some of the configurations as required.


[**Pre-configuration Tasks**](cmdqueryname=Pre-configuration+Tasks)Before configuring STP/RSTP parameters, complete the following task:

* [Configuring basic STP/RSTP functions](dc_vrp_stp_cfg_0004.html)


[Configuring System Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0014.html)

STP/Rapid Spanning Tree Protocol (RSTP) parameters that may affect network convergence include the network diameter, hello time, and timeout period for waiting for Bridge Protocol Data Units (BPDUs) from the upstream (3 x hello time x time factor). Therefore, STP/RSTP parameters need to be set properly to help implement rapid network convergence.

[Configuring Port Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0015.html)

Port parameters that may affect Rapid Spanning Tree Protocol (RSTP) topology convergence include the link type and maximum number of sent Bridge Protocol Data Units (BPDUs). Proper port parameters help RSTP to implement rapid topology convergence.

[Verifying the STP/RSTP Parameter Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0016.html)

After configuring STP/Rapid Spanning Tree Protocol (RSTP) parameters that affect the topology convergence, verify the configuration