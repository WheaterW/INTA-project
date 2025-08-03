peer (VNI view)
===============

peer (VNI view)

Function
--------



The **peer** command creates and displays the VNI peer view.

The **undo peer** command deletes the configured VNI peer view.



By default, no VNI peer view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIp*

**undo peer** *peerIp*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIp* | Specifies the IP address of a peer network virtualization edge. | The address is in dotted decimal notation. |



Views
-----

VNI view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set attributes for a specified peer VNI in the VNI peer view, run the peer command to create and display the VNI peer view.

**Follow-up Procedure**

Run the **description** command to configure a description for a peer VXLAN tunnel.


Example
-------

# Create the VNI peer view with the VNI ID of 4096 and the peer IP address of 1.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] vni 4096
[*HUAWEI-vni4096] peer 1.1.1.1

```