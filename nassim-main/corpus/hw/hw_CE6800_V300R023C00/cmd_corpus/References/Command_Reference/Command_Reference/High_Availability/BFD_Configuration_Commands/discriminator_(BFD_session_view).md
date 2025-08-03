discriminator (BFD session view)
================================

discriminator (BFD session view)

Function
--------



The **discriminator** command sets the local and remote discriminators of a static BFD session.

The **undo discriminator** command deletes the local and remote discriminators of a static BFD session.



By default, the discriminator of a static BFD session is not created.


Format
------

**discriminator local** *discr-value*

**discriminator remote** *discr-value*

**undo discriminator local** [ *discr-value* ]

**undo discriminator remote** [ *discr-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **remote** *discr-value* | Specifies the remote discriminator of a BFD session. | The value is an integer that ranges from 1 to 4294967295. |
| **local** *discr-value* | Specifies the local discriminator of a BFD session. | The value is an integer that ranges from 1 to 16384 . |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During the establishment of a static BFD session, you must run the **discriminator** command to set the local and remote discriminators of the static BFD session; otherwise, the static BFD session cannot be established.

**Prerequisites**



A BFD session has been created.



**Configuration Impact**



Once the local and remote identifiers for the static BFD session are configured successfully, they can be modified.



**Precautions**

* Only a static BFD session requires local and remote discriminators.
* In a BFD session, the local discriminator of the local end must be the same as the remote discriminator of the remote end, and the remote discriminator of the local end must be the same as the local discriminator of the remote end. Otherwise, the BFD session cannot go Up.
* The local and remote discriminators set for a static BFD session can be changed.
* Do not configure the same remote discriminator and local discriminator for different sessions on a device.
* When a BFD session is Up, changing the local or remote discriminator causes the session to enter the administratively Down state. The BFD session recovers automatically without manual intervention.

Example
-------

# Set the local discriminator of the BFD session to 80 and the remote discriminator to 800.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd s1 bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-s1] quit
[*HUAWEI] bfd s1
[*HUAWEI-bfd-session-s1] discriminator local 80
[*HUAWEI-bfd-session-s1] discriminator remote 800

```