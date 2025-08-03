Verifying the Configuration
===========================

After configuring PCE client functions, you can check PCEP session information and PCEP statistics to verify the configuration.

#### Prerequisites

All PCE client configurations have been completed.


#### Procedure

* Run the [**display pce protocol session**](cmdqueryname=display+pce+protocol+session) [ *ip-address* | **verbose** ] command to check PCEPv4 session information.
* Run the [**display pce protocol srv6-te policy**](cmdqueryname=display+pce+protocol+srv6-te+policy)[ **endpoint** *ipv6-address***color** *color-value* ] command to check SRv6 TE Policy information reported by the PCE client to the PCE server.