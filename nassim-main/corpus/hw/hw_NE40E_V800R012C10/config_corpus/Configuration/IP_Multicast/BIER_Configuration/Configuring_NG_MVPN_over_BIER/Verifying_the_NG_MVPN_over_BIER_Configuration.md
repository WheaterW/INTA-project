Verifying the NG MVPN over BIER Configuration
=============================================

After configuring NG MVPN over BIER, verify the configuration.

#### Prerequisites

NG MVPN over BIER has been configured.


#### Procedure

* Run the [**display bier prefix**](cmdqueryname=display+bier+prefix) [ *prefix-ip* ] [ **igp-type isis originate-systemid** *originate-system-id* ] [ **sub-domain** *id* [ **bsl** { 64 | 128 | 256 } ] ] command to check BIER prefix configurations.
* Run the [**display bier sub-domain**](cmdqueryname=display+bier+sub-domain) [ *id* ] command to check information about configured BIER sub-domains.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) { **vpn-instance** *vpn-instance-name* | **all-instance** } **ipmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command to check configurations of I-PMSI tunnels used to carry MVPN services of a specified VPN instance.
* Run the [**display mvpn**](cmdqueryname=display+mvpn) { **vpn-instance** *vpn-instance-name* | **all-instance** } **spmsi** [ **verbose** [ *grpAddr* | *srcAddr* ] \* ] command to check configurations of S-PMSI tunnels used to carry MVPN services of a specified VPN instance.
* Run the [**display bier routing-table**](cmdqueryname=display+bier+routing-table) [ **sub-domain** *id* [ **prefix** *prefix-ip* ] ] command to check BIER routing information.