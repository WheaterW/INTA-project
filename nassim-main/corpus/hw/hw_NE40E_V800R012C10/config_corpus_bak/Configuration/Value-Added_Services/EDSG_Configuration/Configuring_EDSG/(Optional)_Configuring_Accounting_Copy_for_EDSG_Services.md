(Optional) Configuring Accounting Copy for EDSG Services
========================================================

This section describes how to enable the copy function
for EDSG service accounting packets in a user access domain.

#### Context

If the original accounting packet information of EDSG
services is required, a device must send EDSG service accounting packets
to a RADIUS copy server group as the original accounting information
in subsequent settlement.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**service-policy accounting-copy**](cmdqueryname=service-policy+accounting-copy) **radius-server** *group-name*
   
   
   
   EDSG service accounting copy is enabled, and a RADIUS copy
   server group is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.