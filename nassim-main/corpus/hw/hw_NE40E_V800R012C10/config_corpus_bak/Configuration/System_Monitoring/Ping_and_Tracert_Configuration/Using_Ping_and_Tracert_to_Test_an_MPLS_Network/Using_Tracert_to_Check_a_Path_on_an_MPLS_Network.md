Using Tracert to Check a Path on an MPLS Network
================================================

A tracert operation checks the path over which a label distribution protocol (LDP) LSP or a TE tunnel that carries IPv4 packets is established or locate the failure point on the path.

#### Prerequisites

Before performing a ping test, run the [**lspv mpls-lsp-ping echo enable**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable) command to enable the device to respond to MPLS Echo Request packets.![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the device interworks with a non-Huawei device, run the [**lspv echo-reply compitable fec enable**](cmdqueryname=lspv+echo-reply+compitable+fec+enable) command to enable the device to respond to MPLS echo request packets with MPLS echo reply packets that do not carry FEC information.


NQA is a detection method deployed on the main control board. Both the initiator and responder send LSP packets to the main control board for processing. If a large number of packets are sent to the main control board, the CPU usage of the main control board becomes high, affecting normal device running. To prevent this problem, you can run the [**lspv mpls-lsp-ping cpu-defend**](cmdqueryname=lspv+mpls-lsp-ping+cpu-defend) *cpu-defend* command to limit the rate at which MPLS echo request packets are sent to the main control board.


#### Context

Perform the following steps in any view on the client.


#### Procedure

* Check the path over which an LDP LSP that carries IPv4 packets is established or locate the failure point on the path.
  
  
  
  To check the path over which an LDP LSP that carries IPv4 packets is established or locate the failure point on the path, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* | **-s** *size* | **-g** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] [ **nexthop** *nexthop-address* ] [ **detail** ] command.
  
  ```
  <HUAWEI> tracert lsp ip 1.1.1.1 32
    LSP Trace Route FEC: IPV4 PREFIX 1.1.1.1/32 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.1/[3 ]
    1      1.1.1.1            5       Egress           
  ```
* Check the path over which a TE tunnel (RSVP-TE tunnel, static TE tunnel, or dynamic TE tunnel) that carries IPv4 packets is established or locate the failure point on the path.
  
  
  
  To check the path over which a TE tunnel (RSVP-TE tunnel, static TE tunnel, or dynamic TE tunnel) that carries IPv4 packets is established or locate the failure point on the path, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* | **-s** *size* | **-g** ] \* **te** { *tunnelName* | *ifType* *ifNum* } [ **hot-standby** | **primary** ] [ **compatible-mode** ] | **auto-tunnel** *auto-tunnelname* [ **detail** ] command.
  
  ```
  <HUAWEI> tracert lsp te Tunnel 1
    LSP Trace Route FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel1 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.1/[3 ]
    1      1.1.1.1            4       Egress                             
  ```
* Check the path over which an SR-MPLS TE IPv4 tunnel is established or locate the failure point on the path.
  
  
  + To check an SR-MPLS TE tunnel dynamically created, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-t** *time-out* | **-s** *size* | **-g** ] \* **segment-routing** **auto-tunnel** *auto-tunnelname* [ **version** { **draft2** | **draft4** | **rfc8287** } ] [ **hot-standby** | **primary** ] [ **detail** ] command on the ingress to initiate a tracert test to the egress of the tunnel specified by *auto-tunnelname*. This helps locate the failure point on the tunnel.
    
    ```
    <HUAWEI> tracert lsp segment-routing auto-tunnel Tunnel10 version draft4
      LSP  Trace  Route  FEC: AUTO TE TUNNEL IPV4 SESSION QUERY Tunnel10 , press CTRL_C to break.
      TTL     Replier                   Time    Type      Downstream
      0                                         Ingress   10.1.1.2/[284688 ]
      1       10.1.1.2                  7 ms    Egress 
    ```
  + To check an SR-MPLS TE tunnel manually configured, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-t** *time-out* | **-s** *size* | **-g** ] \* **segment-routing** **te** { *tunnelName* | *ifType* *ifNum* } [ **draft2** | **rfc8287** ] [ **hot-standby** | **primary** ] [ **detail** ] command on the ingress to initiate a tracert test to the egress of the tunnel specified by *tunnelName* or *ifType* *ifNum*. This helps locate the failure point on the tunnel.
    
    ```
    <HUAWEI> tracert lsp segment-routing te Tunnel 1 
      LSP  Trace  Route  FEC: AUTO TE TUNNEL IPV4 SESSION QUERY Tunnel 1 , press CTRL_C to break.
      TTL     Replier              Time    Type      Downstream
      0                                    Ingress   10.1.1.2/[284688 ]
      1       10.1.1.2             7 ms    Egress
    ```
* Check the path over which an SR-MPLS BE IPv4 tunnel is established or locate the failure point on the path.
  
  
  
  To locate the failure point on an SR-MPLS BE IPv4 tunnel, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-s** *size* | **-g** ] \* **segment-routing** **ip** *ip-address* *mask-length* [ **flex-algo** *flex-algo-id* ] [ **version draft2** ] [ **bypass** ] [ **remote** *remote-ip* ] command.
  
  ```
  <HUAWEI> tracert lsp segment-routing ip 2.2.2.2 32 version draft2
    LSP Trace Route FEC: SEGMENT ROUTING IPV4 PREFIX 2.2.2.2/32 , press CTRL_C to break.
    TTL    Replier              Time    Type      Downstream
    0                                   Ingress   192.168.1.2/[1001 ]
    1      192.168.1.2          6 ms    Transit   192.168.2.2/[3 ]
    2      192.168.2.2          6 ms    Egress
  ```
* Check the BGP LSP carrying IPv4 packets or locate the failure point on the path.
  
  
  
  To check the BGP LSP carrying IPv4 packets or locate the failure point on the path, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* | **-s** *size* | **-g** ] \* **bgp** *destination-iphost* *mask-length* [ *ip-address* ] [ **detail** ] [ **nexthop** *nexthop-address* [ **out-label** *mplsLabel* ] ] command.
  
  ```
  <HUAWEI> tracert lsp -h 5 bgp 4.4.4.4 32
    LSP Trace Route FEC: IPV4 PREFIX 4.4.4.4/32 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.2/[32967 3 ]
    1      10.1.1.2           5 ms    Transit   10.2.1.2/[32938 3 ]
    2      10.2.1.2           6 ms    Transit   10.3.1.2/[32989 3 ]
    3      4.4.4.4            1 ms    Egress 
  ```
* Locate a failure point on an LDP LSP interworking with an SR-MPLS BE tunnel.
  
  
  
  To locate a failure point on an LDP LSP interworking with an SR-MPLS BE tunnel, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* | **-s** *size* | **-g** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] [ **nexthop** *nexthop-address* ] [ **detail** ] [ **ddmap** ] command on the ingress to initiate a tracert test to the egress of the SR-MPLS BE tunnel.
  
  ```
  <HUAWEI> tracert -h 10 ip 1.1.1.1 32 ddmap
    LSP Trace Route FEC: IPV4 PREFIX 5.5.5.9/32 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.1/[66010 ]
    1      10.1.1.1           9 ms    Transit   10.1.1.2/[33182 ]
    2      10.1.1.2           7 ms    Transit   10.1.1.3/[319836 ]
    3      10.1.1.3           9 ms    Transit   192.168.1.2/[3 ]
    4      5.5.5.9            3 ms    Egress 
  ```
* Locate a failure point on an SR-MPLS BE tunnel interworking with an LDP LSP.
  
  
  
  To locate a failure point on an SR-MPLS BE tunnel interworking with an LDP LSP, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-s** *size* | **-g** ] \* **segment-routing** **ip** *ip-address* *mask-length* [ **flex-algo** *flex-algo-id* ] [ **version draft2** ] [ **bypass** ] **remote** *remote-ip* command on the ingress to initiate a tracert test to the egress of the LDP LSP.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  When checking the connectivity of an SR-MPLS BE tunnel interworking an LDP LSP, specify a remote IP address using the **remote** *remote-ip* parameter.
  
  ```
  <HUAWEI> tracert lsp -h 10 segment-routing ip 5.5.5.9 32 version draft2 remote 5.5.5.9
    LSP Trace Route FEC: SEGMENT ROUTING IPV4 PREFIX 5.5.5.9/32 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.1/[319546 ]
    1      10.1.1.1           7 ms    Transit   10.1.1.2/[319546 ]
    2      10.1.1.2           7 ms    Transit   10.1.1.3/[33517 3 ]
    3      10.1.1.3           11 ms   Transit   192.168.1.2/[3 ]
    4      5.5.5.9            2 ms    Egress    
  ```
* Locate a failure point on an LDP LSP interworking an SR-MPLS BE tunnel (the LDP end does not support interworking).
  
  
  
  To locate a failure point on an LDP LSP interworking with an SR-MPLS BE tunnel, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* | **-s** *size* | **-g** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] [ **nexthop** *nexthop-address* ] [ **detail** ] [ **ddmap** ] command on the ingress to initiate a tracert test to the egress of the SR-MPLS BE tunnel.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  You must run the [**lspv echo-reply fec-validation ldp disable**](cmdqueryname=lspv+echo-reply+fec-validation+ldp+disable) command on the SR-MPLS BE side to disable the LSPV response end from checking the LDP FEC.
  
  ```
  <HUAWEI> tracert lsp ip 1.1.1.1 32
    LSP Trace Route FEC: IPV4 PREFIX 1.1.1.1/32 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.1/[3 ]
    1      1.1.1.1            5       Egress           
  ```
* Locate a failure point on an SR-MPLS BE tunnel interworking with an LDP LSP (the LDP end does not support interworking).
  
  
  
  To locate a failure point on an SR-MPLS BE tunnel interworking with an LDP LSP, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-s** *packet-size* | **-g** | **-t** *time-out* ] \* **segment-routing** **ip** *ip-address* *mask-length* [ **flex-algo** *flex-algo-id* ] [ **version draft2** ] [ **bypass** ] [ **remote-fec** **ldp** *remoteipaddr* *remotemasklen* ] command on the ingress to initiate a tracert test to the egress of the LDP LSP.
  
  ```
  <HUAWEI> tracert lsp -h 10 segment-routing ip 5.5.5.9 32 version draft2 remote-fec ldp 5.5.5.9 32
    LSP Trace Route FEC: SEGMENT ROUTING IPV4 PREFIX 5.5.5.9/32 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.1/[319546 ]
    1      10.1.1.1           7 ms    Transit   10.1.1.2/[319546 ]
    2      10.1.1.2           7 ms    Transit   10.1.1.3/[33517 3 ]
    3      10.1.1.3          11 ms    Transit   192.168.1.2/[3 ]
    4      5.5.5.9            2 ms    Egress    
  ```
* Check the path over which an SR-MPLS TE Policy carrying IPv4 packets is established or the failure point on the path.
  
  
  
  To locate the failure point on an SR-MPLS TE Policy, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-s** *packet-size* | **-t** *time-out* | **-g** ] \* **sr-te** **policy** { **policy-name** *policyname* | **endpoint-ip** *endpoint-ip* **color** *colorid* | [**binding-sid**](cmdqueryname=binding-sid) *bsid* } [ **segment-list** *slid* ] command.
  
  ```
  <HUAWEI> tracert lsp sr-te policy policy-name test
  LSP Trace Route FEC: Nil FEC, press CTRL_C to break.  
  sr-te policy' s segment list:
  Preference : 300; Path Type: main; Protocol-Origin : local; Originator: 0, 0.0.0.0; Discriminator: 300; Segment-List ID : 1;  Xcindex : 1
  TTL   Replier            Time     Type       Downstream  
  0                                Ingress    10.1.2.1/[13312 12]  
  1     10.1.2.1           63 ms   Transit    10.1.2.2/[12 ]  
  2     6.6.6.6            93 ms   Egress
  
  sr-te policy' s segment list:
  Preference : 400; Path Type: backup; Protocol-Origin : local; Originator: 0, 0.0.0.0; Discriminator: 400; Segment-List ID : 1;  Xcindex : 1
  TTL   Replier            Time      Type       Downstream  
  0                                Ingress    10.1.2.1/[13312 12]  
  1     10.1.2.1           63 ms   Transit    10.1.2.2/[12 ]  
  2     6.6.6.6            93 ms   Egress
  ```
* Check the path over which an inter-AS E2E SR-MPLS TE tunnel is established or locate the failure point on the path.
  
  
  
  To locate a failure point on an inter-AS E2E SR-MPLS TE tunnel, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-t** *time-out* | **-s** *packet-size* | **-g** | **-r** *reply-mode* ] \* **segment-routing** { { **auto-tunnel** *srAutoTunnelName* **version** { **draft2** | **draft4** } } | **te** { *tunnelName* | *ifType* *ifNum* } [ **draft2** ] } [ **hot-standby** ] [ **detail** ] command.
  
  ```
  <HUAWEI> [tracert lsp segment-routing te Tunnel 11 draft2](cmdqueryname=tracert+lsp+segment-routing+te+Tunnel+11+draft2)
    LSP Trace Route FEC: SEGMENT ROUTING TE TUNNEL IPV4 SESSION QUERY Tunnel11 , press CTRL_C to break.
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   10.1.1.2/[48061 48120 2000 ]
    1      10.1.1.2           393 ms  Transit   10.2.1.2/[48120 2000 ]
    2      10.2.1.2           18 ms   Transit   10.3.1.2/[2000 ]
    3      10.3.1.2           23 ms   Transit   10.4.1.2/[3 ]
    4      5.5.5.9            30 ms   Egress    
  ```
* Check the path information or locate the failure point in an MPLS LDP ECMP load balancing scenario.
  
  
  
  To locate the failure point of an ECMP load balancing path, run the [**tracert lsp**](cmdqueryname=tracert+lsp)[ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r***reply-mode* | **-t** *time-out* | **-s** *packet-size* | **-g** ] \* **ip***destination-iphost mask-length***multi-loopback-address** [ *begin-address***to***end-address* ] [ **nexthop***nexthopAddr* ] [ **ddmap** ] command
  
  ```
  <HUAWEI> tracert lsp ip 3.3.3.3 32 multi-loopback-address 127.0.0.0 to 127.0.0.3
    LSP Trace Route FEC: IPV4 PREFIX 3.3.3.3/32 , press CTRL_C to break.
    destination-ip-address: 127.0.0.0
    TTL    Replier            Time    Type
    1      10.1.1.2           7 ms    Transit   
    2      3.3.3.3            6 ms    Egress    
    destination-ip-address: 127.0.0.1
    TTL    Replier            Time    Type
    1      10.2.1.2           4 ms    Transit   
    2      3.3.3.3            4 ms    Egress    
    destination-ip-address: 127.0.0.2
    TTL    Replier            Time    Type
    1      10.1.1.2           2 ms    Transit   
    2      3.3.3.3            3 ms    Egress    
    destination-ip-address: 127.0.0.3
    TTL    Replier            Time    Type
    1      10.2.1.2           2 ms    Transit   
    2      3.3.3.3            2 ms    Egress    
    --- summary of all paths ---
    path 1 found
    TTL    Replier            Time    Type
    1      10.1.1.2           2 ms    Transit   
    2      3.3.3.3            3 ms    Egress    
    path 2 found
    TTL    Replier            Time    Type
    1      10.2.1.2           2 ms    Transit   
    2      3.3.3.3            2 ms    Egress    
  ```
* (Optional) Run the [**display lspv statistics**](cmdqueryname=display+lspv+statistics) command to check LSPV packet statistics.
  
  
  
  If the test performed using the [**tracert lsp**](cmdqueryname=tracert+lsp) command fails, you can run this command to check whether the fault occurs on the LSP or the device.
* (Optional) Run the [**reset lspv statistics**](cmdqueryname=reset+lspv+statistics) command to clear LSPV packet statistics.

#### Follow-up Procedure

After the test is completed, you are advised to run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable) command to disable the device from responding to MPLS Echo Request packets so as to prevent system resource occupation.