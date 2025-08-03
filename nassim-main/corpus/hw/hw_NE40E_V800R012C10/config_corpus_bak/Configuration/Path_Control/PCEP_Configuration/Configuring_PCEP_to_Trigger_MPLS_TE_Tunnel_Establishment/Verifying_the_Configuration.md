Verifying the Configuration
===========================

After configuring PCE client functions, you can check PCEP session information and PCEP statistics to verify the configuration.

#### Prerequisites

All PCE client configurations have been completed.


#### Procedure

* Run the [**display pce protocol session**](cmdqueryname=display+pce+protocol+session) [ *ip-address* | **verbose** ] command to check PCEPv4 session information.
* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command to check PCE delegation type of the TE tunnel.