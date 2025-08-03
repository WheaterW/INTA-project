display keychain
================

display keychain

Function
--------



The **display keychain** command displays the configuration of the specified keychain.




Format
------

**display keychain** *keychain-name*

**display keychain** *keychain-name* **key-id** *key-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *keychain-name* | Specifies the name of the keychain to be displayed. | The value is a string of 1 to 47 case-insensitive characters, spaces not supported. |
| **key-id** *key-id* | Specifies the key-id of a particular keychain to be displayed. | The value is an integer ranging from 0 to 63. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To locate or rectify a keychain authentication failure, or collect required information before configuration, you can run the display keychain command to view configurations of a specified keychain.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about a keychain named earth, with the key ID set to 1.
```
<HUAWEI> display  keychain earth key-id  1
 Keychain information:                                                          
 ----------------------                                                         
 Keychain name             : earth                                              
   Timer mode              : Absolute                                           
   Receive tolerance(s)    : 0                                                  
   Digest length           : 32                                                 
   Time zone               : LMT                                                
   TCP kind                : 254                                                
   TCP algorithm ID        :                                                    
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

 Key ID information:                                                            
 ----------------------                                                         
 Key ID                    : 1                                                  
   Key string              : ******                                             
   Algorithm               : HMAC-SHA-256                                       
   Send timer              :                                                    
     Start time            : 2011-03-10 14:40                                   
     End time              : 2011-03-10 14:50                                   
     Status                : Inactive                                           
   Receive timer           :                                                    
     Start time            : 2011-03-10 14:40                                   
     End time              : 2011-03-10 14:50                                   
     Status                : Inactive                                           
   Default send key ID information                                              
     Default               : Not configured

```

# Display information about a keychain named earth, with the key ID set to 1.
```
<HUAWEI> display  keychain earth
 Keychain information:                                                          
 ----------------------                                                         
 Keychain name             : earth                                              
   Timer mode              : Absolute                                           
   Receive tolerance(s)    : 0                                                  
   Digest length           : 32                                                 
   Time zone               : LMT                                                
   TCP kind                : 254                                                
   TCP algorithm ID        :                                                    
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
 Number of key ID          : 1                                                  
 Active send key ID        : None                                               
 Active receive key ID     : None                                               
 Default send key ID       : Not configured                                     
                                                                                
 Key ID information:                                                            
 ----------------------                                                         
 Key ID                    : 1                                                  
   Key string              : ******                                             
   Algorithm               : HMAC-SHA-256                                       
   Send timer              :                                                    
     Start time            : 2011-03-10 14:40                                   
     End time              : 2011-03-10 14:50                                   
     Status                : Inactive                                           
   Receive timer           :                                                    
     Start time            : 2011-03-10 14:40                                   
     End time              : 2011-03-10 14:50                                   
     Status                : Inactive

```

# Display information about a keychain named earth, without a key ID specified.
```
<HUAWEI> display keychain earth
 Keychain information:                                                          
 ----------------------                                                         
 Keychain name             : earth                                              
   Timer mode              : Absolute                                           
   Receive tolerance(s)    : 0                                                  
   Digest length           : 32                                                 
   Time zone               : LMT                                                
   TCP kind                : 254                                                
   TCP algorithm ID        :                                                    
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
 Number of key ID          : 0                                                  
 Active send key ID        : None                                               
 Active receive key ID     : None                                               
 Default send key ID       : Not configured

```

**Table 1** Description of the **display keychain** command output
| Item | Description |
| --- | --- |
| Keychain Name | Keychain name. |
| Timer Mode | Specifies the timing mode of the keychain.   * absolute: The keychain takes effect in an absolute period. For example, the keychain is effective during the period from 2011-11-19 12:30 to 2011-11-19 18:30. * Daily periodic: The keychain takes effect on a daily basis. * Weekly periodic: The keychain takes effect on a weekly basis. * Monthly periodic: The keychain takes effect on a monthly basis. * Yearly periodic: The keychain takes effect on a yearly basis. |
| Receive tolerance(s) | Receive tolerance time configured for the keychain. |
| TCP Kind | TCP type value configured for the keychain. |
| TCP Algorithm IDs | ID of the TCP authentication algorithm configured for the keychain. |
| Key ID | Unique ID of the key configured for the keychain. |
| Key string | Key string configured for the key-ID. |
| Algorithm | Key-ID authentication algorithm. |
| Start time | Start time of the key-ID. |
| End time | End time of the key-ID. |
| Status | Send or receive key-ID status. |
| Default send Key ID | Default send key-ID configured for the keychain. |
| Default | Default send key-ID status. |
| Digest Length | Default digest length of the keychain. |
| Number of Key IDs | Number of key-IDs configured for the keychain. |
| Active Send Key ID | Active send key-ID. |
| Active Receive Key IDs | Active receive key-ID. |
| SEND TIMER | Key-ID sending time. |
| RECEIVE TIMER | Receive time of the key-ID. |
| DEFAULT SEND KEY ID INFORMATION | Default send key-ID information. |