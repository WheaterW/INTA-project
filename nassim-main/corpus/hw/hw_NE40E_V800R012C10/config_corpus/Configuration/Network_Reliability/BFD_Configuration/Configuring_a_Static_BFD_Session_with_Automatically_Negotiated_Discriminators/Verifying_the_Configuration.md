Verifying the Configuration
===========================

After a static BFD session with automatically negotiated discriminators is successfully set up, verify the configurations, such as the type of the BFD session and automatically negotiated discriminators.

#### Prerequisites

A static BFD session with automatically negotiated discriminators has been configured.


#### Procedure

1. Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **static** | **dynamic** | **discriminator** *discr-value* | **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] } [ **verbose** ] command to check information about BFD sessions.
2. Run the [**display bfd interface**](cmdqueryname=display+bfd+interface) command to check information about BFD interfaces.