(Optional) Configuring NETCONF YANG Model Switching
===================================================

You can switch between different NETCONF YANG models.

#### Context

Currently, there are multiple NETCONF YANG models, such as huawei-if-ip.yang and huawei-ip.yang. You can perform the following operations to switch between different models.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**netconf**](cmdqueryname=netconf)
   
   
   
   The NETCONF user interface view is displayed.
3. Run the[**activate module**](cmdqueryname=activate+module) *module-name*
   
   
   
   A NETCONF YANG model is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Multiple models cannot take effect at the same time. When one model is activated, the functions of the other models are disabled.