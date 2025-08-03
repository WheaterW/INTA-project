(Optional) Enabling Check on Zero Fields of RIPng Packets
=========================================================

Certain fields in RIPng packets must be 0, and these fields
are called zero fields.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
   
   
   
   The RIPng process is created, and the RIPng view is displayed.
3. Run [**checkzero**](cmdqueryname=checkzero)
   
   
   
   The check on zero fields of RIPng packets is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   submitted.