Verifying the Configuration
===========================

After configuring a tunnel policy for the backbone network of a BGP/MPLS IP VPN, check the name of and configurations of the tunnel policy.

#### Prerequisites

A tunnel policy has been configured for the backbone network of the BGP/MPLS IP VPN.


#### Procedure

* Run the [**display tunnel-policy**](cmdqueryname=display+tunnel-policy) *policy-name* command to check the configurations of a specified tunnel policy.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** [ *vpn-instance-name* ] command to check the tunnel policy used by a VPN instance.