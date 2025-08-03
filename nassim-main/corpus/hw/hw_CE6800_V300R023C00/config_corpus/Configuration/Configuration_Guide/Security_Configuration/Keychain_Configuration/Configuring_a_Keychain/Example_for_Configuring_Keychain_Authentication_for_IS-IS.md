Example for Configuring Keychain Authentication for IS-IS
=========================================================

Example for Configuring Keychain Authentication for IS-IS

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782712__fig168879525502), DeviceA, DeviceB, and DeviceC communicate with each other through IS-IS.

To ensure the stability and security of IS-IS connections, configure a keychain to provide dynamic security authentication for IS-IS.

**Figure 1** Keychain networking diagram![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface 1 and Interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176742389.png)

To complete the configuration, you need the following data:

* IS-IS process ID
* Network entity title (NET) of an IS-IS process
* keychain name
* Acceptance tolerance of a keychain
* Key ID in a keychain
* Key authentication algorithm and key string
* Send lifetime and accept lifetime of a key

#### Precautions

* NTP must be first configured.
* The configurations on both ends of keychain authentication must be consistent. Take DeviceA and DeviceB as an example:
  + The keychain names configured on DeviceA and DeviceB must be the same.
  + DeviceA and DeviceB must have the same time mode configured for the keychains.
  + The key IDs in the keychains configured on DeviceA and DeviceB must be the same. When multiple keys are configured, the same number of keys with the same IDs must be configured on both ends.
  + For the same key, the same authentication algorithm and key string must be configured on DeviceA and DeviceB.
  + For the same key, the send lifetime and accept lifetime configured on DeviceA and DeviceB must match. For example, the accept lifetime configured on DeviceB must include the send lifetime configured on DeviceA to prevent packet loss. Similarly, the accept lifetime configured on DeviceA also must include the send lifetime configured on DeviceB.
* If multiple keys are configured in a keychain, only one of them can be configured as the default send key.

#### Configuration Roadmap

1. Configure IS-IS.
2. Create a keychain.
3. Configure the key in the keychain and set the authentication algorithm of the key ID to **hmac-sha-256**.
4. Configure keychain authentication for IS-IS.

#### Procedure

1. Configure IS-IS.
   
   # Configure DeviceA.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceB] isis 1
   [*DeviceB-isis-1] is-level level-1
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   [*DeviceB-isis-1] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 192.168.1.2 24
   [*DeviceB-100GE1/0/1] isis enable 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 192.168.2.2 24
   [*DeviceB-100GE1/0/2] isis enable 1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceC] isis 1
   [*DeviceC-isis-1] is-level level-1
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   [*DeviceC-isis-1] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ip address 192.168.2.1 24
   [*DeviceC-100GE1/0/2] isis enable 1
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```
2. Create a keychain.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] keychain huawei mode absolute
   [*DeviceA-keychain-huawei] receive-tolerance 10
   [*DeviceA-keychain-huawei] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] keychain huawei mode absolute
   [*DeviceB-keychain-huawei] receive-tolerance 10
   [*DeviceB-keychain-huawei] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] keychain huawei mode absolute
   [*DeviceC-keychain-huawei] receive-tolerance 10
   [*DeviceC-keychain-huawei] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```
3. Configure a key in the keychain.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] keychain huawei
   [~DeviceA-keychain-huawei] key-id 1
   [*DeviceA-keychain-huawei-keyid-1] algorithm hmac-sha-256
   [*DeviceA-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   [*DeviceA-keychain-huawei-keyid-1] send-time 12:00 2019-12-10 to 18:00 2019-12-10
   [*DeviceA-keychain-huawei-keyid-1] receive-time 12:00 2019-12-10 to 18:00 2019-12-10
   [*DeviceA-keychain-huawei-keyid-1] default send-key-id
   [*DeviceA-keychain-huawei-keyid-1] quit
   [*DeviceA-keychain-huawei] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] keychain huawei
   [~DeviceB-keychain-huawei] key-id 1
   [*DeviceB-keychain-huawei-keyid-1] algorithm hmac-sha-256
   [*DeviceB-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   [*DeviceB-keychain-huawei-keyid-1] send-time 12:00 2019-12-10 to 18:00 2019-12-10
   [*DeviceB-keychain-huawei-keyid-1] receive-time 12:00 2019-12-10 to 18:00 2019-12-10
   [*DeviceB-keychain-huawei-keyid-1] default send-key-id
   [*DeviceB-keychain-huawei-keyid-1] quit
   [*DeviceB-keychain-huawei] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] keychain huawei
   [~DeviceC-keychain-huawei] key-id 1
   [*DeviceC-keychain-huawei-keyid-1] algorithm hmac-sha-256
   [*DeviceC-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   [*DeviceC-keychain-huawei-keyid-1] send-time 12:00 2019-12-10 to 18:00 2019-12-10
   [*DeviceC-keychain-huawei-keyid-1] receive-time 12:00 2019-12-10 to 18:00 2019-12-10
   [*DeviceC-keychain-huawei-keyid-1] default send-key-id
   [*DeviceC-keychain-huawei-keyid-1] quit
   [*DeviceC-keychain-huawei] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   ```
4. Configure keychain authentication for IS-IS.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] isis authentication-mode keychain huawei
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] quit
   ```
   # Configure DeviceB.
   ```
   [DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] isis authentication-mode keychain huawei
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] isis authentication-mode keychain huawei
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   [~DeviceB] quit
   ```
   
   # Configure DeviceC.
   ```
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] isis authentication-mode keychain huawei
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] [commit](cmdqueryname=commit)
   [~DeviceC] quit
   ```

#### Verifying the Configuration

Using DeviceA as an example, check whether keychain authentication is successfully configured for IS-IS.

* Run the [**display keychain**](cmdqueryname=display+keychain) *keychain-name* command to check the key ID in the **Active** state.
  ```
  <DeviceA> display keychain huawei
   Keychain Information:                                                          
   ----------------------                                                         
   Keychain Name             : huawei                                             
     Timer Mode              : Absolute                                           
     Receive Tolerance(min)  : 10                                                 
     Digest Length           : 32                                                 
     Time Zone               : LMT                                                
     TCP Kind                : 254                                                
     TCP Algorithm IDs       :                                                    
       HMAC-MD5              : 5                                                  
       HMAC-SHA1-12          : 2                                                  
       HMAC-SHA1-20          : 6                                                  
       MD5                   : 3                                                  
       SHA1                  : 4                                                  
       HMAC-SHA-256          : 7                                                  
       SHA-256               : 8                                                  
       SM3                   : 9                                                  
       HMAC-SHA-384          : 11                                                 
       HMAC-SHA-512          : 12                                                 
   Number of Key ID         : 1                                                  
   Active Send Key ID        : 1                                                  
   Active Receive Key ID    : 01                                                 
   Default send Key ID       : 1                                                  
  
   Key ID Information: 
       SHA1                  : 4                                                  
       HMAC-SHA-256          : 7                                                  
       SHA-256               : 8                                                  
       SM3                   : 9                                                  
   Number of Key ID         : 1                                                  
   Active Send Key ID        : 1                                                  
   Active Receive Key ID    : 01                                                 
   Default send Key ID       : 1                                                  
  
   Key ID Information:                                                            
   ----------------------                                                         
   Key ID                    : 1                                                  
     Key string              : ******                                             
     Algorithm               : HMAC-SHA-256                                       
     SEND TIMER              :                                                    
       Start time            : 2019-12-10 12:00                                   
       End time              : 2019-12-10 18:00                                   
       Status                : Active                                             
     RECEIVE TIMER           :                                                    
       Start time            : 2019-12-10 12:00                                   
       End time              : 2019-12-10 18:00                                   
       Status                : Active
  ```
* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) **verbose** command to check the details of the IS-IS link state database (LSDB).
  ```
  <DeviceA> display isis lsdb verbose
                          Database information for ISIS(1)                        
                          -----------------------------------                     
  
  
                            Level-1 Link State Database                           
  
  LSPID                  Seq Num    Checksum   HoldTime       Length   ATT/P/OL   
  -----------------------------------------------------------------------------   
  0000.0000.0001.00-00*  0x0000020a 0x94e6     409            68       0/0/0      
   SOURCE       0000.0000.0001.00                                                 
   NLPID        IPV4                                                              
   AREA ADDR    10                                                                
   INTF ADDR    192.168.1.1                                                       
   NBR  ID      0000.0000.0002.01  COST: 10                                       
   IP-Internal  192.168.1.0     255.255.255.0    COST: 10                         
  
  0000.0000.0002.00-00   0x00000219 0xfa60     431            95       0/0/0      
   SOURCE       0000.0000.0002.00                                                 
   NLPID        IPV4                                                              
   AREA ADDR    10                                                                
   INTF ADDR    192.168.1.2                                                       
   INTF ADDR    192.168.2.2
   NBR  ID      0000.0000.0002.01  COST: 10                                       
   NBR  ID      0000.0000.0003.01  COST: 10                                       
   IP-Internal  192.168.1.0     255.255.255.0    COST: 10                         
   IP-Internal  192.168.2.0     255.255.255.0    COST: 10                         
  
  0000.0000.0002.01-00   0x0000007e 0xa767     305            55       0/0/0      
   SOURCE       0000.0000.0002.01                                                 
   NLPID        IPV4                                                              
   NBR  ID      0000.0000.0002.00  COST: 0                                        
   NBR  ID      0000.0000.0001.00  COST: 0                                        
  
  0000.0000.0003.00-00   0x0000020c 0xd59e     322            68       0/0/0      
   SOURCE       0000.0000.0003.00                                                 
   NLPID        IPV4                                                              
   AREA ADDR    10                                                                
   INTF ADDR    192.168.2.1                                                       
   NBR  ID      0000.0000.0003.01  COST: 10                                       
   IP-Internal  192.168.2.0     255.255.255.0    COST: 10                         
  
  0000.0000.0003.01-00   0x0000007e 0xcc3f     322            55       0/0/0      
   SOURCE       0000.0000.0003.01                                                 
   NLPID        IPV4                                                              
   NBR  ID      0000.0000.0003.00  COST: 0
   SOURCE       0000.0000.0002.01                                                 
   NLPID        IPV4                                                              
   NBR  ID      0000.0000.0002.00  COST: 0                                        
   NBR  ID      0000.0000.0001.00  COST: 0                                        
  
  0000.0000.0003.00-00   0x0000020c 0xd59e     322            68       0/0/0      
   SOURCE       0000.0000.0003.00                                                 
   NLPID        IPV4                                                              
   AREA ADDR    10                                                                
   INTF ADDR    192.168.2.1                                                       
   NBR  ID      0000.0000.0003.01  COST: 10                                       
   IP-Internal  192.168.2.0     255.255.255.0    COST: 10                         
  
  0000.0000.0003.01-00   0x0000007e 0xcc3f     322            55       0/0/0      
   SOURCE       0000.0000.0003.01                                                 
   NLPID        IPV4                                                              
   NBR  ID      0000.0000.0003.00  COST: 0                                        
   NBR  ID      0000.0000.0002.00  COST: 0                                        
  
  Total LSP(s): 5                                                                 
      *(In TLV)-Leaking Route, *(By LSPID)-Self LSP, +-Self LSP(Extended),        
             ATT-Attached, P-Partition, OL-Overload
  ```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  keychain huawei mode absolute
   receive-tolerance 10
   #
   key-id 1
    algorithm hmac-sha-256
    key-string cipher %+%#)teP2/_7j#@>|r-p:jgDgyKC%=80dRNA,;Cjwwv~%+%#
    send-time 12:00 2019-12-10 to 18:00 2019-12-10
    receive-time 12:00 2019-12-10 to 18:00 2019-12-10
    default send-key-id
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   isis enable 1
   isis authentication-mode keychain huawei
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  keychain huawei mode absolute
   receive-tolerance 10
   #
   key-id 1
    algorithm hmac-sha-256
    key-string cipher %+%#$V_<R'XnL6F&H`P2DLn#IE7-+'~ks9~\acM<OSf)%+%#
    send-time 12:00 2019-12-10 to 18:00 2019-12-10
    receive-time 12:00 2019-12-10 to 18:00 2019-12-10
    default send-key-id
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0002.00
  #
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   isis enable 1
   isis authentication-mode keychain huawei
  #
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   isis enable 1
   isis authentication-mode keychain huawei
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  keychain huawei mode absolute
   receive-tolerance 10
   #
   key-id 1
    algorithm hmac-sha-256
    key-string cipher %+%#v@>@B\eP.Ruug(%b,;fS!5}]GV:rLU3(]U'zd9|>%+%#
    send-time 12:00 2019-12-10 to 18:00 2019-12-10
    receive-time 12:00 2019-12-10 to 18:00 2019-12-10
    default send-key-id
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0003.00
  #
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   isis enable 1
   isis authentication-mode keychain huawei
  #
  return
  ```