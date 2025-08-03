dhcp relay information enable
=============================

dhcp relay information enable

Function
--------



The **dhcp relay information enable** command enables the Option 82 function for the DHCP relay agent.

The **undo dhcp relay information enable** command disables the Option 82 function for the DHCP relay agent.



By default, the Option 82 function is disabled for the DHCP relay agent.


Format
------

**dhcp relay information enable**

**undo dhcp relay information enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to the DHCP relay agent. When DHCP Request messages carry Option 82 information, the DHCP server can locate user positions accurately and assign IP addresses to users using different policies. After the Option 82 function is enabled on the DHCP relay agent, the device checks the Option 82 field contained in the packets and processes the packets using corresponding policies.

**Prerequisites**

DHCP has been enabled by running the **dhcp enable** command in the system view.DHCP relay has been enabled by running the **dhcp select relay** command in the interface view.

**Follow-up Procedure**

Run the dhcp relay information strategy { drop | keep | replace } command in the interface view to configure strategies for the DHCP relay agent to process Option 82 information.

**Precautions**

If you run the **dhcp relay information enable** command on an interface and the dhcp option82 { insert | rebuild } enable command in the VLAN view or on a physical interface in the VLAN simultaneously, only the **dhcp relay information enable** command takes effect.


Example
-------

# Enable the Option 82 function for the DHCP relay agent on 100GE1/0/1
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp select relay
[*HUAWEI-100GE1/0/1] dhcp relay information enable

```