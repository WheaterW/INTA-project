Configuring the Maximum Number of RIP Routes that Can Be Processed
==================================================================

Configuring the Maximum Number of RIP Routes that Can Be Processed

#### Context

You can configure the maximum number of RIP routes that can be processed in order to fully utilize network resources and improve network performance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure the maximum number of RIP routes that can be processed
   
   
   ```
   [maximum-routes](cmdqueryname=maximum-routes) max-number [ threshold threshold-value ]
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```