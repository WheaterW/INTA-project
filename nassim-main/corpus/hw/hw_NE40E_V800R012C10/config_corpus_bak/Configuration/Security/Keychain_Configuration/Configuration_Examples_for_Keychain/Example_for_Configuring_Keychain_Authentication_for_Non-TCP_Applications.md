Example for Configuring Keychain Authentication for Non-TCP Applications
========================================================================

Example_for_Configuring_Keychain_Authentication_for_Non-TCP_Applications

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372085__fig_dc_vrp_keychain_cfg_002001), configure IS-IS and keychain authentication on all interfaces of DeviceA and Device B, allowing the two devices to communicate through IS-IS.

**Figure 1** Network diagram of keychain![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.


  
![](images/fig_dc_vrp_keychain_cfg_002001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic IS-IS functions.
2. Configure basic keychain functions.
3. Configure keychain authentication for IS-IS on DeviceA and DeviceB, and set the authentication algorithm for the key ID to HMAC-SHA-256.

#### Data Preparation

To complete the configuration, you need the following data:

* Keychain name
* Key ID
* Authentication algorithm and password authentication key
* Send and receive time
* Receive tolerance time

#### Procedure

1. Configure DeviceA.
   
   
   
   # Configure basic IS-IS functions. (The configuration details are omitted.)
   
   # Configure keychain authentication.
   
   ```
   [~DeviceA] keychain huawei mode absolute
   ```
   ```
   [*DeviceA-keychain-huawei] receive-tolerance 100
   ```
   ```
   [*DeviceA-keychain-huawei] key-id 1
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] algorithm hmac-sha-256
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] send-time 14:40 2017-10-10 to 14:50 2017-10-10
   ```
   ```
   [*DeviceA-keychain-huawei-keyid-1] receive-time 14:30 2017-10-10 to 14:50 2017-10-10
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
   [~DeviceA-keychain-huawei] quit
   ```
   
   # Configure keychain authentication for IS-IS.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 192.168.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis authentication-mode keychain huawei
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
2. Configure DeviceB.
   
   
   
   # Configure basic IS-IS functions. (The configuration details are omitted.)
   
   # Configure keychain authentication.
   
   ```
   [~DeviceB] keychain huawei mode absolute
   ```
   ```
   [*DeviceB-keychain-huawei] receive-tolerance 100
   ```
   ```
   [*DeviceB-keychain-huawei] key-id 1
   ```
   ```
   [*DeviceB-keychain-huawei-keyid-1] algorithm hmac-sha-256
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
   [~DeviceB-keychain-huawei] quit
   ```
   
   # Configure keychain authentication for IS-IS.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 192.168.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis authentication-mode keychain huawei
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
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
  receive-tolerance 100
  ```
  ```
   key-id 1
  ```
  ```
    algorithm hmac-sha-256
  ```
  ```
    key-string cipher @%@%b{br9\zi%X+/Y@:Y>Lw(L\v#@%@%
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
  interface gigabitethernet0/1/0
  ```
  ```
   ip address 192.168.1.1 24
  ```
  ```
   isis authentication-mode keychain huawei
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
  receive-tolerance 100
  ```
  ```
   key-id 1
  ```
  ```
    algorithm hmac-sha-256
  ```
  ```
    key-string cipher @%@%VBNCG\zi%X+/Y@:YMHKJES/@%@%
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
  interface Gigabitethernet0/1/0
  ```
  ```
   ip address 192.168.1.2 24
  ```
  ```
   isis authentication-mode keychain huawei
  ```
  ```
  #
  ```
  ```
  return
  ```