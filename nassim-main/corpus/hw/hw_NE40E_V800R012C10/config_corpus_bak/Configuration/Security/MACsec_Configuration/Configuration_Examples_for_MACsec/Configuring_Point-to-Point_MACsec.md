Configuring Point-to-Point MACsec
=================================

MACsec defines IEEE 802-based data security communication methods. MACsec provides users with secure data sending and receiving services at the MAC layer, including data encryption, data frame integrity check, data source validity check and anti-replay functions. MACsec uses Layer 2 encryption technology to provide secure hop-by-hop transmission of data. It applies to scenarios that require high data confidentiality.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372643__fig_dc_ne_macsec_cfg_001401), RouterDeviceA and RouterDeviceB are directly connected, and MACsec data packets are encrypted and decrypted on GE 0/1/0 of DeviceA and DeviceB.

**Figure 1** Configuring point-to-point MACsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations in this example are performed on DeviceA and DeviceB. The HUAWEI NE40E-M2 series can function as DeviceA and DeviceB.
* Interface1 in this example represents GE 0/1/0.

  
![](images/fig_dc_ne_macsec_cfg_001401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

Configure the same static CKN and CAK on GE 0/1/0 of DeviceA and DeviceB.


#### Data Preparation

To complete the configuration, you need the following data:

* CKN and CAK values of the interface
* The MACsec encryption algorithm **gcm-aes-xpn-128**, which is to be configured on the interface of DeviceA

#### Procedure

1. Configure DeviceA.
   
   # Configure CKN and CAK in ciphertext on GE 0/1/0.
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] mka cak-mode static ckn a1 cak cipher b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following are optional MACsec extended configurations.
   
   
   # Set the MKA key server priority on GE 0/1/0.
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] mka keyserver priority 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Set the SAK lifetime on GE 0/1/0.
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] mka timer sak-life 500
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Configure the MACsec encryption algorithm on GE 0/1/0. .
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] macsec cipher-suite gcm-aes-xpn-128
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Set the MACsec encryption offset on GE 0/1/0.
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] macsec confidentiality-offset 50
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Set the MACsec encryption mode on GE 0/1/0. .
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] macsec mode integrity-only
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Set the MACsec replay window size on GE 0/1/0.
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] macsec replay-window 512
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
2. Configure DeviceB.
   
   
   
   # Configure CKN and CAK in ciphertext on GE 0/1/0.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] mka cak-mode static ckn a1 cak cipher b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   mka cak-mode static ckn a1 cak cipher %^%#C1ad()KRM~r1ZmJ:K09&H]R=<*0^A,H.fZE"<WxS%^%#
   macsec replay-window 512
   macsec mode integrity-only
   macsec confidentiality-offset 50
   macsec cipher-suite gcm-aes-xpn-128
   mka keyserver priority 10
   mka timer sak-life 500
  ```
* DeviceB configuration file
  
  ```
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   mka cak-mode static ckn a1 cak cipher %^%#C1ad()KRM~r1ZmJ:K09&H]R=<*0^A,H.fZE"<WxS%^%#
  #
  ```