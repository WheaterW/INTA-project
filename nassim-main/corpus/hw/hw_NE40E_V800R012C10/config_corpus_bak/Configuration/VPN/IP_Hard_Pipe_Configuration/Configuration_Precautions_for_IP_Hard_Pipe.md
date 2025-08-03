Configuration Precautions for IP Hard Pipe
==========================================

Configuration_Precautions_for_IP_Hard_Pipe

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| After an MP2MP IP hard pipe is configured for a VPLS, the default MPLS differentiated services (DS) mode is pipe enhancement. The diffserv-mode command cannot be run with the pipe or shortpipe parameter specified. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| IP hard pipe and the DiffServ mode on an interface are mutually exclusive. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| For multipoint-to-multipoint IP hard pipe services, hard pipe CAR is performed on the upstream NP. Therefore, if AC interfaces reside on different NP modules (trunk member interfaces reside on different NP modules or multiple physical AC interfaces reside on different NP modules), the hard pipe bandwidth is doubled. | NE40E-M2 | NE40E-M2H |
| For an MP2MP IP hard pipe, the pipe attribute of a primary TE tunnel and that of a backup TE tunnel must be the same. That is, they are both soft pipes or both hard pipes. If a hard pipe configured using a command is iterated to a primary tunnel and backup tunnel whose hard pipe attributes are inconsistent, the involved PW does not take effect, and services are interrupted.  If E2E VPLS hard pipe deployment is recommended on the NMS, the preceding requirement does not apply. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| An MP2MP IP hard pipe supports TP OAM for TE to detect link faults and APS for TE to trigger link protection. However, TP OAM for VPLS PW and PW APS are not supported. If TP OAM for VPLS PW and PW APS are configured, the hard pipe function may be unavailable.  It is recommended that TE tunnel detection and protection be used for hard pipe link protection. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| An MP2MP IP hard pipe must be established over a static bidirectional co-routed TE tunnel (public-network tunnel), and the tunnel interface must have hard-pipe bandwidth specified. After a hard pipe is recursed to another tunnel, the PW does not take effect and services are interrupted.  Deploying VPLS hard pipes in E2E mode on the NMS is recommended. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| On an MP2MP IP hard pipe, multiple ACs communicate with multiple PWs. The hard-pipe bandwidth between the ACs and PWs cannot be checked. If the total bandwidth value of all AC interfaces in the same VSI exceeds the PW's hard-pipe bandwidth value, packets are lost.  A PW's hard-pipe bandwidth value must be greater than the total bandwidth value of all AC interfaces in the same VSI. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| An MP2MP IP hard pipe for rail transport and HQoS on an AC interface are mutually exclusive. If an AC interface has HQoS enabled, a VPLS hard pipe cannot be configured on the AC interface. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| The public network side of an MP2MP IP hard pipe does not support tunnel load balancing, and the tunnel interface must be unique. Otherwise, the VPLS hard pipe fails and bandwidth cannot be guaranteed.  If E2E VPLS hard pipe deployment is recommended on the NMS, the preceding requirement does not apply. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |
| If a VLL hard pipe and an MP2MP IP hard pipe co-exist on the same main interface, interface-based bandwidth check for the VLL hard pipe may be inaccurate.  Configuring a VLL hard pipe and an MP2MP IP hard pipe on different interfaces is recommended. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K |