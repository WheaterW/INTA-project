Resetting a GMPLS UNI Tunnel
============================

Resetting a GMPLS UNI tunnel can make tunnel configurations to take effect immediately.

#### Context

If the path within a transport network is re-planned, and configurations on the ingress EN do not change, you can run the following command to reset a GMPLS UNI tunnel. UNI LSPs are re-established according to the new path.


#### Procedure

* Run the [**reset mpls te gmpls tunnel**](cmdqueryname=reset+mpls+te+gmpls+tunnel) *gmpls-tunnel-name* command to reset a GMPLS UNI tunnel.