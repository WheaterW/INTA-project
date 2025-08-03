trace object
============

trace object

Function
--------



The **trace object** command creates a diagnosis object.

The **undo trace object** command deletes a diagnosis object.



By default, no diagnosis object is created. If you do not specify the direction at which information is exported, the default direction is the CLI.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**trace object** { **mac-address** *mac-address* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] } \* [ **output** { **command-line** | **file** *file-name* | **syslog-server** *syslog-server-ip* } ]

**undo trace object** { **mac-address** *mac-address* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] } \* [ **output** { **command-line** | **file** [ *file-name* ] | **syslog-server** [ *syslog-server-ip* ] } ]

**undo trace object** { *service-object-id* | **all** }

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**trace object** { **mac-address** *mac-address* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **interface** { *interface-name* | *interface-type* *interface-number* } | **user-vlan** *user-vlan-id* | **user-name** *username* } \* [ **output** { **command-line** | **file** *file-name* | **syslog-server** *syslog-server-ip* } ]

**undo trace object** { **mac-address** *mac-address* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **interface** { *interface-name* | *interface-type* *interface-number* } | **user-vlan** *user-vlan-id* | **user-name** *username* } \* [ **output** { **command-line** | **file** [ *file-name* ] | **syslog-server** [ *syslog-server-ip* ] } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mac-address** *mac-address* | Creates a diagnosis object based on the MAC address. | The value is in the format of H-H-H, in which each H is a hexadecimal number of 1 to 4 digits, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **ip-address** *ip-address* | Creates a diagnosis object based on an IP address. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **interface** | Creates a diagnosis object by interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| *interface-name* | Specifies the name of an interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| *interface-type* | Specifies the type of an interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| *interface-number* | Specifies an interface number.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **user-vlan** *user-vlan-id* | Creates a diagnosis object based on a user VLAN.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer in the range from 1 to 4094. |
| **user-name** *username* | Creates a diagnosis object by user name.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is a string of 1 to 253 case-insensitive characters, spaces not supported. |
| **output** | Specifies the direction in which diagnostic information is exported. | - |
| **command-line** | Exports diagnostic information to the CLI. | - |
| **file** *file-name* | Exports diagnostic information to a specified file. | file-name specifies the file name. The value is a string of 1 to 255 case-insensitive characters without spaces. |
| **syslog-server** *syslog-server-ip* | Exports diagnosis information to a log server. | The value is in dotted decimal notation. |
| *service-object-id* | Deletes a diagnosis object with a specified ID. | The value is an integer that ranges from 0 to 3. |
| **all** | Deletes all diagnosis objects. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When locating faults during user access, maintenance personnel can create diagnosis objects to diagnose services and locate user access faults.You can create diagnosis objects based on user attributes, which vary according to services.

* DHCP service: Create a diagnosis object based on the MAC address.

**Prerequisites**

The service diagnosis function has been enabled using the **trace enable** command.

**Precautions**

Diagnosis objects can be created based on MAC addresses or IP addresses. Generally, various service processes can be diagnosed. If diagnosis objects are created based on other parameters, service diagnosis cannot be performed because other parameters cannot be obtained in service processes. You are advised to create a diagnosis object based on the MAC address or IP address.When different output modes are configured, they do not overwrite each other and take effect at the same time. To configure the terminal display function, run the terminal monitor and terminal debugging commands in the user view.The maximum size of the file to which diagnostic information is exported is 1 MB. When the file size reaches 1 MB, new diagnostic information will not be recorded.You can run the **undo trace object** command to delete a diagnosis object in any of the following ways:

To delete a diagnosis object based on service diagnosis attributes, run the **undo trace object** command. For example, two diagnosis objects have been configured on the device, such as diagnosis object 1 (10.10.10.1) and diagnosis object 2 (10.10.10.1+00e0-fc12-3456). If maintenance personnel want to delete diagnosis objects by IP address, run the undo trace object ip-address 10.10.10.1 command to delete diagnosis objects 1 and 2.To delete a diagnosis object based on the diagnosis object ID, run the **undo trace object service-object-id** command. You can run the **display trace object** command to view the diagnosis object ID.To delete all diagnosis objects, run the **undo trace object all** command.


Example
-------

# Create a diagnosis object on the interface with the MAC address of 00e0-fc12-3456.
```
<HUAWEI> system-view
[~HUAWEI] trace object mac-address 00e0-fc12-3456

```