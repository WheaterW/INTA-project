Configuring Route or Tunnel Recursion Suppression in Case of Flapping
=====================================================================

Configuring Route or Tunnel Recursion Suppression in Case of Flapping

#### Usage Scenario

In route or tunnel recursion scenarios, if a route or tunnel flaps frequently, services that depend on the route or tunnel perform recursion frequently, causing frequent route updates. As a result, the CPU usage of the system keeps increasing. To solve the problem, enable route or tunnel recursion suppression in case of flapping. The suppression reduces the route update frequency and the CPU usage. To configure suppression periods for route or tunnel recursion, run the [**route recursive-lookup delay**](cmdqueryname=route+recursive-lookup+delay) command.


#### Pre-configuration Tasks

Before configuring route or tunnel recursion suppression in case of flapping, complete the following tasks:

* Configure link layer protocol parameters and IPv4 addresses for interfaces and ensure that the link layer protocol of the interfaces is Up.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**undo route recursive-lookup delay disable**](cmdqueryname=undo+route+recursive-lookup+delay+disable)
   
   
   
   Route or tunnel recursion suppression in case of flapping is enabled.
   
   
   
   To disable route or tunnel recursion suppression in case of flapping, run the [**route recursive-lookup delay disable**](cmdqueryname=route+recursive-lookup+delay+disable) command.
3. (Optional) Run [**route recursive-lookup delay**](cmdqueryname=route+recursive-lookup+delay) **start-time** *start-time* **increase-time** *increase-time* **max-time** *max-time*
   
   
   
   Suppression periods are configured for route or tunnel recursion, including the initial suppression period, incremental suppression period since the second suppression, and the maximum suppression period.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **|** **include** **route recursive-lookup delay** command to check configurations.