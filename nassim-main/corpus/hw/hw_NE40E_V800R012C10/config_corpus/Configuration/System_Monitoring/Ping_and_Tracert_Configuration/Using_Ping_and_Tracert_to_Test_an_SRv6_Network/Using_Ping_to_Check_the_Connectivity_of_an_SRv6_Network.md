Using Ping to Check the Connectivity of an SRv6 Network
=======================================================

Ping can be used to check the connectivity of an SRv6 network.

#### Context

After SRv6 configurations are complete, you can perform the following operations in any view of the client.


#### Procedure

* Specify SIDs to check the connectivity of an SRv6 network.
  
  
  
  To check the connectivity of an SRv6 network, run the [**ping ipv6-sid**](cmdqueryname=ping+ipv6-sid) [ **-a** *source-ipv6-address* | **-c** *echo-number* | **-m** *wait-time* | **-s** *packetsize* | **-t** *timeout* | { **-tc** *traffic-class-value* | **-dscp***dscp* } | **-h***hopLimit* | **-ri** | **-p***pattern* | **ignore-mtu** | **-nexthop***nextHopAddr* | **-i** { *ifName* | *ifType**ifNum* } ]\* [ **segment-by-segment** ] *sid* <1-11> command on the ingress to initiate a ping test to the egress by specifying SRv6 SIDs.
  
  ```
  <HUAWEI> ping ipv6-sid 2001:DB8:200::222 2001:DB8:300::333 2001:DB8:400::444 2001:DB8:400::400
    PING ipv6-sid 2001:DB8:200::222 2001:DB8:300::333 2001:DB8:400::444 2001:DB8:400::400 : 56  data bytes, press CTRL_C to break
      Reply from 2001:DB8:400::400
      bytes=56 Sequence=1 hop limit=62 time=7 ms 
      Reply from 2001:DB8:400::400
      bytes=56 Sequence=2 hop limit=62 time=2 ms 
      Reply from 2001:DB8:400::400
      bytes=56 Sequence=3 hop limit=62 time=3 ms 
      Reply from 2001:DB8:400::400
      bytes=56 Sequence=4 hop limit=62 time=3 ms 
      Reply from 2001:DB8:400::400
      bytes=56 Sequence=5 hop limit=62 time=2 ms 
            
    --- ipv6-sid ping statistics---  
      5 packet(s) transmitted 
      5 packet(s) received  
      0.00% packet loss
      round-trip min/avg/max=2/3/7 ms
  ```
  
  
  
  To check the connectivity of an SRv6 network in network slicing scenarios, run the [**ping ipv6-sid**](cmdqueryname=ping+ipv6-sid) [ **-a** *source-ipv6-address* | **-c** *echo-number* | **-m** *wait-time* | **-s** *packetsize* | **-t** *timeout* | { **-tc** *traffic-class-value* | **-dscp***dscp* } | **-h***hopLimit* | **-ri** | **-p***pattern* | **ignore-mtu** | **-nexthop***nextHopAddr* | **-i** { *ifName* | *ifType**ifNum* } ]\* [ **segment-by-segment** ] *sid* & <1-11> [ **network-slice** *sliceid* [ **force-match-slice** ]] command on the ingress to initiate a ping test to the egress by specifying SRv6 SIDs.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The **force-match-slice** keyword is used to forcibly match network slices and takes effect only for segment lists with slice attributes.
  
  ```
  <HUAWEI> ping ipv6-sid 2001:DB8:10::1 2001:DB8:20::2 2001:DB8:30::3 network-slice 100 force-match-slice
    PING ipv6-sid 2001:DB8:10::1 2001:DB8:20::2 2001:DB8:30::3 : 56  data bytes, press CTRL_C to break
      Reply from 2001:DB8:30::3 
      bytes=56 Sequence=1 hop limit=64 time=2 ms
      Reply from 2001:DB8:30::3 
      bytes=56 Sequence=2 hop limit=64 time=1 ms
      Reply from 2001:DB8:30::3 
      bytes=56 Sequence=3 hop limit=64 time=1 ms
      Reply from 2001:DB8:30::3 
      bytes=56 Sequence=4 hop limit=64 time=1 ms
      Reply from 2001:DB8:30::3 
      bytes=56 Sequence=5 hop limit=64 time=1 ms
   --- ipv6-sid ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max=1/1/2 ms
  ```
* Check the connectivity of an SRv6 TE Policy.
  
  
  1. (Optional) Configure an End.OP SID on the remote endpoint of the SRv6 TE Policy.
     
     An End.OP SID (OAM endpoint with punt) is an OAM SID that specifies the punt behavior to be implemented for OAM packets. You can run the [**remote end-op**](cmdqueryname=remote+end-op) command or specify an End.OP SID to enable the device to initiate a ping test. Note that if the last SID of an SRv6 TE Policy segment list is an End.X SID or binding SID, the [**remote end-op**](cmdqueryname=remote+end-op) command does not take effect. In this case, you need to specify an End.OP SID when running the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) command. An End.OP SID must have been configured before you specify the **end-op** parameter.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
        
        The SRv6 view is displayed.
     3. Run [**locator**](cmdqueryname=locator) *locator-name*
        
        The locator view is displayed.
        
        Ensure that the locator has been created and advertised through IS-IS. The locator is also used by the created SRv6 TE Policy.
     4. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-op**
        
        An opcode is configured for an End.OP SID.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If an End SID is used to implement a test, you can initiate a ping operation without the need to run the [**remote end-op**](cmdqueryname=remote+end-op) command or specify an End.OP SID. Note that if the last SID of an SRv6 TE Policy segment list is an End.X SID or binding SID, you need to specify the **destination** parameter.
  2. To check the connectivity of the SRv6 TE Policy, run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy){ **policy-name** *policyName* | **endpoint-ip** *endpointIpv6* **color** *colorId* | **binding-sid** *bsid* } [ **end-op** *endOp* | **destination** *dest* ] [ **segment-list** *slid* ] [ **-a** *sourceAddr6* | **-c***count* | **-m** *interval* | **-s** *packetSize* | **-t** *timeout* | { **-tc***tc* | **-dscp***dscp* } | **-h** *hopLimit* | **-ri** | **-p***pattern* | **ignore-mtu** | **-i** { *ifName* | *ifType**ifNum* } | **-nexthop***nextHopAddr* ] \* command with the **policy-name***policyName*, **endpoint-ip** *endpointIpv6* **color** *colorId*, or **binding-sid** *bsid* parameter specified on the headend of the SRv6 TE Policy to initiate a ping test.
     ```
     <HUAWEI> ping srv6-te policy policy-name test end-op 2001:DB8:2::1 -a 2001:DB8:1::1 -c 5 -m 2000 -t 2000 -s 100 -tc 0 -h 255
       PING srv6-te policy : 100  data bytes, press CTRL_C to break
       srv6-te policy's segment list:
       Preference: 200; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 200; Segment-List ID: 1; Xcindex: 1; end-op: 2001:DB8:2::1
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=1 time=8 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=2 time=2 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=3 time=3 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=4 time=3 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=5 time=3 ms
       --- srv6-te policy ping statistics ---
         5 packet(s) transmitted
         5 packet(s) received
         0.00% packet loss
         round-trip min/avg/max = 2/3/8 ms
     ```
     To check the connectivity of the SRv6 TE Policy in network slicing scenarios, run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy){ **policy-name** *policyName* | **endpoint-ip** *endpointIpv6* **color** *colorId* | **binding-sid** *bsid* } [ **network-slice** *sliceid* ] [ **force-match-slice** ] [ **end-op** *endOp* | **destination** *dest* ] [ **segment-list** *slid* ] [ **-a** *sourceAddr6* | **-c***count* | **-m** *interval* | **-s** *packetSize* | **-t** *timeout* | { **-tc***tc* | **-dscp***dscp* } | **-h** *hopLimit* | **-ri** | **-p***pattern* | **ignore-mtu** | **-i** { *ifName* | *ifType**ifNum* } | **-nexthop***nextHopAddr* ] \* command with the **policy-name***policyName*, **endpoint-ip** *endpointIpv6* **color** *colorId*, or **binding-sid** *bsid* parameter specified on the headend of the SRv6 TE Policy to initiate a ping test.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The **force-match-slice** keyword is used to forcibly match network slices and takes effect only for segment lists with slice attributes.
     
     ```
     <HUAWEI> ping srv6-te policy policy-name test force-match-slice
       PING srv6-te policy : 100  data bytes, press CTRL_C to break
       srv6-te policy's segment list:
       Preference: 200; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 200; Segment-List ID: 1; Xcindex: 1
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=1 time=8 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=2 time=2 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=3 time=3 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=4 time=3 ms
         Reply from 2001:DB8:2::1
         bytes=100 Sequence=5 time=3 ms
       --- srv6-te policy ping statistics ---
         5 packet(s) transmitted
         5 packet(s) received
         0.00% packet loss
         round-trip min/avg/max = 2/3/8 ms
     ```