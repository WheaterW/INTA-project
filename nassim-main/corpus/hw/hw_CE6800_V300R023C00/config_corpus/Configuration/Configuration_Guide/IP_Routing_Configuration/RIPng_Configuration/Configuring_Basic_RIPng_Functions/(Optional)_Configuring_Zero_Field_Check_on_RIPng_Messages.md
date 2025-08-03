(Optional) Configuring Zero Field Check on RIPng Messages
=========================================================

(Optional) Configuring Zero Field Check on RIPng Messages

#### Context

Certain fields in RIPng messages must be 0, and these fields are called zero fields. By default, RIPng checks the zero fields of received messages and discards the messages in which any of the zero fields is not 0.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIPng process and enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
3. Configure zero field check on RIPng messages.
   
   
   ```
   [checkzero](cmdqueryname=checkzero)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```