Example for Configuring IP Address-based Microsegmentation
==========================================================

Example for Configuring IP Address-based Microsegmentation

#### Networking Requirements

On a distributed VXLAN gateway network (BGP EVPN) shown in [Figure 1](#EN-US_TASK_0000001513154514__fig1823813615012), the physical server, database server, VM1, and VM2 are deployed in the data center. The requirements are as follows:

* VM1, VM2, and the physical server can access the database server.
* VM1 and VM2 cannot communicate with the physical server.
* VM1 and VM2 can communicate with each other.

**Figure 1** Network diagram for configuring IP address-based microsegmentation![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 on DeviceA represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

In this example, interface 1, interface 2, and interface 3 on DeviceB represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

In this example, interface 1 and interface 2 on DeviceC represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001512834986.png)

**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | 100GE1/0/1 | 192.168.2.1/24 |
| LoopBack0 | 2.2.2.2/32 |
| DeviceB | 100GE1/0/1 | 192.168.3.1/24 |
| LoopBack0 | 1.1.1.1/32 |
| DeviceC | 100GE1/0/1 | 192.168.2.2/24 |
| 100GE1/0/2 | 192.168.3.2/24 |
| LoopBack0 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable microsegmentation.
2. Configure default microsegmentation policies.
3. Configure EPGs.
4. Specify GBPs.

#### Procedure

1. Configure VXLANs. For details, see the configuration files.
2. Enable microsegmentation.
   
   
   
   # Configure DeviceA. The configuration of DeviceB is the same as that of DeviceA. For details, see the configuration files.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] traffic-segment enable
   [*DeviceA] commit
   ```
3. Configure default microsegmentation policies.
   
   
   
   # Configure DeviceA. The configuration of DeviceB is the same as that of DeviceA. For details, see the configuration files.
   
   
   
   ```
   [~DeviceA] traffic-segment unknown-segment permit   //Configure the default access control policy for unknown EPG members. The default access control policy is permit.
   [~DeviceA] traffic-segment default-policy deny       //Configure the default access control policy for EPG members. The default access control policy is deny.
   [~DeviceA] traffic-segment same-segment permit      //Configure the default access control policy for members in an EPG. The default access control policy is none.
   [*DeviceA] commit
   ```
4. Configure an EPG.
   
   # On DeviceA, add VM1 and VM2 to EPG1.
   ```
   [~DeviceA] traffic-segment segment-id 32768 segment-name EPG1
   [*DeviceA-traffic-segment-32768] segment-member ip 192.168.10.1 32 vpn-instance vpn1
   [*DeviceA-traffic-segment-32768] segment-member ip 192.168.20.1 32 vpn-instance vpn1   
   [*DeviceA-traffic-segment-32768] quit
   [*DeviceA] commit
   ```
   
   # On DeviceB, add the physical server to EPG2 and the database server to EPG3.
   ```
   [~DeviceB] traffic-segment segment-id 32769 segment-name EPG2
   [*DeviceB-traffic-segment-32769] segment-member ip 192.168.30.1 32 vpn-instance vpn1 
   [*DeviceB-traffic-segment-32769] quit
   [*DeviceB] traffic-segment segment-id 32770 segment-name EPG3
   [*DeviceB-traffic-segment-32770] segment-member ip 192.168.40.1 32 vpn-instance vpn1
   [*DeviceB-traffic-segment-32770] quit
   [*DeviceA] commit
   ```
5. Specify GBPs.
   
   On DeviceA, specify GBPs. The configuration of DeviceB is the same as that of DeviceA. For details, see the configuration files.
   1. Create segment classifiers EPG1-EPG3 and EPG2-EPG3 on DeviceA and enter the segment classifier view.
      ```
      [~Device A]  segment classifier EPG1-EPG3     //Configure a matching rule for the traffic transmitted between EPG1 and EPG3.
      [*DeviceA-segmentclassifier-EPG1-EPG3] rule permit source-segment 32768 destination-segment 32770   
      [*DeviceA-segmentclassifier-EPG1-EPG3] rule permit source-segment 32770 destination-segment 32768  
      [*DeviceA-segmentclassifier-EPG1-EPG3] quit
      [*DeviceA] commit
      [~DeviceA] segment classifier EPG2-EPG3      //Configure a matching rule for the traffic transmitted between EPG2 and EPG3.
      [*DeviceA-segmentclassifier-EPG2-EPG3] rule permit source-segment 32769 destination-segment 32770  
      [*DeviceA-segmentclassifier-EPG2-EPG3] rule permit source-segment 32770 destination-segment 32769
      [*DeviceA-segmentclassifier-EPG2-EPG3] quit
      [*DeviceA] commit
      ```
   2. Create segment behaviors EPG1-EPG3 and EPG2-EPG3 on DeviceA and enter the segment behavior view.
      ```
      [~Device A]  segment behavior EPG1-EPG3   //Configure a behavior for the traffic transmitted between EPG1 and EPG3.
      [*DeviceA-segmentbehavior-EPG1-EPG3] quit
      [*DeviceA] commit
      [~Device A]  segment behavior EPG2-EPG3   //Configure a behavior for the traffic transmitted between EPG2 and EPG3.
      [*DeviceA-segmentbehavior-EPG2-EPG3] quit
      [*DeviceA] commit
      ```
   3. Create and apply a segment policy GBP on DeviceA.
      ```
      [~DeviceA] segment policy GBP  
      [*DeviceA-segmentpolicy-GBP] classifier EPG1-EPG3 behavior EPG1-EPG3
      [*DeviceA-segmentpolicy-GBP] classifier EPG2-EPG3 behavior EPG2-EPG3
      [*DeviceA-segmentpolicy-GBP] quit
      [*DeviceA] segment-policy GBP
      [*DeviceA] commit
      ```

#### Verifying the Configuration

# Run the [**display traffic-segment configured-information**](cmdqueryname=display+traffic-segment+configured-information) command on DeviceA to check the EPG configuration.

```
<HUAWEI>  display traffic-segment configured-information
--------------------------------------------------------------------------------
 Segment-Id      Segment-Name                    Member-Type        Member-Num  
--------------------------------------------------------------------------------
        32768      EPG1                          IPv4                        2  
                                                 IPv6                        0 
--------------------------------------------------------------------------------
Total: 1 Segment, 2 Member.
```

#### Configuration Scripts

* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  evpn-overlay enable
  #
  traffic-segment enable
  #
  traffic-segment same-segment permit
  #
  traffic-segment segment-id 32768 segment-name EPG1 intra-epg-behavior none                                                                                  
   segment-member ip 192.168.10.1 255.255.255.255 vpn-instance vpn1                                                                   
   segment-member ip 192.168.20.1 255.255.255.255 vpn-instance vpn1                                                                   
  #
  segment classifier EPG1-EPG3                                                                                                        
   rule 0 permit source-segment 32768 destination-segment 32770                                                                        
   rule 1 permit source-segment 32770 destination-segment 32768                                                                         
  #                                                                                                                                   
  segment classifier EPG2-EPG3                                                                                                        
   rule 0 permit source-segment 32769 destination-segment 32770                                                                        
   rule 1 permit source-segment 32770 destination-segment 32769                                                                         
  #                                                                                                                                   
  segment behavior EPG1-EPG3                                                                                                          
  #                                                                                                                                   
  segment behavior EPG2-EPG3                                                                                                          
  #                                                                                                                                   
  segment policy GBP                                                                                                                  
   classifier EPG1-EPG3 behavior EPG1-EPG3 precedence 3                                                                               
   classifier EPG2-EPG3 behavior EPG2-EPG3 precedence 6                                                                               
  #
  segment-policy GBP
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    vpn-target 1:1 export-extcommunity
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 10
   vxlan vni 10
   evpn 
    route-distinguisher 10:1
    vpn-target 10:1 export-extcommunity
    vpn-target 11:1 export-extcommunity
    vpn-target 10:1 import-extcommunity
  #
  bridge-domain 20
   vxlan vni 20
   evpn 
    route-distinguisher 20:1
    vpn-target 20:1 export-extcommunity
    vpn-target 11:1 export-extcommunity
    vpn-target 20:1 import-extcommunity
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 192.168.10.2 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 192.168.20.2 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/3.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface Nve1
   source 2.2.2.2
   vni 10 head-end peer-list protocol bgp
   vni 20 head-end peer-list protocol bgp
  #
  bgp 200
   peer 192.168.2.2 as-number 100
   #
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    peer 192.168.2.2 enable
  #
  bgp 100 instance evpn1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family vpn-instance vpn1                                                  
    import-route direct                                                           
    advertise l2vpn evpn 
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
  #
  return
  ```
* DeviceB configuration file
  ```
  #
  sysname SwitchB
  #
  evpn-overlay enable
  #
  traffic-segment enable
  #
  traffic-segment same-segment permit
  #
  traffic-segment segment-id 32769 segment-name EPG2 intra-epg-behavior none                                                                                  
   segment-member ip 192.168.30.1 255.255.255.255 vpn-instance vpn1                                                                   
  #                                                                                                                                   
  traffic-segment segment-id 32770 segment-name EPG3 intra-epg-behavior none                                                                                  
   segment-member ip 192.168.40.1 255.255.255.255 vpn-instance vpn1
  #
  segment classifier EPG1-EPG3                                                                                                        
   rule 0 permit source-segment 32768 destination-segment 32770                                                                         
   rule 1 permit source-segment 32770 destination-segment 32768                                                                         
  #                                                                                                                                   
  segment classifier EPG2-EPG3                                                                                                        
   rule 0 permit source-segment 32769 destination-segment 32770                                                                         
   rule 1 permit source-segment 32770 destination-segment 32769                                                                         
  #                                                                                                                                   
  segment behavior EPG1-EPG3                                                                                                          
  #                                                                                                                                   
  segment behavior EPG2-EPG3                                                                                                          
  #                                                                                                                                   
  segment policy GBP                                                                                                                  
   classifier EPG1-EPG3 behavior EPG1-EPG3 precedence 3                                                                               
   classifier EPG2-EPG3 behavior EPG2-EPG3 precedence 6                                                                               
  #
  segment-policy GBP
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 22:22
    vpn-target 2:2 export-extcommunity
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 30
   vxlan vni 30
   evpn 
    route-distinguisher 30:1
    vpn-target 30:1 export-extcommunity
    vpn-target 11:1 export-extcommunity
    vpn-target 30:1 import-extcommunity
  #
  bridge-domain 40
   vxlan vni 40
   evpn 
    route-distinguisher 40:1
    vpn-target 40:1 export-extcommunity
    vpn-target 11:1 export-extcommunity
    vpn-target 40:1 import-extcommunity
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 192.168.30.2 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 192.168.40.2 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 30
   bridge-domain 30
  #
  interface 100GE1/0/3.1 mode l2
   encapsulation dot1q vid 40
   bridge-domain 40
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  interface Nve1
   source 1.1.1.1
   vni 30 head-end peer-list protocol bgp
   vni 40 head-end peer-list protocol bgp
  #
  bgp 300
   peer 192.168.3.2 as-number 100
   #
   ipv4-family unicast
    network 1.1.1.1 255.255.255.255
    peer 192.168.3.2 enable
  #
  bgp 100 instance evpn1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   ipv4-family vpn-instance vpn1                                                  
    import-route direct                                                           
    advertise l2vpn evpn 
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
  #
  return
  ```
* DeviceC configuration file
  ```
  #
  sysname SwitchC
  #
  evpn-overlay enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 192.168.2.1 as-number 200
   peer 192.168.3.1 as-number 300
   #
   ipv4-family unicast
    network 3.3.3.3 255.255.255.255
    peer 192.168.2.1 enable
    peer 192.168.3.1 enable
  #
  bgp 100 instance evpn1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise irb
    peer 2.2.2.2 reflect-client
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
    peer 1.1.1.1 reflect-client
  #
  return
  ```