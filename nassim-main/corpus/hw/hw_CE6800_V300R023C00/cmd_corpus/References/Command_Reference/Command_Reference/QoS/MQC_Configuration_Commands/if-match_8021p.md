if-match 8021p
==============

if-match 8021p

Function
--------



The **if-match 8021p** command configures a matching rule based on the 802.1p priority of VLAN packets in a traffic classifier.

The **undo if-match 8021p** command deletes a matching rule based on the 802.1p priority of VLAN packets in a traffic classifier.



By default, a matching rule based on the 802.1p priority of VLAN packets is not configured in a traffic classifier.


Format
------

**if-match 8021p** *8021p-value* &<1-8>

**undo if-match 8021p**

**undo if-match 8021p** *8021p-value* &<1-8>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *8021p-value* | Specifies the 802.1p priority in VLAN packets. | The value is an integer that ranges from 0 to 7. A larger value indicates a higher priority. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match 8021p** command to classify traffic based on the 802.1p priority in VLAN packets so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

* Regardless of whether the relationship between traffic classification rules is AND or OR, if you enter multiple values of 802.1p priorities, the packet that matches one 802.1p priority matches a rule.
* If you run the **if-match 8021p** command in the same traffic classifier view multiple times, only the latest configuration takes effect.
* After this command is configured, the switch matches only the 802.1p priority in single-tagged packets. To match the 802.1p priority in double-tagged packets, configure a matching rule based on double tags of packets in a traffic policy.


Example
-------

# Configure a matching rule based on the 802.1p priority of 2 of VLAN packets in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match 8021p 2

```