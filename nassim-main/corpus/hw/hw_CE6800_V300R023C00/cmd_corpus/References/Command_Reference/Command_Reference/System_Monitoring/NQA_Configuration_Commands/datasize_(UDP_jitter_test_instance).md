datasize (UDP jitter test instance)
===================================

datasize (UDP jitter test instance)

Function
--------



The **datasize** command sets the size of the data area in a UDP jitter NQA test packet.

The **undo datasize** command restores the default configuration.



If the jitter-codec command is not configured:

* If version-number is set to 1 in the nqa jitter tag-version command, the default size of the data field in an NQA test packet is 68 bytes.
* If version-number is set to 2 in the nqa jitter tag-version command, the default size of the data field in an NQA test packet is 20 bytes.

If the jitter-codec command is configured:

* If the value of jitter-codec is g711a or g711u, the default size of the data field in an NQA test packet is 172 bytes.
* If the value of jitter-codec is g729a, the default size of the data field in an NQA test packet is 32 bytes.


Format
------

**datasize** *datasizeValue*

**undo datasize**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *datasizeValue* | Specifies the size of the data field in an NQA test packet. | The value ranges from 0 to 8100, in bytes.  If version-number is set to 1 in the nqa jitter tag-version command and the configured value of size is less than the default value 68, the size of the data field in a test packet is 68 bytes.  If version-number is set to 2 in the nqa jitter tag-version command and the configured value of size is less than the default value 20, the size of the data field in a test packet is 20 bytes. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **datasize** command sets the size of the data field in a test packet. This ensures that the size of the test packet is closer to the size of the actual data packet and the statistics obtained is more accurate.For example, if a UDP jitter test instance is used to detect VoIP services, you can run the **datasize** command to set the size of the data field in a test packet to have the same size as the actual voice packet so as to simulate the actual traffic in a period of time.

**Configuration Impact**

If the commands jitter-codec and datasize have been run to set the packet size, running the **datasize** command again overrides the previous configuration.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the size of the data field in an NQA test packet named user test to 100 bytes.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type jitter
[*HUAWEI-nqa-user-test] datasize 100

```