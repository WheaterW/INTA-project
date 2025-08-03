source-interface (UDP Jitter test instance)
===========================================

source-interface (UDP Jitter test instance)

Function
--------



The **source-interface** command specifies a source interface for an NQA test instance of UDP Jitter test.

The **undo source-interface** command deletes the source interface for an NQA test instance of UDP Jitter test.



By default, the outbound interface that sends test packets is used as the source interface. You can check the routing table based on the destination address for confirmation.


Format
------

**source-interface** { *ifName* | *ifType* *ifNum* }

**undo source-interface**

**undo source-interface** { *ifName* | *ifType* *ifNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ifName* | Specifies the name of a source interface. | - |
| *ifType* | Specifies the type of a source interface. | - |
| *ifNum* | Specifies the number of a source interface. | - |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **source-interface** command specifies a source interface for an NQA test instance.The **source-interface** command is applicable to the following scenarios:

* If both a source IP address and a source interface are specified for an NQA test instance, test packets are sent through the specified source interface.
* If no source IP address is specified, the IP address of the source interface is used as the source IP address of the NQA test instance. In this case, the test packets are sent and received on the source interface configured using the **source-interface** command.

**Prerequisites**

The specified source interface is Up.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Configure the source interface for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] source-interface 100GE 1/0/1

```