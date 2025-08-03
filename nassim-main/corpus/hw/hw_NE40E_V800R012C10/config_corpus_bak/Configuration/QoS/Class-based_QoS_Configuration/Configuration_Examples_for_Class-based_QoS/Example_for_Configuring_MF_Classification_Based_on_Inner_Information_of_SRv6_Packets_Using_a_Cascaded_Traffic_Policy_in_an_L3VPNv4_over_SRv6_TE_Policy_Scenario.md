Example for Configuring MF Classification Based on Inner Information of SRv6 Packets Using a Cascaded Traffic Policy in an L3VPNv4 over SRv6 TE Policy Scenario
===============================================================================================================================================================

This section provides an example for configuring and applying traffic classifiers and behaviors in an L3VPNv4 over SRv6 TE Policy scenario.

#### Networking Requirements

On the network shown in [Figure 1](../vrp/dc_vrp_srv6_cfg_all_0102.html#EN-US_TASK_0184674100__fig184238288365):

* PE1, the P, and PE2 are in the same AS and run IS-IS to implement IPv6 network connectivity.
* PE1, the P, and PE2 are Level-1 devices that belong to IS-IS process 1.

It is required that a bidirectional SRv6 TE Policy be deployed between PE1 and PE2 to carry L3VPNv4 services.

Apply a cascaded traffic policy to interface1 and interface2 on the P to perform MF classification on communication packets between CE1 and CE2 based on inner information of SRv6 packets.

**Figure 1** L3VPNv4 over SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 and interface2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001223918348.png)

#### Configuration Roadmap

1. Configure L3VPNv4 over SRv6 TE Policy.
2. Configure MF classification based on inner information of SRv6 packets.
   1. Configure an ACL rule.
   2. Configure traffic classifiers.
   3. Configure traffic behaviors.
   4. Configure a traffic policy.
   5. Apply the traffic policy.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL number
* Names of traffic classifiers, traffic behaviors, and traffic policies, and numbers of the interfaces to which the traffic policies are applied

#### Procedure

1. Configure L3VPNv4 over SRv6 TE Policy.
   
   
   
   For details about how to configure L3VPNv4 over SRv6 TE Policy, see [Example for Configuring L3VPNv4 over SRv6 TE Policy](../vrp/dc_vrp_srv6_cfg_all_0102.html) in *HUAWEI NE40E-M2 series* *Configuration Guide > Segment Routing IPv6 Configuration*.
2. Configure MF classification based on inner information of SRv6 packets.
   1. Configure an ACL rule for a child traffic policy.
      
      
      ```
      [~P] acl number 3000
      ```
      ```
      [*P-acl-advance-3000] rule 5 permit ip dscp cs6 
      ```
      ```
      [*P-acl-advance-3000] commit
      ```
      ```
      [~P-acl-advance-3000] quit
      ```
   2. Configure traffic classifiers for parent and child traffic policies.
      
      
      
      # Configure a traffic classifier for a parent traffic policy.
      
      ```
      [~P] traffic classifier outer
      ```
      ```
      [*P-classifier-outer] if-match ipv6 any
      ```
      ```
      [*P-classifier-outer] commit
      ```
      ```
      [~P-classifier-outer] quit
      ```
      
      
      
      # Configure a traffic classifier for a child traffic policy.
      
      ```
      [~P] traffic classifier inner
      ```
      ```
      [*P-classifier-inner] if-match acl 3000
      ```
      ```
      [*P-classifier-inner] commit
      ```
      ```
      [~P-classifier-inner] quit
      ```
   3. Define a traffic behavior named **inner** for a child traffic policy, create a child traffic policy named **inner**, and bind the traffic classifier and behavior in the child traffic policy.
      
      
      ```
      [~P] traffic behavior inner
      ```
      ```
      [*P-behavior-inner] permit
      ```
      ```
      [*P-behavior-inner] commit
      ```
      ```
      [~P-behavior-inner] quit
      ```
      
      
      ```
      [~P] traffic policy inner
      ```
      ```
      [*P-trafficpolicy-inner] classifier inner behavior inner
      ```
      ```
      [*P-trafficpolicy-inner] statistics enable
      ```
      ```
      [*P-trafficpolicy-inner] commit
      ```
      ```
      [~P-trafficpolicy-inner] quit
      ```
   4. Define a traffic behavior named **outer** for a parent traffic policy, create a parent traffic policy named **outer**, and bind the traffic classifier and behavior in the parent traffic policy.
      
      
      
      # Configure a cascaded traffic policy named **inner** based on inner information of SRv6 packets in the traffic behavior **outer**.
      
      ```
      [~P] traffic behavior outer
      ```
      ```
      [*P-behavior-outer] traffic-policy inner ip-layer srv6-inner
      ```
      ```
      [*P-behavior-outer] commit
      ```
      ```
      [~P-behavior-outer] quit
      ```
      ```
      [~P] traffic policy outer
      ```
      ```
      [*P-trafficpolicy-outer] classifier outer behavior outer
      ```
      ```
      [*P-trafficpolicy-outer] undo share-mode
      ```
      ```
      [*P-trafficpolicy-outer] statistics enable
      ```
      ```
      [*P-trafficpolicy-outer] commit
      ```
      ```
      [~P-trafficpolicy-outer] quit
      ```
   5. Apply the traffic policy.
      
      
      
      Apply the parent traffic policy **outer** to the inbound and outbound directions of GE 0/1/0 and GE 0/2/0 that connect the P to the PEs.
      
      ```
      [~P] interface gigabitethernet 0/1/0
      ```
      ```
      [*P-GigabitEthernet0/1/0] traffic-policy outer outbound
      ```
      ```
      [*P-GigabitEthernet0/1/0] traffic-policy outer inbound
      ```
      ```
      [*P-GigabitEthernet0/1/0] commit
      ```
      ```
      [~P-GigabitEthernet0/1/0] quit
      ```
      ```
      [~P] interface gigabitethernet 0/2/0
      ```
      ```
      [*P-GigabitEthernet0/2/0] traffic-policy outer outbound
      ```
      ```
      [*P-GigabitEthernet0/2/0] traffic-policy outer inbound
      ```
      ```
      [*P-GigabitEthernet0/2/0] commit
      ```
      ```
      [~P-GigabitEthernet0/2/0] quit
      ```
3. Verify the configuration.
   
   
   
   After the preceding configuration is complete, CE1 and CE2 can communicate with each other. You can run the [**display traffic policy statistics**](cmdqueryname=display+traffic+policy+statistics) command on the P to check statistics about service traffic between CE1 and CE2.
   
   * Run the **display traffic policy name inner statistics interface gigabitethernet 0/1/0 inbound** command to check statistics about received packets that match SRv6 inner information on the P.
   * Run the **display traffic policy name inner statistics interface gigabitethernet 0/2/0 outbound** command to check statistics about sent packets that match SRv6 inner information on the P.

#### Configuration Files

P configuration file

```
#
sysname P
#
#
acl number 3000
 rule 5 permit ip dscp cs6
#
traffic classifier inner 
 if-match acl 3000 precedence 1
#
traffic classifier outer 
 if-match ipv6 any
#
traffic behavior inner
 permit
#
traffic behavior outer
 traffic-policy inner ip-layer srv6-inner
#
traffic policy inner
 
 statistics enable
 classifier inner behavior inner precedence 1
#
traffic policy outer
 undo share-mode
 statistics enable
 classifier outer behavior outer precedence 1
#
interface GigabitEthernet0/1/0
 undo shutdown
   traffic-policy outer inbound  
   traffic-policy outer outbound
# 
interface GigabitEthernet0/2/0
 undo shutdown
  traffic-policy outer inbound
  traffic-policy outer outbound
# 
return
```