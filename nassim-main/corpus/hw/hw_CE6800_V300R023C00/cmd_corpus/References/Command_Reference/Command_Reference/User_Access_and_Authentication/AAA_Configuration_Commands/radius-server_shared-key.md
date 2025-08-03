radius-server shared-key
========================

radius-server shared-key

Function
--------

The **radius-server shared-key** command configures the shared key of a RADIUS server.

The **undo radius-server shared-key** command deletes the shared key of a RADIUS server.

By default, no shared key of RADIUS server is configured.



Format
------

**radius-server shared-key cipher** *key-string*

**undo radius-server shared-key**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-string* | Specifies the shared key of a RADIUS server. | The value is a string of 1 to 128 case-sensitive characters in plaintext or a string of 128 to 268 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |
| **cipher** | Indicates the shared key in cipher text. | - |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

The shared key is used to encrypt the password and generate the response authenticator.

When exchanging authentication packets with a RADIUS server, the device encrypt important data such as the password to ensure security of data transmission over the network. To ensure validity of both communication parties, the device and RADIUS server must be configured with the same shared key.

Example
-------

# Set the shared key of the RADIUS server to YsHsjx\_202206YsHsjx\_202206 in cipher text. (The key does not contain special characters. If you want to use the key, select Y for interaction information.)
```
<HUAWEI> system-view
Enter system view, return user view with return command.                                                                            
[~HUAWEI] radius-server template huawei0209
[*HUAWEI-radius-huawei0209] radius-server shared-key cipher YsHsjx_202206YsHsjx_202206
Warning: The shared-key complexity is low. It is recommended that the password contain at least sixteen characters and be a combinat
ion of at least two of the following categories: Uppercase letters <A-Z>; Lowercase letters <a-z>; Numerals <0-9>; Symbols (all char
acters not defined as letters or numerals), such as !,$,#, and %. Continue? [Y/N]:Y                                                 
Info: The shared key is not automatically negotiated by the two communication parties, please update the shared key periodically to 
prevent key leakage.                                                                                                                
[*HUAWEI-radius-huawei0209]

```

# Set the shared key of the RADIUS server to YsHsjx\_202206YsHsjx\_202206 in cipher text. (The key does not contain special characters. If the key is not used, select N for interaction information.)
```
<HUAWEI> system-view
Enter system view, return user view with return command.                                                                            
[~HUAWEI] radius-server template huawei0209
[*HUAWEI-radius-huawei0209] radius-server shared-key cipher YsHsjx_202206YsHsjx_202206
Warning: The shared-key complexity is low. It is recommended that the password contain at least sixteen characters and be a combinat
ion of at least two of the following categories: Uppercase letters <A-Z>; Lowercase letters <a-z>; Numerals <0-9>; Symbols (all char
acters not defined as letters or numerals), such as !,$,#, and %. Continue? [Y/N]:N                                                 
[*HUAWEI-radius-huawei0209]

```