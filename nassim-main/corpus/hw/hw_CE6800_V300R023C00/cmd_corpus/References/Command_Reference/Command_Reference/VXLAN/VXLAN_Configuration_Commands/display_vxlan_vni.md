display vxlan vni
=================

display vxlan vni

Function
--------



The **display vxlan vni** command displays VXLAN configurations.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vxlan vni** [ *vni-id* [ **verbose** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies a VNI ID. | The value is an integer ranging from 1 to 16777215. |
| **verbose** | Displays detailed configurations of the VXLAN with a specified VNI ID. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After a VXLAN is configured, to check the VNI status and BD to which the VNI is mapped, run the **display vxlan vni** command. The command output helps you determine whether the VXLAN is correctly configured.

**Precautions**

* Before running the **display vxlan vni** command, ensure that the specified VNI exists. Otherwise, the information obtained will be inapplicable.
* If both ingress replication and another replication are configured in a VSI, the mode for forwarding BUM packets is displayed as another replication in the command output.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed configurations of the VXLAN with VNI 5010.
```
<HUAWEI> display vxlan vni 5010 verbose
    BD ID                  : 10
    State                  : up
    NVE                    : 1610612739
    Source Address         : 1.1.1.1
    Source IPv6 Address    : -
    UDP Port               : 4789
    BUM Mode               : head-end
    Group Address          : -
    Peer List              : 2.2.2.2 2.2.2.3
    IPv6 Peer List         : -

```

# Display VXLAN configurations.
```
<HUAWEI> display vxlan vni
Number of vxlan vni: 2
VNI            BD-ID            State
---------------------------------------
5010           10               up
5020           20               up

```

**Table 1** Description of the **display vxlan vni** command output
| Item | Description |
| --- | --- |
| BD ID | ID of the BD to which a VNI is mapped. |
| State | VNI status:   * up. * down.   The VNI status is Up only when the VXLAN tunnel corresponding to the VNI exists and is Up.  If the VNI status is Down, check whether the values of the Source and Peer List Destination fields in the command output are the same as those of the Source and Destination fields in the display vxlan tunnel command:   * If they are different, the VXLAN tunnel corresponding to the specified VNI does not exist.   Run the source ip-address or vni <vni-id> head-end peer-list command to change the source or destination IP address of the VXLAN tunnel to ensure that the VXLAN tunnel exists.   * If they are the same, collect related configuration information and contact technical support personnel. |
| NVE | NVE interface index, which is automatically generated when an NVE interface is created using the interface nve command. This index is used only for internal query. |
| Source Address | Source VTEP's IP address, which can be configured using the source ip-address command. |
| Source IPv6 Address | IPv6 address of the source VTEP. |
| IPv6 Peer List | IPv6 address of the remote VTEP.  When BUM Mode is flood-vtep replication or multicast replication, the field is not displayed in the command output. |
| UDP Port | Destination UDP port number, which is fixed at 4789. |
| BUM Mode | Broadcast, unknown unicast, and multicast mode.  head-end: A VXLAN tunnel forwards BUM packets using the ingress replication mode.  flood-vtep replication: A VXLAN tunnel forwards BUM packets using the centralized replication mode.  multicast replication: A VXLAN tunnel forwards BUM packets in multicast replication mode. |
| Group Address | Group address mode, which allows a VNI to use multicast replication to forward BUM packets.  This field displays as a hyphen (-) because multicast replication is not supported. |
| Peer List | IP address of a remote VTEP, which can be configured or changed using the vni <vni-id> head-end peer-list command.  This field is not displayed when BUM Mode is flood-vtep replication or multicast replication.  To view the centralized replication list containing IP addresses of the remote VTEPs, run the display vxlan flood-vtep command. |
| Number of vxlan vni | Number of VNIs configured. |
| VNI | VNI ID, which can be configured using the vxlan vni <vni-id> command. |
| BD-ID | BD ID associated with a VNI, which is configured using the bridge-domain <bd-id> command. |