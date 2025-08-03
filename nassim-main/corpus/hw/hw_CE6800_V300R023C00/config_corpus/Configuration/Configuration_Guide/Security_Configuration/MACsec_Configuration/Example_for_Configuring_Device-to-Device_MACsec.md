Example for Configuring Device-to-Device MACsec
===============================================

Example for Configuring Device-to-Device MACsec

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512689218__fig1528244419247), DeviceA and DeviceB are connected and exchange important information, which needs to be protected.

**Figure 1** Network diagram of device-to-device MACsec![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001564008617.png)
#### Configuration Roadmap

When MACsec is configured on two devices, the configuration roadmap is as follows:

1. Configure the key server priority. In this example, DeviceA is configured as the key server.
2. Set the encryption mode to normal, indicating that both data encryption and integrity check are enabled.
3. Set the CKN and CAK for MKA session negotiation to f1c3b2a4d6d9a7c5b4e1ab56dc21ed79ac97be533671dcab2678ac55cf71aced and ab2145369adcadef69512347adceb210, respectively.

![](public_sys-resources/note_3.0-en-us.png) 

![](figure/en-us_image_0000001691092389.png)

In this example, if transparent transmission devices DeviceC, DeviceD, and DeviceE are deployed between DeviceA and DeviceB, the transparent transmission devices must support Layer 2 protocol tunneling to ensure that DeviceA and DeviceB can perform MACsec session negotiation. The procedure is as follows:

1. Run the **l2protocol-tunnel user-defined-protocol** *protocol-name* **protocol-mac** **0180-c200-0003** **group-mac** *group-mac* command in the system view of DeviceC and DeviceE to configure Layer 2 transparent transmission of EAP packets.
2. Run the **l2protocol-tunnel user-defined-protocol** *protocol-name* **enable** command on the interface used by DeviceC to connect to DeviceA and the interface used by DeviceE to connect to DeviceB to enable Layer 2 protocol tunneling on these interfaces.
3. When MACsec session negotiation is performed between DeviceA and DeviceB, all types of packets except LLDP, MKA, 1588, and pause packets are encrypted. As a result, DeviceC, DeviceD, and DeviceE cannot identify these encrypted packets. For example, after STP packets are encrypted on DeviceA, DeviceC cannot identify them. In this case, you need to configure Layer 2 protocol tunneling.

This procedure is only for reference. For configuration details, see "Layer 2 Protocol Tunneling Configuration" in CLI Configuration Guide > Ethernet Switching Configuration.




#### Procedure

1. Configure DeviceA.
   
   
   
   # Create a MACsec profile.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] mac-security-profile name test1
   ```
   
   # Set the key server priority of DeviceA to 1 and the encryption mode to normal.
   
   ```
   [*DeviceA-macsec-profile-test1] mka keyserver priority 1
   [*DeviceA-macsec-profile-test1] macsec mode normal
   [*DeviceA-macsec-profile-test1] quit
   [*DeviceA] commit
   ```
   
   # Set the CKN to **f1c3b2a4d6d9a7c5b4e1ab56dc21ed79ac97be533671dcab2678ac55cf71aced** and CAK to **ab2145369adcadef69512347adceb210**, and apply the MACsec profile.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] mka cak-mode static ckn f1c3b2a4d6d9a7c5b4e1ab56dc21ed79ac97be533671dcab2678ac55cf71aced cak ab2145369adcadef69512347adceb210
   [~DeviceA-100GE1/0/1] mac-security-profile test1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
2. Configure DeviceB.
   
   
   
   # Create a MACsec profile.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*DeviceB] commit
   [~DeviceB] mac-security-profile name test2
   ```
   
   # Set the key server priority of DeviceB to 2 and the encryption mode to normal.
   
   ```
   [*DeviceB-macsec-profile-test2] mka keyserver priority 2
   [*DeviceB-macsec-profile-test2] macsec mode normal
   [*DeviceB-macsec-profile-test2] quit
   [*DeviceB] commit
   ```
   
   # Set the CKN to **f1c3b2a4d6d9a7c5b4e1ab56dc21ed79ac97be533671dcab2678ac55cf71aced** and CAK to **ab2145369adcadef69512347adceb210**, and apply the MACsec profile.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] mka cak-mode static ckn f1c3b2a4d6d9a7c5b4e1ab56dc21ed79ac97be533671dcab2678ac55cf71aced cak ab2145369adcadef69512347adceb210
   [~DeviceB-100GE1/0/1] mac-security-profile test2
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the configuration on DeviceA.

```
[~DeviceA] display mka interface 100ge 1/0/1
Interface 100GE1/0/1:
  CKN: F1C3B2A4D6D9A7C5B4E1AB56DC21ED79AC97BE533671DCAB2678AC55CF71ACED
  MKA status      : SUCCEEDED
  MI              : 5B8D4074D0E0639D8AE1AF1E 
  MN              : 52
  MACsec mode     : normal
  Key server      : YES
  Live peers      : 1
  Potential peers : 0
  Live peers list :
  MI                         MN          Priority  Capability  Rx-SCI
  67C7271E983BA02C04A88ACD   53          2         3           000B09BACF0A0024
  Potential peers list:
  MI                         MN          Priority  Capability  Rx-SCI
  --                         --          --        --          --
```

# Check the configuration on DeviceB.

```
[~DeviceB] display mka interface 100ge 1/0/1
Interface 100GE1/0/1:
  CKN: F1C3B2A4D6D9A7C5B4E1AB56DC21ED79AC97BE533671DCAB2678AC55CF71ACED
  MKA status      : SUCCEEDED
  MI              : 67C7271E983BA02C04A88ACD 
  MN              : 56
  MACsec mode     : normal
  Key server      : NO
  Live peers      : 1
  Potential peers : 0
  Live peers list :
  MI                         MN          Priority  Capability  Rx-SCI
  5B8D4074D0E0639D8AE1AF1E   55          1         3           000B09C312CE0031
  Potential peers list:
  MI                         MN          Priority  Capability  Rx-SCI
  --                         --          --        --          --
```

In the preceding command outputs, the **MKA status** field displays **SUCCEEDED**, indicating that MKA session negotiation is successful, and the **MACsec mode** field displays **normal**, indicating that the MACsec encryption mode is normal.


#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
mac-security-profile name test1
 mka keyserver priority 1
 macsec mode normal
#
interface 100GE1/0/1
 mka cak-mode static ckn f1c3b2a4d6d9a7c5b4e1ab56dc21ed79ac97be533671dcab2678ac55cf71aced cak %^%#&gqJ1f*uV0vqB$ZT5hr#qwL/;Cd/`OmO<m2+hh1A1&w{)jh1"'poiXB\UAn9%^%#
 mac-security-profile test1
#
return
```

DeviceB

```
#
sysname DeviceB
#
mac-security-profile name test2
 mka keyserver priority 2
 macsec mode normal
#
interface 100GE1/0/1
 mka cak-mode static ckn f1c3b2a4d6d9a7c5b4e1ab56dc21ed79ac97be533671dcab2678ac55cf71aced cak %^%#W5_!'~9]i>47d&X^Vro#S!z<4s+/N5\Ek*#27i_Wz-U3/"3tJM1.6++,nP+Z%^%#
 mac-security-profile test2
#
return
```