datasize (ICMP Ping test instance)
==================================

datasize (ICMP Ping test instance)

Function
--------



The **datasize** command sets the size of the data field in an NQA test packet of ICMP Ping test type.

The **undo datasize** command restores the default data field size.



By default, the size of the data field in an NQA test packet is 0 bytes.


Format
------

**datasize** *datasizeValue*

**undo datasize**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *datasizeValue* | Specifies the size of the data field in an NQA test packet. | The value ranges from 0 to 8100, in bytes. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **datasize** command sets the size of the data field in a test packet. This ensures that the size of the test packet is closer to the size of the actual data packet and the statistics obtained is more accurate.

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
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] datasize 100

```