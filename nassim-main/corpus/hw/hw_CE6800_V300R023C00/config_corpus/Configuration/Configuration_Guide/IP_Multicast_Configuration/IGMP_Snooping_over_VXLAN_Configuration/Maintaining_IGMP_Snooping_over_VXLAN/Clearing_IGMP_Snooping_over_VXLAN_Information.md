Clearing IGMP Snooping over VXLAN Information
=============================================

Clearing IGMP Snooping over VXLAN Information

#### Context

![](public_sys-resources/notice_3.0-en-us.png) 

* After static entries are cleared, they cannot be automatically restored. In this case, static member ports need to be configured using commands again.
* If dynamic entries are cleared, hosts in a BD will temporarily fail to receive the multicast traffic that depends on the entries. This problem persists until hosts send IGMP Report messages and the device generates forwarding entries again. Therefore, exercise caution when clearing dynamic entries.
* After IGMP snooping over VXLAN statistics are cleared, they cannot be restored. Therefore, exercise caution when clearing such statistics.
* Deleting port information entries of multicast groups on a dot1q interface may temporarily interrupt multicast traffic received by hosts connected to this interface. Therefore, exercise caution when clearing such entries.

**Table 1** 
| Operation | Command |
| --- | --- |
| Clear the configuration of statically adding a Layer 2 sub-interface to a multicast group. | 1. Enter the system view.    ```    [system-view](cmdqueryname=system-view)    ``` 2. Enter the Layer 2 sub-interface view.    ```    [interface](cmdqueryname=interface) interface-type interface-number.subnum mode l2    ``` 3. Enter the BD view.    ```    [bridge-domain](cmdqueryname=bridge-domain) bd-id    ``` 4. Cancel the configuration of statically adding the Layer 2 sub-interface to a multicast group.    ```    [undo igmp snooping static-group](cmdqueryname=undo+igmp+snooping+static-group) [ source-address source-ip-address ] group-address { group-ip-address | all } [ dot1q vid vid | qinq pe-vid pe-vid ce-vid ce-vid ]    ``` 5. Commit the configuration.    ```    [commit](cmdqueryname=commit)    ``` |
| Clear dynamic outbound ports in multicast outbound port information in the BD. | **reset igmp snooping group bridge-domain** { *BdId* | **all** } |
| Clear IGMP snooping over VXLAN statistics. | [**reset igmp snooping statistics**](cmdqueryname=reset+igmp+snooping+statistics) **bridge-domain** { **all** | *bd-id* } |
| Clear port information entries of multicast groups on a dot1q interface. | [**reset igmp snooping qinq-group**](cmdqueryname=reset+igmp+snooping+qinq-group) { **all** | **interface** { *interface-type* *interface-number* | *interface-name* } [ **pe-vid** *pe-vid* [ *group-address* [ **mask** { *group-mask* | *mask-length* } ] [ *source-address* [ **mask** { *source-mask* | *source-mask-length* } ] ] ] ] } |