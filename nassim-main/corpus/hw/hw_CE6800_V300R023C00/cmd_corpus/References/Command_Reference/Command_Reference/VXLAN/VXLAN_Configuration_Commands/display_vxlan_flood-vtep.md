display vxlan flood-vtep
========================

display vxlan flood-vtep

Function
--------



The **display vxlan flood-vtep** command displays information about a VXLAN centralized replication list.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vxlan flood-vtep** [ **vni** *vni-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vni** *vni-id* | Displays information about a VXLAN centralized replication list of a specified VNI ID. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Data packets entering a VXLAN tunnel can be forwarded using the centralized replication mode. Centralized replication means that a centralized replication list containing multiple remote VTEP IP addresses is configured using the **vni flood-vtep** command. Among the remote VTEP IP addresses, only one is in the working state, and others are in the backup state.To check information about the VXLAN centralized replication list, run the **display vxlan flood-vtep** command. The information includes the VNI, source and destination VTEP IP addresses, configuration mode of the centralized replication list, and working status of the remote VTEP IP addresses.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the VXLAN centralized replication list.
```
<HUAWEI> display vxlan flood-vtep
Number of peers : 7
Vni ID    Source             Destination       Type       Status
----------------------------------------------------------------------
1         1.1.1.1            1.1.1.3           static     primary          
1         1.1.1.1            1.1.1.4           static     backup           
2         1.1.1.1            1.1.1.4           static     primary          
2         1.1.1.1            1.1.1.5           static     backup           
3         1.1.1.1            1.1.1.6           static     primary          
3         1.1.1.1            1.1.1.7           static     backup           
3         1.1.1.1            1.1.1.8           static     backup

```

**Table 1** Description of the **display vxlan flood-vtep** command output
| Item | Description |
| --- | --- |
| Number of peers | Number of remote VTEPs in the centralized replication list. |
| Vni ID | VNI ID, which is configured using the vxlan vni vni-id command. |
| Source | Source VTEP's IP address, which can be configured using the source ip-address command. |
| Destination | Destination VTEP's IP address, which can be configured using the vni vni-id flood-vtep ip-address &<1-10> command. |
| Type | Configuration mode of the centralized replication list. The value can only be static, meaning manual configuration. |
| Status | Status of a remote VTEP:   * primary: working state. * backup: backup state. |