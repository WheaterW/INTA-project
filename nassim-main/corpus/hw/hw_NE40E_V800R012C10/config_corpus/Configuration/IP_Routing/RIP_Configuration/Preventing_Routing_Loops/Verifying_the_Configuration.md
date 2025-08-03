Verifying the Configuration
===========================

After routing loop prevention is configured, you can view the current running status of RIP, information about interfaces, and RIP routing information.

#### Prerequisites

Routing loop prevention has been configured.
#### Procedure

* Run the [**display
  rip**](cmdqueryname=display+rip) [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check RIP running status and configuration.
* Run the [**display rip**](cmdqueryname=display+rip) *process-id* **route** command to check RIP routes.
* Run the [**display rip**](cmdqueryname=display+rip) *process-id* **interface** command to check information about RIP interfaces.