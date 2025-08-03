Using Tracert to Check the Forwarding Path on a P2MP MPLS Network
=================================================================

Run the tracert commands to check path information on a Point-to-Multipoint (P2MP) MPLS network so that faults can be located.

#### Usage Scenario

On a VPLS over P2MP network, tracert can be used to check the following tunnels:

* P2MP label distribution protocol (LDP) label switched paths (LSPs)
* P2MP TE tunnels that are automatically generated

#### Pre-configuration Tasks

Before using tracert to check the P2MP network connectivity, ensure that P2MP is correctly configured.


#### Procedure

1. Run the [**tracert multicast-lsp**](cmdqueryname=tracert+multicast-lsp) command to check path information about the following tunnels on a VPLS over P2MP network:
   
   
   * VPLS over P2MP LDP LSPs
     
     [**tracert multicast-lsp**](cmdqueryname=tracert+multicast-lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-j** *jitter-value* | **-r** *reply-mode* | **-t** *time-out* | **t-flag** ] \* **mldp p2mp root-ip** *root-ip-address* { **lsp** *lsp-id* | **opaque-value** *opaque-value* } [ **detail** ]
   * VPLS over P2MP TE tunnels that are automatically generated
     
     [**tracert multicast-lsp**](cmdqueryname=tracert+multicast-lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-j** *jitter-value* | **-r** *reply-mode* | **-t** *time-out* | **t-flag** ] \* **te-auto-tunnel** *auto-tunnel-name* [ **leaf-destination** *leaf-destination* ] [ **detail** ]
   
   # Use tracert to check path information about a P2MP LDP LSP.
   
   ```
   <HUAWEI> tracert multicast-lsp -h 10 mldp p2mp root-ip 1.1.1.1 lsp-id 1
     LSP Trace Route FEC: Multicast P2MP LDP , press CTRL_C to break.
     TTL   Replier            Time    Type      Downstream
     1     192.168.1.9        40 ms   Transit   192.168.2.12/[1024 ]
     2     10.10.10.10        110 ms  Egress
     3     10.10.10.10        140 ms  Egress
     4     10.10.10.10        50 ms   Egress
     5     10.10.10.10        70 ms   Egress
     6     10.10.10.10        80 ms   Egress
     7     10.10.10.10        70 ms   Egress
     8     10.10.10.10        30 ms   Egress
     9     10.10.10.10        60 ms   Egress
     10    10.10.10.10        110 ms  Egress
   ```
   
   # Use tracert to check path information about a P2MP TE tunnel.
   
   ```
   <HUAWEI> tracert multicast-lsp -h 2 te-auto-tunnel P2MPoh5121
     LSP Trace Route FEC: RSVP P2MP IPv4 P2MP-Auto-tunnel P2MPoh5121 , press CTRL_C to break.
     TTL   Replier            Time    Type      Downstream
     1     2.2.2.2            30 ms   Bud       172.16.3.2/[1048575 ]
     1     4.1.1.2            40 ms   Transit   5.1.1.2/[900001 ]
     2     2.2.2.2            30 ms   Bud       172.16.3.2/[1048575 ]
     2     6.6.6.6            60 ms   Egress
     2     3.3.3.3            80 ms   Egress
     2     5.5.5.5            80 ms   Egress 
   
   ```