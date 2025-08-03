Failed to Establish an IPv6 IS-IS Neighbor Relationship
=======================================================

Failed to Establish an IPv6 IS-IS Neighbor Relationship

#### Fault Symptom

An IPv6 IS-IS neighbor relationship fails to be established when the link runs properly.


#### Possible Causes

1. The IS-IS levels of the devices at both ends of the link do not match.
2. The area addresses of the devices at both ends of the link do not match.
3. The authentication configurations of the devices at both ends of the link do not match.

#### Procedure

1. Check that the IS-IS levels of the devices at both ends of the link match.
   
   
   * Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **isis** | **include is-level** command to check the IS-IS level configurations of IS-IS processes at both ends.
   * Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** *interface-type* *interface-number* | **include isis circuit-level** command to check the IS-IS level configurations of involved interfaces at both ends.
   
   An IS-IS neighbor relationship can be established only if IS-IS levels of the devices at both ends of the link match.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If no interface level is displayed in the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** *interface-type* *interface-number* | **include isis circuit-level** command output, the interface level is the default level. To view the default level, run the [**display default-parameter isis**](cmdqueryname=display+default-parameter+isis) command to check the **Circuit-Level** field.
   
   The IS-IS levels of interfaces at both ends must match as follows:
   * If the level of the local interface is **Level-1**, the level of the peer interface must be **Level-1** or **Level-1-2**.
   * If the level of the local interface is **Level-2**, the level of the peer interface must be **Level-2** or **Level-1-2**.
   * If the level of the local interface is **Level-1-2**, the level of the peer interface can be **Level-1**, **Level-2**, or **Level-1-2**.
   
   If the levels of devices at both ends do not match, perform the following operations as required:
   * Run the [**is-level**](cmdqueryname=is-level) command in the IS-IS view to change the global IS-IS level.
   * Run the [**isis circuit-level**](cmdqueryname=isis+circuit-level) command in the interface view to change the interface IS-IS level.
2. Check that area addresses of the devices at both ends of the link match.
   
   
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **isis** command to check area address information.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If an IS-IS Level-1 neighbor relationship needs to be established between two devices, they must reside in the same area.
   
   A maximum of three area addresses can be configured for an IS-IS process. Devices at both ends can establish an IS-IS Level-1 neighbor relationship as long as the two devices have one area address in common.
   
   If an IS-IS Level-2 neighbor relationship needs to be established between two devices, they do not check area address consistency.
   
   If the area addresses of the two devices are different, run the [**network-entity**](cmdqueryname=network-entity) command in the IS-IS view on either end to ensure that the two devices have one area address in common.
3. Check that authentication configurations of the devices at both ends of the link match.
   
   
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** *interface-type* *interface-number* | **include isis authentication-mode** command to check the IS-IS authentication configurations of the interfaces on both ends of the link.
   
   If the two interfaces use different authentication modes, run the [**isis authentication-mode**](cmdqueryname=isis+authentication-mode) command in the view of one interface to ensure that this interface has the same authentication mode and password as those on the other interface.