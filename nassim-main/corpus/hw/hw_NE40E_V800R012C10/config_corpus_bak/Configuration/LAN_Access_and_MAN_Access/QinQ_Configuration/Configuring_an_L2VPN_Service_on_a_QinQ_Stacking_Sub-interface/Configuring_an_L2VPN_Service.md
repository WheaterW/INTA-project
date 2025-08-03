Configuring an L2VPN Service
============================

Layer 2 virtual private network (L2VPN) services include virtual private wire service (VPWS) and virtual private LAN service (VPLS). After you configure QinQ stacking sub-interfaces, bind these sub-interfaces to a virtual switching instance (VSI) or VPWS instance to provide L2VPN access for users.

#### Context

For configuration details, see "VPWS Configuration" and "VPLS Configuration" in *HUAWEI NE40E-M2 series Configuration Guide - VPN*.

If you use QinQ stacking sub-interfaces to provide VPWS access, the number of VLANs on both ends of the VPWS must be the same.

Perform the following steps on the device on which an L2VPN is to be configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface)*interface-type interface-number.subinterface-number*
   
   
   
   The view of the QinQ stacking sub-interface is displayed.
3. Configure a QinQ stacking sub-interface to provide L2VPN access, as shown in [Table 1](#EN-US_TASK_0172363285__tab_1).
   
   
   
   **Table 1** QinQ stacking sub-interfaces providing L2VPN access
   | Service Type | QinQ Stacking Sub-interface Configuration | Description |
   | --- | --- | --- |
   | VPWS | Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \* command to create a VPWS connection. | * **ip-interworking** must be configured when Huawei devices interwork with each other over heterogeneous media. * **ip-layer2** must be configured when Huawei devices interwork with non-Huawei devices over heterogeneous media. |
   | VPLS | Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the VLAN tag termination sub-interface to a VSI. | - |
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run the [**qinq stacking client-mode single**](cmdqueryname=qinq+stacking+client-mode+single) command to enable a QinQ stacking sub-interface to learn the MAC address mapped to the smallest VLAN ID among all VLAN ranges that share the MAC address when the sub-interface accesses VPLS services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.