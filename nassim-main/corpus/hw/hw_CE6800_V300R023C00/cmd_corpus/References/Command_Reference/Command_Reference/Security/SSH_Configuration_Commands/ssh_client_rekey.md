ssh client rekey
================

ssh client rekey

Function
--------



The **ssh client rekey** command sets the criteria that trigger SSH client key re-negotiation.

The **undo ssh client rekey** command restores the default values of criteria that trigger SSH client key re-negotiation.



By default, key re-negotiation is triggered on the SSH client when one of the following conditions is met:

* The total size of sent and received packets reaches 1000 MB.
* The total number of sent and received packets reaches 2147483648.
* The online duration reaches 60 minutes.


Format
------

**ssh client rekey** { { **max-packet** *max-packet* } | { **time** *minutes* } | { **data-limit** *data-limit* } } \*

**undo ssh client rekey** { { **max-packet** [ *max-packet* ] } | { **time** [ *minutes* ] } | { **data-limit** [ *data-limit* ] } } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **max-packet** *max-packet* | Specifies the maximum number of packets that triggers key re-negotiation. | The value is an integer ranging from 268435456 to 2147483648. |
| **time** *minutes* | Specifies the session duration that triggers key re-negotiation. | The value is an integer in the range of 30 to 1440, in minutes. |
| **data-limit** *data-limit* | Specifies the maximum packet data volume that triggers key re-negotiation. | The value is an integer ranging from 100 to 10000, in MB. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When an SSH session meets one or more of the following criteria, the system re-negotiates a key and uses the new key to establish SSH session connections, improving system security.

* The number of interaction packets meets the configured key re-negotiation criterion.
* The accumulated packet data volume meets the configured key re-negotiation criterion.
* The session duration meets the configured key re-negotiation criterion.A key re-negotiation request is initiated when either the SSH client or server meets the key re-negotiation criteria, and the other party responds.This command takes effect for both IPv4 and IPv6 SSH clients.

**Precautions**

A key re-negotiation request is initiated when either the SSH client or server meets the key re-negotiation criteria, and the other party responds.


Example
-------

# Configure key re-negotiation to be triggered on the SSH client when the total size of sent and received packets reaches 10000 MB, the total number of sent and received packets reaches 268435456, or the online duration reaches 1440 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ssh client rekey data-limit 10000 max-packet 268435456 time 1440

```