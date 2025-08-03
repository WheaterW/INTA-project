Enabling Private-and-Public-Network Separation for MPLS Services
================================================================

This section describes how to configure private-and-public-network separation for MPLS services.

#### Context

When both VPLS and MPLS services are configured, private-and-public-network separation for MPLS services triggers the generation of a FES table on the forwarding plane to implement the separation of the private and public networks for MPLS services. This function helps improve convergence performance if a tunnel fails.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls multistep separate enable**](cmdqueryname=mpls+multistep+separate+enable)
   
   
   
   Private-and-public-network separation is enabled for MPLS services.
   
   
   
   Before running this command, run the [**mpls vpls convergence separate enable**](cmdqueryname=mpls+vpls+convergence+separate+enable) command to enable VPLS public-and-private network decoupling.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.