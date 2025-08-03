description (NQA view)
======================

description (NQA view)

Function
--------



The **description** command configures the description for an NQA test instance.

The **undo description** command deletes the description of an NQA test instance.



By default, no description is configured for an NQA test instance.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | Specifies the description of an NQA test instance. | The value is a string of 1 to 230 characters, spaces supported. The default value is null. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **description** command describes a test instance, which facilitates maintenance.Generally test items or test objects of a test instance are described.

**Configuration Impact**

If the description has been configured for an NQA test instance, running the description again overrides the previous configuration.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Configure the description fortest for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] description fortest

```