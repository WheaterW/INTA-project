Using Ping to Check BIERv6 Network Connectivity
===============================================

On a BIERv6 network, you can perform a ping operation to check network connectivity, BFR reachability, and performance indicators such as the packet loss rate and delay.

#### Prerequisites

Before using the [**ping bier ipv6**](cmdqueryname=ping+bier+ipv6) command to check connectivity of a BIERv6 network, ensure that a BIERv6 tunnel has been correctly configured.


#### Procedure

1. Run the [**ping bier ipv6**](cmdqueryname=ping+bier+ipv6) **sub-domain** *subDomainId* **bsl** { **64** | **128** | **256** } { **bfr-id** *bfrID* | **bfr-id-start** *bfrIdStartVal* **bfr-id-end** *bfrIdEndVal* } [ **-a** *source-ip-address* | **-c** *count* | **-h** *ttl-value* | **-m** *interval* | **-t** *timeout* | **udp-port** *dstPort6* ] \* command to check the connectivity, BFR reachability, packet loss rate, and delay of the BIERv6 network.
   
   
   ```
   <HUAWEI> ping bier ipv6 sub-domain 1 bsl 256 bfr-id 2
     Ping BIER IPv6: Subdomain ID: 1, BSL: 256, BFRID: 2, press CTRL_C to break
       Reply from BFRID: 2 (2001:DB8:1::1) 
         bytes=72 Sequence=1 time=10 ms
       Reply from BFRID: 2 (2001:DB8:1::1) 
         bytes=72 Sequence=2 time=4 ms
       Reply from BFRID: 2 (2001:DB8:1::1) 
         bytes=72 Sequence=3 time=4 ms
       Reply from BFRID: 2 (2001:DB8:1::1) 
         bytes=72 Sequence=4 time=4 ms
       Reply from BFRID: 2 (2001:DB8:1::1) 
         bytes=72 Sequence=5 time=4 ms
   
     --- Destination BFRID: 2 (2001:DB8:1::1) ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=4/5/10 ms
   ```
   
   
   
   In network slicing scenarios, run the [**ping bier ipv6**](cmdqueryname=ping+bier+ipv6) **sub-domain** *subDomainId* **bsl** { **64** | **128** | **256** } { **bfr-id** *bfrID* | **bfr-id-start** *bfrIdStartVal* **bfr-id-end** *bfrIdEndVal* } [ **network-slice***sliceid* [ **force-match-slice** ]] [ **-a** *source-ip-address* | **-c** *count* | **-h** *ttl-value* | **-m** *interval* | **-t** *timeout* | **udp-port** *dstPort6* ]\* command to check BIERv6 network connectivity, BFR reachability, and performance indicators such as the packet loss rate and delay.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **force-match-slice** keyword is used to forcibly match network slices and takes effect only for segment lists with slice attributes.
   
   ```
   <HUAWEI> ping bier ipv6 sub-domain 0 bsl 256 bfr-id 2 network-slice 20 force-match-slice
     Ping BIER IPv6: Subdomain ID: 0, BSL: 256, BFRID: 2, network-slice: 20, press CTRL_C to break
       Reply from BFRID: 2 (2001:DB8:20::1) Slice-ID:20
         bytes=116 Sequence=1 time=5 ms
       Reply from BFRID: 2 (2001:DB8:20::1) Slice-ID:20
         bytes=116 Sequence=2 time=3 ms
       Reply from BFRID: 2 (2001:DB8:20::1) Slice-ID:20
         bytes=116 Sequence=3 time=3 ms
       Reply from BFRID: 2 (2001:DB8:20::1) Slice-ID:20
         bytes=116 Sequence=4 time=5 ms
       Reply from BFRID: 2 (2001:DB8:20::1) Slice-ID:20
         bytes=116 Sequence=5 time=3 ms
   
     --- Destination BFRID: 2 (2001:DB8:20::1) ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=3/3/5 ms
   ```
2. (Optional) Run the following commands to configure functions related to BIERv6 Echo Request messages.
   
   
   * Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   * Run the [**nqa bier ipv6 receive rate-limit**](cmdqueryname=nqa+bier+ipv6+receive+rate-limit) *bierCpuLimit6* command to limit the rate at which BIERv6 Echo Request messages are sent to the main control board.
   * Run the [**nqa bier ipv6 udp-port**](cmdqueryname=nqa+bier+ipv6+udp-port) *udpPort6* command to set the UDP port number for receiving BIERv6 Echo Request messages.
   * Run the [**nqa bier ipv6 echo-reply disable**](cmdqueryname=nqa+bier+ipv6+echo-reply+disable) command to disable the function of responding to BIERv6 Echo Request messages.