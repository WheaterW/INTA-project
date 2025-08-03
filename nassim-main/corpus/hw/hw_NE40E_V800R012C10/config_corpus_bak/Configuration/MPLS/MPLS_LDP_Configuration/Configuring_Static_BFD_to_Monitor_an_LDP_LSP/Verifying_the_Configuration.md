Verifying the Configuration
===========================

After configuring BFD to monitor an LDP LSP, verify the configurations of the BFD session, such as the session type and status.

#### Prerequisites

Static BFD used to monitor an LDP LSP has been configured.
#### Procedure

* Run the [**display bfd session**](cmdqueryname=display+bfd+session+all+static+dynamic+discriminator+verbose) { **all** | **static** | **dynamic** | **discriminator** *discr-value* } [ **verbose** ] command to check information about BFD sessions.
* Run the [**display bfd statistics
  session**](cmdqueryname=display+bfd+statistics+session+all+static+dynamic+discriminator) { **all** | **static** | **dynamic** | **discriminator** *discr-value* | **peer-ip** *peer-ip* } command to check statistics about BFD sessions.