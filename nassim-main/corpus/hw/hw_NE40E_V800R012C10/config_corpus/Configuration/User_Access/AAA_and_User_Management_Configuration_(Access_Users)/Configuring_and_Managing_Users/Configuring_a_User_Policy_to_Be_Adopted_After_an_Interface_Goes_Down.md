Configuring a User Policy to Be Adopted After an Interface Goes Down
====================================================================

Configuring a User Policy to Be Adopted After an Interface Goes Down

#### Context

When an interface goes down due to an interface or direct link fault, the users on the interface are logged out. After the fault is rectified, the interface goes up, and users go online again. If an interface frequently alternates between up and down due to an interface or direct link fault, the users also frequently go online and offline through the interface. To address this problem, run the [**user-policy interface-down**](cmdqueryname=user-policy+interface-down) command to configure a user policy to be adopted when an interface goes down. The policy can be forcibly logging out the users or keeping them online.


#### Procedure

* In the system view, configure a user policy to be adopted when an interface goes down.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**user-policy interface-down**](cmdqueryname=user-policy+interface-down) { **offline** | **online** }
     
     A policy is configured and applied to online users when the BAS interface goes down. The policy can be forcibly logging out the users or keeping them online.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* In the interface view, configure a user policy to be adopted when an interface goes down.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ *.subinterface-number* ]
     
     The interface view is displayed.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
  4. Run [**bas**](cmdqueryname=bas)
     
     A BAS interface is created and its view is displayed.
  5. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **bas-interface-name** *bname* | **default-domain** { **pre-authentication** *predname* | **authentication** [ **force** | **replace** ] *dname* }\* | **accounting-copy** **radius-server** *rd-name* ]\*
     
     The access type is set to Layer 2 common users, and related attributes are configured.
     
     Or run [**access-type**](cmdqueryname=access-type) **layer3-subscriber** [ **default-domain** { **pre-authentication** *dname* | **authentication** [ **force** | **replace** ] *dname* }\* ] The access type is set to Layer 3 common users, and related attributes are configured.
  6. Run [**user-policy interface-down**](cmdqueryname=user-policy+interface-down) { **offline** | **online** }
     
     A policy is configured and applied to online users when the BAS interface goes down. The policy can be forcibly logging out the users or keeping them online.
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + If the **user-policy interface-down** command is run in both the system and BAS interface views, the configuration in the BAS interface view determines whether users are logged out when this BAS interface goes down, and the configuration in the system view determines whether users are logged out when other BAS interfaces go down.
  + If the [**user-policy interface-down**](cmdqueryname=user-policy+interface-down) **online** command has been run to keep users online after an interface goes down, the user detection mechanism configured for the users still takes effect. That is, the users are still logged out upon a detection failure.