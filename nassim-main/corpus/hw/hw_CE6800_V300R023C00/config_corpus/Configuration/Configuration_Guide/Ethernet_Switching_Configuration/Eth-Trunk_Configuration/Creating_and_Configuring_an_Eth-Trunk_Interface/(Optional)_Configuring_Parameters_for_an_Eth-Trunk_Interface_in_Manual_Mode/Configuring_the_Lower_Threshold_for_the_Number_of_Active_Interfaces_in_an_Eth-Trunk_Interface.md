Configuring the Lower Threshold for the Number of Active Interfaces in an Eth-Trunk Interface
=============================================================================================

Configuring the Lower Threshold for the Number of Active Interfaces in an Eth-Trunk Interface

#### Context

When the number of active interfaces falls below the lower threshold, the Eth-Trunk interface goes down. Configuring the lower threshold for the number of active interfaces in an Eth-Trunk ensures that the Eth-Trunk has the minimum required bandwidth. Determine whether to set this parameter based on the network plan. The default value is recommended in non link-redundancy networking scenarios. By default, the lower threshold for the number of active interfaces is 1.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
3. Configure the lower threshold for the number of active interfaces in the Eth-Trunk interface.
   
   
   ```
   [least active-linknumber](cmdqueryname=least+active-linknumber) link-number
   ```
   
   This parameter value can be different on local and peer devices, in which case the larger value is used.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```