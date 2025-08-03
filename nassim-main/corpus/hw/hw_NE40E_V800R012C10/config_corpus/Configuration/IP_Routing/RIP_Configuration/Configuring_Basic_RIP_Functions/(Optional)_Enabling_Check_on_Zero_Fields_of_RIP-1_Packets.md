(Optional) Enabling Check on Zero Fields of RIP-1 Packets
=========================================================

Certain fields in RIP-1 packets must be 0, and these fields
are called zero fields.

#### Context

Certain fields in RIP-1 packets must be 0, and RIP-2 packets
contain no zero fields.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**checkzero**](cmdqueryname=checkzero)
   
   
   
   The check on zero fields of RIP-1 packets is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.