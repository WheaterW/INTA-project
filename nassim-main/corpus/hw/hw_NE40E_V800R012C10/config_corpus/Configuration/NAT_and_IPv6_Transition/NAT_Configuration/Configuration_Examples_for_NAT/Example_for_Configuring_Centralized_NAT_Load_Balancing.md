Example for Configuring Centralized NAT Load Balancing
======================================================

This section provides an example for configuring centralized NAT load balancing to implement many-to-many translation between private and public networks and allow PCs on a specified network segment to access the Internet.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

On the network shown in [Figure 1](#EN-US_TASK_0000001093157612__en-us_task_0172374594_fig_dc_ne_cfg_nat_005701), in a centralized NAT scenario, the Router performs the NAT function to help PCs within an enterprise network access the Internet. The Router uses the Ethernet interface 0/2/0 to connect to the enterprise network.

[Figure 1](#EN-US_TASK_0000001093157612__en-us_task_0172374594_fig_dc_ne_cfg_nat_005701) shows IP addresses of interfaces. The configuration requirements are as follows:

* Only PCs on the network segment of 192.168.10.0/24 can access the Internet.
* Many-to-many NAT needs to be performed for IP addresses between the private and public networks.

**Figure 1** Network diagram of centralized NAT load balancing![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/2/0.


  
![](images/fig_dc_ne_cfg_nat_0009.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a NAT load balancing instance.
2. Configure a CGN global static address pool.
3. Bind the NAT instance to the global address pool.
4. Configure a NAT traffic diversion policy.
5. Configure a NAT conversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* NAT load balancing instance
* ID of the NAT address pool and the name of the global static address pool to be bound to the NAT instance
* Information about the NAT traffic diversion policy![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the address pool usage is too high, perform the following operations. Otherwise, address pool resources will be unevenly allocated, causing users to fail to access the Internet.
  
  + Before CPU capacity expansion, expand address pool resources so that new CPUs can be assigned normal initial address segments.
  + After capacity expansion, you are advised to run the **reset nat session table** command to clear the sessions and perform load balancing again.


#### Procedure

1. Create a NAT load balancing instance.
   1. Set the maximum number of sessions that can be created on the CPU of the NAT service board to 6M.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname CGNA
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~CGNA] vsm on-board-mode disable
      ```
      ```
      [*CGNA] commit
      ```
      ```
      [~CGNA] license
      ```
      ```
      [~CGNA-license] active nat session-table size 6 slot 1
      ```
      ```
      [~CGNA-license] active nat session-table size 6 slot 2
      ```
      ```
      [~CGNA-license] active nat bandwidth-enhance 40 slot 1
      ```
      ```
      [~CGNA-license] active nat bandwidth-enhance 40 slot 2
      ```
      ```
      [~CGNA-license] quit
      ```
   2. Create a service-instance group named **groupa** and bind it to service-location groups **1** and **2**.
      
      ```
      [~CGNA] service-location 1
      ```
      ```
      [*CGNA-service-location-1] location slot 1
      ```
      ```
      [*CGNA-service-location-1] commit
      ```
      ```
      [~CGNA-service-location-1] quit
      ```
      ```
      [~CGNA] service-location 2
      ```
      ```
      [*CGNA-service-location-2] location slot 2
      ```
      ```
      [*CGNA-service-location-2] commit
      ```
      ```
      [~CGNA-service-location-2] quit
      ```
      ```
      [~CGNA] service-instance-group groupa
      ```
      ```
      [*CGNA-service-instance-group-groupa] service-location 1
      ```
      ```
      [*CGNA-service-instance-group-groupa] service-location 2
      ```
      ```
      [*CGNA-service-instance-group-groupa] commit
      ```
      ```
      [~CGNA-service-instance-group-groupa] quit
      ```
   3. Bind a NAT instance named **cpe1** to the service-instance group named **groupa**.
      
      ```
      [~CGNA] nat instance cpe1 id 11
      ```
      ```
      [*CGNA-nat-instance-cpe1] service-instance-group groupa
      ```
      ```
      [*CGNA-nat-instance-cpe1] commit
      ```
      ```
      [~CGNA-nat-instance-cpe1] quit
      ```
2. Configure a CGN global static address pool.
   
   # Create an address segment 11.11.11.1/24 in the CGN global static address pool named **pool1**.
   
   ```
   [~CGNA] nat ip-pool pool1
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] nat-instance subnet length initial 25 extend 27
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] nat-instance ip used-threshold upper-limit 60 lower-limit 40
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] nat alarm ip threshold 60
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] commit
   ```
   ```
   [~CGNA-nat-ip-pool-pool1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) When users are online, if you want to change the address segment of a global address pool or the length of an assigned address segment, run the **section lock** command first. For example:
   ```
   [~CGNA] nat ip-pool pool1
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] section 0 11.11.11.1 mask 24
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] section 0 lock
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] commit
   ```
   ```
   [~CGNA-nat-ip-pool-pool1] reset nat user nat-ip-pool pool1 section 0
   ```
   ```
   [~CGNA-nat-ip-pool-pool1] undo section 0
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] commit
   ```
   ```
   [~CGNA-nat-ip-pool-pool1] nat-instance subnet initial 24 extend 24
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] commit
   ```
   ```
   [~CGNA-nat-ip-pool-pool1] section 0 1.2.3.4 mask 24
   ```
   ```
   [*CGNA-nat-ip-pool-pool1] commit
   ```
   ```
   [~CGNA-nat-ip-pool-pool1] quit
   ```
3. Bind the NAT instance to the global address pool.
   
   # Bind the address pool named **group1** in the NAT instance named **cpe1** to the global static address pool named **pool1**.
   
   ```
   [~CGNA] nat instance cpe1
   ```
   ```
   [~CGNA-nat-instance-cpe1] nat address-group group1 group-id 1 bind-ip-pool pool1
   ```
   ```
   [*CGNA-nat-instance-cpe1] commit
   ```
   ```
   [~CGNA-nat-instance-cpe1] quit
   ```
4. Configure a NAT traffic diversion policy.
   
   1. Configure an ACL numbered **3001** and an ACL rule numbered **1** to allow hosts only within the network segment 192.168.10.0/24 to access the Internet.
      
      ```
      [~CGNA] acl 3001
      ```
      ```
      [*CGNA-acl4-advance-3001] rule 1 permit ip source 192.168.10.0 0.0.0.255
      ```
      ```
      [*CGNA-acl4-advance-3001] commit
      ```
      ```
      [~CGNA-acl4-advance-3001] quit
      ```
   2. Configure a traffic classifier.
      
      ```
      [~CGNA] traffic classifier c1
      ```
      ```
      [*CGNA-classifier-c1] if-match acl 3001
      ```
      ```
      [*CGNA-classifier-c1] commit
      ```
      ```
      [~CGNA-classifier-c1] quit
      ```
   3. Configure a traffic behavior named **b1**, which binds traffic to the NAT instance named **cpe1**.
      
      ```
      [~CGNA] traffic behavior b1
      ```
      ```
      [*CGNA-behavior-b1] nat bind instance cpe1
      ```
      ```
      [*CGNA-behavior-b1] commit
      ```
      ```
      [~CGNA-behavior-b1] quit
      ```
   4. Define a NAT policy to associate the ACL rule with the traffic behavior.
      
      ```
      [~CGNA] traffic policy p1
      ```
      ```
      [*CGNA-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*CGNA-trafficpolicy-p1] commit
      ```
      ```
      [~CGNA-trafficpolicy-p1] quit
      ```
   5. Apply the NAT traffic diversion policy in the interface view.
      
      ```
      [~CGNA] interface gigabitEthernet 0/2/0
      ```
      ```
      [~CGNA-GigabitEthernet0/2/0] ip address 192.168.10.1 24
      ```
      ```
      [*CGNA-GigabitEthernet0/2/0] traffic-policy p1 inbound
      ```
      ```
      [*CGNA-GigabitEthernet0/2/0] commit
      ```
      ```
      [~CGNA-GigabitEthernet0/2/0] quit
      ```
5. Configure a NAT conversion policy.
   
   ```
   [~CGNA] nat instance cpe1
   ```
   ```
   [~CGNA-nat-instance-cpe1] nat outbound 3001 address-group group1
   ```
   ```
   [*CGNA-nat-instance-cpe1] commit
   ```
   ```
   [~CGNA-nat-instance-cpe1] quit
   ```
6. Verify the configuration.
   
   # Display detailed user information on CPU 0 of the service board in slot 1.
   
   ```
   [~CGNA] display nat user-information slot 1 verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...             
   Slot: 1                                                               
   Total number:  1.                                                          
     --------------------------------------------------------------- 
     User Type                             :  NAT444                               
     CPE IP                                :  192.168.10.100                           
     User ID                               :  -                                    
     VPN Instance                          :  -                                    
     Address Group                         :  group1                                    
     NoPAT Address Group                   :  -
     NAT Instance                          :  cpe1                                 
     Public IP                             :  11.11.11.1                          
     Start Port                            :  1152                                 
     Port Range                            :  0                                   
     Port Total                            :  5                                   
     Extend Port Alloc Times               :  0                                    
     Extend Port Alloc Number              :  0                                    
     First/Second/Third Extend Port Start  :  0/0/0                                
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512                 
     Total/TCP/UDP/ICMP Session Current    :  5/5/0/0                              
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512                 
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0                              
     Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0                              
     Total/TCP/UDP/ICMP Port Current       :  5/5/0/0                              
     Nat ALG Enable                        :  NULL                                  
     Token/TB/TP                           :  0/0/0                                
     Port Forwarding Flag                  :  Non Port Forwarding                  
     Port Forwarding Ports                 :  0 0 0 0 0                            
     Aging Time(s)                         :  -                                    
     Left Time(s)                          :  -                                    
     Port Limit Discard Count              :  0                                    
     Session Limit Discard Count           :  0                                    
     Fib Miss Discard Count                :  0                                    
     -->Transmit Packets                   :  15                                   
     -->Transmit Bytes                     :  660                                  
     -->Drop Packets                       :  0                                    
     <--Transmit Packets                   :  40                                   
     <--Transmit Bytes                     :  1740                                 
     <--Drop Packets                       :  0                                    
   ---------------------------------------------------------------
   ```
   
   # Display load balancing statistics of the NAT instance named **cpe1** on the service board in slot 1.
   
   ```
   [~CGNA] display nat statistics global nat-instance cpe1 slot 1
   ```
   ```
   Slot: 1                                                          
   ---------------------------------------------------------------------------
    Session table number                           :20
    User table number                              :0
    Total setup sessions                           :10
    Total teardown sessions                        :10
   ---------------------------------------------------------------------------
   
   Slot: 1                                                          
   ---------------------------------------------------------------------------
    Session table number                           :30
    User table number                              :0
    Total setup sessions                           :15
    Total teardown sessions                        :15
   ---------------------------------------------------------------------------
   ```

#### Configuration Files

CGNA configuration file

```
#
sysname CGNA
vsm on-board-mode disable
#
license
 active nat session-table size 6 slot 1 engine 0
 active nat session-table size 6 slot 2  engine 1
 active nat bandwidth-enhance 40 slot 1
 active nat bandwidth-enhance 40 slot 2 
service-location 1      
 location slot 1 
#
service-location 2      
 location slot 2 
#
service-instance-group groupa      
 service-location 1      
 service-location 2
#
nat ip-pool pool1
 section 0 11.11.11.1 mask 24
 nat-instance subnet length initial 25 extend 27
 nat-instance ip used-threshold upper-limit 60 lower-limit 40
 nat alarm ip threshold 60
#
nat instance cpe1 id 11     
 service-instance-group groupa      
 nat address-group group1 group-id 1 bind-ip-pool pool1
 nat outbound 3001 address-group group1 
#
acl number 3001
 rule 1 permit ip source 192.168.10.0 0.0.0.255
#
traffic classifier c1 operator or
 if-match acl 3001 precedence 1
#
traffic behavior b1
 nat bind instance cpe1
#
traffic policy p1
 classifier c1 behavior b1 precedence 1
#
interface GigabitEthernet 0/2/0
 undo shutdown
 ip address 192.168.10.1 255.255.255.0
 traffic-policy p1 inbound
#
return

```