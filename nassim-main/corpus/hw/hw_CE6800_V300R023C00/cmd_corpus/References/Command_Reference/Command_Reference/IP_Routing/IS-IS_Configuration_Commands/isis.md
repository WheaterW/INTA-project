isis
====

isis

Function
--------



The **isis** command starts an IS-IS process and specifies a VPN instance.

The **undo isis** command deletes an IS-IS process.



By default, an IS-IS process runs in a public network instance.


Format
------

**isis** *process-id* [ **vpn-instance** *vpn-instance-name* ]

**isis** [ **vpn-instance** *vpn-instance-name* ]

**undo isis** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The·value·is·an·integer·ranging·from·1·to·4294967295.·The·default·value·is·1. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure other functions and features of IS-IS or IS-IS interfaces, you need to enable IS-IS first. You can enter the IS-IS view after the **isis** command is run.On a large-scale network, if a large number of devices run IS-IS, there will be a huge number of routes, increasing maintenance costs, slowing down route convergence, and affecting network stability. To resolve the problem, you can run the **isis** command to start multiple processes to reduce the number of routes to be maintained.In addition, to ensure that different services are forwarded properly on the network, you can run the **isis** command to start multiple IS-IS processes on one device to isolate these services.

**Follow-up Procedure**



Run the **network-entity** command to set a NET for the device, and run the **isis enable** command to enable IS-IS on each interface that needs to run IS-IS. You can start IS-IS only when these configurations are completed.



**Precautions**

The **undo isis** command deletes all configurations of a specified IS-IS process. Exercise caution when running this command.


Example
-------

# Start an IS-IS process 1 which has the system ID 0000.0000.0002 and the area ID 01.0001.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 01.0001.0000.0000.0002.00

```