Setting a Timeout Period for DAD Messages
=========================================

If many VLANs are configured on a VLAN tag termination sub-interface, DAD messages may fail to be transmitted within the default timeout period (1s). To resolve this issue, run the [**ipv6 nd dad timeout**](cmdqueryname=ipv6+nd+dad+timeout) command to prolong the timeout period for DAD messages.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subinterface-number*
   
   
   
   The view of the sub-interface where a timeout period needs to be set for DAD messages is displayed.
3. Run **ipv6 enable**
   
   
   
   IPv6 is enabled.
4. Run [**ipv6 nd dad timeout**](cmdqueryname=ipv6+nd+dad+timeout) *value*
   
   
   
   A timeout period is set for DAD messages.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.