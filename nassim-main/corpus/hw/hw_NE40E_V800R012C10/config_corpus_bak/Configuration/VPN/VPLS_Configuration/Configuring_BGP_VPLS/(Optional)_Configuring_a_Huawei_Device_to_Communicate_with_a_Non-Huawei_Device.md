(Optional) Configuring a Huawei Device to Communicate with a Non-Huawei Device
==============================================================================

(Optional)_Configuring_a_Huawei_Device_to_Communicate_with_a_Non-Huawei_Device

#### Context

To enable a Huawei device to communicate with a non-Huawei device, disable the VSI MTU check.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The VSI view is displayed.
3. Run [**pwsignal**](cmdqueryname=pwsignal) **bgp**
   
   
   
   The VSI-BGP view is displayed.
4. Run [**mtu-negotiate disable**](cmdqueryname=mtu-negotiate+disable)
   
   
   
   The VSI MTU check is disabled.
   
   
   
   If the MTUs of the same VSI on two PEs are different, the two PEs cannot exchange information or establish a connection.
   
   To enable a Huawei device to communicate with non-Huawei devices that do not support the VSI MTU check on a BGP VPLS network, run the [**mtu-negotiate disable**](cmdqueryname=mtu-negotiate+disable) command to disable the VSI MTU check on the Huawei device.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.