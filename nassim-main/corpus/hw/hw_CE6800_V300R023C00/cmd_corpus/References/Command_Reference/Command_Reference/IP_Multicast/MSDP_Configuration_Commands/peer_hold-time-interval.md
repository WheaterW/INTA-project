peer hold-time-interval
=======================

peer hold-time-interval

Function
--------



The **peer hold-time-interval** command sets a holdtime timer value for the entry of a MSDP peer relationship.

The **undo peer hold-time-interval** command restores the default setting.



By default, the holdtime timer value for the entry of an MSDP peer relationship is 90s.


Format
------

**peer** *peer-address* **hold-time-interval** *holdtime-value*

**undo peer** *peer-address* **hold-time-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the IP address of an MSDP peer. | The value is in dotted decimal notation. |
| *holdtime-value* | Specifies a holdtime timer value for the entry of an MSDP peer relationship. | The value is an integer ranging from 3 to 150, in seconds. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an MSDP peer relationship is established, an MSDP peer entry is created, and a holdtime timer is started for the entry. The holdtime timer is reset each time a message is received from the MSDP peer and deleted when the relationship is torn down. The entry is deleted if no message is received from the peer before the holdtime timer expires.To set the holdtime for an MSDP peer entry, run the peer hold-time-interval command.

**Prerequisites**

The peer connect-interface (MSDP) command has been run to set up MSDP peer relationships.

**Precautions**

The lifetime of MSDP peer entries configured on the local end must be longer than the interval for sending keepalive messages for MSDP peer entries configured using the peer keepalive-interval command.


Example
-------

# Set the holdtime timer value to 100s for an MSDP peer entry in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.10.10 connect-interface vlanif 10
[*HUAWEI-msdp] peer 10.10.10.10 hold-time-interval 100

```