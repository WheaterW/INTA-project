Using Ping to Check Link Connectivity on a P2MP MPLS Network
============================================================

Run the ping commands to check the connectivity between nodes on a Point-to-Multipoint (P2MP) MPLS network.

#### Usage Scenario

On a VPLS over P2MP network, ping can be used to check the following tunnels:

* P2MP label distribution protocol (LDP) label switched paths (LSPs)
* P2MP TE tunnels that are automatically generated

#### Pre-configuration Tasks

Before using ping to check the P2MP network connectivity, ensure that P2MP is correctly configured.


#### Procedure

1. Run the [**ping multicast-lsp**](cmdqueryname=ping+multicast-lsp) command to check the connectivity of the following tunnels on a P2MP network:
   
   
   * P2MP LDP LSPs
     
     [**ping multicast-lsp**](cmdqueryname=ping+multicast-lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-j** *jitter-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** ] \* **mldp p2mp root-ip** *root-ip-address* { **lsp** *lsp-id* | **opaque-value** *opaque-value* } [ **leaf-destination** *leaf-destination* ]
   * P2MP TE tunnels that are automatically generated
     
     [**ping multicast-lsp**](cmdqueryname=ping+multicast-lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-j** *jitter-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** ] \* **te-auto-tunnel** *auto-tunnel-name* [ **leaf-destination** *leaf-destination* ]
   
   # Use ping to check the P2MP LDP LSP connectivity.
   
   ```
   <HUAWEI> ping multicast-lsp mldp p2mp root-ip 1.1.1.1 lsp-id 1
     LSP PING FEC: Multicast P2MP LDP root-ip 1.1.1.1 opaque-value 01000400014497 : 100  data bytes, press CTRL_C to break
       Reply from 10.10.10.10: bytes=100 Sequence=1 time=60 ms
       Reply from 10.10.10.10: bytes=100 Sequence=2 time=50 ms
       Reply from 10.10.10.10: bytes=100 Sequence=3 time=30 ms
       Reply from 10.10.10.10: bytes=100 Sequence=4 time=100 ms
       Reply from 10.10.10.10: bytes=100 Sequence=5 time=80 ms
   
       round-trip min/avg/max = 30/64/100 ms
   ```
   
   # Use ping to check the P2MP TE tunnel connectivity.
   
   ```
   <HUAWEI> ping multicast-lsp te-auto-tunnel P2MPoh5121 
     LSP PING FEC: RSVP P2MP IPv4 P2MP-Auto-tunnel P2MPoh5121 : 100  data bytes, press CTRL_C to break                                            
       Reply from 2.2.2.2: bytes=100 Sequence=1 time=10 ms                                                                                
       Reply from 3.3.3.3: bytes=100 Sequence=1 time=60 ms                                                                                 
       Reply from 5.5.5.5: bytes=100 Sequence=1 time=60 ms                                                                             
       Reply from 6.6.6.6: bytes=100 Sequence=1 time=80 ms                                                                             
       Reply from 2.2.2.2: bytes=100 Sequence=2 time=20 ms                                                                             
       Reply from 5.5.5.5: bytes=100 Sequence=2 time=50 ms                                                                             
       Reply from 6.6.6.6: bytes=100 Sequence=2 time=70 ms                                                                             
       Reply from 3.3.3.3: bytes=100 Sequence=2 time=70 ms                                                                             
       Reply from 2.2.2.2: bytes=100 Sequence=3 time=50 ms                                                                             
       Reply from 6.6.6.6: bytes=100 Sequence=3 time=100 ms                                                                            
       Reply from 3.3.3.3: bytes=100 Sequence=3 time=110 ms                                                                            
       Reply from 5.5.5.5: bytes=100 Sequence=3 time=110 ms                                                                            
       Reply from 2.2.2.2: bytes=100 Sequence=4 time=30 ms                                                                             
       Reply from 6.6.6.6: bytes=100 Sequence=4 time=50 ms                                                                             
       Reply from 5.5.5.5: bytes=100 Sequence=4 time=60 ms                                                                             
       Reply from 3.3.3.3: bytes=100 Sequence=4 time=60 ms                                                                             
       Reply from 2.2.2.2: bytes=100 Sequence=5 time=30 ms                                                                             
       Reply from 6.6.6.6: bytes=100 Sequence=5 time=40 ms                                                                             
       Reply from 5.5.5.5: bytes=100 Sequence=5 time=80 ms                                                                             
       Reply from 3.3.3.3: bytes=100 Sequence=5 time=80 ms                                                                             
                                                                                                                                       
     --- Destination: 2.2.2.2  ping statistics ---                                                                                     
       5 packet(s) transmitted                                                                                                         
       5 packet(s) received                                                                                                            
       0.00% packet loss                                                                                                               
       round-trip min/avg/max = 10/28/50 ms                                                                                            
                                                                                                                                       
     --- Destination: 3.3.3.3  ping statistics ---                                                                                     
       5 packet(s) transmitted                                                                                                         
       5 packet(s) received                                                                                                            
       0.00% packet loss                                                                                                               
       round-trip min/avg/max = 60/76/110 ms                                                                                           
                                                                                                                                       
     --- Destination: 5.5.5.5  ping statistics ---                                                                                     
       5 packet(s) transmitted                                                                                                         
       5 packet(s) received                                                                                                            
       0.00% packet loss                                                                                                               
       round-trip min/avg/max = 50/72/110 ms                                                                                           
                                                                                                                                       
     --- Destination: 6.6.6.6  ping statistics ---                                                                                     
       5 packet(s) transmitted                                                                                                         
       5 packet(s) received                                                                                                            
       0.00% packet loss                                                                                                               
       round-trip min/avg/max = 40/68/100 ms                                
   
   ```