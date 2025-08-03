jitter-codec
============

jitter-codec

Function
--------



The **jitter-codec** command specifies a code type for a UDP voice jitter test instance.

The **undo jitter-codec** command deletes a code type configured for a UDP voice jitter test instance.



By default, a UDP jitter test instance is not a simulated voice test instance.


Format
------

**jitter-codec** { **g711a** | **g711u** | **g729a** }

**undo jitter-codec**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **g711a** | Sets the code type of a UDP voice jitter test instance to g711alaw. In G.711 a-law, the transmission rate is 64 kbit/s. | - |
| **g711u** | Sets the code type of a UDP voice jitter test instance to g711ulaw. In G.711 muHmm-law, the transmission rate is 64 kbit/s. | - |
| **g729a** | Sets the code type of a UDP voice jitter test instance to g729a. In G.729A, the transmission rate is 8 kbit/s. | - |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a UDP jitter test instance is used to monitor VoIP services, the **jitter-codec** command can be used to specify the codec types used for conversion between simulated voice signals and digital signals. You can specify various code types based on actual code types in VoIP applications.The three code types of g711a, g711u, and g729a are implemented differently in jitter test instances.The differences in implementing code types are as follows:

* g711a: the data length is 172 bytes, the sent packets number is 1000, and the packet transmission rate is 20 ms.
* g711u: the data length is 172 bytes, the sent packets number is 1000, and the packet transmission rate is 20 ms.
* g729a: the data length is 32 bytes, the sent packets number is 1000, and the packet transmission rate is 20 ms.After configuring the code types, you can run the **adv-factor** command to set the advantage factor for the simulated voice test calculation so that the UDP jitter test instance can be performed by simulating actual voice packets. When calculating the quality parameter R value of the voice transmission network, a testing engineer needs to specify a advantage factor according to the transmission distance and media. The advantage factor is the compensation paid in advance by the user for the quality loss during voice transmission on the network to be tested. The value of an advantage factor depends on the type of the network to be tested and is defined by the user. The greater the anticipated loss, the greater the value. The value represents the tolerance of the user on the quality loss during voice transmission on the network.Running the jitter-codec and **adv-factor** commands to configure UDP jitter test instances helps monitor VoIP networks and analyze service traffic.

**Prerequisites**

* The **jitter-codec** command is applicable only to UDP jitter test instances.
* Before a UDP jitter test instance starts, ensure that the **nqa server udpecho** command is used on the peer device to respond to the UDP jitter tests.

**Configuration Impact**

* If no code type is specified for a UDP jitter test instance, the UDP jitter test instance is not a simulated voice test instance by default. In this case, the UDP jitter test instance is used for testing jitter of common services.
* If a code type has been specified, running the **jitter-codec** command again overrides the previous configuration.
* If the code type of a test instance is changed using the **jitter-codec** command, the previously configured advantage factor becomes invalid, and a new advantage factor needs to be set.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the code type of a UDP voice jitter test instance to g711a.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance admin jitter
[*HUAWEI-nqa-admin-Jitter] test-type jitter
[*HUAWEI-nqa-admin-Jitter] jitter-codec g711a

```