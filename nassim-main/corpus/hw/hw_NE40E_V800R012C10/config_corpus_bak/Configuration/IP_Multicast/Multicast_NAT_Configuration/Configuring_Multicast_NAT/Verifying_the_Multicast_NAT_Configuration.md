Verifying the Multicast NAT Configuration
=========================================

After configuring multicast NAT, verify the configuration.

#### Prerequisites

Multicast NAT has been configured.


#### Procedure

* Run the [**display multicast-nat instance**](cmdqueryname=display+multicast-nat+instance) command to check information about the multicast NAT instance, including the outbound interfaces to which the instance is bound and the characteristics of the post-translation multicast streams.
* Run the [**display this**](cmdqueryname=display+this) command in the interface view to check the traffic policy configuration on the inbound interface of multicast streams.