Configuring the MACsec VLAN Tag in the Clear Function
=====================================================

This section describes how to configure MACsec VLAN tag in the clear on the HUAWEI NE40E-M2 seriess.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0174517131__fig1452771893111), RouterDevice A and RouterDevice B are directly connected, and MACsec data packets are encrypted and decrypted on GE 0/1/0.1 of Device A and Device B.

**Figure 1** Configuring MACsec VLAN tag in the clear![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The operations in this example are performed on the Device A and Device B, which can be HUAWEI NE40E-M2 seriess.
* Interface 1 in this example represents GE 0/1/0.1

  
![](figure/en-us_image_0263994233.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

Configure the same vlan id on GE 0/1/0.1 of Device A and Device B.

Configure the same static CKN and CAK on GE 0/1/0.1 of Device A and Device B.

Configure MACsec VLAN tag in the clear on GE 0/1/0.1 of Device A and Device B.

#### Data Preparation

To complete the configuration, you need the following data:

* CKN and CAK values of the interface


#### Procedure

1. Configure Device A.
   
   
   
   # Configure the dot1q encapsulation type on GE 0/1/0.1 and associate GE 0/1/0.1 with VLAN 10.
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface gigabitethernet0/1/0.1
   [~DeviceA-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   [*DeviceA-GigabitEthernet0/1/0.1] commit
   ```
   
   
   
   # Configure CKN and CAK in ciphertext on GE 0/1/0.1.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] mka cak-mode static ckn a1 cak cipher b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1
   [*DeviceA-GigabitEthernet0/1/0.1] commit
   ```
   
   
   
   # Configure MACsec VLAN tag in the clear on GE 0/1/0.1.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0.1] macsec dot1q-in-clear
   [*DeviceA-GigabitEthernet0/1/0.1] commit
   ```
2. Configure Device B.
   
   
   
   # Configure the dot1q encapsulation type on GE 0/1/0.1 and associate GE 0/1/0.1 with VLAN 10.
   
   ```
   <DeviceB> system-view
   [~DeviceB] interface gigabitethernet0/1/0.1
   [~DeviceB-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   [*DeviceB-GigabitEthernet0/1/0.1] commit
   ```
   
   
   
   # Configure CKN and CAK in ciphertext on GE 0/1/0.1.
   
   ```
   [~DeviceB-GigabitEthernet0/1/0.1] mka cak-mode static ckn a1 cak cipher b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1
   [*DeviceB-GigabitEthernet0/1/0.1] commit
   ```
   
   
   
   # Configure MACsec VLAN tag in the clear on GE 0/1/0.1.
   
   ```
   [~DeviceB-GigabitEthernet0/1/0.1] macsec dot1q-in-clear
   [*DeviceB-GigabitEthernet0/1/0.1] commit
   ```

#### Configuration Files

* Device A configuration file
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   mka cak-mode static ckn a1 cak cipher %^%#C1ad()KRM~r1ZmJ:K09&amp;H]R=&lt;*0^A,H.fZE"&lt;WxS%^%#
   macsec dot1q-in-clear
  ```
* Device B configuration file
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0.1
   undo shutdown
   vlan-type dot1q 10
   mka cak-mode static ckn a1 cak cipher %^%#C1ad()KRM~r1ZmJ:K09&amp;H]R=&lt;*0^A,H.fZE"&lt;WxS%^%#
   macsec dot1q-in-clear
  ```