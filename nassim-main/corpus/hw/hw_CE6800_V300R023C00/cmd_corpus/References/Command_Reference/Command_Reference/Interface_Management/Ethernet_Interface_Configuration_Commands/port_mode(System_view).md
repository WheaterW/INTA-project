port mode(System view)
======================

port mode(System view)

Function
--------



The **port mode** command sets the rate of an interface to that of the optical module installed on the interface.

The **undo port mode** command restores the default interface rate.



By default, a 25GE interface works at the rate of 25 Gbit/s after it has a 25GE optical module installed and does not go Up after it has a 50GE optical module installed; a 100GE interface works at the rate of 100 Gbit/s after it has a 100GE optical module installed and does not go Up after it has a 200GE optical module installed.


Format
------

**port mode 50GE interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-18>

**port mode 200GE interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-18>

**undo port mode 50GE interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-18>

**undo port mode 200GE interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-18>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name1* | Specifies an interface name. | - |
| *interface-type1* | Specifies an interface type. | The value can be:   * 25GE * 100GE |
| *interface-number1* | Specifies an interface number. | - |
| **to** | The to keyword specifies an interface range that includes all interfaces between these two interfaces. You can omit the space between interface-type and interface-number when entering the command. | - |
| *interface-name2* | Specifies an interface name. | - |
| *interface-type2* | Specifies an interface type. | The value can be:   * 25GE * 40GE * 100GE |
| *interface-number2* | Specifies an interface number. | - |
| **200GE** | Configures a 100GE interface to work at the rate of 200 Gbit/s. | - |
| **interface** | Indicates an interface. | - |
| **50GE** | Configures a 25GE interface to work at the rate of 50 Gbit/s. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The forty-eight 25GE interfaces on the CE6885, CE6885-T, CE6885-LL, CE6885-SAN, CE6863E-48S8CQ, CE6866, CE6860-HAM, CE6866K or CE6860-SAN are divided into six interface groups based on the interface numbers: interfaces 1 to 8, interfaces 9 to 16, interfaces 17 to 24, interfaces 25 to 32, interfaces 33 to 40, and interfaces 41 to 48. By default, these 25GE interfaces work at the rate of 25 Gbit/s. To configure the 25GE interfaces to work at the rate of 50 Gbit/s, run the port mode 50ge command. If the rate of an interface is switched from 25 Gbit/s to 50 Gbit/s and then a 25GE optical module is installed on the interface, the interface is backward compatible with the rate of 25 Gbit/s.The eight 100GE interfaces on the CE6885, CE6885-T, CE6885-LL, CE6855-48XS8CQ, CE6885-SAN, CE6863E-48S8CQ are divided into four interface groups based on the interface numbers: interfaces 1 and 2, interfaces 3 and 4, interfaces 5 and 6, and interfaces 7 and 8. By default, these 100GE interfaces work at the rate of 100 Gbit/s. To configure the 100GE interfaces to work at the rate of 200 Gbit/s, run the port mode 200ge command. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 40GE optical module is installed on the interface, the interface is backward compatible with the rate of 40 Gbit/s. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 100GE optical module is installed on the interface, the interface is backward compatible with the rate of 100 Gbit/s.The eight 100GE interfaces on the CE6866, CE6860-HAM, CE6866K, CE6860-SAN are divided into two interface groups based on the interface numbers: interfaces 1 to 4 and interfaces 5 to 8. By default, these 100GE interfaces work at the rate of 100 Gbit/s. To configure the 100GE interfaces to work at the rate of 200 Gbit/s, run the port mode 200ge command. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 40GE optical module is installed on the interface, the interface is backward compatible with the rate of 40 Gbit/s. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 100GE optical module is installed on the interface, the interface is backward compatible with the rate of 100 Gbit/s.The eight 100GE interfaces on the CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K or CE8850-SAN are divided into sixteen interface groups based on the interface numbers: interfaces 1 to 2, interfaces 3 to 4, interfaces 5 to 6, interfaces 7 to 8, interfaces 9 to 10, interfaces 11 to 12, interfaces 13 to 14, interfaces 15 to 16, interfaces 17 to 18, interfaces 19 to 20, interfaces 21 to 22, interfaces 23 to 24, interfaces 25 to 26, interfaces 27 to 28, interfaces 29 to 30, and interfaces 31 to 32. By default, these 100GE interfaces work at the rate of 100 Gbit/s. To configure the 100GE interfaces to work at the rate of 200 Gbit/s, run the port mode 200ge command. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 40GE optical module is installed on the interface, the interface is backward compatible with the rate of 40 Gbit/s. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 100GE optical module is installed on the interface, the interface is backward compatible with the rate of 100 Gbit/s.The last four 100GE interfaces on the CE8855, CE8851-32CQ4BQ are divided into two interface groups: one containing interfaces 33 and 34, and the other containing interfaces 35 and 36. By default, these 100GE interfaces work at the rate of 100 Gbit/s. To configure the 100GE interfaces to work at the rate of 200 Gbit/s, run the port mode 200ge command. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 40GE optical module is installed on the interface, the interface is backward compatible with the rate of 40 Gbit/s. If the rate of an interface is switched from 100 Gbit/s to 200 Gbit/s and then a 100GE optical module is installed on the interface, the interface is backward compatible with the rate of 100 Gbit/s.If the rate of any interface in an interface group is switched, all other interfaces in the interface group automatically work at the target rate. If the to keyword is used in the command to specify an interface range, the target rate applies to all interfaces in the range.



**Precautions**



After you run the **port mode** command to switch the interface rate, all configurations on the interface are deleted. Therefore, exercise caution when running this command.After you run this command to switch the interface rate, the original interface number does not exist. For example, if you configure 100GE1/0/1 to work at the rate of 200 Gbit/s, the original interface number 100GE1/0/1 changes to 200GE1/0/1. To enter the interface view, run the interface 200GE1/0/1 command.After an interface is added to an Eth-Trunk interface, you cannot run the **port mode** or **undo port mode** command to change the interface rate. To change the interface rate, remove the interface from the Eth-Trunk interface and then change the interface rate.After a sub-interface is created on an interface, you cannot run the **port mode** or **undo port mode** command to switch the interface rate. To change the interface rate, delete the sub-interface and then change the interface rate.The remote interfaces must work at the same rate.The CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H and CE6881H-K do not support this command.




Example
-------

# Set the rate of 100GE1/0/1 to 200 Gbit/s.
```
<HUAWEI> system-view
[~HUAWEI] port mode 200GE interface 100GE 1/0/1
Warning: This operation will delete current port(100GE1/0/1 to 100GE1/0/2) and all configurations of the current port(s) will be cleared, Continue? [Y/N]:y

```