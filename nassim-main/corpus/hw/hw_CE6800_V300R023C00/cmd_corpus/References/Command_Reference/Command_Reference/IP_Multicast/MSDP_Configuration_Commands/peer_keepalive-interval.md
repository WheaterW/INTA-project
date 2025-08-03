peer keepalive-interval
=======================

peer keepalive-interval

Function
--------



The **peer keepalive-interval** command sets a keepalive timer value for a Multicast Source Discovery Protocol (MSDP) peer.

The **undo peer keepalive-interval** command restores the default setting.



By default, the keepalive timer value for an MSDP peer is 60s.


Format
------

**peer** *peer-address* **keepalive-interval** *keepalive-time-value*

**undo peer** *peer-address* **keepalive-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the IP address of an MSDP peer. | The value is in dotted decimal notation. |
| *keepalive-time-value* | Sets a keepalive timer value. | The value is an integer ranging from 1 to 60, in seconds. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an MSDP peer relationship is established, both ends send keepalive messages, and a keepalive timer is started for the MSDP peer. The keepalive timer is reset each time the local end sends a keepalive message upon timer expiration and deleted when the relationship is torn down.To set a keepalive timer value, that is, the interval at which a keepalive message is sent, run the peer keepalive-interval command.

**Prerequisites**

The peer connect-interface(MSDP) command is run to set up MSDP peer relationships.

**Precautions**

The keepalive timer value set on the local end must be less than the holdtime timer value set by the **peer hold-time-interval** command on the peer end for the corresponding MSDP peer relationship entry.


Example
-------

# Set the keepalive timer value to 30s in the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.10.10 connect-interface vlanif 10
[*HUAWEI-msdp] peer 10.10.10.10 keepalive-interval 30

```