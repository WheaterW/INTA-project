Configuring BGP Adaptive Routing
================================

Configuring BGP Adaptive Routing

#### Context

In a direct connection topology scenario, to enable a BGP device to adaptively adjust forwarding paths based on network topology and traffic load changes, you can configure the adaptive routing function.

![](public_sys-resources/note_3.0-en-us.png) 

This function is supported only by the following: CE6866, CE6860-HAM, CE6866K, CE6860-SAN, CE6885, CE6885-T, CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-LL (low latency mode), CE6855-48XS8CQ, CE8851K, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure BGP adaptive routing to automatically adjust traffic forwarding paths based on network topology and traffic load changes.
   
   
   ```
   [load-balancing adaptive-routing](cmdqueryname=load-balancing+adaptive-routing)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configuration is complete, check the configuration in the diagnostic view.

* Run the [**display bgp component**](cmdqueryname=display+bgp+component) **BGP\_RM\_IPV4** *99* **vpn-instance** *vpn-instance-name* command to check ECMP-group prefix information.
* Run the [**display bgp component**](cmdqueryname=display+bgp+component) **BGP\_RM\_IPV4** *100* **vpn-instance** *vpn-instance-name* command to check ECMP-group information.