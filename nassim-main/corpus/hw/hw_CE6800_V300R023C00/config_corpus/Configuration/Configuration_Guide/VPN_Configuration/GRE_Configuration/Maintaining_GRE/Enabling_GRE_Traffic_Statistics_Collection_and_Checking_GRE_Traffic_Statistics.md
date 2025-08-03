Enabling GRE Traffic Statistics Collection and Checking GRE Traffic Statistics
==============================================================================

Enabling GRE Traffic Statistics Collection and Checking GRE Traffic Statistics

#### Context

To check the network status or locate network faults, you can enable the GRE traffic statistics collection function so that such statistics can be checked.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a tunnel interface.
   
   
   ```
   [interface tunnel](cmdqueryname=interface+tunnel) interface-number
   ```
3. Enable the GRE traffic statistics collection function.
   
   
   ```
   [statistics enable](cmdqueryname=statistics+enable)
   ```
   
   By default, the traffic statistics collection function is disabled on a tunnel interface.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
5. Check traffic statistics on GRE tunnel interfaces.
   
   
   ```
   [display interface tunnel](cmdqueryname=display+interface+tunnel)
   ```