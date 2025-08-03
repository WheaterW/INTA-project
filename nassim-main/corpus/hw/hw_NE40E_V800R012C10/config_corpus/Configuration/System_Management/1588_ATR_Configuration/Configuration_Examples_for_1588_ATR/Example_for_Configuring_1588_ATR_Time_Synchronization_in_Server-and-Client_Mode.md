Example for Configuring 1588 ATR Time Synchronization in Server-and-Client Mode
===============================================================================

Example for Configuring 1588 ATR Time Synchronization in Server-and-Client Mode

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001782197726__fig169571636162013), the NE40E can be directly connected to a time server and be configured to work in 1588 ATR server-and-client mode. The T-BC can be connected to a base station or a hierarchical node to output time signals to the downstream device. The interface that directly connects T-BC1 to the time server needs to be configured to work in G.8275.1 mode. Some NEs on the intermediate microwave network do not support clock synchronization, but network devices can properly communicate with each other.

**Figure 1** T-BC time synchronization  
![](figure/en-us_image_0000001782197738.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

* On the upstream device:

1. Enable ITU-T G.8275.1, set the device type to T-BC, and enable 1588 ATR time source synchronization.
2. Enable 1588 ATR.
3. Configure the device to support ITU-T G.8275.2.
4. Configure the device to work in server-and-client mode.
5. Configure the local IP address of the master-only-vport.
6. Configure an IP address for the outbound interface and enable ATR on the interface.
7. Enable unicast negotiation.
8. Verify the configuration.

* On the downstream device:

1. Enable 1588v2, set the device type to BC, and enable 1588 ATR time synchronization.
2. Enable 1588 ATR.
3. Configure the device to support ITU-T G.8275.2.
4. Configure the device to work in server-and-client mode.
5. Configure the local IP address of the vport and the list of remote clock servers that support negotiation.
6. Configure an IP address for the inbound interface and enable ATR on the interface.
7. Enable unicast negotiation.
8. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* Local IP address of the upstream device
* Local IP address of the downstream device
* Outbound interface of upstream 1588 ATR packets
* Inbound interface of downstream 1588 ATR packets


#### Procedure

1. Enable ITU-T G.8275.1 and 1588 ATR time source synchronization on T-BC1.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] ptp enable
   ```
   ```
   [~HUAWEI] ptp profile g-8275-1 enable
   ```
   ```
   [*HUAWEI] ptp device-type t-bc
   ```
   ```
   [*HUAWEI] ptp clock-source atr enable
   ```
   ```
   [*HUAWEI] commit
   ```
2. Enable 1588 ATR time source synchronization on T-BC2.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] ptp enable
   ```
   ```
   [*HUAWEI] ptp device-type bc
   ```
   ```
   [*HUAWEI] ptp clock-source atr enable
   ```
   ```
   [*HUAWEI] commit
   ```
3. Enable 1588 ATR on the device, configure the device to support ITU-T G.8275.2, and configure the device to work in server-and-client mode.
   
   
   
   # Configure T-BC1.
   
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname T-BC1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~T-BC1] ptp-adaptive enable
   ```
   ```
   [*T-BC1] ptp-adaptive time profile 
   ```
   ```
   [*T-BC1] ptp-adaptive device-type server-and-client
   ```
   ```
   [*T-BC1] commit
   ```
   
   # Enable 1588 ATR on T-BC2, configure T-BC2 to support ITU-T G.8275.2, and configure T-BC2 to work in server-and-client mode. The configuration is similar to that on T-BC1.
4. Configure the master-only-vport information on T-BC1.
   
   
   ```
   [~T-BC1] ip vpn-instance vpn1 
   ```
   ```
   [*T-BC1-vpn-instance-vpn1] commit
   ```
   ```
   [~T-BC1-vpn-instance-vpn1] quit
   ```
   ```
   [~T-BC1] ptp-adaptive master-only-vport 1 port-ip 10.1.1.2 vpn-instance vpn1
   ```
   ```
   [*T-BC1] commit
   ```
5. Configure the vport of T-BC2 and the list of remote clock servers.
   
   
   ```
   [~T-BC2] ip vpn-instance vpn1 
   ```
   ```
   [*T-BC2-vpn-instance-vpn1] commit
   ```
   ```
   [~T-BC2-vpn-instance-vpn1] quit
   ```
   ```
   [~T-BC2] ptp-adaptive vport 1 port-ip 10.1.1.1 vpn-instance vpn1
   ```
   ```
   [*T-BC2] ptp-adaptive vport 1 remote-port-ip 10.1.1.2
   ```
   ```
   [*T-BC2] commit
   ```
6. Enable ATR on an interface and configure a local IP address for the interface.
   
   
   
   # Configure T-BC1.
   
   
   
   ```
   [~T-BC1] interface gigabitethernet 0/2/1
   ```
   ```
   [*T-BC1-GigabitEthernet0/2/1] ptp-adaptive atr enable
   ```
   ```
   [*T-BC1-GigabitEthernet0/2/1] ip binding vpn-instance vpn1
   ```
   ```
   [*T-BC1-GigabitEthernet0/2/1] ip address 10.1.1.2 24
   ```
   ```
   [*T-BC1-GigabitEthernet0/2/1] commit
   ```
   ```
   [~T-BC1-GigabitEthernet0/2/1] quit
   ```
   
   # Configure T-BC2.
   
   ```
   [~T-BC2] interface gigabitethernet 0/2/1
   ```
   ```
   [*T-BC2-GigabitEthernet0/2/1] ptp-adaptive atr enable
   ```
   ```
   [*T-BC2-GigabitEthernet0/2/1] ip binding vpn-instance vpn1
   ```
   ```
   [*T-BC2-GigabitEthernet0/2/1] ip address 10.1.1.1 24
   ```
   ```
   [*T-BC2-GigabitEthernet0/2/1] commit
   ```
   ```
   [~T-BC2-GigabitEthernet0/2/1] quit
   ```
7. Enable unicast negotiation.
   
   
   
   # Configure T-BC1.
   
   ```
   [~T-BC1] ptp-adaptive atr unicast-negotiate enable 
   [*T-BC1] commit
   ```
   
   # Enable unicast negotiation on T-BC2. The configuration is similar to that on T-BC1.
8. Verify the configuration.
   
   
   
   # Display all configurations of the 1588 ATR module.
   
   ```
   <T-BC1> display ptp-adaptive all
   ```
   ```
   Device config info                                                                                                                
     ------------------------------------------------------------------------------                                                    
     Ptp adaptive state      :enable           Device type        :server-and-client
     Sync mode               :time             Current state      :master+slave
     Packet dscp             :56               Domain value       :44                                                                  
     Announce interval       :10               Announce duration  :300s                                                                
     Sync interval           :3                Sync duration      :300s                                                                
     Delay_resp interval     :3                Delay_resp duration:300s                                                                
     Announce receipt timeout:3                One-way or two-way :two-way                                                             
     Profile                 :time                                                                
     
     BMCA run info                                                                                                                     
     ------------------------------------------------------------------------------                                                    
     Current trace source    :local                                                                                                    
   
     Vport list                                                                                                                        
     ------------------------------------------------------------------------------                                                    
     ID  Port state   Negotiate state                                                                                                  
   
     Master-only-vport list                                                                                                            
     ------------------------------------------------------------------------------                                                    
     ID  Ip Address      VPN                                      Client number                                                        
     1   10.1.1.2        vpn1                                     1  
   ```
   
   # Display information about successful negotiation of T-BC2.
   
   ```
   <T-BC2> display ptp-adaptive all
   ```
   ```
     Device config info                                                                                                                
     ------------------------------------------------------------------------------                                                    
     Ptp adaptive state      :enable         Device type        :server-and-client                                                     
     Sync mode               :time           Current state      :master+slave                                                          
     Packet dscp             :56             Domain value       :44                                                                    
     Announce interval       :10             Announce duration  :300s                                                                  
     Sync interval           :3              Sync duration      :300s                                                                  
     Delay_resp interval     :3              Delay_resp duration:300s                                                                  
     Announce receipt timeout:3              One-way or two-way :two-way                                                               
     Profile                 :time                                                                                                     
   
     BMCA run info                                                                                                                     
     ------------------------------------------------------------------------------                                                    
     Current trace source    :vport 1                                                                                                  
   
     Time performance statistics                                                                                                       
     ------------------------------------------------------------------------------                                                    
     Realtime(T2-T1)   :+0s, 127ns                                                                                                     
     Max(T2-T1)        :+11163s, 2057757ns                                                                                             
     Min(T2-T1)        :-0s, 62882358ns                                                                                                
     Realtime(T4-T3)   :+0s, 119ns                                                                                                     
     Max(T4-T3)        :+114224s, 804881946ns                                                                                          
     Min(T4-T3)        :-0s, 110ns                                                                                                     
   
     Vport list                                                                                                                        
     ------------------------------------------------------------------------------                                                    
     ID  Port state   Negotiate state                                                                                                  
     1   slave        Nego success
   ```
   
   # Display 1588 ATR vport information.
   
   ```
   <T-BC1> display ptp-adaptive master-only-vport
   ```
   ```
     Master-only-vport list                                                                                                            
     ------------------------------------------------------------------------------                                                    
     ID  Ip Address      VPN                                      Client number                                                        
     1   10.1.1.2        vpn1                                     1                                                                    
   
     Master-only-vport 1 client list                                                                                                   
         ID  Ip Address      Clock ID          Mode     Announce  Sync  Delay_resp                                                     
     ------------------------------------------------------------------------------                                                    
     0   14  10.1.1.1        202008fffe261204  two-way  0         -7    -7   
   ```
   
   # Display vport information on the downstream device.
   
   ```
   <T-BC2> display ptp-adaptive vport
   ```
   ```
     Vport 1                                                                                                                           
     ------------------------------------------------------------------------------                                                    
     VPN                     :vpn1 
     Local ip                :10.1.1.1         Remote port ip     :10.1.1.2                                                            
     Negotiate state         :Nego success                                                                                             
     Port state              :slave            Clock Class        :6                                                                   
     Pri2                    :128              Accuracy           :0xFE                                                                
     Local priority          :128              Asymmetry(ns)      :0    
   ```

#### Configuration Files

T-BC1 configuration file

```
#
sysname T-BC1
#
ptp-adaptive enable
ptp-adaptive time profile
ptp-adaptive device-type server-and-client                                                                                          
ptp-adaptive atr unicast-negotiate enable                                                                                           
ptp-adaptive master-only-vport 1 port-ip 10.1.1.2  
#                                                                                                                             
ptp enable                                                                                                                          
ptp profile g-8275-1 enable
ptp device-type t-bc
ptp clock-source atr enable
#   
interface GigabitEthernet0/2/1
 undo shutdown
 ip binding vpn-instance vpn1
 ip address 10.1.1.2 255.255.255.0
 ptp-adaptive atr enable
#
return
```

T-BC2 configuration file

```
#
sysname T-BC2
#
ptp-adaptive enable
ptp-adaptive time profile
ptp-adaptive device-type server-and-client                                                                                          
ptp-adaptive atr unicast-negotiate enable                                                                                           
ptp-adaptive vport 1 port-ip 10.1.1.1                                                                                               
ptp-adaptive vport 1 remote-port-ip 10.1.1.2 
#
ptp enable                                                                                                                          
ptp device-type bc   
                                                                                                               
ptp clock-source atr enable
# 
interface GigabitEthernet0/2/1
 undo shutdown
 ip binding vpn-instance vpn1
 ip address 10.1.1.1 255.255.255.0
 ptp-adaptive atr enable
# 
return
```