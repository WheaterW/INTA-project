authentication keychain
=======================

authentication keychain

Function
--------



The **authentication keychain** command configures keychain authentication for the OpenFlow connection between the SDN controller and device.

The **undo authentication keychain** command restores the default configuration.



By default, keychain authentication is not configured for an OpenFlow connection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**authentication keychain** *keychain-name*

**undo authentication keychain** [ *keychain-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *keychain-name* | Specifies the name of a keychain. | The value must be an existing keychain name configured on the device. |



Views
-----

OpenFlow-forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To improve network security and prevent access of unauthorized users, configure keychain authentication for the OpenFlow connection.

**Configuration Impact**

After the configuration is complete, keychain authentication is used for sessions between the device and the specified server.

**Precautions**

The agent must use the same keychain configuration. Otherwise, the OpenFlow session will be interrupted or cannot be established.


Example
-------

# Configure keychain authentication for the OpenFlow connection.
```
<HUAWEI> system-view
[~HUAWEI] keychain kk mode absolute
[*HUAWEI-keychain-kk] quit
[*HUAWEI] sdn agent
[*HUAWEI-sdn-agent] controller-ip 10.1.1.1
[*HUAWEI-sdn-agent-ctrl-10.1.1.1] openflow agent
[*HUAWEI-sdn-agent-ctrl-10.1.1.1-openflow] authentication keychain kk

```