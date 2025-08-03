Verifying the Configuration of IS-IS Local MT
=============================================

After configuring local MT, check the MIGP routing table, routing information, SPF tree, and IS-IS statistics.

#### Prerequisites

Local MT has been configured.


#### Procedure

* Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] **migp-routing** [*ip-address* [ *mask* | *mask-length* ] | [ **level-1** | **level-2** ] | **verbose** ]command to check the IS-IS MIGP routing table.