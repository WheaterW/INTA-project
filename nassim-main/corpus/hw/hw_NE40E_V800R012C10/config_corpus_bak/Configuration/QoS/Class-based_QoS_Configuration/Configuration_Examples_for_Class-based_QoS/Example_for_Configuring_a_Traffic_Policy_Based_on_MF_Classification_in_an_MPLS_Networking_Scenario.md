Example for Configuring a Traffic Policy Based on MF Classification in an MPLS Networking Scenario
==================================================================================================

This section provides an example for configuring and applying traffic classifiers and behaviors in an MPLS networking scenario.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172371306__fig_dc_ne_qos_cfg_006901), PE1, the P, and PE2 are routers on the MPLS backbone network, and CE1 and CE2 are access routers on the edge of the backbone network. Three users from the local network access the Internet through CE1.

* On CE1, the CIR of the traffic of the user from the network segment 1.1.1.0 is limited to 10 Mbit/s, and the CBS is limited to 150000 bytes.
* On CE1, the CIR of the traffic of the user from the network segment 2.1.1.0 is limited to 5 Mbit/s, and the CBS is limited to 100000 bytes.
* On CE1, the CIR of the traffic of the user from the network segment 3.1.1.0 is limited to 2 Mbit/s, and the CBS is limited to 100000 bytes.
* On CE1, the DSCP values of the service packets from the three network segments are re-marked to 40, 26, and 0.
* On PE1, the CIR, CBS, PIR, and PBS for accessing the MPLS backbone network are limited to 15 Mbit/s, 300000 bytes, 20 Mbit/s, and 500000 bytes, respectively.
* On CE1, the CIR, CBS, PIR, and PBS of the UDP packets (except DNS, SNMP, SNMP trap, and syslog packets) are limited to 5 Mbit/s, 100000 bytes, 15 Mbit/s, and 200000 bytes, respectively.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GE 0/1/0, GE 0/2/0, GE 0/3/0, and GE 0/1/8, respectively.


**Figure 1** Configuring a traffic policy based on MF classification  
![](images/fig_dc_ne_qos_cfg_006901.png)  


#### Configuration Notes

When configuring a traffic policy based on MF classification, pay attention to the following:

* If both the **if-match any** and **deny** commands are configured, the MF classification function prevents all packets (including protocol packets) from passing through an interface. Therefore, exercise caution when using a combination of the preceding commands.
* If the permit or deny action is configured in both the **rule** command and the traffic behavior view, only the packets permitted by the **rule** command are processed based on the traffic behavior. If the deny action is configured in either the **rule** command or the traffic behavior view, all matched packets are discarded.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure ACL rules.
2. Configure traffic classifiers.
3. Configure traffic behaviors.
4. Configure traffic policies.
5. Apply the traffic policies to interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL numbers: 2001, 2002, 2003, 3001, and 3002
* Re-marked DSCP values for the packets from the three network segments: 40, 26, and 0
* CIRs of the traffic of users from the three network segments: 10 Mbit/s, 5 Mbit/s, and 2 Mbit/s; corresponding CBSs: 150000 bytes, 100000 bytes, and 100000 bytes
* CIR, CBS, PIR, and PBS of the UDP packets on CE1: 5 Mbit/s, 100000 bytes, 15 Mbit/s, and 200000 bytes
* CIR, CBS, PIR, and PBS on PE1: 15 Mbit/s, 300000 bytes, 20 Mbit/s, and 500000 bytes
* Names of traffic classifiers, traffic behaviors, and traffic policies, and numbers of the interfaces to which the traffic policies are applied

#### Procedure

1. Configure interface IP addresses, routes, and basic MPLS functions (for details, see the configuration files).
2. Configure MF classification on CE1 to limit the user traffic that accesses CE1 from the three local networks.
   
   
   
   # Configure ACL rules.
   
   ```
   [~CE1] acl number 2001
   ```
   ```
   [*CE1-acl4-basic-2001] rule permit source 1.1.1.0 0.0.0.255
   ```
   ```
   [*CE1-acl4-basic-2001] commit
   ```
   ```
   [~CE1-acl4-basic-2001] quit
   ```
   ```
   [~CE1] acl number 2002
   ```
   ```
   [*CE1-acl4-basic-2002] rule permit source 2.1.1.0 0.0.0.255
   ```
   ```
   [*CE1-acl4-basic-2002] commit
   ```
   ```
   [~CE1-acl4-basic-2002] quit
   ```
   ```
   [~CE1] acl number 2003
   ```
   ```
   [*CE1-acl4-basic-2003] rule permit source 3.1.1.0 0.0.0.255
   ```
   ```
   [*CE1-acl4-basic-2003] commit
   ```
   ```
   [~CE1-acl4-basic-2003] quit
   ```
   ```
   [~CE1] acl number 3001
   ```
   ```
   [*CE1-acl4-advance-3001] rule 0 permit udp destination-port eq dns
   ```
   ```
   [*CE1-acl4-advance-3001] rule 1 permit udp destination-port eq snmp
   ```
   ```
   [*CE1-acl4-advance-3001] rule 2 permit udp destination-port eq snmptrap
   ```
   ```
   [*CE1-acl4-advance-3001] rule 3 permit udp destination-port eq syslog 
   ```
   ```
   [*CE1-acl4-advance-3001] commit
   ```
   ```
   [~CE1-acl4-advance-3001] quit
   ```
   ```
   [~CE1] acl number 3002
   ```
   ```
   [*CE1-acl4-advance-3002] rule 4 permit udp 
   ```
   ```
   [*CE1-acl4-advance-3002] commit
   ```
   ```
   [~CE1-acl4-advance-3002] quit
   ```
   
   # Configure traffic classifiers and define ACL-based matching rules.
   
   ```
   [~CE1] traffic classifier a
   ```
   ```
   [*CE1-classifier-a] if-match acl 2001
   ```
   ```
   [*CE1-classifier-a] commit
   ```
   ```
   [~CE1-classifier-a] quit
   ```
   ```
   [~CE1] traffic classifier b
   ```
   ```
   [*CE1-classifier-b] if-match acl 2002
   ```
   ```
   [*CE1-classifier-b] commit
   ```
   ```
   [~CE1-classifier-b] quit
   ```
   ```
   [~CE1] traffic classifier c
   ```
   ```
   [*CE1-classifier-c] if-match acl 2003
   ```
   ```
   [*CE1-classifier-c] commit
   ```
   ```
   [~CE1-classifier-c] quit
   ```
   ```
   [~CE1] traffic classifier udplimit
   ```
   ```
   [*CE1-classifier-udplimit] if-match acl 3001
   ```
   ```
   [*CE1-classifier-udplimit] commit
   ```
   ```
   [~CE1-classifier-udplimit] quit
   ```
   ```
   [~CE1] traffic classifier udplimit1
   ```
   ```
   [*CE1-classifier-udplimit1] if-match acl 3002
   ```
   ```
   [*CE1-classifier-udplimit1] commit
   ```
   ```
   [~CE1-classifier-udplimit1] quit
   ```
   
   After the preceding configuration is complete, run the **display traffic classifier** command to check the traffic classifier configuration.
   
   ```
   [~CE1] display traffic classifier user-defined
   ```
   ```
   User Defined Classifier Information:
   ```
   ```
      Total: 65535  Used: 6  Free: 65529
   ```
   ```
      Classifier: a
   ```
   ```
       Description:
   ```
   ```
       Operator: or
   ```
   ```
       Rule(s):
   ```
   ```
         if-match acl 2001 precedence 1
   ```
   ```
      Classifier: b
   ```
   ```
       Description:
   ```
   ```
       Operator: or
   ```
   ```
       Rule(s):
   ```
   ```
         if-match acl 2002 precedence 2
   ```
   ```
      Classifier: c
   ```
   ```
       Description:
   ```
   ```
       Operator: or
   ```
   ```
       Rule(s):
   ```
   ```
         if-match acl 2003 precedence 3
   ```
   ```
      Classifier: udplimit
   ```
   ```
       Description:
   ```
   ```
       Operator: or
   ```
   ```
       Rule(s) :
   ```
   ```
         if-match acl 3001 precedence 4
   ```
   ```
      Classifier: udplimit1
   ```
   ```
       Description:
   ```
   ```
       Operator: or
   ```
   ```
       Rule(s) :
   ```
   ```
         if-match acl 3002
   ```
   
   # Define traffic behaviors, and configure traffic policing and DSCP values to be re-marked.
   
   ```
   [~CE1] traffic behavior e
   ```
   ```
   [*CE1-behavior-e] car cir 10000 cbs 150000 pbs 0
   ```
   ```
   [*CE1-behavior-e] remark dscp 40
   ```
   ```
   [*CE1-behavior-e] commit
   ```
   ```
   [~CE1-behavior-e] quit
   ```
   ```
   [~CE1] traffic behavior f
   ```
   ```
   [*CE1-behavior-f] car cir 5000 cbs 100000 pbs 0
   ```
   ```
   [*CE1-behavior-f] remark dscp 26
   ```
   ```
   [*CE1-behavior-f] commit
   ```
   ```
   [~CE1-behavior-f] quit
   ```
   ```
   [~CE1] traffic behavior g
   ```
   ```
   [*CE1-behavior-g] car cir 2000 cbs 100000 pbs 0
   ```
   ```
   [*CE1-behavior-g] remark dscp 0
   ```
   ```
   [*CE1-behavior-g] commit
   ```
   ```
   [~CE1-behavior-g] quit
   ```
   ```
   [~CE1] traffic behavior udplimit
   ```
   ```
   [*CE1-behavior-udplimit] permit
   ```
   ```
   [*CE1-behavior-udplimit] commit
   ```
   ```
   [~CE1-behavior-udplimit] quit
   ```
   ```
   [~CE1] traffic behavior udplimit1
   ```
   ```
   [*CE1-behavior-udplimit1] car cir 5000 pir 15000 cbs 100000 pbs 200000 green pass yellow discard red discard
   ```
   ```
   [*CE1-behavior-udplimit1] commit
   ```
   ```
   [~CE1-behavior-udplimit1] quit
   ```
   
   # Define traffic policies to associate the traffic classifiers with the traffic behaviors.
   
   ```
   [~CE1] traffic policy 1
   ```
   ```
   [*CE1-trafficpolicy-1] classifier a behavior e
   ```
   ```
   [*CE1-trafficpolicy-1] commit
   ```
   ```
   [~CE1-trafficpolicy-1] quit
   ```
   ```
   [~CE1] traffic policy 2
   ```
   ```
   [*CE1-trafficpolicy-2] classifier b behavior f
   ```
   ```
   [*CE1-trafficpolicy-2] commit
   ```
   ```
   [~CE1-trafficpolicy-2] quit
   ```
   ```
   [~CE1] traffic policy 3
   ```
   ```
   [*CE1-trafficpolicy-3] classifier c behavior g
   ```
   ```
   [*CE1-trafficpolicy-3] commit
   ```
   ```
   [~CE1-trafficpolicy-3] quit
   ```
   ```
   [~CE1] traffic policy udplimit
   ```
   ```
   [*CE1-trafficpolicy-udplimit] classifier udplimit behavior udplimit
   ```
   ```
   [*CE1-trafficpolicy-udplimit] classifier udplimit1 behavior udplimit1
   ```
   ```
   [*CE1-trafficpolicy-udplimit] commit
   ```
   ```
   [~CE1-trafficpolicy-udplimit] quit
   ```
   
   After completing the preceding configuration, run the **display traffic policy** command to check information about the configured traffic policies, traffic classifiers, and traffic behaviors.
   
   ```
   [~CE1] display traffic policy user-defined
   ```
   ```
   User Defined Traffic Policy Information:
     Total: 10239  Used: 4  Free: 10235
     Policy: 1
     Total: 5120 Used: 2 Free: 5118
      Description:
      Step: 1 
      Share-mode
        Classifier: a Precedence: 1 
        Behavior: e
         Committed Access Rate:
           CIR 10000 (Kbps), PIR 0 (Kbps), CBS 150000 (byte), PBS 0 (byte), ADJUST 0 
           Conform Action: pass  Yellow  Action: pass  Exceed  Action: discard  Color-aware: no 
         Marking:
           remark dscp cs5
        Classifier: default-class Precedence: 65535
        Behavior:   be
          -none-  
     Policy: 2
     Total: 5120 Used: 2 Free: 5118
      Description:
      Step: 1 
      Share-mode
        Classifier: b Precedence: 1 
        Behavior: f
         Committed Access Rate:
           CIR 5000 (Kbps), PIR 0 (Kbps), CBS 100000 (byte), PBS 0 (byte), ADJUST 0 
           Conform Action: pass  Yellow  Action: pass  Exceed  Action: discard  Color-aware: no
         Marking:
           remark dscp af31     
        Classifier: default-class Precedence: 65535
        Behavior:   be
          -none-  
     Policy: 3
     Total: 5120 Used: 2 Free: 5118
      Description:
      Step: 1 
      Share-mode
        Classifier: c Precedence: 1 
        Behavior: g
         Committed Access Rate:
           CIR 2000 (Kbps), PIR 0 (Kbps), CBS 100000 (byte), PBS 0 (byte), ADJUST 0
           Conform Action: pass  Yellow  Action: pass  Exceed  Action: discard  Color-aware: no
         Marking:
           remark dscp default
        Classifier: default-class Precedence: 65535
        Behavior:   be
          -none-  
     Policy: udplimit
     Total: 5120 Used: 2 Free: 5118
      Description:
      Step: 1 
      Share-mode
        Classifier: udplimit Precedence: 1 
        Behavior: udplimit
         -none-
        Classifier: udplimit1 Precedence: 10 
        Behavior: udplimit1
         Committed Access Rate:
          CIR 5000 (Kbps), PIR 15000 (Kbps), CBS 100000 (byte), PBS 200000 (byte), ADJUST 0
          Conform Action: pass  Yellow  Action: pass  Exceed  Action: discard  Color-aware: no
        Classifier: default-class Precedence: 65535
        Behavior:   be
          -none-  
   ```
   
   # Apply the traffic policies to the inbound interfaces.
   
   ```
   [~CE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] traffic-policy 1 inbound
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [~CE1] interface gigabitethernet 0/3/0
   ```
   ```
   [~CE1-GigabitEthernet0/3/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/3/0] traffic-policy 2 inbound
   ```
   ```
   [*CE1-GigabitEthernet0/3/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [~CE1] interface gigabitethernet 0/1/8
   ```
   ```
   [~CE1-GigabitEthernet0/1/8] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/8] traffic-policy 3 inbound
   ```
   ```
   [*CE1-GigabitEthernet0/1/8] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/8] quit
   ```
   ```
   [~CE1] interface gigabitethernet 0/2/0
   ```
   ```
   [~CE1-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] traffic-policy udplimit outbound
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~CE1-GigabitEthernet0/2/0] quit
   ```
3. Configure MF classification on PE1 to limit the traffic that goes to the MPLS backbone network.
   
   
   
   # Configure a traffic classifier and define a matching rule.
   
   ```
   [~PE1] traffic classifier pe
   ```
   ```
   [*PE1-classifier-pe] if-match any
   ```
   ```
   [*PE1-classifier-pe] commit
   ```
   ```
   [~PE1-classifier-pe] quit
   ```
   
   After the preceding configuration is complete, run the **display traffic classifier** command to check the traffic classifier configuration.
   
   ```
   [~PE1] display traffic classifier user-defined
   ```
   ```
   User Defined Classifier Information:
   ```
   ```
      Total: 65535  Used: 6  Free: 65529
   ```
   ```
      Classifier: pe
   ```
   ```
       Description:
   ```
   ```
       Operator: or
   ```
   ```
   Rule(s):
   ```
   ```
     if-match any
   ```
   
   # Define a traffic behavior and configure traffic policing.
   
   ```
   [~PE1] traffic behavior pe
   ```
   ```
   [*PE1-behavior-pe] car cir 15000 pir 20000 cbs 300000 pbs 500000
   ```
   ```
   [*PE1-behavior-pe] commit
   ```
   ```
   [~PE1-behavior-pe] quit
   ```
   
   # Define a traffic policy to associate the traffic classifier with the traffic behavior.
   
   ```
   [~PE1] traffic policy pe
   ```
   ```
   [*PE1-trafficpolicy-pe] classifier pe behavior pe
   ```
   ```
   [*PE1-trafficpolicy-pe] commit
   ```
   ```
   [~PE1-trafficpolicy-pe] quit
   ```
   
   After completing the preceding configuration, run the **display traffic policy** command to check information about the configured traffic policy, traffic classifier, and traffic behavior.
   
   ```
   [~PE1] display traffic policy user-defined
   ```
   ```
   User Defined Traffic Policy Information:
     Total: 10239  Used: 1     Free: 10238
     Policy: pe
      Total: 5120  Used: 2  Free: 5118
      Description:
      Step: 1 
      Share-mode
        Classifier: pe Precedence: 1 
        Behavior: pe
         Committed Access Rate:
           CIR 15000 (Kbps), PIR 2000 (Kbps), CBS 300000 (byte), PBS 500000 (byte), ADJUST 0                                                                             
          Conform Action: pass  Yellow  Action: pass  Exceed  Action: discard  Color-aware: no 
        Classifier: default-class Precedence: 65535
        Behavior:   be
          -none-  
   ```
   
   # Apply the traffic policy to the inbound interface.
   
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] traffic-policy pe inbound
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
4. Verify the configuration.
   
   
   
   After completing the preceding configuration, run the **display interface** command on CE1 and PE1 to check the traffic statistics on the interfaces. The command output shows that the traffic policies have been applied to the interfaces.

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  acl number 2001
   rule 5 permit source 1.1.1.0 0.0.0.255
  acl number 2002
   rule 5 permit source 2.1.1.0 0.0.0.255
  acl number 2003
   rule 5 permit source 3.1.1.0 0.0.0.255
  acl number 3001 
   rule 0 permit udp destination-port eq dns   
   rule 1 permit udp destination-port eq snmp  
   rule 2 permit udp destination-port eq snmptrap 
   rule 3 permit udp destination-port eq syslog
  acl number 3002
   rule 4 permit udp 
  #
  traffic classifier a operator or
   if-match acl 2001
  #
  traffic classifier b operator or
   if-match acl 2002
  #
  traffic classifier c operator or
   if-match acl 2003
  #
  traffic classifier udplimit operator or 
   if-match acl 3001
  #
  traffic classifier udplimit1 operator or 
   if-match acl 3002
  #
  traffic behavior e
   car cir 10000 cbs 150000 green pass red discard
   remark dscp cs5
  #
  traffic behavior f
   car cir 5000 cbs 100000 green pass red discard
   remark dscp af31
  #
  traffic behavior g
   car cir 2000 cbs 100000 green pass red discard
   remark dscp default
  #
  traffic behavior udplimit
  #
  traffic behavior udplimit1
   car cir 5000 pir 15000 cbs 100000 pbs 200000 green pass yellow discard red discard
  #
  traffic policy 1
   classifier a behavior e precedence 1
  #
  traffic policy 2
   classifier b behavior f precedence 1
  #
  traffic policy 3
   classifier c behavior g precedence 1
  #
  traffic policy udplimit  
   classifier udplimit behavior udplimit precedence 1
   classifier udplimit1 behavior udplimit1 precedence 2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
   traffic-policy 1 inbound
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   traffic-policy udplimit outbound
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 2.1.1.1 255.255.255.0
   traffic-policy 2 inbound
  #
  interface GigabitEthernet0/1/8
   undo shutdown
   ip address 3.1.1.1 255.255.255.0
   traffic-policy 3 inbound
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.0 0.0.0.255
    network 2.1.1.0 0.0.0.255
    network 3.1.1.0 0.0.0.255
    network 10.1.1.0 0.0.0.255
  #
  return 
  ```
* PE1 configuration file
  
  ```
  #
  ```
  ```
  sysname PE1
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 11.11.11.11
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
  #
  ```
  ```
  traffic classifier pe operator or
  ```
  ```
   if-match any
  ```
  ```
  #
  ```
  ```
  traffic behavior pe
  ```
  ```
   car cir 15000 pir 20000 cbs 300000 pbs 500000 green pass yellow pass red discard
  ```
  ```
  #
  ```
  ```
  traffic policy pe
  ```
  ```
   classifier pe behavior pe precedence 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
   traffic-policy pe inbound
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.10.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 11.11.11.11 255.255.255.255
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.10.1.0 0.0.0.255
  ```
  ```
    network 11.11.11.11 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return 
  ```
* P configuration file
  
  ```
  #
  ```
  ```
  sysname P
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 33.33.33.33
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.10.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.11.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 33.33.33.33 255.255.255.255
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.10.1.0 0.0.0.255
  ```
  ```
    network 10.11.1.0 0.0.0.255
  ```
  ```
    network 33.33.33.33 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
  ```
  #
  ```
  ```
  sysname PE2
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 22.22.22.22
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.12.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.11.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 22.22.22.22 255.255.255.255
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.11.1.0 0.0.0.255
  ```
  ```
    network 10.12.1.0 0.0.0.255
  ```
  ```
    network 22.22.22.22 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE2 configuration file
  
  ```
  #
  ```
  ```
  sysname CE2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.12.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.12.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```