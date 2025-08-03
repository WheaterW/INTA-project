Configuring Route or Tunnel Recursion Flapping Suppression
==========================================================

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low-latency mode does not support this configuration.


#### Prerequisites

Before configuring route or tunnel recursion flapping suppression, you have completed the following task:

* Set data link layer protocol parameters and IPv4 addresses for interfaces to ensure that the data link layer protocol status on each interface is up.

#### Context

When a recursive route or tunnel frequently flaps, services that depend on the route or tunnel are re-diverted again, triggering repeated route updates. As a result, CPU usage keeps increasing. To address this problem, enable route or tunnel recursion flapping suppression. After this function is enabled, route or tunnel recursion is performed after a specified delay, which reduces route update frequency and CPU usage. To set the delay, run the [**route recursive-lookup delay**](cmdqueryname=route+recursive-lookup+delay) command.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable route or tunnel recursion flapping suppression.
   ```
   [undo route recursive-lookup delay disable](cmdqueryname=undo+route+recursive-lookup+delay+disable)
   ```
   
   By default, route or tunnel recursion flapping suppression is enabled.
3. Set a delay for route or tunnel recursion.
   ```
   [route recursive-lookup delay](cmdqueryname=route+recursive-lookup+delay) start-time start-time increase-time increase-time max-time max-time
   ```
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **|** **include** **route recursive-lookup delay** command to check the configuration.