Verifying the Configuration
===========================

After configuring the BIERv6 network, check the committed configurations and whether they have taken effect. In addition, perform ping operations to check the BIERv6 network connectivity, BFR reachability, and network performance indicators such as the packet loss rate and delay.

#### Procedure

* Run the [**display bier ipv6 sub-domain**](cmdqueryname=display+bier+ipv6+sub-domain) [ *id* ] command to check BIERv6 sub-domain information.
* Run the [**display bier ipv6 prefix**](cmdqueryname=display+bier+ipv6+prefix) [ *prefix-ipv6* ] [ **igp-type** **isis** [ *process-id* ] **originate-systemid** *originate-system-id* ] [ **sub-domain** *id* [ **bsl** { **64** | **128** | **256** } ] ] command to check BIERv6 prefix information.
* Run the [**display bier ipv6 routing-table**](cmdqueryname=display+bier+ipv6+routing-table) [ **sub-domain** *id* [ **bsl** { **64** | **128** | **256** } ] ] [ **prefix** *prefix-ipv6* ] [ **verbose** ] command to check BIERv6 routing information.
* Run the [**ping bier ipv6 sub-domain**](cmdqueryname=ping+bier+ipv6+sub-domain) *subDomainId* **bsl** { **64** | **128** | **256** } { **bfr-id** *bfrID* | **bfr-id-start** *bfrIdStartVal* **bfr-id-end** *bfrIdEndVal* } [ **network-slice***sliceid* [ **force-match-slice** ] ] [ **-a** *source-ip-address* | **-c** *count* | **-h** *ttl-value* | **-m** *interval* | **-t** *timeout* | **udp-port** *dstPort6* ] \* command to check BIERv6 network connectivity, BFR reachability, and performance indicators such as the packet loss rate and delay.
* Run the [**display bier ipv6 sub-domain**](cmdqueryname=display+bier+ipv6+sub-domain+preferred-prefix) *id* **preferred-prefix** [ *prefix-ipv*6 ] command to check configured BFR prefixes and preferred prefixes in the BIERv6 sub-domain.