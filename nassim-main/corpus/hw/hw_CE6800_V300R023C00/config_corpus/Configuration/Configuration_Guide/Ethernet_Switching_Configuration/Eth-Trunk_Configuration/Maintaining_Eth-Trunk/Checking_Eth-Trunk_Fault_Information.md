Checking Eth-Trunk Fault Information
====================================

Checking Eth-Trunk Fault Information

#### Context

If an Eth-Trunk interface fails, such as a negotiation failure or status flapping occurs, or if LACP goes down, run the following commands in any view to check the reasons for failure. The command output helps you locate the failure.


#### Procedure

[Checking Eth-Trunk Fault Information](vrp_eth-trunk_cfg_0032.html) lists the commands for checking fault information about an Eth-Trunk interface.

**Table 1** Checking the reason for an Eth-Trunk interface failure
| Operation | Command |
| --- | --- |
| Check the reason for an Eth-Trunk interface failure. | **display eth-trunk troubleshooting** |
| Check the reason for LACP going down. | **display lacp troubleshooting** |