icmp-jitter-mode
================

icmp-jitter-mode

Function
--------



The **icmp-jitter-mode** command specifies an ICMP jitter test mode.

The **undo icmp-jitter-mode** command restores the default ICMP jitter test mode.



By default, an ICMP jitter test is in icmp-timestamp mode.


Format
------

**icmp-jitter-mode** { **icmp-echo** | **icmp-timestamp** }

**undo icmp-jitter-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **icmp-echo** | Indicates that an ICMP jitter test is performed using ICMP echo packets. | datafill and datasize can be specified for ICMP jitter and path jitter test instances only when the icmp-jitter-mode value is icmp-echo. |
| **icmp-timestamp** | Indicates that an ICMP jitter test is performed using ICMP timestamp packets. | - |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set an ICMP jitter test mode, run the **icmp-jitter-mode** command. The command output includes the date and time when the destination received ICMP packets.If the peer device can respond to the ICMP timestamp packets, use the icmp-timestamp mode so that accurate test results can be displayed.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the mode to icmp-echo for the ICMP jitter test named admin icmpjitter.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance admin icmpjitter
[*HUAWEI-nqa-admin-icmpjitter] test-type icmpjitter
[*HUAWEI-nqa-admin-icmpjitter] icmp-jitter-mode icmp-echo

```