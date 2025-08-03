(Optional) Configuring the Function to Log Route Quantity Threshold Crossing
============================================================================

(Optional) Configuring the Function to Log Route Quantity Threshold Crossing

#### Context

In distributed VXLAN gateway scenarios, EVPN implements control plane functions to deliver routes. As more and more hosts access the gateway, the number of routes stored on the control plane greatly increases, consuming significant memory resources. To address this issue, you can configure the function to log route quantity threshold crossing. After the function is configured, a user log is generated when the number of routes exceeds the threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view or BGP multi-instance view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
   ```
3. Enter the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
   
   
   ```
   [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
   ```
4. Set a log generation threshold and log recovery percentage for the number of EVPN routes.
   
   
   ```
   [alarm-threshold route](cmdqueryname=alarm-threshold+route) route-number [ recovery-percentage percentage ]
   ```
   
   By default, the log generation threshold and log recovery percentage for the number of EVPN routes are not configured.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```