Verifying the Configuration of Communication Between the NMS and a Device Using NETCONF
=======================================================================================

After NETCONF is configured to allow the NMS to remotely manage device configurations, check detailed SSH session information, the SSH connection between the SSH server and client, and the capabilities that the server supports.

#### Prerequisites

NETCONF has been configured to manage device configurations.


#### Procedure

* Run the [**display ssh user-information**](cmdqueryname=display+ssh+user-information) *username* command on the SSH server (server) to check information about all SSH users or a specified one.
* Run the [**display local-user**](cmdqueryname=display+local-user) command to check the local user list.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **status** command on the SSH server to check its global configuration.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **session** command on the SSH server to check information about sessions between the SSH server and the SSH client (client).
* Run the [**display netconf capability**](cmdqueryname=display+netconf+capability) command to check the capabilities that the server supports.
* You can run the following commands to check NETCONF authorization information:
  
  
  + Run the [**display netconf authorization statistics**](cmdqueryname=display+netconf+authorization+statistics) command to check NETCONF authorization information.
  + Run the [**display netconf authorization task-group-rules**](cmdqueryname=display+netconf+authorization+task-group-rules)*task-group-name* [ **rule-name***rulename* ] command to check NETCONF authorization information based on a specified authorization task group.
  + Run the [**display netconf authorization user-group-rules**](cmdqueryname=display+netconf+authorization+user-group-rules)*user-group-name* [ **rule-name***rulename* ] command to check NETCONF authorization information based on a specified authorization user group.
* Run the [**display netconf session**](cmdqueryname=display+netconf+session) command to check information about all NETCONF sessions.
* Run the [**display netconfc session**](cmdqueryname=display+netconfc+session) [ **peer-id** *ap-id* ] command to check NETCONFC session information.