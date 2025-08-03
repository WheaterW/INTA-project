Verifying the Configuration
===========================

Check the name of the tunnel policy applied to a VPN and the configurations of the tunnel policy.

#### Prerequisites

A tunnel policy has been configured for the backbone network of the BGP/MPLS IPv6 VPN.
#### Procedure

* Run the [**display tunnel-policy**](cmdqueryname=display+tunnel-policy) *policy-name* command to check the configurations of a specified tunnel policy.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** [ *vpn-instance-name* ] command to check the tunnel policy used by a VPN instance.