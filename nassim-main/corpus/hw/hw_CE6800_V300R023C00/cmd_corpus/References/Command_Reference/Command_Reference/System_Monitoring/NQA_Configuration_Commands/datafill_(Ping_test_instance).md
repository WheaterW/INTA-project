datafill (Ping test instance)
=============================

datafill (Ping test instance)

Function
--------



The **datafill** command fills padding characters into the Data field of packets to be sent in an NQA test instance.

The **undo datafill** command disables a device from filling padding characters into the Data field of packets to be sent in an NQA test instance.



By default, there are no padding characters in the Data field.


Format
------

**datafill** *fill-string*

**undo datafill**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *fill-string* | Specifies the padding characters filled into NQA test packets. | The value is a string of 1 to 230 characters. The default value is a null string with no characters. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To fill special padding characters into the Data field of the test packets to be sent for identification, run the **datafill** command.For example, if a test packet sent in an ICMP test instance is destined for a port that does not exist, the destination that receives the test packet replies to the transmit end with a port unreachable packet containing the contents of the test packet. The transmit end will receive a great number of reply packets, but it can identify different test instances based on the padding characters.

**Configuration Impact**

When you run the **datafill** command to fill in packets:

* If the size of the data packet to be sent in the test instance is smaller than the configured padding data, the padding character string is filled in sequence based on the actual size of the data packet to be sent.
* If the size of the data packet to be sent in the test is greater than the configured padding data, the padding character string is used for cyclic padding.For example, if the padding character string is set to abcd and the size of the test data packet is 3, only abc is used for padding. If the size of the test data packet is 6, abcdab is used for padding.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Fill the padding characters abcd into the test packet for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] datafill abcd

```