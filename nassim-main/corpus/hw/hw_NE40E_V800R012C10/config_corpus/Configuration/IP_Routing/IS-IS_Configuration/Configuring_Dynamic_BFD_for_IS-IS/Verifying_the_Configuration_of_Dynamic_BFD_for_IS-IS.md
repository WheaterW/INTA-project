Verifying the Configuration of Dynamic BFD for IS-IS
====================================================

After configuring dynamic BFD for IS-IS, check information about the BFD session and dynamic BFD for IS-IS on an interface.

#### Prerequisites

Dynamic BFD for IS-IS has been configured.


#### Procedure

* Run the [**display isis bfd**](cmdqueryname=display+isis+bfd) [ *process-id* | **vpn-instance** *vpn-instance-name* ] **session** { **peer** *ip-address* | **all** } command to view the information about the BFD session.
* Run the [**display isis bfd**](cmdqueryname=display+isis+bfd) [ *process-id* ] **interface** command to view the information about BFD on an interface.