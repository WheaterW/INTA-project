Example for Configuring the ATM Complex Traffic Classification
==============================================================

This section provides an example for configuring ATM complex traffic classification.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371696__fig_dc_ne_qos_qos_cfg_01261101), DeviceA, DeviceB, and DeviceC are at the edge of the ATM network. They provide IP network access, enabling communications between the three separated packet switched networks (PSNs). IP packets are encapsulated into AAL5 frames when they are transmitted over the ATM network. The service is therefore called the IPoA service. When the packets leave the ATM network, the AAL5 frame headers are removed on the Router before the packets are forwarded to other types of interfaces.

* The IP addresses of the ATM interfaces of the three Routers are 202.38.160.1/24, 202.38.160.2/24, and 202.38.160.3/24.
* On the ATM network, the VPIs/VCIs of DeviceA are 0/40 and 0/50, which connect DeviceB and DeviceC respectively; the VPIs/VCIs of DeviceB are 0/40 and 0/60, which connect DeviceA and DeviceC respectively; the VPIs/VCIs of DeviceC are 0/50 and 0/60 respectively, which connect DeviceA and DeviceB respectively.
* All PVCs on the ATM interfaces of the three Routers are in IPoA mode.

The specific requirements are as follows:

The downstream ATM 0/1/0 on DeviceA is enabled with the complex traffic classification. All ATM cells carrying the IP packets with the IP precedence of 5, 6, and 7 can pass; the ATM cells carrying the IP packets with the IP precedence of 4 are guaranteed a bandwidth of 2 Mbit/s.

**Figure 1** Networking diagram for configuring the ATM complex traffic classification![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 in this example represents ATM0/1/0.


  
![](images/fig_dc_ne_qos_cfg_01261101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for the interfaces.
2. Configure IPoA mappings for PVCs on interfaces.
3. Configure traffic classifiers.
4. Configure traffic behaviors.
5. Configure traffic policies.
6. Apply traffic policies to the ATM interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the ATM interfaces of the three Routers: 202.38.160.1/24, 202.38.160.2/24, and 202.38.160.3/24.
* VPIs/VCIs of DeviceA: 0/40 and 0/50, which connect DeviceB and DeviceC respectively
* VPIs/VCIs of DeviceB: 0/40 and 0/60, which connect DeviceA and DeviceC respectively
* VPIs/VCIs of DeviceC: 0/50 and 0/60, which connect DeviceA and DeviceB respectively
* Parameters for the ATM complex traffic classification: names of traffic classifiers, IP precedence, names of traffic behaviors, guaranteed bandwidths, the name of a traffic policy, and interfaces to which the policy is applied

#### Procedure

1. Enter the system view and configure IP addresses for the ATM interfaces of the Routers.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface atm 0/1/0
   ```
   ```
   [~DeviceA-Atm0/1/0] undo shutdown
   ```
   ```
   [~DeviceA-Atm0/1/0] ip address 202.38.160.1 255.255.255.0
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceA-Atm0/1/0] return
   ```
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface atm 0/1/0
   ```
   ```
   [~DeviceB-Atm0/1/0] undo shutdown
   ```
   ```
   [~DeviceB-Atm0/1/0] ip address 202.38.160.2 255.255.255.0
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceB-Atm0/1/0] return
   ```
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] interface atm 0/1/0
   ```
   ```
   [~DeviceC-Atm0/1/0] undo shutdown
   ```
   ```
   [~DeviceC-Atm0/1/0] ip address 202.38.160.3 255.255.255.0
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceC-Atm0/1/0] return
   ```
2. Create PVCs and configure IPoA mappings for the PVCs.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface atm 0/1/0
   ```
   ```
   [~DeviceA-Atm0/1/0] pvc to_b 0/40
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] map ip 202.38.160.2
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] commit
   ```
   ```
   [~DeviceA-atm-pvc-Atm0/1/0-0/40-to_b] quit
   ```
   ```
   [~DeviceA-Atm0/1/0] pvc to_c 0/50
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/50-to_c] map ip 202.38.160.3
   ```
   ```
   [*DeviceA-atm-pvc-Atm0/1/0-0/50-to_c] commit
   ```
   ```
   [~DeviceA-atm-pvc-Atm0/1/0-0/50-to_c] return
   ```
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface atm 0/1/0
   ```
   ```
   [~DeviceB-Atm0/1/0] pvc to_a 0/40
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] map ip 202.38.160.1
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] commit
   ```
   ```
   [~DeviceB-atm-pvc-Atm0/1/0-0/40-to_a] quit
   ```
   ```
   [~DeviceB-Atm0/1/0] pvc to_c 0/60
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/60-to_c] map ip 202.38.160.3
   ```
   ```
   [*DeviceB-atm-pvc-Atm0/1/0-0/60-to_c] commit
   ```
   ```
   [~DeviceB-atm-pvc-Atm0/1/0-0/60-to_c] return
   ```
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] interface atm 0/1/0
   ```
   ```
   [~DeviceC-Atm0/1/0] pvc to_a 0/50
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/50-to_a] map ip 202.38.160.1
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/50-to_a] quit
   ```
   ```
   [*DeviceC-Atm0/1/0] pvc to_b 0/60
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/60-to_b] map ip 202.38.160.2
   ```
   ```
   [*DeviceC-atm-pvc-Atm0/1/0-0/60-to_b] commit
   ```
   ```
   [~DeviceC-atm-pvc-Atm0/1/0-0/60-to_b] return
   ```
3. Configure the ATM complex traffic classification.
   
   
   
   # Create traffic classifiers and define matching rules.
   
   ```
   [~DeviceA] traffic classifier a
   ```
   ```
   [*DeviceA-classifier-a] if-match ip-precedence 7
   ```
   ```
   [*DeviceA-classifier-a] if-match ip-precedence 6
   ```
   ```
   [*DeviceA-classifier-a] if-match ip-precedence 5
   ```
   ```
   [*DeviceA-classifier-a] quit
   ```
   ```
   [*DeviceA] traffic classifier b
   ```
   ```
   [*DeviceA-classifier-b] if-match ip-precedence 4
   ```
   ```
   [*DeviceA-classifier-b] commit
   ```
   ```
   [~DeviceA-classifier-b] quit
   ```
   
   After the preceding configuration, you can run the **display** command to view the configuration of the traffic classifiers.
   
   ```
   [~DeviceA] display traffic classifier user-defined
   ```
   ```
   User Defined Classifier Information:
   ```
   ```
      Classifier: b
   ```
   ```
       Operator: OR
   ```
   ```
   Rule(s): if-match ip-precedence 4 
   ```
   ```
      Classifier: a
   ```
   ```
       Operator: OR
   ```
   ```
   Rule(s) : if-match ip-precedence 7
   ```
   ```
               if-match ip-precedence 6
   ```
   ```
               if-match ip-precedence 5 
   ```
   
   # Define traffic behaviors.
   
   ```
   [~DeviceA] traffic behavior a
   ```
   ```
   [*DeviceA-behavior-a] permit
   ```
   ```
   [*DeviceA-behavior-a] quit
   ```
   ```
   [*DeviceA] traffic behavior b
   ```
   ```
   [*DeviceA-behavior-b] car cir 2000
   ```
   ```
   [*DeviceA-behavior-b] commit
   ```
   ```
   [~DeviceA-behavior-b] quit
   ```
   
   After the preceding configuration, you can run the **display** command to view the configuration of the traffic classifiers.
   
   ```
   [~DeviceA] display traffic behavior user-defined
   ```
   ```
   User Defined Behavior Information:
   ```
   ```
       Behavior: b
   ```
   ```
         Committed Access Rate:
   ```
   ```
           CIR 2000 (Kbps), PIR 0 (Kbps), CBS 10000 (byte), PBS 0 (byte)
   ```
   ```
           Conform Action: pass
   ```
   ```
           Yellow  Action: pass
   ```
   ```
           Exceed  Action: discard
   ```
   ```
       Behavior: a
   ```
   ```
         Firewall:
   ```
   ```
           permit  
   ```
   
   # Define a traffic policy and associate the traffic classifiers with the traffic behaviors.
   
   ```
   [~DeviceA] traffic policy p
   ```
   ```
   [*DeviceA-trafficpolicy-a] classifier a behavior a
   ```
   ```
   [*DeviceA-trafficpolicy-a] classifier b behavior b
   ```
   ```
   [*DeviceA-trafficpolicy-a] commit
   ```
   ```
   [~DeviceA-trafficpolicy-a] quit
   ```
   
   # Apply the traffic policy to the outbound interface.
   
   ```
   [~DeviceA] interface atm 0/1/0
   ```
   ```
   [~DeviceA-Atm0/1/0] undo shutdown
   ```
   ```
   [~DeviceA-Atm0/1/0] traffic-policy p outbound
   ```
   ```
   [*DeviceA-Atm0/1/0] commit
   ```
   ```
   [~DeviceA-Atm0/1/0] quit
   ```
4. Verify the configuration.
   
   
   
   Run the **display** **traffic** **policy** command. You can view the configuration of the traffic policies, traffic classifiers defined in the traffic policies, and the traffic behaviors associated with traffic classifiers.
   
   ```
   [~DeviceA] display traffic policy user-defined
   ```
   ```
   User Defined Traffic Policy Information:
   ```
   ```
    Policy: p
   ```
   ```
      Classifier: default-class
   ```
   ```
        Behavior: be
   ```
   ```
         -none-
   ```
   ```
      Classifier: a
   ```
   ```
        Behavior: a
   ```
   ```
         Firewall:
   ```
   ```
           permit
   ```
   ```
      Classifier: b
   ```
   ```
        Behavior: b
   ```
   ```
         Committed Access Rate:
   ```
   ```
           CIR 2000 (Kbps), PIR 0 (Kbps), CBS 10000 (byte), PBS 0 (byte)
   ```
   ```
           Conform Action: pass
   ```
   ```
           Yellow  Action: pass
   ```
   ```
           Exceed  Action: discard  
   ```
   
   Run the **display interface** command on DeviceA. You can view that the traffic on the interfaces is controlled according to the specified requirements.

#### Configuration Files

* Configuration file of DeviceA
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
  traffic classifier a
  ```
  ```
   if-match ip-precedence 7
  ```
  ```
  if-match ip-precedence 6
  ```
  ```
  if-match ip-precedence 5
  ```
  ```
  traffic classifier b
  ```
  ```
   if-match ip-precedence 4
  ```
  ```
  #
  ```
  ```
  traffic behavior a
  ```
  ```
   permit
  ```
  ```
  traffic behavior b
  ```
  ```
  car cir 2000 cbs 10000 pbs 0 green pass red discard 
  ```
  ```
  #
  ```
  ```
  traffic policy p
  ```
  ```
   classifier a behavior a
  ```
  ```
   classifier b behavior b
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  pvc to_b 0/40
  ```
  ```
    map ip 202.38.160.2
  ```
  ```
  pvc to_c 0/50
  ```
  ```
    map ip 202.38.160.3
  ```
  ```
  ip address 202.38.160.1 255.255.255.0
  ```
  ```
  traffic-policy p outbound
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of DeviceB
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  pvc to_a 0/40
  ```
  ```
    map ip 202.38.160.1
  ```
  ```
  pvc to_c 0/60
  ```
  ```
    map ip 202.38.160.3
  ```
  ```
  ip address 202.38.160.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* Configuration file of DeviceC
  
  ```
  #
  ```
  ```
   sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface Atm0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
  pvc to_a 0/50
  ```
  ```
    map ip 202.38.160.1
  ```
  ```
  pvc to_b 0/60
  ```
  ```
    map ip 202.38.160.2
  ```
  ```
  ip address 202.38.160.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  return
  ```