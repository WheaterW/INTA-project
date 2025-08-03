timeout (TCP test instance)
===========================

timeout (TCP test instance)

Function
--------



The **timeout** command sets the timeout period of packets in an NQA test instance of TCP test type.

The **undo timeout** command restores the default timeout period.



By default, the timeout period is 3s.


Format
------

**timeout** *time*

**undo timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time* | Specifies the timeout period of probe packets. | The value is an integer ranging from 1 to 60, in seconds. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On networks with poor quality and the low transmission rate, increase the timeout period of probe packets so that packets in response to probe packets can be returned. The timeout period is the period for waiting for a response packet after a request packet is sent. If no response packet is received within the timeout period, the test is considered failed.The value of the timeout period depends on the actual networking. If the value is too small, the NQA test instance may fail.

**Configuration Impact**

You are advised to set the timeout period based on the RTT value. The timeout period configured using the **timeout** command must be greater than the RTT value.The timeout period set using the **timeout** command must be less than or equal to the interval for sending NQA test packets configured using the **interval** command. Otherwise, packets time out.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the timeout period to 60 seconds in the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type tcp
[*HUAWEI-nqa-user-test] timeout 60

```