Configuring a Dynamic Load Balancing Mode
=========================================

Configuring a Dynamic Load Balancing Mode

#### Context

Traditional static load balancing cannot balance the usage of member links, leading to congestion or even packet discarding on some member links in scenarios involving a large amount of data flows. After the dynamic load balancing function is enabled, traffic of an Eth-Trunk is dynamically load balanced over its member links, ensuring evenly load balanced traffic.

![](public_sys-resources/note_3.0-en-us.png) 

Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ support dynamic load balancing modes.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a dynamic load balancing profile and enter the dynamic load balancing profile view, or enter the view of an existing dynamic load balancing profile.
   
   
   ```
   [load-balance profile dynamic](cmdqueryname=load-balance+profile+dynamic) profile-name
   ```
   
   By default, the system defines a dynamic load balancing profile named **default**, which can be modified but not deleted.
3. Configure a dynamic load balancing mode for an Eth-Trunk interface.
   
   
   ```
   [eth-trunk mode](cmdqueryname=eth-trunk+mode) { spray | fixed | eligible [ flowlet-gap-time gap-time ] }
   ```
   
   
   
   By default, the dynamic load balancing mode of an Eth-Trunk interface is **eligible** (a recommended mode), and the interval for sending packets in a flowlet is 1000 microseconds.
4. Return to the system view and enter the Eth-Trunk interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
5. Apply the dynamic load balancing profile to the Eth-Trunk interface.
   
   
   ```
   [load-balance dynamic profile](cmdqueryname=load-balance+dynamic+profile) profile-name
   ```
   
   
   
   By default, no dynamic load balancing profile is applied to an Eth-Trunk interface.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display load-balance profile dynamic**](cmdqueryname=display+load-balance+profile+dynamic) [ *profile-name* ] command to view detailed information about a specified dynamic load balancing profile.