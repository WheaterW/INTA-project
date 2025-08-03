snmp-agent local-engineid
=========================

snmp-agent local-engineid

Function
--------



The **snmp-agent local-engineid** command sets an engine ID for a local SNMP agent.

The **undo snmp-agent local-engineid** command restores the engine ID of a local SNMP agent to the default value.



By default, the system uses an internal algorithm to automatically generate an engine ID that consists of an enterprise number and device information.


Format
------

**snmp-agent local-engineid** *engineid*

**undo snmp-agent local-engineid**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local-engineid** *engineid* | Specifies the engine ID of a local SNMP agent. | The value is a string of 10 to 64 hexadecimal characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Each device managed by the NMS needs only one engine ID to identify an SNMP agent. By default, each device has one engine ID. The network administrator needs to ensure that every engine ID in a domain is unique. Communication between the NMS and SNMP agent can be authenticated and encrypted using this engine ID.The **snmp-agent local-engineid** command configures the engine ID of a local SNMP entity. The algorithm for generating the engine ID follows the following rules:

* The first four bytes are the vendor's private engine ID allocated by the Internet Assigned Numbers Authority (IANA). The engine ID of Huawei devices is 2011 in decimal notation. The first binary digit has a fixed value 1. Therefore, the engine ID in hexadecimal format is 800007DB.
* The device information can be configured manually. It is recommended that the IP address or MAC address of the device be used as the device information to uniquely identify the device.Note:If a local engine ID is configured or changed, information about existing SNMPv3 users is deleted.

**Configuration Impact**

The password summary used by an SNMPv3 user is calculated using MD5 or SHA based on the user password and engine ID of a local SNMP agent. If the engine ID of the local SNMP agent is changed, the generated password summary becomes invalid. As a result, a new password summary needs to be generated for the SNMPv3 user.

**Precautions**

* The default engine ID is saved in the configuration file. Restarting the device or replacing the main control board does not change the engine ID.
* If snmp-agent local-engineid is configured, the configured value is used as the engine ID of the device.
* After SNMP is enabled using the **snmp-agent** command, the system automatically generates a local engine ID. The default value is used.


Example
-------

# Set the engine ID of a local SNMP agent to 800007DB03360102101100.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent local-engineid 800007DB03360102101100

```