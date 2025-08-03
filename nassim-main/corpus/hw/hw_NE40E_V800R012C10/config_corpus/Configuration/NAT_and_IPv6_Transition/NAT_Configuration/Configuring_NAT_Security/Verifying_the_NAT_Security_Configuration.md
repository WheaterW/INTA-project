Verifying the NAT Security Configuration
========================================

After configuring the NAT security functions, you can run **display** commands to check the configuration.

#### Prerequisites

NAT security functions have been configured.


#### Procedure

* Run the [**display nat flow-defend**](cmdqueryname=display+nat+flow-defend) { **forward** | **reverse** | **fragment** } **rate** [ **slot** *slot-id* ] command to check the configured limit on the rate at which the first packet is sent to create sessions.
* Run the [**display nat user-information**](cmdqueryname=display+nat+user-information) command to check NAT user information.
* Run the [**display nat flow-defend reverse-blacklist**](cmdqueryname=display+nat+flow-defend+reverse-blacklist) **slot** *slot-id* command to check blacklist entry about the first reverse packet on a CPU of the dedicated board.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.