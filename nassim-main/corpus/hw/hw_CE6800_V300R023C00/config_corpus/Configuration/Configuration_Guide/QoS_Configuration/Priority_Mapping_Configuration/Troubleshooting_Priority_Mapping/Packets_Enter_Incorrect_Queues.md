Packets Enter Incorrect Queues
==============================

Packets Enter Incorrect Queues

#### Fault Symptoms

Packets enter incorrect queues.


#### Possible Causes

Possible causes are as follows:

* Priority mappings configured in the DiffServ domain bound to the inbound interface are incorrect.
* There are configurations affecting packet queuing on the inbound interface.
* There are configurations affecting packet queuing in the VLAN to which the packets belong.
* There are configurations affecting packet queuing in the system.


#### Procedure

1. Check whether priority mappings are correct.
   
   
   
   Run the [**display this**](cmdqueryname=display+this) command in the inbound interface view to check the configuration of the [**trust upstream**](cmdqueryname=trust+upstream) command. (If the [**trust upstream**](cmdqueryname=trust+upstream) command is not configured, the DiffServ domain **default** is applied to an interface.) Then run the [**display diffserv domain**](cmdqueryname=display+diffserv+domain) [ *ds-domain-name* | **brief** ] command to check whether the priority mappings configured in the trusted DiffServ domain are correct.
   
   * If the priority mappings are incorrect, run the [**ip-dscp-inbound**](cmdqueryname=ip-dscp-inbound) or [**8021p-inbound**](cmdqueryname=8021p-inbound) command to correctly configure priority mappings.
   * If the priority mappings are correct, go to step 2.
2. Check whether any configurations are affecting packet queuing on the inbound interface.
   
   The following configurations affect the queues that packets enter on the inbound interface:
   * If the packets match a traffic policy that is applied to the inbound direction (using the [**traffic-policy**](cmdqueryname=traffic-policy) command) and contains the action of [**remark local-precedence**](cmdqueryname=remark+local-precedence), the device sends the packets to queues based on the re-marked internal priorities.
   * If the [**trust upstream**](cmdqueryname=trust+upstream) **none** command is configured, the device does not perform priority mapping for incoming packets on the interface. Instead, the device places packets into queues based on interface priorities.
   * If the [**port link-type**](cmdqueryname=port+link-type) **dot1q-tunnel** command is configured but the [**trust**](cmdqueryname=trust) **8021p inner** command is not, all incoming packets enter queues mapped to interface priorities.
   
   Check whether any of the preceding configurations exist on the inbound interface.
   
   * If such configurations are found, delete or modify them.
   * If none of the configurations is found, go to step 3.
3. Check whether any configurations are affecting packet queuing in the VLAN to which the packets belong.
   
   
   
   The following configurations affect packet queuing in a VLAN:
   
   * If the packets match a traffic policy that is applied to the inbound direction (using the [**traffic-policy**](cmdqueryname=traffic-policy) command) and contains the action of [**remark local-precedence**](cmdqueryname=remark+local-precedence), the device sends the packets to queues based on the re-marked internal priorities.
   * If the packets match a traffic policy that is applied to the inbound direction (using the [**traffic-policy**](cmdqueryname=traffic-policy) command) and contains the action of [**remark 8021p**](cmdqueryname=remark+8021p), the device maps the re-marked priorities of packets to internal priorities and sends the packets to queues based on the mapped internal priorities.Check whether any of the preceding configurations exist in the VLAN.
   * If such configurations are found, delete or modify them.
   * If none of the configurations is found, go to step 4.
4. Check whether any configurations are affecting packet queuing in the system.
   
   
   
   The following configurations affect packet queuing in the system:
   
   * If the packets match a global policy that is applied to the inbound direction (using the [**traffic-policy global**](cmdqueryname=traffic-policy+global) command) and contains the action of [**remark local-precedence**](cmdqueryname=remark+local-precedence), the device sends packets to queues based on the re-marked internal priorities.
   * If the packets match a global policy that is applied to the inbound direction (using the [**traffic-policy global**](cmdqueryname=traffic-policy+global) command) and contains the action of [**remark 8021p**](cmdqueryname=remark+8021p), the device maps the re-marked priorities of packets to internal priorities and sends the packets to queues based on the mapped internal priorities.
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check for the preceding configurations in the system. If such configurations are found, delete or modify them.