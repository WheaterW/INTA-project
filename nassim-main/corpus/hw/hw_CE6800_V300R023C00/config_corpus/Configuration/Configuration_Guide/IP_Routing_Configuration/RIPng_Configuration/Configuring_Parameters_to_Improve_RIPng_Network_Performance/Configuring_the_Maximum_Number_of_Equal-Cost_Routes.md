Configuring the Maximum Number of Equal-Cost Routes
===================================================

Configuring the Maximum Number of Equal-Cost Routes

#### Context

You can configure the maximum number of equal-cost RIPng routes in order to adjust the number of routes for load balancing.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIPng process and enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
3. Configure the maximum number of equal-cost routes.
   
   
   ```
   [maximum load-balancing](cmdqueryname=maximum+load-balancing) number
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```