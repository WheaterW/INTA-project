isis dis-name
=============

isis dis-name

Function
--------



The **isis dis-name** command configures a name for the Designated Intermediate System (DIS).

The **undo isis dis-name** command deletes the name configured for the DIS.



By default, no name is configured for DIS.


Format
------

**isis dis-name** *symbolic-name*

**undo isis dis-name**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *symbolic-name* | Specifies a name for the DIS. | The value is a string of 1 to 64 characters. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

For easy identification and memorization, you can run the **isis dis-name** command to configure a DIS name.

**Prerequisites**

An IS-IS process has been created, and the IS-IS process has been enabled on a specified broadcast interface.

**Configuration Impact**

If the local device is the DIS, the DIS name can be associated with a system ID, and the DIS name can be advertised through pseudonode LSPs.

**Precautions**

The **isis dis-name** command takes effect only on the DIS.If you run the **isis circuit-type** command to simulate a broadcast interface as a P2P interface, the **isis dis-name** command cannot be executed on this interface. If you run the **undo isis circuit-type** command to restore the interface to a broadcast interface, the **isis dis-name** command can be executed on this interface.


Example
-------

# Configure a name for the DIS.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis dis-name LOCALAREA

```