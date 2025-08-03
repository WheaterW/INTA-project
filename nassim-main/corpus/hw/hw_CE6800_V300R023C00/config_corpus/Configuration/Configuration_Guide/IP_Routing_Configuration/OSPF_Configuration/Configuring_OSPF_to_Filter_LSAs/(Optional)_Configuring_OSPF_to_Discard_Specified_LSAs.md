(Optional) Configuring OSPF to Discard Specified LSAs
=====================================================

(Optional) Configuring OSPF to Discard Specified LSAs

#### Context

OSPF can be configured to discard specified LSAs in the following scenarios:

1. When devices on the entire network restart repeatedly due to abnormal LSAs and you have located the LSA that causes protocol restarts, you can configure this function as a last resort to prevent the device from restarting continuously. However, if this function is incorrectly configured, routing loops may occur.
2. If an LSA is identified as an attack packet as it is not supposed to appear in the local area and has caused serious problems, such as device restarts, you can configure this function to filter out the LSA under the condition that the attack source cannot be located temporarily and that the LSA does not affect topology path computation.
3. If an LSA is identified as an attack packet as it is not supposed to appear in the local area and it affects topology path computation and has caused serious problems, such as network-wide device restarts, you can configure this function on each device to discard the LSA to prevent it from participating in network-wide calculation.![](../public_sys-resources/note_3.0-en-us.png) 
   
   To filter out the LSA that affects topology path computation, you must ensure that it is removed from all the LSDBs on the entire network. Otherwise, routing loops may occur.
4. If an LSA is identified as an unreachable residual LSA and the device that advertised the LSA becomes permanently unreachable, you can configure this function to filter out the LSA upon reception under the condition that the LSA does not affect topology path computation.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Configure the device to discard LSAs of a specified type.
   
   
   ```
   [ignore-receive-lsa advertise-router](cmdqueryname=ignore-receive-lsa+advertise-router) adv-rtr-id [ lsa-type type-value [ area { area-id | area-idipv4 } ] | link-state-id ls-id ] *
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If this command is incorrectly configured, services cannot be restored even if the [**undo ignore-receive-lsa advertise-router**](cmdqueryname=undo+ignore-receive-lsa+advertise-router) *adv-rtr-id* [ **lsa-type** *type-value* [ **area** { *area-id* | *area-idipv4* } ] | **link-state-id** *ls-id* ] \* command is run. In this case, you may need to reset the process or neighbor to restore services.
   
   You are not advised to run this command to filter out the LSAs that exist on the network as running this command may filter out normal service LSAs.
   
   As an attack LSA can have any key, it is difficult to defend against the LSA using this command. Therefore, you are advised to directly isolate the attack source.
   
   This command cannot be used to defend against attacks as it goes against protocol processing rules and affects services. Therefore, exercise caution when running this command.
   
   If the fault is caused by a bug, you are advised to run this command temporarily. After the patch is installed, run the [**undo ignore-receive-lsa advertise-router**](cmdqueryname=undo+ignore-receive-lsa+advertise-router) *adv-rtr-id* [ **lsa-type** *type-value* [ **area** { *area-id* | *area-idipv4* } ] | **link-state-id** *ls-id* ] \* command immediately and check whether services are affected. If services are affected, re-establish all neighbor relationships to restore services.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```