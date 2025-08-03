Verifying the Configuration
===========================

After configuring packet loss ratio testing for a physical link, verify the configurations.

#### Prerequisites

Packet loss ratio testing has been configured.


#### Procedure

* Run the [**display efm session**](cmdqueryname=display+efm+session) { **all** | [**interface**](cmdqueryname=interface) *interface-type interface-number* } command to check the EFM OAM status of interfaces.
* Run the [**display test-packet result**](cmdqueryname=display+test-packet+result) command to check statistics about testing packets.