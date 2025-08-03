adv-factor
==========

adv-factor

Function
--------



The **adv-factor** command specifies the advantage factor for a UDP voice jitter test instance.

The **undo adv-factor** command deletes the advantage factor configured for a UDP voice jitter test instance.



By default, the advantage factor configured for a UDP voice jitter test instance is 0.


Format
------

**adv-factor** *factor-value*

**undo adv-factor**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *factor-value* | Specifies the advantage factor for a UDP voice jitter test instance. | The value is an integer ranging from 0 to 20. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Prerequisites**

The **adv-factor** command can be used to specify an advantage factor only after the following conditions are met:

* A UDP jitter test is being performed.
* The **jitter-codec** command is used to specify a code type for a UDP voice jitter test instance. The code type can be g711a, g711u, or g729a. They are used in VoIP services for conversion between simulated voice signals and digital signals. Before configuring an advantage factor, you can specify different code types based on actual code types used in VoIP applications.Before a UDP jitter test instance starts, ensure that the **nqa server udpecho** command is used on the peer device to respond to the UDP jitter tests.

**Configuration Impact**

If an advantage factor has been configured, running the **adv-factor** command again overrides the previous configuration.If the code type of a test instance is changed using the **jitter-codec** command, the previously configured advantage factor becomes invalid, and a new advantage factor needs to be set.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the advantage factor for a UDP voice jitter test instance to 20.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance admin Jitter
[*HUAWEI-nqa-admin-Jitter] test-type jitter
[*HUAWEI-nqa-admin-Jitter] jitter-codec g711a
[*HUAWEI-nqa-admin-Jitter] adv-factor 20

```