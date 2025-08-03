Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) { **all** { [ **for-ip** ] | **for-ipv6** } | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-name* ] | **default-ip** } | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-name* ] | **static** { [ **for-ip** ] | **for-ipv6** } | **static-auto** } command to check BFD session statistics.
* Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) command to check global BFD statistics.
* Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) { **all** { [ **for-ip** ] | **for-ipv6** } | **discriminator** *discr-value* | **dynamic** | **peer-ip** { *peer-ip* [ **vpn-instance** *vpn-instance-name* ] | **default-ip** } | **peer-ipv6** *peer-ipv6* [ **vpn-instance** *vpn-instance-name* ] | **static** { [ **for-ip** ] | **for-ipv6** } | **static-auto** } command to check BFD session statistics.