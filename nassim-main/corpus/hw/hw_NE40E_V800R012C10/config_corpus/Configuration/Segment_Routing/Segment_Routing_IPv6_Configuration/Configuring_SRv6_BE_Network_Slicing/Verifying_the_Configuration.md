Verifying the Configuration
===========================

After configuring SRv6 BE network slicing, you can verify the configuration.

#### Prerequisites

SRv6 BE network slicing has been configured.


#### Procedure

1. Run the [**display network-slice bandwidth usage statistics interface**](cmdqueryname=display+network-slice+bandwidth+usage) { *ifname* | *iftype* *ifnum* } command to check the SRv6 network slice bandwidth usage on a specified interface.
2. Run the [**display network-slice flex-channel statistics slice-id**](cmdqueryname=display+network-slice+flex-channel+statistics) *sliceId* **interface** { *ifname* | *iftype* *ifnum* } command to check flow queue statistics about the slice with a specified ID on a specified interface.
3. Run the [**display network-slice**](cmdqueryname=display+network-slice) [ *slice-id* ] **binding-list** [ **interface** *ifIndex* ] command to check the binding relationships between base and network slice interfaces in a network slice instance.