default send-key-id
===================

default send-key-id

Function
--------



Using the **default send-key-id** command, you can configure a particular key-id as the default send-key-id for that keychain.

Using the **undo default send-key-id** command, you can delete default send-key-id.



By default, no key-id is configured as default send-key-id.


Format
------

**default send-key-id**

**undo default send-key-id**


Parameters
----------

None

Views
-----

weekly Key-ID view,yearly Key-ID view,daily Key-ID view,monthly Key-ID view,absolute Key-ID view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The keychain protocol can be used to periodically and dynamically change the authentication algorithm and key to ensure the security of protocol packet transmission without the need to manually change the algorithm and key. Each keychain consists of multiple key IDs, each of which has its own sending and receiving time. Different key IDs are active within a specified period.If no send-key-id exists in the keychain or there is no active send-key-id in a certain period, the keychain cannot authenticate or encrypt protocol packets. As a result, the application protocol is disconnected due to an authentication failure. Configuring the default send-key-id ensures that the keychain uses this key ID to authenticate and encrypt protocol packets when no active key ID is available. This ensures normal communication of protocol packets.



**Precautions**

Each keychain can have only one default key ID for packet sending.

* If the default key ID for packet sending is an existing key ID, the authentication and encryption algorithms, and key corresponding to the key ID are used.
* If the default key ID for packet sending is a newly created key ID, configure the authentication and encryption algorithms, and key for the key ID.


Example
-------

# Configure the send-key-id 1 as default in keychain huawei.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] key-id 1
[*HUAWEI-keychain-huawei-keyid-1] default send-key-id

```