Example for Configuring the PUPP Mode
=====================================

This section provides an example for configuring the PUPP mode.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172375031__fig_01), three users in an enterprise access the Internet over a Layer 3 leased line. To implement access control between users in the enterprise, configure a traffic policy on a BAS interface.

**Figure 1** DAA networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/1.


  
![](images/fig_dc_ne_daa_cfg_0014_002.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure advanced ACLs.
2. Configure traffic classifiers.
3. Configure traffic behaviors.
4. Configure traffic policies.
5. Configure a BAS interface.
6. Apply the traffic policies to the BAS interface.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL numbers
* Traffic classifier names
* Traffic behavior names
* Traffic policy names

#### Procedure

1. Configure advanced ACLs.
   
   
   ```
   [~HUAWEI] acl number 3001
   ```
   ```
   [*HUAWEI-acl-adv-3001] rule 1 permit ip source 10.11.11.1 0
   ```
   ```
   [*HUAWEI-acl-adv-3001] rule 2 permit ip source 10.11.11.2 0
   ```
   ```
   [*HUAWEI-acl-adv-3001] quit
   ```
   ```
   [~HUAWEI] acl number 3002
   ```
   ```
   [*HUAWEI-acl-adv-3002] rule 3 permit ip source 10.11.11.3 0
   ```
   ```
   [*HUAWEI-acl-adv-3002] quit
   ```
2. Configure traffic classifiers.
   
   
   ```
   [*HUAWEI] traffic classifier tc1
   ```
   ```
   [*HUAWEI-classifier-tc1] if-match acl 3001
   ```
   ```
   [*HUAWEI-classifier-tc1] quit
   ```
   ```
   [*HUAWEI] traffic classifier tc2
   ```
   ```
   [*HUAWEI-classifier-tc2] if-match acl 3002
   ```
   ```
   [*HUAWEI-classifier-tc2] quit
   ```
3. Configure traffic behaviors.
   
   
   ```
   [*HUAWEI] traffic behavior tb1
   ```
   ```
   [*HUAWEI-behavior-tb1] permit
   ```
   ```
   [*HUAWEI-behavior-tb1] match termination
   ```
   ```
   [*HUAWEI-behavior-tb1] quit
   ```
   ```
   [*HUAWEI] traffic behavior tb2
   ```
   ```
   [*HUAWEI-behavior-tb2] permit
   ```
   ```
   [*HUAWEI-behavior-tb2] match termination
   ```
   ```
   [*HUAWEI-behavior-tb2] quit
   ```
4. Configure traffic policies.
   
   
   ```
   [*HUAWEI] traffic policy p1
   ```
   ```
   [*HUAWEI-trafficpolicy-p1] classifier tc1 behavior tb1
   ```
   ```
   [*HUAWEI-trafficpolicy-p1] quit
   ```
   ```
   [*HUAWEI] traffic policy p2
   ```
   ```
   [*HUAWEI-trafficpolicy-p2] classifier tc2 behavior tb2
   ```
   ```
   [*HUAWEI-trafficpolicy-p2] quit
   ```
5. Configure a BAS interface.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1-bas] access-type layer3-leased-line user-name sr-test-eth password cipher root_123 default-domain authentication enterprise_sr
   ```
6. Apply the traffic policies to the BAS interface.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/1] bas
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1-bas] traffic-policy p1 inbound
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1-bas] traffic-policy p2 outbound
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/1-bas] quit
   ```
7. Verify the configuration.
   
   
   
   Run the [**display access traffic-policy statistics**](cmdqueryname=display+access+traffic-policy+statistics) command to check statistics about the PUPP traffic policy.
   
   ```
   <HUAWEI> display access traffic-policy statistics user-id 18496 inbound
   ```
   ```
   --------------------------------------------------------------------------------
     slot 1
   --------------------------------------------------------------------------------
   Policy name: p1
     Classifier name: tc1
       Acl 3001
          rule 1 permit ip source 10.11.11.1 0
         (00 packets, 00 bytes)
   
   ```

#### Configuration Files

```
#
sysname HUAWEI
#
acl number 3001
 rule 1 permit ip source 10.11.11.1 0
 rule 2 permit ip source 10.11.11.2 0
#
acl number 3002
 rule 3 permit ip source 10.11.11.3 0
#
traffic classifier tc1
 if-match acl 3001
traffic classifier tc2
 if-match acl 3002
#
traffic behavior tb1
 permit
 match termination
traffic behavior tb2
 permit
 match termination
#
traffic policy p1
 classifier tc1 behavior tb1
#
traffic policy p2
  classifier tc2 behavior tb2
#
interface GigabitEthernet0/1/1
 bas
  access-type layer3-leased-line user-name sr-test-eth password cipher %@%##!!!!!!!!!"!!!!"!!!!!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8% default-domain authentication enterprise_sr
  traffic-policy p1 inbound
  traffic-policy p2 outbound
#
return

```