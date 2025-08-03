Using Ping to Check Link Connectivity on an MPLS Network
========================================================

Ping can be used to check the connectivity of label distribution protocol (LDP) label switched path (LSPs) that carry IPv4 packets and TE tunnels that carry IPv4 and IPv6 packets.

#### Prerequisites

Before performing a ping test, run the [**lspv mpls-lsp-ping echo enable**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable) command to enable the device to respond to MPLS Echo Request packets.

NQA is a detection method deployed on the main control board. Both the initiator and responder send LSP packets to the main control board for processing. If a large number of packets are sent to the main control board, the CPU usage of the main control board becomes high, affecting normal device running. To prevent this problem, you can run the [**lspv mpls-lsp-ping cpu-defend**](cmdqueryname=lspv+mpls-lsp-ping+cpu-defend) *cpu-defend* command to limit the rate at which MPLS echo request packets are sent to the main control board.

If the MPLS packet length of an NQA test instance is greater than the MTU of a specified MPLS tunnel, MPLS packets fail to pass through the tunnel. To allow the packets to pass through the tunnel, run the [**fragment enable**](cmdqueryname=fragment+enable) command to enable MPLS packet fragmentation.


#### Context

Perform the following steps in any view on the client.


#### Procedure

* Check the connectivity of an LDP LSP that carries IPv4 packets.
  
  
  
  To check the connectivity of an LDP LSP that carries IPv4 packets, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] [ **nexthop** *nexthop-address* ] [ **remote** *remote-address* ] command.
  
  ```
  <HUAWEI> ping lsp -v ip 3.3.3.3 32 
    LSP PING FEC: IPV4 PREFIX 3.3.3.3/32 : 100  data bytes, press CTRL_C to break
      Reply from 3.3.3.3: bytes=100 Sequence=1 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=2 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=3 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=4 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=5 time = 5 ms Return Code 3, Subcode 1
  
    --- FEC: IPV4 PREFIX 3.3.3.3/32 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 4/4/5 ms   
  ```
* Check the connectivity of a TE tunnel (RSVP-TE tunnel, static TE tunnel, or dynamic TE tunnel) that carries IPv4 packets.
  
  
  
  To check the connectivity of a TE tunnel (RSVP-TE tunnel, static TE tunnel, or dynamic TE tunnel) that carries IPv4 packets, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **te** { *tunnelName* | *ifType* *ifNum* } [ **hot-standby** | **primary** ] [ **compatible-mode** ] | **auto-tunnel** *auto-tunnelname* } command.
  
  ```
  <HUAWEI> ping lsp te Tunnel 1
    LSP PING FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel1 : 100  data bytes, press CTRL_C to break
      Reply from 1.1.1.1: bytes=100 Sequence=1 time = 4 ms
      Reply from 1.1.1.1: bytes=100 Sequence=2 time = 2 ms
      Reply from 1.1.1.1: bytes=100 Sequence=3 time = 2 ms
      Reply from 1.1.1.1: bytes=100 Sequence=4 time = 2 ms
      Reply from 1.1.1.1: bytes=100 Sequence=5 time = 2 ms
  
    --- FEC: RSVP IPV4 SESSION QUERY Tunnel1 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 2/2/4 ms                     
  ```
* Check the connectivity of an SR-MPLS TE IPv4 tunnel.
  
  
  + To check the connectivity of an SR-MPLS TE tunnel dynamically created, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **segment-routing** { { **auto-tunnel** *auto-tunnelname* [ **version** { **draft2** | **draft4** } ] } } [ **remote** *remote-address* ] [ **hot-standby** | **primary** ] command and specify *auto-tunnelname* on the ingress to initiate a ping test to the egress.
    
    ```
    <HUAWEI> ping lsp -c 3 segment-routing auto-tunnel Tunnel10 version draft4 
      LSP PING FEC: AUTO TE TUNNEL IPV4 SESSION QUERY Tunnel10 : 100 data bytes, press CTRL_C to break
        Reply from 10.1.1.2: bytes=100 Sequence=1 time=11 ms
        Reply from 10.1.1.2: bytes=100 Sequence=2 time=9 ms
        Reply from 10.1.1.2: bytes=100 Sequence=3 time=6 ms
    
      --- FEC: AUTO TE TUNNEL IPV4 SESSION QUERY Tunnel10 ping statistics ---
        3 packet(s) transmitted
        3 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 6/8/11 ms
    ```
  + To check the connectivity of an SR-MPLS TE tunnel manually configured, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **segment-routing** **te** { *tunnelName* | *ifType* *ifNum* } [ **draft2** ] [ **remote** *remote-address* ] [ **hot-standby** | **primary** ] command to initiate a ping test to the egress.
    
    ```
    <HUAWEI> ping lsp -c 3 segment-routing te Tunnel10
      LSP PING FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel10 : 100 data bytes, press CTRL_C to break
        Reply from 10.1.1.2: bytes=100 Sequence=1 time=11 ms
        Reply from 10.1.1.2: bytes=100 Sequence=2 time=9 ms
        Reply from 10.1.1.2: bytes=100 Sequence=3 time=6 ms
    
      --- FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel10 ping statistics ---
        3 packet(s) transmitted
        3 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 6/8/11 ms
    ```
* Check the connectivity of an SR-MPLS BE IPv4 tunnel.
  
  
  
  To check the connectivity of an SR-MPLS BE IPv4 tunnel, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **segment-routing** **ip** *destination-address* *mask-length* [ **flex-algo** *flex-algo-id* ] [ **version draft2** ] [ **bypass** ] [ **remote** *remote-ip* ] command.
  
  ```
  <HUAWEI> ping lsp segment-routing ip 3.3.3.9 32 version draft2
    LSP PING FEC: SEGMENT ROUTING IPV4 PREFIX 3.3.3.9/32 : 100  data bytes, press CTRL_C to break
      Reply from 3.3.3.9: bytes=100 Sequence=1 time=13 ms
      Reply from 3.3.3.9: bytes=100 Sequence=2 time=9 ms
      Reply from 3.3.3.9: bytes=100 Sequence=3 time=2 ms
      Reply from 3.3.3.9: bytes=100 Sequence=4 time=3 ms
      Reply from 3.3.3.9: bytes=100 Sequence=5 time=6 ms
  
    --- FEC: SEGMENT ROUTING IPV4 PREFIX 3.3.3.9/32 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 2/6/13 ms
  ```
* Check the connectivity of a BGP LSP that carries IPv4 packets.
  
  
  
  To check the connectivity of a BGP LSP that carries IPv4 packets, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **bgp** *destination-iphost* *mask-length* [ **vpn-instance** *vpn-name* ] [ *ip-address* ] [ **nexthop** *nexthop-address* [ **out-label** *mplsLabel* ] ] command.
  
  ```
  <HUAWEI> ping lsp -c 2 bgp 4.4.4.4 32
    LSP PING FEC: BGP LABELED IPV4 PREFIX 4.4.4.4/32/ : 100 data bytes, press CTRL_C to break
      Reply from 4.4.4.4: bytes=100 Sequence=1 time=46 ms
      Reply from 4.4.4.4: bytes=100 Sequence=2 time=2 ms
  
    --- FEC: BGP LABELED IPV4 PREFIX 4.4.4.4/32 ping statistics ---
      2 packet(s) transmitted
      2 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 2/24/46 ms
  ```
* Check the connectivity of an LDP LSP interworking an SR-MPLS BE tunnel.
  
  
  
  To check the connectivity of an LDP LSP interworking with an SR-MPLS BE tunnel, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] [ **nexthop** *nexthop-address* ] [ **remote** *remote-address* ] command on the ingress to initiate a ping test to the egress of the SR-MPLS BE tunnel.
  
  ```
  <HUAWEI> ping lsp -c 3 ip 5.5.5.9 32 remote 5.5.5.9
    LSP PING FEC: IPV4 PREFIX 5.5.5.9/32/ : 100  data bytes, press CTRL_C to break
      Reply from 5.5.5.9: bytes=100 Sequence=1 time=3 ms
      Reply from 5.5.5.9: bytes=100 Sequence=2 time=3 ms
      Reply from 5.5.5.9: bytes=100 Sequence=3 time=3 ms
  
    --- FEC: IPV4 PREFIX 5.5.5.9/32 ping statistics ---
      3 packet(s) transmitted
      3 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 3/3/3 ms
  ```
* Check the connectivity of an SR-MPLS BE tunnel interworking with an LDP LSP.
  
  To check the connectivity of an SR-MPLS BE tunnel interworking with an LDP LSP, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **segment-routing** **ip** *destination-address* *mask-length* [ **flex-algo** *flex-algo-id* ] [ **version draft2** ] [ **bypass** ] **remote** *remote-ip* command on the ingress to initiate a ping test to the egress of the LDP LSP.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  When performing a ping operation to check the connectivity of an SR-MPLS BE tunnel interworking with an LDP LSP, specify a remote IP address using the **remote** *remote-ip* parameter.
  
  
  ```
  <HUAWEI> ping lsp -c 3 segment-routing ip 5.5.5.9 32 version draft2 remote 5.5.5.9
    LSP PING FEC: IPV4 PREFIX 5.5.5.9/32 : 100  data bytes, press CTRL_C to break
      Reply from 5.5.5.9: bytes=100 Sequence=1 time=9 ms
      Reply from 5.5.5.9: bytes=100 Sequence=2 time=2 ms
      Reply from 5.5.5.9: bytes=100 Sequence=3 time=3 ms
  
    --- FEC: IPV4 PREFIX 5.5.5.9/32 ping statistics ---
      3 packet(s) transmitted
      3 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 2/4/9 ms
  ```
* Check the connectivity of an LDP LSP interworking with an SR-MPLS BE tunnel (the LDP end does not support interworking).
  
  
  
  To check the connectivity of an LDP LSP interworking with an SR-MPLS BE tunnel, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] [ **nexthop** *nexthop-address* ] [ **remote** *remote-address* ] command on the ingress to initiate a ping test to the egress of the SR-MPLS BE tunnel.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  You must run the [**lspv echo-reply fec-validation ldp disable**](cmdqueryname=lspv+echo-reply+fec-validation+ldp+disable) command on the SR-MPLS BE side to disable the LSPV response end from checking the LDP FEC.
  
  ```
  <HUAWEI> ping lsp -v ip 3.3.3.3 32 
    LSP PING FEC: IPV4 PREFIX 3.3.3.3/32 : 100  data bytes, press CTRL_C to break
      Reply from 3.3.3.3: bytes=100 Sequence=1 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=2 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=3 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=4 time = 4 ms Return Code 3, Subcode 1
      Reply from 3.3.3.3: bytes=100 Sequence=5 time = 5 ms Return Code 3, Subcode 1
  
    --- FEC: IPV4 PREFIX 3.3.3.3/32 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 4/4/5 ms   
  ```
* Check the connectivity of an SR-MPLS BE tunnel interworking with an LDP LSP (the LDP end does not support interworking).
  
  
  
  To check the connectivity of an SR-MPLS BE tunnel interworking with an LDP LSP, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **segment-routing** **ip** *destination-address* *mask-length* [ **flex-algo** *flex-algo-id* ] [ **version draft2** ] [ **bypass** ] **remote-fec** { **ldp** *remoteipaddr* *remotemasklen* | **nil** } command on the ingress to initiate a ping test to the egress of the LDP LSP.
  
  ```
  <HUAWEI> ping lsp -c 3 segment-routing ip 5.5.5.9 32 version draft2 remote-fec ldp 5.5.5.9 32
    LSP PING FEC: IPV4 PREFIX 5.5.5.9/32 : 100  data bytes, press CTRL_C to break
      Reply from 5.5.5.9: bytes=100 Sequence=1 time=9 ms
      Reply from 5.5.5.9: bytes=100 Sequence=2 time=2 ms
      Reply from 5.5.5.9: bytes=100 Sequence=3 time=3 ms
  
    --- FEC: IPV4 PREFIX 5.5.5.9/32 ping statistics ---
      3 packet(s) transmitted
      3 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 2/4/9 ms
  ```
* Check the connectivity of an SR-MPLS TE Policy carrying IPv4 packets.
  
  
  
  To check the connectivity of an SR-MPLS TE Policy carrying IPv4 packets, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-v** | **-g** ] \* **sr-te** **policy** { **policy-name** *policyname* | **endpoint-ip** *endpoint-ip* **color** *colorid* | [**binding-sid**](cmdqueryname=binding-sid) *bsid* } [ **segment-list** *slid* ] command.
  
  ```
  <HUAWEI> ping lsp sr-te policy policy-name test
    LSP PING FEC:  Nil FEC  : 100 data bytes, press CTRL_C to break
    sr-te policy' s segment list:
    Preference : 300; Path Type: main; Protocol-Origin : local; Originator: 0, 0.0.0.0; Discriminator: 300; Segment-List ID : 1;  Xcindex : 1
      Reply from 3.3.3.9: bytes=100 Sequence=1 time=13 ms     
      Reply from 3.3.3.9: bytes=100 Sequence=2 time=9 ms    
      Reply from 3.3.3.9: bytes=100 Sequence=3 time=2 ms     
      Reply from 3.3.3.9: bytes=100 Sequence=4 time=3 ms     
      Reply from 3.3.3.9: bytes=100 Sequence=5 time=6 ms
     
    --- FEC: Nil FEC ping statistics ---
      5 packet(s) transmitted     
      5 packet(s) received     
      0.00% packet loss     
      round-trip min/avg/max = 2/6/13 ms
  
    sr-te policy' s segment list:
    Preference : 400; Path Type: backup; Protocol-Origin : local; Originator: 0, 0.0.0.0; Discriminator: 400; Segment-List ID : 2;  Xcindex : 2     
     Reply from 3.3.3.9: bytes=100 Sequence=1 time=13 ms     
     Reply from 3.3.3.9: bytes=100 Sequence=2 time=9 ms     
     Reply from 3.3.3.9: bytes=100 Sequence=3 time=2 ms     
     Reply from 3.3.3.9: bytes=100 Sequence=4 time=3 ms     
     Reply from 3.3.3.9: bytes=100 Sequence=5 time=6 ms
  
    --- FEC: Nil FEC ping statistics --- 
      5 packet(s) transmitted     
      5 packet(s) received     
      0.00% packet loss
      round-trip min/avg/max = 2/6/13 ms 
  ```
* Check the connectivity of an inter-AS E2E SR-MPLS TE tunnel.
  
  To check the connectivity of an inter-AS E2E SR-MPLS TE tunnel, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-s** *packet-size* | **-t** *timeout* | **-v** | **-g** | **-r** *reply-mode* ] \* **segment-routing** { { **auto-tunnel** *srAutoTnlName* **version** { **draft2** | **draft4** } } | **te** { *tunnelName* | *ifType* *ifNum* } [ **draft2** ] } [ **remote** *remoteAddress* ] [ **hot-standby** ] command.
  ```
  <HUAWEI> [ping lsp segment-routing te Tunnel 11 draft2](cmdqueryname=ping+lsp+segment-routing+te+Tunnel+11+draft2) 
    LSP PING FEC: SEGMENT ROUTING TE TUNNEL IPV4 SESSION QUERY Tunnel11 : 100  data bytes, press CTRL_C to break
      Reply from 5.5.5.9: bytes=100 Sequence=1 time=14 ms
      Reply from 5.5.5.9: bytes=100 Sequence=2 time=12 ms
      Reply from 5.5.5.9: bytes=100 Sequence=3 time=9 ms
      Reply from 5.5.5.9: bytes=100 Sequence=4 time=11 ms
      Reply from 5.5.5.9: bytes=100 Sequence=5 time=8 ms
  
    --- FEC: SEGMENT ROUTING TE TUNNEL IPV4 SESSION QUERY Tunnel11 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 8/10/14 ms
  ```
* (Optional) Run the [**display lspv statistics**](cmdqueryname=display+lspv+statistics) command to check LSPV packet statistics.
  
  
  
  If the test using the [**ping lsp**](cmdqueryname=ping+lsp) command fails, you can run this command to check whether the fault occurs on the LSP or the device.
* (Optional) Run the [**reset lspv statistics**](cmdqueryname=reset+lspv+statistics) command to clear LSPV packet statistics.

#### Follow-up Procedure

After the test is completed, you are advised to run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable) command to disable the device from responding to MPLS Echo Request packets so as to prevent system resource occupation.