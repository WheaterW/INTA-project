Disabling Master/Slave Main Control Board Switching Triggered by Unexpected OSPF LSA Aging
==========================================================================================

Disabling Master/Slave Main Control Board Switching Triggered by Unexpected OSPF LSA Aging

#### Prerequisites

Before disabling master/slave main control board switching triggered by unexpected OSPF LSA aging, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

If a local device's aging timer expires unexpectedly, the local device clears all router LSAs received from its neighbors, leading to large-scale route flapping and service interruption. To prevent this problem, master/slave main control board switching triggered by unexpected OSPF LSA aging is enabled by default, and is triggered to restore network connections and service traffic when the following condition is met: (Number of cleared router LSAs/Total number of router LSAs) x 100% â¥ 80% (Router LSAs are those sent by the neighboring devices to the local device)

If you do not require this function, perform the following steps.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable master/slave main control board switching triggered by unexpected OSPF LSA aging.
   
   
   ```
   [ospf maxage-lsa auto-protect disable](cmdqueryname=ospf+maxage-lsa+auto-protect+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **statistics maxage-lsa** command to check information about the router LSAs that have reached the maximum aging time.