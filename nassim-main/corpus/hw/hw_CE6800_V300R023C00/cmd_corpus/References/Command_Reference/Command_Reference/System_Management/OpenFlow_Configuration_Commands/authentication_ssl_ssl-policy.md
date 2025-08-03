authentication ssl ssl-policy
=============================

authentication ssl ssl-policy

Function
--------



The **authentication ssl ssl-policy** command configures the SSL policy for the OpenFlow connection between the SDN controller and switch.

The **undo authentication ssl ssl-policy** command restores the default setting.



By default, no SSL policy is configured for an OpenFlow connection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**authentication ssl ssl-policy** *ssl-policy-name*

**undo authentication ssl** [ **ssl-policy** *ssl-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ssl-policy-name* | Specifies the name of an SSL policy. | The value is a string of 1 to 23 case-insensitive characters, spaces not supported. |



Views
-----

OpenFlow-forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The switch and SDN controller exchange information through the OpenFlow connection. To prevent access of unauthorized users and improve network security, configure an SSL policy for the OpenFlow connection.

**Prerequisites**

The switch functions as an SSL client. The SSL policy has been configured.

**Configuration Impact**

After the configuration is successful, SSL authentication is used for the session between the device and the specified server.

**Precautions**

The SSL authentication mode and keychain authentication mode are mutually exclusive.The server and device must use the same SSL configuration. Otherwise, the OpenFlow session will be interrupted or fail to be established.


Example
-------

# Configure an SSL policy for an OpenFlow connection.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy aaa
[~HUAWEI-ssl-policy-aaa] quit
[~HUAWEI] sdn agent
[~HUAWEI-sdn-agent] controller-ip 1.1.1.1
[~HUAWEI-sdn-agent-ctrl-1.1.1.1] openflow agent
[~HUAWEI-sdn-agent-ctrl-1.1.1.1-openflow] authentication ssl ssl-policy aaa

```