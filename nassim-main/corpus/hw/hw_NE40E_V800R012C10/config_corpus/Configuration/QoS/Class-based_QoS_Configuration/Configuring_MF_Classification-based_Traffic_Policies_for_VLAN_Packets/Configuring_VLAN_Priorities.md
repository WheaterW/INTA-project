Configuring VLAN Priorities
===========================

This section describes how to configure the VLAN priorities.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
   
   
   
   A traffic behavior is configured and its view is displayed.
3. Perform one of the following operations to re-mark 802.1p values.
   
   
   * To re-mark the 802.1p values in both inner and outer VLAN tags, run the [**remark 8021p**](cmdqueryname=remark+8021p) *8021p-value* command.
   * To re-mark the 802.1p value in either inner or outer VLAN tag, run either of the following commands:
     
     + Run the [**remark inner-8021p**](cmdqueryname=remark+inner-8021p) *8021p-value* command to enable a device to re-mark the 802.1p value in the inner VLAN tag of double-tagged VLAN packets.
     + Run the [**remark outer-8021p**](cmdqueryname=remark+outer-8021p) *8021p-value* command to enable a device to re-mark the 802.1p value in the outer VLAN tag of double-tagged VLAN packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.