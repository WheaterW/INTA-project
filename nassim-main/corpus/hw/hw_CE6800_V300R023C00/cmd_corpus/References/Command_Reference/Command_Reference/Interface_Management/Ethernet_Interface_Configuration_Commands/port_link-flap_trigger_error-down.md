port link-flap trigger error-down
=================================

port link-flap trigger error-down

Function
--------



The **port link-flap trigger error-down** command enables an Ethernet interface to transit to the Error-Down state due to link flapping.

The **undo port link-flap trigger error-down** command disables an Ethernet interface from transiting to the Error-Down state due to link flapping.



By default, link flapping protection is enabled on an interface.


Format
------

**port link-flap trigger error-down**

**undo port link-flap trigger error-down**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Faults such as network cable faults or active/standby switchover may cause the interface status to frequently alternate between Up and Down. As a result, the network topology changes frequently. If some Layer 2 protocols are configured on an interface, the interface sends TC BPDUs to update ARP entries. If ARP entries are not updated in a timely manner, user network services are interrupted, affecting user communication.To solve this problem, configure an interface to enter the Error-Down state due to link flapping. After this function is configured, the device checks the number of interface flapping times and interval when receiving an interface Up/Down message. If the number of interface flapping times within a specified period reaches the specified value, the interface enters the Error-Down state to protect the network. After this function is enabled, an interface enters the Error-Down state if the interface status changes five times within 10s by default. When a device detects a fault on an interface, the device sets the interface status to Error-Down. The interface cannot send or receive packets, and the interface indicator is off.

**Follow-up Procedure**

* The link flapping detection interval and number of link flapping times are configured on the interface.
* If an interface enters the Error-Down state, you are advised to check whether the optical modules at both ends of the optical interface are properly installed or whether the optical modules or optical fibers are faulty, and check whether the network cables at both ends of the electrical interface are properly installed.You can use either of the following methods to restore the interface status:
* Manually rectify the fault (after the Error-Down event occurs).If only a few interfaces are in Error-Down state, run the **shutdown** and **undo shutdown** commands in the interface view or run the **restart** command in the interface view to restart the interfaces. For an optical interface, you can also remove and install the transmission medium to restore the interface status.
* Automatic recovery (before an Error-Down event occurs)If a large number of interfaces are in Error-Down state, manually restoring the interfaces one by one will cause a lot of repeated work and some interfaces may not be configured. To prevent this problem, run the **error-down auto-recovery cause link-flap interval** command in the system view to enable the auto-recovery function and set the auto-recovery delay. You can run the **display error-down recovery** command to check information about automatic interface recovery.

**Precautions**

This method does not take effect on interfaces that are already in Error-Down state. It takes effect only on interfaces that enter Error-Down state after this command is run.


Example
-------

# Enable link flapping protection.
```
<HUAWEI> system-view
[~HUAWEI] port link-flap trigger error-down

```