port split
==========

port split

Function
--------



The **port split** command splits a specified interface.

The **undo port split** command cancels the split configuration on a specified interface.



By default, an interface is not split.


Format
------

**port split dimension interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-24> [ **split-type** *split-type* ]

**undo port split dimension interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-24> [ **split-type** *split-type* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name1* | Specifies the name of the start interface. | You can enter a question mark (?) and select a value based on the prompt. |
| *interface-type1* | Specifies the type of a start interface. | You can enter a question mark (?) and select a value based on the prompt. |
| *interface-number1* | Specifies the number of a start interface. | You can enter a question mark (?) and select a value based on the prompt. |
| **to** | The keyword to specifies an interface range that includes all interfaces between these two interfaces. These interfaces must be of the same type. | - |
| *interface-name2* | Specifies the name of the end interface. | The value of interface-number2 must not be less than that of interface-number1. |
| *interface-type2* | Specifies the type of an end interface. | You can enter a question mark (?) and select a value based on the prompt. |
| *interface-number2* | Specifies the number of an end interface. | You can enter a question mark (?) and select a value based on the prompt. |
| **split-type** *split-type* | Specifies the interface split type. | You can enter a question mark (?) and select a value from the displayed value range. A 100GE interface supports four 25GE or two 50GE interfaces. A 200GE interface supports two 100GE or four 50GE interfaces. A 400GE interface supports four 100GE or two 200GE interfaces. |
| **undo** | Cancels current configuration. | - |
| **port** | Specifies a port. | - |
| **split** | Indicates port splitting. | - |
| **dimension** | Indicates that converted interfaces are numbered using the dimension numbering rule. | - |
| **interface** | Specifies an interface. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The interface split function allows a high-bandwidth physical interface on the device to be split into multiple independent low-bandwidth interfaces. A high-bandwidth interface on the device can be split into multiple low-bandwidth interfaces or directly used based on the interface type on the remote device. The interface split function allows for flexible networking and lowers hardware costs.Converted interfaces are numbered using the dimension numbering rule. For example, after 100GE 1/0/1 is split into four 25GE interfaces, the 25GE interfaces are still in the 100GE interface view and are numbered 100GE 1/0/1:1, 100GE 1/0/1:2, 100GE 1/0/1:3, and 100GE 1/0/1:4.Dynamic interface split indicates that interfaces take effect after being split without the need of restarting the device. Currently, all devices support dynamic interface split.You can check whether dynamic interface split is supported according to the displayed message. When the **port split** command is run, if the message "Warning: This operation will delete current port(s) and create new port(s). New port(s) will be offline before the board of slot 1 is reset." is displayed, you need to restart the device to make converted interfaces take effect; if the message "Warning: This operation will delete current port(s) and all configurations of the current port(s) will be cleared. After the operation is done, it may take a few seconds before viewing the port information." is displayed, converted interfaces can directly take effect without the need of restarting the device.



**Precautions**



After interface split or interface split is canceled, the original interface does not exist and the configuration on the original interface is lost. If you run the **rollback configuration** command to roll back the configuration to the status before interface split, the configuration on the original interface cannot be restored. You need to manually configure the interface again. Exercise caution when performing this operation.After an interface is added to an Eth-Trunk interface or a sub-interface is created on the interface, the interface cannot be split or canceled.The CE6820H, CE6820S, CE6863H, and CE6881H do not support this command.You are advised to use the Interface Split Query Tool to query the interface split procedure, cables and optical modules used after interface split, precautions, and FAQs. Interface split query tool: https://info.support.huawei.com/network/ptmngsys/Web/interface\_split\_tool/cn/index.html.




Example
-------

# Split a 100GE interface into four 25GE interfaces and display the converted interface view.
```
<HUAWEI> system-view
[~HUAWEI] port split dimension interface 100GE 1/0/1 split-type 4*25GE

```