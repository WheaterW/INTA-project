Verifying the Configuration of Distributed NAT for User Traffic
===============================================================

After configuring a NAT traffic policy, you can run **display** commands to check the configuration.

#### Prerequisites

NAT traffic policy has been configured.


#### Procedure

* Run the [**display nat instance**](cmdqueryname=display+nat+instance) [ *instance-name* ] command to check the configuration of a NAT instance.
* Run the [**display nat user-information**](cmdqueryname=display+nat+user-information) { **cpe** **ipv4** *ipv4-address* | **port-usage** *port-usage* | **session-discard** | **top-ten** | **domain** *domain-name* | **user-id** *user-id* | **user-name** *user-name*} [ **slot** *slot-id* ] [ **verbose** ] command to check NAT user information.