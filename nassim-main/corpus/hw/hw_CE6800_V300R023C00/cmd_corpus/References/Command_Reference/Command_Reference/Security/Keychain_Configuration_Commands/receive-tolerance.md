receive-tolerance
=================

receive-tolerance

Function
--------



Using the **receive-tolerance** command, you can set receive tolerance for all the receive keys under the keychain.

Using the **undo receive-tolerance** command, you can delete the receive-tolerance configuration.



By default, the receive tolerance value is 0.


Format
------

**receive-tolerance** { *value* | **infinite** | **seconds** *secvalue* }

**undo receive-tolerance** [ **seconds** *secvalue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the receive tolerance time. | The integer value ranges from 1 to 14400. |
| **infinite** | Specifies that the receive tolerance is infinite, so the receive key will always be valid. | - |
| **seconds** *secvalue* | Specifies the value of the receive tolerance time, in seconds. | The value is an integer ranging from 1 to 864000, in seconds. |



Views
-----

Keychain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In keychain authentication mode, secure protocol packet transmission is provided by changing the authentication algorithm and key dynamically. Each key ID is configured with an authentication algorithm. When a key ID becomes valid, the corresponding authentication algorithm is used, ensuring the dynamic change of authentication algorithms.Due to the networking environment or clock asynchronization on the packet sender and receiver, packet transmission may be delayed. The receiver may receive a packet sent from the sender after its key ID for packet receiving becomes invalid. As a result, the receiver discards the packet and packet transmission is interrupted. To address such a problem, set a tolerance time to ensure that the validity period of the key ID for packet receiving on the receiver expires after all packets sent from the sender reach the receiver.



**Implementation Procedure**



After a tolerance time is set, the tolerance time is added to the start time and end time when the key ID for packet receiving becomes valid.



**Precautions**



A tolerance time is required for each keychain. The set tolerance time takes effect for all key IDs in the keychain.




Example
-------

# Set the receive tolerance time to 1000 seconds.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] receive-tolerance seconds 1000

```

# Configure the receive-tolerance as 570 minutes.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] receive-tolerance 570

```

# Configure the receive-tolerance as infinite.
```
<HUAWEI> system-view
[~HUAWEI] keychain huawei mode absolute
[*HUAWEI-keychain-huawei] receive-tolerance infinite

```