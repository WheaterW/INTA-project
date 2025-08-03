discriminator local (BFD session view)
======================================

discriminator local (BFD session view)

Function
--------



The **discriminator local** command sets the local discriminator of a static BFD session.

The **undo discriminator local** command deletes the local discriminator of a static BFD session.



By default, the local discriminator of a static BFD session is not created.


Format
------

**discriminator local** *discr-value*

**undo discriminator local**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *discr-value* | Specifies the local discriminator of a BFD session. | The value is an integer that ranges from 1 to 16384 . |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During the establishment of a static BFD session, you must run the **discriminator local** command to set the local discriminator of the static BFD session; otherwise, the static BFD session cannot be established.

**Prerequisites**



A BFD session has been created.



**Precautions**

* Only a static BFD session requires local and remote discriminators.
* In a BFD session, the local discriminator of the local end must be the same as the remote discriminator of the remote end, and the remote discriminator of the local end must be the same as the local discriminator of the remote end. Otherwise, the BFD session cannot go Up.
* The local and remote discriminators set for a static BFD session can be changed.
* Do not configure the same remote discriminator and local discriminator for different sessions on a device.
* When a BFD session is Up, changing the local or remote discriminator causes the session to enter the administratively Down state. The BFD session recovers automatically without manual intervention.


Example
-------

# Set the local discriminator of the one-arm-echo BFD session to 80.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] ip address 10.1.1.2 24
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd test bind peer-ip 10.1.1.1 interface 100GE 1/0/1 one-arm-echo
[*HUAWEI-bfd-session-test] discriminator local 80

```