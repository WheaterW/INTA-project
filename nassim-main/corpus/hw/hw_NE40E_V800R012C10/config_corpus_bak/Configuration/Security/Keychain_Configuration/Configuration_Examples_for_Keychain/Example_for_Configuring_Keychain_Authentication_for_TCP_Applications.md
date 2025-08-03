Example for Configuring Keychain Authentication for TCP Applications
====================================================================

Example_for_Configuring_Keychain_Authentication_for_TCP_Applications

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372088__fig_dc_vrp_keychain_cfg_002101), configure BGP and keychain authentication on DeviceA and Device B, allowing the two devices to communicate through BGP.

**Figure 1** Network diagram of keychain![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.


  
![](images/fig_dc_vrp_keychain_cfg_002101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic keychain functions.
2. Configure Device to use keychain authentication for BGP.

#### Data Preparation

To complete the configuration, you need the following data:

* Keychain name
* Key-id
* Key-id authentication algorithm (SHA-256) and authentication string
* Send and receive time
* Receive tolerance time
* TCP type value and TCP algorithm ID that represents the SHA-256 authentication algorithm

#### Procedure

1. Configure DeviceA.
   
   
   
   Configuring keychain.
   
   ```
   [~DeviceA] keychain huawei mode absolute
   ```
   ```
   [*DeviceA-keychain-huawei] tcp-kind 182
   ```
   ```
   [*DeviceA-keychain-huawei] tcp-algorithm-id sha-256 17
   ```
   ```
   [*DeviceA-keychain-huawei] receive-tolerance 100
   ```
   ```
   [*DeviceA-keychain-huawei] key-id 1
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] algorithm sha-256
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] send-time 14:30 2017-10-10 to 14:50 2017-10-10
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] receive-time 14:40 2017-10-10 to 14:50 2017-10-10
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] default send-key-id
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] commit
   ```
   ```
   [~DeviceA-keychain-huawei-keyid-1] quit
   ```
   ```
   [*DeviceA-keychain-huawei] key-id 2
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-2] algorithm sha-256
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-2] key-string cipher YsHsjx_202207
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-2] send-time 08:30 2017-10-10 to 13:30 2017-10-10
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-2] receive-time 09:30 2017-10-10 to 14:30 2017-10-10
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-2] commit
   ```
   ```
   [~DeviceA-keychain-huawei-keyid-2] quit
   ```
   ```
   [~DeviceA-keychain-huawei] quit
   ```
   
   Configure keychain authentication.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 192.168.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] bgp 1
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 192.168.1.2 as-number 1
   ```
   ```
   [*DeviceA-bgp] peer 192.168.1.2 keychain huawei
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
2. Configure DeviceB.
   
   
   
   Configure keychain.
   
   ```
   [~DeviceB] keychain huawei mode absolute
   ```
   ```
   [*DeviceB-keychain-huawei] tcp-kind 182
   ```
   ```
   [*DeviceB-keychain-huawei] tcp-algorithm-id sha-256 17
   ```
   ```
   [*DeviceB-keychain-huawei] receive-tolerance 100
   ```
   ```
   [*DeviceB-keychain-huawei] key-id 1
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-1] algorithm sha-256
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-1] send-time 14:40 2017-10-10 to 14:50 2017-10-10
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-1] receive-time 14:30 2017-10-10 to 14:50 2017-10-10
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-1] default send-key-id
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-1] commit
   ```
   ```
   [~DeviceB-keychain-huawei-keyid-1] quit
   ```
   ```
   [*DeviceB-keychain-huawei] key-id 2
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-2] algorithm sha-256
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-2] key-string cipher YsHsjx_202207
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-2] send-time 09:30 2017-10-10 to 14:30 2017-10-10
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-2] receive-time 08:30 2017-10-10 to 13:30 2017-10-10
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-2] commit
   ```
   ```
   [~DeviceB-keychain-huawei-keyid-2] quit
   ```
   ```
   [~DeviceB-keychain-huawei] quit
   ```
   
   Configure keychain authentication.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 192.168.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] bgp 1
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 192.168.1.1 as-number 1
   ```
   ```
   [*DeviceB-bgp] peer 192.168.1.1 keychain huawei 
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```

#### Configuration Files

* DeviceA configuration file
  
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
  keychain huawei mode absolute
  ```
  ```
  tcp-kind 182
  ```
  ```
  tcp-algorithm-id sha-256 17
  ```
  ```
  receive-tolerance 100
  ```
  ```
  #
  ```
  ```
   key-id 1
  ```
  ```
    algorithm sha-256
  ```
  ```
    key-string cipher @%@%Hb'c;\@iU'@X,k6.E\Z,*.S#@%@%
  ```
  ```
    send-time 14:30 2017-10-10 to 14:50 2017-10-10
  ```
  ```
    receive-time 14:40 2017-10-10 to 14:50 2017-10-10
  ```
  ```
    default send-key-id
  ```
  ```
  #
  ```
  ```
   key-id 2
  ```
  ```
    algorithm sha-256
  ```
  ```
    key-string cipher %^%#[aqxE3`@U8L*%n."1(<$,]k_QrVTf1X;K+;My)k;%^%#
  ```
  ```
    send-time 08:30 2017-10-10 to 13:30 2017-10-10
  ```
  ```
    receive-time 09:30 2017-10-10 to 14:30 2017-10-10
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
  ip address 192.168.1.1 24
  ```
  ```
  #
  ```
  ```
  bgp 1
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   peer 192.168.1.2 as-number 1
  ```
  ```
   peer 192.168.1.2 keychain huawei
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
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
  keychain huawei mode absolute
  ```
  ```
  tcp-kind 182
  ```
  ```
  tcp-algorithm-id sha-256 17
  ```
  ```
  receive-tolerance 100
  ```
  ```
  #
  ```
  ```
   key-id 1
  ```
  ```
    algorithm sha-256
  ```
  ```
    key-string cipher @%@%;TYJ;\@iU'SGHRH.C\V,*.A#@%@%
  ```
  ```
    send-time 14:40 2017-10-10 to 14:50 2017-10-10
  ```
  ```
    receive-time 14:30 2017-10-10 to 14:50 2017-10-10
  ```
  ```
    default send-key-id
  ```
  ```
  #
  ```
  ```
   key-id 2
  ```
  ```
    algorithm sha-256
  ```
  ```
    key-string cipher %^%#X=O%EC@ta4QKkn"ur~Y::h@#'6737A4eq<W^~qn+%^%#
  ```
  ```
    send-time 09:30 2017-10-10 to 14:30 2017-10-10
  ```
  ```
    receive-time 08:30 2017-10-10 to 13:30 2017-10-10
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
  ip address 192.168.1.2 24
  ```
  ```
  #
  ```
  ```
  bgp 1
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   peer 192.168.1.1 as-number 1
  ```
  ```
   peer 192.168.1.1 keychain huawei
  ```
  ```
  #
  ```
  ```
  return
  ```