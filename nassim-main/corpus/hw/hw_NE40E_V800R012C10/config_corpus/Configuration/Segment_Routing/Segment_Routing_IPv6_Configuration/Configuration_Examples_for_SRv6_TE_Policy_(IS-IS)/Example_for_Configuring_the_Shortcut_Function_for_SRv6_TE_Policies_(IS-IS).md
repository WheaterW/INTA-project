Example for Configuring the Shortcut Function for SRv6 TE Policies (IS-IS)
==========================================================================

This section provides an example for configuring the shortcut function for SRv6 TE Policies.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001166635625__fig184238288365):

* All devices are Level-1 devices that belong to IS-IS process 1.
* A bidirectional SRv6 TE Policy is deployed along the path PE1-P1-PE2.

It is required that IS-IS routes recurse to the SRv6 TE Policy between PE1 and PE2 for traffic forwarding.

**Figure 1** Networking diagram for configuring the shortcut function for SRv6 TE Policies![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0000001119915842.png)

#### Precautions

1. To ensure that the shortcut function is correctly configured, the endpoint of the SRv6 TE Policy configured on the local device must be the same as the global TE IPv6 router ID advertised by IS-IS on the remote device.
2. During SRv6 TE Policy configuration, ensure that the last SID of the SRv6 TE Policy has the USD capability. Otherwise, a forwarding error will occur.
3. In SRv6 TE Policy shortcut scenarios, the Encaps or Insert-Encaps mode must be set for the corresponding SRv6 TE Policy.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, P1, P2, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, P1, P2, and PE2.
3. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, P1, and PE2.
4. Deploy an SRv6 TE Policy between PE1 and PE2.
5. Configure the shortcut function for the SRv6 TE Policy on PE1 and PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, P1, P2, and PE2
* IS-IS process ID of PE1, P1, P2, and PE2
* IS-IS level of PE1, P1, P2, and PE2
* Global TE IPv6 router ID of PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1. The configurations of P1, P2, and PE2 are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001166635625__example121226172748) in this section.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:11::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/3/0
   [*PE1-GigabitEthernet0/3/0] ipv6 enable
   [*PE1-GigabitEthernet0/3/0] ipv6 address 2001:DB8:13::1 96
   [*PE1-GigabitEthernet0/3/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-1
   [*DeviceA-isis-1] cost-style wide
   [*DeviceA-isis-1] network-entity 10.0000.0000.0005.00
   [*DeviceA-isis-1] ipv6 enable topology ipv6
   [*DeviceA-isis-1] quit
   [*DeviceA] interface gigabitethernet 0/1/0
   [*DeviceA-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface loopback1
   [*DeviceA-LoopBack1] isis ipv6 enable 1
   [*DeviceA-LoopBack1] commit
   [~DeviceA-LoopBack1] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-1
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   [*PE1-isis-1] ipv6 enable topology ipv6
   [*PE1-isis-1] ipv6 traffic-eng level-1
   [*PE1-isis-1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] interface gigabitethernet 0/3/0
   [*PE1-GigabitEthernet0/3/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/3/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] isis 1 
   [*P1-isis-1] is-level level-1
   [*P1-isis-1] cost-style wide
   [*P1-isis-1] network-entity 10.0000.0000.0002.00
   [*P1-isis-1] ipv6 enable topology ipv6
   [*P1-isis-1] ipv6 traffic-eng level-1
   [*P1-isis-1] quit
   [*P1] interface gigabitethernet 0/1/0
   [*P1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*P1-GigabitEthernet0/1/0] quit
   [*P1] interface gigabitethernet 0/2/0
   [*P1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P1-GigabitEthernet0/2/0] quit
   [*P1] interface loopback1
   [*P1-LoopBack1] isis ipv6 enable 1
   [*P1-LoopBack1] commit
   [~P1-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   [*PE2-isis-1] is-level level-1
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] ipv6 traffic-eng level-1
   [*PE2-isis-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface gigabitethernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] interface gigabitethernet 0/3/0
   [*PE2-GigabitEthernet0/3/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/3/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   
   
   # Configure P2.
   
   ```
   [~P2] isis 1 
   [*P2-isis-1] is-level level-1
   [*P2-isis-1] cost-style wide
   [*P2-isis-1] network-entity 10.0000.0000.0004.00
   [*P2-isis-1] ipv6 enable topology ipv6
   [*P2-isis-1] ipv6 traffic-eng level-1
   [*P2-isis-1] quit
   [*P2] interface gigabitethernet 0/1/0
   [*P2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*P2-GigabitEthernet0/1/0] quit
   [*P2] interface gigabitethernet 0/2/0
   [*P2-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*P2-GigabitEthernet0/2/0] quit
   [*P2] interface loopback1
   [*P2-LoopBack1] isis ipv6 enable 1
   [*P2-LoopBack1] commit
   [~P2-LoopBack1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] is-level level-1
   [*DeviceB-isis-1] cost-style wide
   [*DeviceB-isis-1] network-entity 10.0000.0000.0006.00
   [*DeviceB-isis-1] ipv6 enable topology ipv6
   [*DeviceB-isis-1] quit
   [*DeviceB] interface gigabitethernet 0/1/0
   [*DeviceB-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*DeviceB-GigabitEthernet0/1/0] quit
   [*DeviceB] interface loopback1
   [*DeviceB-LoopBack1] isis ipv6 enable 1
   [*DeviceB-LoopBack1] commit
   [~DeviceB-LoopBack1] quit
   ```
   
   After the configuration is complete, run the **display isis peer** command to check whether IS-IS has been configured successfully.
3. Configure SRv6 SIDs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] opcode ::100 end psp-usp-usd
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE1-isis-1] commit
   [~PE1-isis-1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] segment-routing ipv6
   [*P1-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*P1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
   [*P1-segment-routing-ipv6-locator] opcode ::100 end psp-usp-usd
   [*P1-segment-routing-ipv6-locator] quit
   [*P1-segment-routing-ipv6] quit
   [*P1] isis 1
   [*P1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*P1-isis-1] commit
   [~P1-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] opcode ::100 end psp-usp-usd
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   [*PE2-isis-1] commit
   [~PE2-isis-1] quit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:100::100/128                        FuncType    : End 
   Flavor      : PSP USP USD                                  SidCompress : NO
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:24:18.785                                                                       
   
   Total SID(s): 1  
   ```
   ```
   [~P1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:200::100/128                        FuncType    : End 
   Flavor      : PSP USP USD                                  SidCompress : NO
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:29:22.633                                                                  
   
   Total SID(s): 1
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table                        
                       ---------------------------------                        
   
   SID         : 2001:DB8:300::100/128                        FuncType    : End 
   Flavor      : PSP USP USD                                  SidCompress : NO
   LocatorName : as1                                          LocatorID   : 1   
   ProtocolType: STATIC                                       ProcessID   : --  
   UpdateTime  : 2021-05-05 09:36:31.017                                        
   
   Total SID(s): 1
   ```
4. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] te ipv6-router-id 2001:DB8:1::1
   [*PE1] segment-routing ipv6 
   [*PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:300::100
   [*PE1-segment-routing-ipv6-segment-list-list1] quit
   [*PE1-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10
   [*PE1-segment-routing-ipv6-policy-policy1] encapsulation-mode encaps
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE1-segment-routing-ipv6-policy-policy1-path] quit
   [*PE1-segment-routing-ipv6-policy-policy1] quit
   [*PE1-segment-routing-ipv6] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] te ipv6-router-id 2001:DB8:3::3
   [*PE2] segment-routing ipv6 
   [*PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:200::100
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100::100
   [*PE2-segment-routing-ipv6-segment-list-list1] quit
   [*PE2-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10
   [*PE2-segment-routing-ipv6-policy-policy1] encapsulation-mode encaps
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] quit
   [*PE2-segment-routing-ipv6-policy-policy1] quit
   [*PE2-segment-routing-ipv6] commit
   ```
   
   After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy
   PolicyName : policy1                                    
   Color                   : 10                             Endpoint             : 2001:DB8:3::3 
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -             
   Policy State            : Up                             State Change Time    : 2021-06-10 12:06:45 
   Admin State             : Up                             Traffic Statistics   : Disable       
   Backup Hot-Standby      : Disable                        BFD                  : Disable       
   Interface Index         : 26                             Interface Name       : SRv6TE-Policy-5
   Interface State         : Up                             Encapsulation Mode   : Encaps
   Binding SID             : 2001:DB8:100::900(Encaps, Preferred)
   Candidate-path Count    : 1                             
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary       
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0    
    Discriminator          : 100                            Binding SID          : 2001:DB8:100::900
    GroupId                : 1                              Policy Name          : policy1
    Template ID            : 0                              Path Verification    : Disable       
    DelayTimerRemain       : -                              Network Slice ID     : - 
    Segment-List Count     : 1                             
     Segment-List          : list1                         
      Segment-List ID      : 1                              XcIndex              : 1             
      List State           : Up                             DelayTimerRemain     : - 
      Verification State   : -                              SuppressTimeRemain   : -             
      PMTU                 : 9600                           Active PMTU          : 9600          
      Weight               : 1                              BFD State            : - 
      Loop Detection State : Up                             BFD Delay Remain     : -          
      Network Slice ID     : -     
      Binding SID          : -
      Reverse Binding ID   : -
      SID :          
            2001:DB8:200::100                              
            2001:DB8:300::100 
   ```
5. Configure the shortcut function for the SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip ipv6-prefix p1 permit 2001:DB8:20:: 96 
   [*PE1] ip ipv6-prefix p1 permit 2001:DB8:6::6 128
   [*PE1] route-policy rp1 permit node 10                     
   [*PE1-route-policy] if-match ipv6 address prefix-list p1
   [*PE1-route-policy] quit
   [*PE1] segment-routing ipv6 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1
   [*PE1-segment-routing-ipv6-policy-policy1] igp shortcut isis route-policy rp1
   [*PE1-segment-routing-ipv6-policy-policy1] isis ipv6 enable 1 
   [*PE1-segment-routing-ipv6-policy-policy1] igp metric relative -1 
   [*PE1-segment-routing-ipv6-policy-policy1] quit 
   [*PE1-segment-routing-ipv6] commit
   [~PE1-segment-routing-ipv6] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip ipv6-prefix p1 permit 2001:DB8:10:: 96 
   [*PE2] ip ipv6-prefix p1 permit 2001:DB8:5::5 128
   [*PE2] route-policy rp1 permit node 10                     
   [*PE2-route-policy] if-match ipv6 address prefix-list p1
   [*PE2-route-policy] quit
   [*PE2] segment-routing ipv6 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1
   [*PE2-segment-routing-ipv6-policy-policy1] igp shortcut isis route-policy rp1
   [*PE2-segment-routing-ipv6-policy-policy1] isis ipv6 enable 1  
   [*PE2-segment-routing-ipv6-policy-policy1] igp metric relative -1 
   [*PE2-segment-routing-ipv6-policy-policy1] quit 
   [*PE2-segment-routing-ipv6] commit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After the configuration is complete, run the **display isis route ipv6** command to check IS-IS routing information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis route ipv6                                             
   
   
                            Route information for ISIS(1)                      
                            -----------------------------       
   
                           ISIS(1) Level-1 Forwarding Table  
                           --------------------------------      
    IPV6 Dest.       ExitInterface      NextHop                    Cost     Flags    
   --------------------------------------------------------------------------------
   2001:DB8:1::1/128 Loop1              Direct                     0        D/-/L/-                               
   2001:DB8:2::2/128 GE0/1/0            FE80::3AB0:9EFF:FE31:307   10       A/-/-/-                  
   2001:DB8:3::3/128 GE0/1/0            FE80::3AB0:9EFF:FE31:307   10       A/-/-/-                             
   2001:DB8:5::5/128 GE0/2/0            FE80::3AB0:9EFF:FE21:300   10       A/-/-/-                  
   2001:DB8:6::6/128 SRv6TE-Policy-5    ::                         25       A/S/-/-                             
   2001:DB8:10::/96  GE0/2/0            Direct                     10       D/-/L/-                              
   2001:DB8:11::/96  GE0/1/0            Direct                     10       D/-/L/-                             
   2001:DB8:12::/96  GE0/1/0            FE80::3AB0:9EFF:FE31:307   20       A/-/-/-                 
   2001:DB8:20::/96  SRv6TE-Policy-5    ::                         25       A/S/-/-                 
   2001:DB8:100::/64 NULL0              -                          0        A/-/L/-                                 
   2001:DB8:200::/64 GE0/1/0            FE80::3AB0:9EFF:FE31:307   10       A/-/-/-                  
   2001:DB8:300::/64 GE0/1/0            FE80::3AB0:9EFF:FE31:307   15       A/-/-/- 
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid        
        Protect Type: L-Link Protect, N-Node Protect 
   ```
   
   Run the **display ipv6 routing-table brief** command to check IPv6 routing information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ipv6 routing-table brief 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route  
   ------------------------------------------------------------------------------    
   Routing Table : _public_                                   
            Destinations : 18       Routes : 18               
   Format :                                                   
   Destination/Mask                             Protocol      
   Nexthop                                      Interface     
   ------------------------------------------------------------------------------
    ::1/128                                     Direct        
     ::1                                        InLoopBack0   
    ::FFFF:127.0.0.0/104                        Direct        
     ::FFFF:127.0.0.1                           InLoopBack0   
    ::FFFF:127.0.0.1/128                        Direct        
     ::1                                        InLoopBack0   
    2001:DB8:1::1/128                           Direct        
     ::1                                        LoopBack1     
    2001:DB8:2::2/128                           ISIS-L1       
     FE80::3AB0:9EFF:FE31:307                   GE0/1/0  
    2001:DB8:3::3/128                           ISIS-L1       
     FE80::3AB0:9EFF:FE31:307                   GE0/1/0  
    2001:DB8:5::5/128                           ISIS-L1       
     FE80::3AB0:9EFF:FE21:300                   GE0/2/0  
    2001:DB8:6::6/128                           ISIS-L1  
     ::                                         SRv6TE-Policy-5 
    2001:DB8:10::/96                            Direct        
     2001:DB8:10::1                             GE0/2/0  
    2001:DB8:10::1/128                          Direct        
     ::1                                        GE0/2/0  
    2001:DB8:11::/96                            Direct        
     2001:DB8:11::1                             GE0/1/0  
    2001:DB8:11::1/128                          Direct        
     ::1                                        GE0/1/0  
    2001:DB8:12::/96                            ISIS-L1       
     FE80::3AB0:9EFF:FE31:307                   GE0/1/0  
    2001:DB8:20::/96                            ISIS-L1       
     ::                                         SRv6TE-Policy-5 
    2001:DB8:100::/64                           ISIS-L1       
     ::                                         NULL0         
    2001:DB8:200::/64                           ISIS-L1       
     FE80::3AB0:9EFF:FE31:307                   GE0/1/0  
    2001:DB8:300::/64                           ISIS-L1       
     FE80::3AB0:9EFF:FE31:307                   GE0/1/0  
    FE80::/10                                   Direct        
     ::                                         NULL0
   ```
   
   Because the IGP metric value of the shortcut route of the SRv6 TE Policy is less than that of a common route, the outbound interface of the route 2001:DB8:6::6/128 on PE1 is the SRv6 TE Policy.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  te ipv6-router-id 2001:DB8:1::1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator as1 ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::100 end psp-usp-usd
   srv6-te-policy locator as1                                        
   segment-list list1
    index 5 sid ipv6 2001:DB8:200::100 
    index 10 sid ipv6 2001:DB8:300::100
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 10  
    encapsulation-mode encaps   
    igp shortcut isis route-policy rp1
    isis ipv6 enable 1  
    candidate-path preference 100
     segment-list list1
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   ipv6 traffic-eng level-1
   segment-routing ipv6 locator as1 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:13::1/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  # 
  ip ipv6-prefix p1 index 10 permit 2001:DB8:20:: 96
  ip ipv6-prefix p1 index 20 permit 2001:DB8:6::6 128
  #
  route-policy rp1 permit node 10                 
   if-match ipv6 address prefix-list p1           
  #                                               
  return 
  ```
* P1 configuration file
  
  ```
  #
  sysname P1        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator as1 ipv6-prefix 2001:DB8:200:: 64 static 32
   opcode ::100 end psp-usp-usd
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   ipv6 traffic-eng level-1
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:11::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  te ipv6-router-id 2001:DB8:3::3
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3 
   locator as1 ipv6-prefix 2001:DB8:300:: 64 static 32 
    opcode ::100 end psp-usp-usd
   srv6-te-policy locator as1
   segment-list list1
    index 5 sid ipv6 2001:DB8:200::100 
    index 10 sid ipv6 2001:DB8:100::100
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 10   
    encapsulation-mode encaps
    igp shortcut isis route-policy rp1
    isis ipv6 enable 1 
    candidate-path preference 100
     segment-list list1          
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   ipv6 traffic-eng level-1
   segment-routing ipv6 locator as1 auto-sid-disable
   #               
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #   
  ip ipv6-prefix p1 index 10 permit 2001:DB8:10:: 96
  ip ipv6-prefix p1 index 20 permit 2001:DB8:5::5 128
  #
  route-policy rp1 permit node 10                 
   if-match ipv6 address prefix-list p1           
  #                                               
  return
  ```
* P2 configuration file
  
  ```
  #
  sysname P2                     
  #               
  isis 1         
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #              
   ipv6 enable topology ipv6
   ipv6 traffic-eng level-1
   #  
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:13::2/96
   isis ipv6 enable 1
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::1/96
   isis ipv6 enable 1 
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:4::4/128
   isis ipv6 enable 1
  #               
  return
  ```
* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0005.00
   #              
   ipv6 enable topology ipv6
   # 
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:10::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:5::5/128
   isis ipv6 enable 1          
  #               
  return 
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #               
  isis 1        
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0006.00
   #              
   ipv6 enable topology ipv6
   #  
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/96
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:6::6/128
   isis ipv6 enable 1
  #
  return
  ```