Using Tracert to Check a Path on an BIERv6 Network
==================================================

Tracert can be used to locate the failure point on a BIERv6 network, facilitating fault diagnosis.

#### Prerequisites

Before using the [**tracert bier ipv6**](cmdqueryname=tracert+bier+ipv6) command to locate the failure point on a BIERv6 network, ensure that a BIERv6 tunnel has been correctly configured.


#### Procedure

1. Run the [**tracert bier ipv6**](cmdqueryname=tracert+bier+ipv6) **sub-domain** *subDomainId* **bsl** { **64** | **128** | **256** } { **bfr-id** *bfrID* | **bfr-id-start** *bfrIdStartVal* **bfr-id-end** *bfrIdEndVal* } [ **-a** *source-ip-address* | **-f** *first-ttl-val* | **-m** *max-ttl-val* | **-w** *timeout* | **udp-port** *dstPort6* | **entropy** *entropy-val* ] \* command to discover the gateways through which packets to the destination BIERv6 device passes and locate the failure point on the BIERv6 network.
   
   
   ```
   <HUAWEI> tracert bier ipv6 sub-domain 1 bsl 64 bfr-id 152
     Tracert BIER IPv6: Subdomain ID: 1, BSL: 64, BFRID: 152, press CTRL_C to break
     TTL     Replier(BFR-ID)                                   Time      Type
     0                                                                   Ingress
     1       2001:DB8:1::1(152)                                516 ms    Egress
   ```
   
   
   
   In network slicing scenarios, run the [**tracert bier ipv6**](cmdqueryname=tracert+bier+ipv6) **sub-domain** *subDomainId* **bsl** { **64** | **128** | **256** } { **bfr-id** *bfrID* | **bfr-id-start** *bfrIdStartVal* **bfr-id-end** *bfrIdEndVal* } [ **network-slice***sliceid* [ **force-match-slice** ]] [ **-a** *source-ip-address* | **-f** *first-ttl-val* | **-m** *max-ttl-val* | **-w** *timeout* | **udp-port** *dstPort6* | **entropy** *entropy-val* ]\* command to discover the gateways through which packets to the destination BIERv6 device passes and locate the failure point on the BIERv6 network.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **force-match-slice** keyword is used to forcibly match network slices and takes effect only for segment lists with slice attributes.
   
   ```
   <HUAWEI> tracert bier ipv6 sub-domain 0 bsl 256 bfr-id 2 network-slice 20 force-match-slice 
     Tracert BIER IPv6: Subdomain ID: 0, BSL: 256, BFRID: 2, network-slice: 20, press CTRL_C to break
     TTL     Replier(BFR-ID)(Slice-ID)                                     Time      Type
     0                                                                               Ingress
     1       2001:DB8:40::1(-)(20)                                         5    ms   Transit
     2       2001:DB8:20::1(2)(20)                                         4    ms   Egress
   ```
2. (Optional) Run the following commands to configure functions related to BIERv6 Echo Request messages.
   
   
   * Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   * Run the [**nqa bier ipv6 receive rate-limit**](cmdqueryname=nqa+bier+ipv6+receive+rate-limit) *bierCpuLimit6* command to limit the rate at which BIERv6 Echo Request messages are sent to the main control board.
   * Run the [**nqa bier ipv6 udp-port**](cmdqueryname=nqa+bier+ipv6+udp-port) *udpPort6* command to set the UDP port number for receiving BIERv6 Echo Request packets.
   * Run the [**nqa bier ipv6 echo-reply disable**](cmdqueryname=nqa+bier+ipv6+echo-reply+disable) command to disable the function of responding to BIERv6 Echo Request packets.