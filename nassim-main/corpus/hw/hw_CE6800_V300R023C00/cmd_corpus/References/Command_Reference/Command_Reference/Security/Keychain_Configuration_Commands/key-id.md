key-id
======

key-id

Function
--------



Using the **key-id** command, you can create a new key-id of Keychain.

Using the **undo key-id** command, you can delete the key-id configuration of Keychain.



By default, no key-id of Keychain is configured.


Format
------

**key-id** *key-id*

**undo key-id** *key-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-id* | Specifies the key identification number of a keychain. | The integer value ranges from 0 to 63. |



Views
-----

Keychain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To improve transmission security of protocol packets, you need to periodically change the authentication and encryption algorithms of protocol packets to prevent unauthorized users from obtaining the authentication and encryption algorithms and keys. The keychain protocol can be used to periodically and dynamically change the authentication algorithm and key to ensure the security of protocol packet transmission without the need to manually change the algorithm and key.Keychain-based dynamic switching of the authentication algorithm is implemented through key IDs. Each keychain consists of multiple key IDs and each key ID is configured with an authentication algorithm. Different key IDs are valid in different time periods.



**Follow-up Procedure**



After a key ID is created, specify the authentication and encryption algorithms, and the key for the key ID; set the time when a key ID becomes valid or invalid.The time period within which a key ID for packet sending or receiving is valid, and the time mode configured for the key ID must be identical with that configured for the keychain.



**Precautions**



If a key ID becomes invalid and no other key IDs become valid in time, there is no key ID available for packet authentication and encryption. To ensure the normal packet transmission, specifying a key ID as the default key ID for packet sending is recommended.




Example
-------

# Configure the key-id 1.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] key-id 1

```