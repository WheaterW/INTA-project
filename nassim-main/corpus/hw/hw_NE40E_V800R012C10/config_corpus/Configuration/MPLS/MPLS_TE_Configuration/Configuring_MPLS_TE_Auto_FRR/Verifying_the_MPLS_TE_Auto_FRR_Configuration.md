Verifying the MPLS TE Auto FRR Configuration
============================================

After configuring MPLS TE Auto FRR, you can view detailed information about the bypass tunnel.

#### Prerequisites

MPLS TE Auto FRR has been configured.


#### Procedure

* Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) **verbose** command to check the binding of a primary tunnel and an automatic bypass tunnel.
* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command to check detailed information about an automatic bypass tunnel.
* Run the [**display mpls te tunnel path**](cmdqueryname=display+mpls+te+tunnel+path) command to check information about paths of a primary or bypass tunnel.