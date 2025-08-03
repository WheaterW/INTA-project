Enabling Microsegmentation
==========================

Enabling Microsegmentation

#### Context

You must enable microsegmentation before configuring microsegmentation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable microsegmentation.
   
   
   ```
   [traffic-segment enable](cmdqueryname=traffic-segment+enable)
   ```
   
   By default, microsegmentation is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```