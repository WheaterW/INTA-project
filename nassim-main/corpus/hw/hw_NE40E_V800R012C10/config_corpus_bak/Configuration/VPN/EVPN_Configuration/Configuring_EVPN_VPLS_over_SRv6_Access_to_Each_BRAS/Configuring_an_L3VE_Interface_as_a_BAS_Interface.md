Configuring an L3VE Interface as a BAS Interface
================================================

Configure an L3VE interface on a vBRAS-pUP as a BAS interface to implement BRAS access.

#### Context

A BAS interface on a vBRAS-pUP can be configured in either of the following modes:

* The BAS interface configuration is performed on the vBRAS-pUP and applies to scenarios where CU separation is not deployed.
* The BAS interface configuration is delivered by a vBRAS-CP to the vBRAS-pUP in the southbound direction. This configuration applies to CU separation scenarios.


#### Procedure

* Directly perform configurations on the vBRAS-pUP. For configuration details, see [Configuring PPPoE Access](../ne/dc_ne_pppoe_cfg_0004.html).
* Configure a vBRAS-CP to deliver the configurations to the vBRAS-pUP through a southbound interface. In this case, the vBRAS-UP configurations need to be completed on the vBRAS-CP and delivered to the vBRAS-pUP through a southbound channel. For details, see VNE 9000 (vBRAS-CP) Product Documentation > Configuration Guide > User Access Configuration > PPPoE Access Configuration.