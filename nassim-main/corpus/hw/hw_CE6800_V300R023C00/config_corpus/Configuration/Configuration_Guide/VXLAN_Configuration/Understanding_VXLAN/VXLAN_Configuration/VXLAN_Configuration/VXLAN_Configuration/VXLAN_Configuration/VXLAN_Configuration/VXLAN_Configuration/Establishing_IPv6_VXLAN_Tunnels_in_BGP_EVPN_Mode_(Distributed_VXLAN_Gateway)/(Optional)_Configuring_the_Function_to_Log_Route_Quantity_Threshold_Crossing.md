(Optional) Configuring the Function to Log Route Quantity Threshold Crossing
============================================================================

(Optional) Configuring the Function to Log Route Quantity Threshold Crossing

#### Context

In IPv6 distributed VXLAN gateway scenarios, EVPN serves as the control plan to deliver routes. As more and more hosts access the gateway, the number of routes stored on the control plane greatly increases, consuming significant memory resources. To address this issue, you can configure the function to log route quantity threshold crossing. After the function is configured, a user log is generated when the number of routes exceeds the threshold.


#### Procedure

* Set a threshold and log recovery percentage for the number of EVPN routes.
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
  4. Set a threshold and log recovery percentage for the number of EVPN routes.
     
     
     ```
     [alarm-threshold route](cmdqueryname=alarm-threshold+route) route-number [ recovery-percentage percentage ]
     ```
     
     By default, the threshold and log recovery percentage for the number of EVPN routes are not configured.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Set a threshold and log recovery percentage for the number of VPN routes.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Set a threshold and log recovery percentage for the number of VPN routes.
     
     
     ```
     [alarm-threshold route](cmdqueryname=alarm-threshold+route) route-number [ recovery-percentage percentage ] { ipv4 | ipv6 } vpn-instance vpn-instance-name
     ```
     
     By default, the threshold and log recovery percentage for the number of VPN routes are not configured.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```