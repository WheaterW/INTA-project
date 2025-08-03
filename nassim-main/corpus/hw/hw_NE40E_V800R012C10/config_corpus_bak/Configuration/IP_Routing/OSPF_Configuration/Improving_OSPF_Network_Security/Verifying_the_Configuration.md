Verifying the Configuration
===========================

After configuring OSPF functions to improve OSPF network security, check the configuration.

#### Prerequisites

The configurations of improving the security of an OSPF network are complete.


#### Procedure

* Run the [**display ospf**](cmdqueryname=display+ospf+brief) [ *process-id* ] **brief** command to check brief OSPF information. The command output shows the authentication configuration of the OSPF area. The **Authtype** field in the command output indicates the authentication mode.
* Run the [**display this**](cmdqueryname=display+this) command in the interface view to check the authentication configuration of the current interface.