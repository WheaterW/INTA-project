vrrp vrid authentication-mode (Interface view)
==============================================

vrrp vrid authentication-mode (Interface view)

Function
--------



The **vrrp vrid authentication-mode** command configures an authentication mode and key for a VRRP group.

The **undo vrrp vrid authentication-mode** command cancels authentication for a VRRP group.



By default, a VRRP group does not authenticate packets.


Format
------

**vrrp vrid** *virtual-router-id* **authentication-mode** { **simple** *key* | **md5** *md5-key* }

**vrrp vrid** *virtual-router-id* **authentication-mode** **simple** { **plain** *key* | **cipher** *cipher-key* }

**undo vrrp vrid** *virtual-router-id* **authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| **simple** *key* | Specifies the authentication key in simple authentication mode.   * To prevent high security risks, you are advised to select the ciphertext mode. To ensure device security, change the password periodically. | The value is a string of 1 to 8 case-sensitive characters, spaces not supported.  When double quotation marks are used around the string, spaces are allowed in the string. |
| **md5** *md5-key* | Specifies the authentication key for HMAC-MD5 authentication. | The value is a string of 1 to 8 case-sensitive characters in plaintext or a string of 128 case-sensitive characters in ciphertext. The value can be letters or digits. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **plain** *key* | Indicates plaintext authentication.  When configuring an authentication password, select the ciphertext mode. If you select the simple text mode, the password is saved as a simple text in the configuration file, which has a high risk. To ensure device security, change the password periodically. | The value is a string of 1 to 8 case-sensitive characters, spaces not supported.  When double quotation marks are used around the string, spaces are allowed in the string. |
| **cipher** *cipher-key* | Specifies an authentication key for ciphertext authentication. | The value is a string of 1 to 8 case-sensitive characters in plaintext or a string of 1 to 128 case-sensitive characters in ciphertext. The value can be letters or digits. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To help improve security of protocol packets, run the **vrrp vrid authentication-mode** command to configure an authentication mode and key for a specified VRRP group.

**Prerequisites**

A VRRP group has been configured using the **vrrp vrid** command.

**Configuration Impact**

After you set authentication mode and key for a specified VRRP group, a backup device in the group compares its authentication mode and key with the authentication mode and key in a received VRRP Advertisement packet.

* If the authentication modes and keys are the same, the backup device discards the packet and resets the timer after the VRRP module finishes processing.
* If the authentication modes and keys are different, the backup device directly discards the packet. The operation does not affect the VRRP group status.

**Precautions**

* If all virtual IP addresses in a VRRP group are deleted, the system automatically deletes the VRRP group.
* Devices in the same VRRP group must be configured with the same authentication mode. Otherwise, master and backup devices negotiation fails.
* The authentication mode of a VRRP group can only be simple or HMAC-MD5. Both authentication modes have security risks. HMAC-MD5 is recommended because it is more secure than simple authentication.

Example
-------

# Set the authentication mode of VRRP group 1 on 100GE 1/0/1 to MD5 and the authentication key to YsH\_2022.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.10.10.9 24
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.10
[*HUAWEI-100GE1/0/1] vrrp vrid 1 authentication-mode md5 YsH_2022

```