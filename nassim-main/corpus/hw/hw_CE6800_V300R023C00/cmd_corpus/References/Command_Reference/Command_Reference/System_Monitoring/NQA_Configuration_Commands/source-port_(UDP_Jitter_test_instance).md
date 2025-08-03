source-port (UDP Jitter test instance)
======================================

source-port (UDP Jitter test instance)

Function
--------



The **source-port** command sets the source port number for an NQA UDP jitter test instance.

The **undo source-port** command restores the default source port number.



By default, the source port number is 0, and the system automatically allocates the port number.


Format
------

**source-port** *portValue*

**undo source-port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *portValue* | Specifies the source port number for an NQA test instance. | The value is an integer that ranges from 1 to 65535. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the source port number for an NQA test instance, run the **source-port** command.

* If no source port number is set for an NQA test instance, a port is randomly selected to send and receive test packets.
* If a source port number is set for an NQA test instance, the set source port is used to send and receive test packets.Specifying the source port number allows NQA test packets to be sent and received in a standard manner and prevents NQA test packets from being filtered out by ACL rules.

**Prerequisites**

The source port configured with the **source-port** command must be a valid port. Otherwise, the test fails.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the source port number to 2000 for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] source-port 2000

```