Verifying the Configuration
===========================

After configuring PMTUs, verify the configuration.

#### Prerequisites

PMTUs have been configured.


#### Procedure

1. Run the [**display ipv6 pathmtu**](cmdqueryname=display+ipv6+pathmtu+vpn-instance+all+dynamic+static) [ **vpn-instance** *vpn-instance-name* ] { *ipv6-address* | **all** | **dynamic** | **static** } command to check all PMTU entries.
2. Run the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface+brief) [ *interface-type* *interface-number* | **brief** ] command to check the current MTU on an interface.