Verifying the BOD Configuration
===============================

After configuring BOD, verify the configuration.

#### Procedure

* Run the [**display value-added-service policy**](cmdqueryname=display+value-added-service+policy) command to check value-added service policy information.
* Run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) command to check value-added service information.
* Run the [**display diameter-group bind-info**](cmdqueryname=display+diameter-group+bind-info) command to check the bindings between AAA domains and Diameter server groups.
* Run the [**display dhcp option-64 qos-profile**](cmdqueryname=display+dhcp+option-64+qos-profile) [ **domain** *domain-name* ] **configuration** command to check the Option 64 parsing mode configured in the system view or the AAA domain view.
* Run the [**display dhcp receive server-packet**](cmdqueryname=display+dhcp+receive+server-packet) [ **domain** *domain-name* ] **configuration** command to check whether the Router is enabled in the system view or the domain view to process ACK packets destined for gateways from a DHCP server.