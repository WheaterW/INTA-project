IPSG Does Not Take Effect Because It Is Not Enabled on an Interface or in a VLAN
================================================================================

IPSG Does Not Take Effect Because It Is Not Enabled on an Interface or in a VLAN

#### Fault Symptom

Binding entries have been generated, but IPSG does not take effect.

#### Possible Causes

IPSG is not enabled on the specified interface or in the specified VLAN.


#### Procedure

1. Check whether IPSG is enabled on the user-side interface.
   
   
   ```
   [display ip source check user-bind status static](cmdqueryname=display+ip+source+check+user-bind+status+static) [ { interface interface-type interface-number | ip-address ip-address | mac-address mac-address | vlan  vlan-id } * ] [ valid | invalid ] [ slot slot-id ]
   ```
2. If IPSG is not enabled on the interface, check whether IPSG is enabled on the user-side VLAN in the VLAN view.
   
   
   ```
   [display this](cmdqueryname=display+this)
   ```
3. If IPSG is not enabled on the interface or VLAN, that is, **ipv4 source check user-bind enable** is not displayed in the command output, enable IPSG in the interface view or VLAN view.
   
   
   ```
   [ipv4 source check user-bind enable](cmdqueryname=ipv4+source+check+user-bind+enable)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You need to enable IPSG on the interface or in the VLAN. The differences are as follows:
   
   * Enabling IPSG on an interface: IPSG checks all packets received by the interface against binding entries. Use this method if you want to perform an IPSG check on specified interfaces and trust other interfaces. This method is suitable for scenarios in which an interface belongs to multiple VLANs, because it eliminates the need to enable IPSG in each VLAN.
   * Enabling IPSG in a VLAN: IPSG checks the packets received by all interfaces in the VLAN against binding entries. Use this method if you want to perform an IPSG check in specified VLANs and trust other VLANs. This method is suitable for scenarios in which multiple interfaces belong to the same VLAN, because it eliminates the need to enable IPSG on each interface.
   
   IPSG takes effect only on the interface or in the VLAN where it is enabled, and an IPSG check will not be performed on the IPSG-disabled interfaces or in the IPSG-disabled VLANs. As such, if IPSG does not take effect on an interface or in a VLAN, it may not be enabled on this interface or in this VLAN.