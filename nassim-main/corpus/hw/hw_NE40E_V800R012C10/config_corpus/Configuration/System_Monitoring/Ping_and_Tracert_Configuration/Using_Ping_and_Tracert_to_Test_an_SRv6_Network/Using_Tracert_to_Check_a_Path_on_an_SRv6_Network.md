Using Tracert to Check a Path on an SRv6 Network
================================================

Tracert can be used to check a path on an SRv6 network.

#### Context

After configuring SRv6, you can perform the following configurations in any view of a client.


#### Procedure

* Specify SIDs to check a path on an SRv6 network or locate the failure point on the path.
  
  
  
  To locate the failure point on an SRv6 network, run the [**tracert ipv6-sid**](cmdqueryname=tracert+ipv6-sid) [ **-f** *first-hop-limit* | **-m** *max-hop-limit* | **-p** *port-number* | **-fixedPort** | **-q** *probes* | **-w** *timeout* | **-s** *packetsize* | **-a** *source-ipv6-address* | **ignore-mtu** { **-tc** *tc* | **-dscp** *dscp* } | **-nexthop** *nextHopAddr* | **-i** { *ifName* | *ifType* *ifNum* } ]\* [ **overlay** ] *sid* & <1-11> command on the ingress to initiate a tracert test to the egress by specifying SRv6 SIDs.
  
  ```
  <HUAWEI> tracert ipv6-sid 2001:DB8:10::1 2001:DB8:20::2 2001:DB8:30::3
    traceroute ipv6-sid 2001:DB8:10::1 2001:DB8:20::2 2001:DB8:30::3  64 hops max,60 bytes packet
  1  2001:DB8:1:2::21(SRH: 2001:DB8:30::3, 2001:DB8:20::2, 2001:DB8:10::1, SL=2) 5 ms 3 ms 2 ms
  2  2001:DB8:2:3::31(SRH: 2001:DB8:30::3, 2001:DB8:20::2, 2001:DB8:10::1, SL=1) 5 ms 2 ms 2 ms
  3  2001:DB8:30::3(SRH: 2001:DB8:30::3, 2001:DB8:20::2, 2001:DB8:10::1, SL=1) 5 ms 10 ms 0.759 ms
  ```
  
  
  
  To initiate a tracert test to the egress by specifying SRv6 SIDs in network slicing scenarios, run the [**tracert ipv6-sid**](cmdqueryname=tracert+ipv6-sid) [ **-f** *first-hop-limit* | **-m** *max-hop-limit* | **-p** *port-number* | **-fixedPort** | **-q** *probes* | **-w** *timeout* | **-s** *packetsize* | **-a** *source-ipv6-address* | **ignore-mtu** { **-tc** *tc* | **-dscp** *dscp* } | **-nexthop** *nextHopAddr* | **-i** { *ifName* | *ifType* *ifNum* } ]\* [ **overlay** ] *sid* & <1-11> [ **network-slice** *sliceid* [ **force-match-slice** ] ] command. This helps locate the failure point on the SRv6 network.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The **force-match-slice** keyword is used to forcibly match network slices and takes effect only for segment lists with slice attributes.
  
  ```
  <HUAWEI> tracert ipv6-sid 2001:DB8:10::1 2001:DB8:20::2 2001:DB8:30::3 network-slice 100 force-match-slice
    traceroute ipv6-sid 2001:DB8:10::1 2001:DB8:20::2 2001:DB8:30::3  64 hops max,60 bytes packet
  1  2001:DB8:1:2::21(SRH: 2001:DB8:30::3, 2001:DB8:20::2, 2001:DB8:10::1, SL=2, Slice-ID:100) 5 ms 3 ms 2 ms
  2  2001:DB8:2:3::31(SRH: 2001:DB8:30::3, 2001:DB8:20::2, 2001:DB8:10::1, SL=1, Slice-ID:100) 5 ms 2 ms 2 ms
  3  2001:DB8:30::3(SRH: 2001:DB8:30::3, 2001:DB8:20::2, 2001:DB8:10::1, SL=1, Slice-ID:100) 5 ms 10 ms 0.759 ms
  ```
* Check the path over which an SRv6 TE Policy is established or locate the failure point on the path.
  
  
  1. (Optional) Configure an End.OP SID on the remote endpoint of the SRv6 TE Policy.
     
     An End.OP SID (OAM endpoint with punt) is an OAM SID that specifies the punt behavior to be implemented for OAM packets. You can run the [**remote end-op**](cmdqueryname=remote+end-op) command or specify an End.OP SID to enable the device to initiate a tracert test. Note that if the last SID of an SRv6 TE Policy segment list is an End.X SID or binding SID, the [**remote end-op**](cmdqueryname=remote+end-op) command does not take effect. In this case, you need to specify an End.OP SID when running the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) command. An End.OP SID must have been configured before you specify the **end-op** parameter.
     
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
     
     If an End SID is used to implement a test, you can initiate a tracert operation without needing to run the [**remote end-op**](cmdqueryname=remote+end-op) command or specify an End.OP SID. Note that if the last SID of an SRv6 TE Policy segment list is an End.X SID or binding SID, you need to specify the **destination** parameter.
  2. On the headend of the SRv6 TE Policy, run the [**tracert srv6-te policy**](cmdqueryname=tracert+srv6-te+policy){ **policy-name***policyName* | **endpoint-ip***endpointIpv6***color***colorId* | **binding-sid***bsid* } [ **end-op***endOp* | **destination** *dest* ] [ **segment-list** *slid* ] [ **-a***sourceAddr6* | **-f** *initHl* | **-m***maxHl* |**-s***packetSize* | **-w***timeout* | **-p***destPort* | **-fixedPort** | { **-tc***tc* | **-dscp** *dscp* } | **ignore-mtu** | **-i** { *ifName* | *ifType**ifNum* } | **-nexthop***nextHopAddr* ] \* command with the **policy-name***policyName*, **endpoint-ip** *endpointIpv6* **color***colorId*, or **binding-sid***bsid* parameter specified to initiate a tracert test to check all transit nodes through which the SRv6 TE Policy passes.
     ```
     <HUAWEI> tracert srv6-te policy policy-name test end-op 2001:DB8:2::1 -a 2001:DB8:1::1 -p 5 -m 20 -tc 0
       Trace Route srv6-te policy  : 100  data bytes, press CTRL_C to break
       srv6-te policy's segment list:
       Preference: 200; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 200; Segment-List ID: 1; Xcindex: 1; end-op: 2001:DB8:2::1
       TTL    Replier                                 Time    Type      SRH(SID[n], ..., SID[0](the last SID to be processed))
       0                                                      Ingress   (SRH: 2001:DB8:1::F:1, 2001:DB8:2::F:1, 2001:DB8:2::1, SL=2)
       1      2001:DB8:A::192:168:103:2               22 ms   Transit   (SRH: 2001:DB8:1::F:1, 2001:DB8:2::F:1, 2001:DB8:2::1, SL=2)
       2      2001:DB8:A::192:168:106:2               10 ms   Transit   (SRH: 2001:DB8:1::F:1, 2001:DB8:2::F:1, 2001:DB8:2::1, SL=1) 
       3      2001:DB8:2::1                           4 ms    Egress 
     ```
     On the headend of the SRv6 TE Policy in a network slicing scenario, run the [**tracert srv6-te policy**](cmdqueryname=tracert+srv6-te+policy){ **policy-name***policyName* | **endpoint-ip***endpointIpv6***color***colorId* | **binding-sid***bsid* } [ **network-slice** *sliceid* ] [ **force-match-slice** ] [ **end-op***endOp* | **destination** *dest* ] [ **segment-list** *slid* ] [ **-a***sourceAddr6* | **-f** *initHl* | **-m***maxHl* |**-s***packetSize* | **-w***timeout* | **-p***destPort* | **-fixedPort** | { **-tc***tc* | **-dscp** *dscp* } | **ignore-mtu** | **-i** { *ifName* | *ifType**ifNum* } | **-nexthop***nextHopAddr* ] \* command with the **policy-name***policyName*, **endpoint-ip** *endpointIpv6* **color***colorId*, or **binding-sid***bsid* parameter specified to initiate a tracert test to check all transit nodes through which the SRv6 TE Policy passes.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The **force-match-slice** keyword is used to forcibly match network slices and takes effect only for segment lists with slice attributes.
     
     ```
     <HUAWEI> tracert srv6-te policy policy-name policy1 force-match-slice
       Trace Route srv6-te policy : 100  data bytes, press CTRL_C to break
       srv6-te policy's segment list:
       Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 1; Xcindex: 1
       TTL    Replier                                 Time    Type      SRH(SID[n], ..., SID[0](the last SID to be processed))
       0                                                      Ingress   (SRH: 2001:DB8:120::1:0:0, 2001:DB8:130::1:0:0, 2001:DB8:130::100, SL=2, Slice-ID:100)
       1      2001:DB8:10::2                          61 ms   Transit   (SRH: 2001:DB8:120::1:0:0, 2001:DB8:130::1:0:0, 2001:DB8:130::100, SL=2, Slice-ID:100)
       2      2001:DB8:130::100                       4 ms    Egress    (SRH: 2001:DB8:120::1:0:0, 2001:DB8:130::1:0:0, 2001:DB8:130::100, SL=1, Slice-ID:100)
     ```