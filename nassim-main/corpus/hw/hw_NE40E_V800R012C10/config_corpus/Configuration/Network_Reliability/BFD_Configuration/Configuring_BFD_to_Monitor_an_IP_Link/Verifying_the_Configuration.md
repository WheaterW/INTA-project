Verifying the Configuration
===========================

After configuring the BFD detection parameters, verify the configurations, including the minimum intervals at which BFD control packets are sent and received, WTR time, and description of the BFD session.

#### Prerequisites

BFD has been configured to monitor an IP link.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You can view statistics about a BFD session and information about the BFD session only after all BFD parameters are set and the BFD session is successfully set up.




#### Procedure

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** | **discriminator** *discr-value* | **dynamic** | **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] | **static** } [ **verbose** ] command to check information about BFD sessions.
* Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) command to check global BFD statistics.
* Run the [**display bfd statistics
  session**](cmdqueryname=display+bfd+statistics+session) { **all** | **static** | **dynamic** | **discriminator** *discr-value* | **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] } command to check statistics about BFD sessions.
* Run the [**display bfd interface**](cmdqueryname=display+bfd+interface) command to check information about BFD-enabled interfaces.