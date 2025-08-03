Enabling Fast EBGP Peer Reset
=============================

Enabling Fast EBGP Peer Reset

#### Context

Fast EBGP peer reset is enabled by default so that EBGP can quickly detect the status of interfaces used to establish EBGP connections. If the interface status changes frequently, you can disable fast EBGP peer reset so that direct EBGP sessions will not be reestablished and deleted as interfaces alternate between up and down. This configuration speeds up network convergence.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Enable fast EBGP peer reset.
   
   
   ```
   [ebgp-interface-sensitive](cmdqueryname=ebgp-interface-sensitive)
   ```
   
   
   
   After this function is enabled, BGP4+ can rapidly detect EBGP link faults and reset BGP4+ peers on the interface immediately.
   
   If the interface on which a BGP4+ connection is established alternates between up and down, you can run the [**undo ebgp-interface-sensitive**](cmdqueryname=ebgp-interface-sensitive) command to prevent repeated reestablishment and deletion of the BGP4+ session caused by route flapping. This saves network bandwidth.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) [ *ipv6-address* ] **verbose** command to check detailed BGP4+ peer information.