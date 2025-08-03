Verifying the Configuration
===========================

After configuring fast RIP convergence, check the running status of RIP, RIP routing information, all active routes in the RIP database, and information about interfaces.

#### Prerequisites

Fast RIP convergence has been configured.


#### Procedure

* Run the [**display
  rip**](cmdqueryname=display+rip) [ *process-id* | **vpn-instance** *vpn-instance-name* ] command to check RIP running status and configuration.
* Run the [**display rip**](cmdqueryname=display+rip) *process-id* **route** command to check RIP routes.
* Run the [**display rip**](cmdqueryname=display+rip) *process-id* **database** [ **verbose** ] command to check all active routes in the RIP database.
* Run the [**display rip**](cmdqueryname=display+rip) *process-id* **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check information about RIP interfaces.