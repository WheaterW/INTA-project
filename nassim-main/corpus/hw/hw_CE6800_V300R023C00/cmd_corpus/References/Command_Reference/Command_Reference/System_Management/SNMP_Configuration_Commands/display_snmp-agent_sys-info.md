display snmp-agent sys-info
===========================

display snmp-agent sys-info

Function
--------



The **display snmp-agent sys-info** command displays system information on an existing SNMP device. The information includes contact information about the system maintenance, the physical location of the device, and the SNMP version.




Format
------

**display snmp-agent sys-info** [ **contact** | **location** | **version** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **contact** | Displays contact information on an existing SNMP device. | - |
| **location** | Displays physical location information of an existing SNMP device. | - |
| **version** | Displays the SNMP version running on an existing device. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view the contact information about the system maintenance, physical location of the device, and SNMP version, run the **display snmp-agent sys-info** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display system information on an SNMP agent.
```
<HUAWEI> display snmp-agent sys-info
   The contact person for this managed node:
           R&D Beijing, *** Technologies co.,Ltd.
   The physical location of this node:
           Beijing China
   SNMP version running in the system:
           SNMPv3

```

# Display physical location information on an existing SNMP device.
```
<HUAWEI> display snmp-agent sys-info location
   The physical location of this node:
           Beijing China

```

# Display the contact information of an existing SNMP device.
```
<HUAWEI> display snmp-agent sys-info contact
  The contact person for this managed node:
           R&D Beijing, *** Technologies co.,Ltd.

```

# Display the SNMP version running on an existing device.
```
<HUAWEI> display snmp-agent sys-info version
   SNMP version running in the system:
           SNMPv3

```

**Table 1** Description of the **display snmp-agent sys-info** command output
| Item | Description |
| --- | --- |
| The contact person for this managed node | Contact person of a managed device. |
| The physical location of this node | Location of the managed device. |
| SNMP version running in the system | SNMP version running on the managed device: SNMPv1 SNMPv2c SNMPv3. |