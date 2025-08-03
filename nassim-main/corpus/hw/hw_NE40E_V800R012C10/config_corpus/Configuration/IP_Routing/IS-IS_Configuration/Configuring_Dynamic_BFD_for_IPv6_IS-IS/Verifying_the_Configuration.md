Verifying the Configuration
===========================

After configuring dynamic IPv6 BFD for IS-IS, check information about the BFD session and dynamic BFD for IS-IS on an interface.

#### Prerequisites

Dynamic IPv6 BFD for IS-IS has been configured.


#### Procedure

* Run the [**display isis ipv6 bfd**](cmdqueryname=display+isis+ipv6+bfd) [ *process-id* | **vpn-instance** *vpn-instance-name* ] **session** { **all** | **peer** *ipv6-address* | **interface** *interface-type* *interface-number* } command to check information about BFD sessions.
* Run the [**display isis ipv6
  bfd**](cmdqueryname=display+isis+ipv6+bfd) [ *process-id* | **vpn-instance** *vpn-instance-name* ] **interface** command to check BFD configurations on an interface.