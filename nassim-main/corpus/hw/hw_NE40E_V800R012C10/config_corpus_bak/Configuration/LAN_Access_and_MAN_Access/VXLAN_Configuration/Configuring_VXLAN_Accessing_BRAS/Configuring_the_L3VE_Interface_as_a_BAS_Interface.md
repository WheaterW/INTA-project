Configuring the L3VE Interface as a BAS Interface
=================================================

Configure the L3VE interface on the pUP as a BAS interface for BRAS access.

#### Context

A BAS interface on a pUP can be configured in either of the following modes:

* The BAS interface is directly configured on the pUP. This mode applies to scenarios where CU separation is not deployed.
* The BAS interface configurations are delivered by a CP to the pUP. This mode applies to CU separation scenarios.


#### Procedure

* Directly perform configurations on the pUP. For detailed configurations, see [Configuring PPPoE Access](../ne/dc_ne_pppoe_cfg_0004.html).
* Use a CP to deliver configurations to the pUP. In this case, the UP plane configurations need to be completed on the CP and delivered to the pUP through a southbound channel. For detailed configurations, see VNE 9000 (vBRAS-CP) Product Documentation > CU Separation Configuration > User Access Configuration > PPPoE Access Configuration.