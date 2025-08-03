authentication-mode (DFS group view)
====================================

authentication-mode (DFS group view)

Function
--------



The **authentication-mode** command specifies the authentication mode and password of DFS group synchronization packets. To ensure successful M-LAG pairing, you must configure the authentication mode and password.



By default, the authentication mode of DFS group synchronization packets is not configured.


Format
------

**authentication-mode hmac-sha256 password** *pwdtext*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hmac-sha256** | Specifies the HMAC-SHA256 authentication mode. | - |
| **password** *pwdtext* | Specifies the authentication password character string. | The value is a string of 8 to 16 case-sensitive characters in clear text or a string of 128 case-sensitive characters in ciphertext. The characters can be letters, symbols, or digits. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When malicious packets attack the network, information on the entire network may be stolen. Therefore, you are advised to configure DFS group authentication to improve network security. After DFS group authentication is configured, you can encapsulate authentication information into DFS group synchronization packets to check the validity and correctness of DFS group synchronization packets sent by the peer device.

**Precautions**

The authentication passwords for DFS group pairing must be the same.After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used.


Example
-------

# Configure authentication for DFS group synchronization packets and set the password to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206

```