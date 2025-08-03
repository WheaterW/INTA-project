Configuring a MAC Address Learning Limit Rule
=============================================

Configuring a MAC address learning limit rule can control the number of access users. If the number of learned MAC addresses reaches the maximum number, no additional MAC addresses will be learned. In addition, the packet discarding and alarm functions can be configured to prevent MAC address attacks and improve network security.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before configuring a MAC address learning limit rule, run the [**reset mac-address**](cmdqueryname=reset+mac-address) command to clear the learned MAC addresses to ensure that the number of MAC addresses that can be learned is limited accurately.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform one or more of the following configurations as required.
   
   
   * Configure a MAC address learning limit rule on an interface to control the number of users connected to the interface. Choose one of the following configuration modes:
     
     **Table 1** Configuring a MAC address learning limit rule on an interface
     | Configuring a MAC Address Learning Limit Rule | Operation |
     | --- | --- |
     | Specifying a rule name | 1. Run the [**mac-limit rule-name**](cmdqueryname=mac-limit+rule-name) *rule-name* { **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** } | **maximum** *max* [ **rate** *interval* ] } \* command to create the global MAC address learning limit rule. 2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the Ethernet interface view. 3. Run the [**mac-limit rule-name**](cmdqueryname=mac-limit+rule-name) *rule-name* command to apply the global MAC address learning limit rule on the interface. |
     | Without specifying a rule name | 1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view. 2. Run the [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** } | **maximum** *max* } \* command to configure a MAC address learning limit rule. |
   * Configure a MAC address learning limit rule in a VLAN to control the number of users in the VLAN.
     
     1. Run the [**vlan**](cmdqueryname=vlan) *vlan-id* command to enter the VLAN view.
     2. Run the [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** }| **maximum** *maxValue* [ **rate** *interval* ] } \* command to configure a MAC address learning limit rule.
     3. (Optional) Run the [**mac-limit**](cmdqueryname=mac-limit) **up-threshold** *up-threshold* **down-threshold** *down-threshold* command to configure the threshold percentage of MAC addresses that have alarms generated and cleared.
   * Configure a MAC address learning limit rule on an interface in a VLAN to control the number of VLAN users connected to the interface. Choose one of the following configuration modes:
     
     **Table 2** Configuring a MAC address learning limit rule on an interface in a VLAN
     | Configuring a MAC Address Learning Limit Rule | Operation |
     | --- | --- |
     | Specifying a rule name | 1. Run the [**mac-limit rule-name**](cmdqueryname=mac-limit+rule-name) *rule-name* { **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** } | **maximum** *max* [ **rate** *interval* ] } \* command to create the global MAC address learning limit rule. 2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view. 3. Run the [**mac-limit vlan**](cmdqueryname=mac-limit+vlan) *vlan-id1* [ **to** *vlan-id2* ] **rule-name** *rule-name* command to apply the global MAC address learning limit rule to the VLAN to which the interface belongs. |
     | Without specifying a rule name | 1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view. 2. Run the [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** } | **maximum** *maxValue* } \* command to configure a MAC address learning limit rule. |
   * Configure a MAC address learning limit rule in a virtual switching instance (VSI) to control the number of users in the VSI.
     
     1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the VSI view.
     2. Run the [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **maximum** *max* [ **rate** *interval* ] } \* command to configure a MAC address learning limit rule.
     3. Run the [**mac-limit**](cmdqueryname=mac-limit) **up-threshold** *up-threshold* **down-threshold** *down-threshold* command to configure alarm rising and falling thresholds for MAC address learning.
   * Configure a MAC address learning limit rule on a pseudo wire (PW) to control the number of users on the PW.
     
     1. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the VSI view.
     2. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to enter the VSI LDP view.
     3. Run the [**vsi-id**](cmdqueryname=vsi-id) *vsi-id* command to configure the VSI ID.
     4. Run the [**peer**](cmdqueryname=peer) *peer-address* command to configure the IPv4 address of a VSI peer.
     5. Run the [**peer**](cmdqueryname=peer) *peer-address* **pw** *pw-name* command to create a PW.
     6. Run the [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **alarm** { **disable** | **enable** } | **maximum** *maxValue* [ **rate** *interval* ] } \* command to configure a MAC address learning limit rule.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.