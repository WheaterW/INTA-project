(Optional) Parsing Option 64 to Manage User Bandwidth
=====================================================

The Router can parse the QoS profile name from the Option 64 field delivered by the DHCP server to manage user bandwidth.

#### Context

A Router is configured with different QoS profiles that contain the parameters used to control user bandwidth. The Router selects a QoS profile to allocate bandwidth to users based on the service package that they apply for. QoS profile names are encapsulated into Option 64 fields of ACK packets delivered by a DHCP server. As such, you need to configure an Option 64 parsing mode on the Router to obtain QoS profile names.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The Router allocates bandwidth to users after they have been authenticated. To change user bandwidth when users are already online, run the [**dhcp receive server-packet**](cmdqueryname=dhcp+receive+server-packet) command.

You can configure an Option 64 parsing mode in the system view or the AAA domain view. The mode configured in the AAA domain view takes precedence if you configure an Option 64 parsing mode in both views.



#### Procedure

* Configure the function to parse QoS profile names from Option 64 fields in the system view.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**dhcp option-64 qos-profile**](cmdqueryname=dhcp+option-64+qos-profile) [ **parse-mode** **separator** *separator* **segment** *segment* ] command in the system view to configure an Option 64 parsing mode.
  3. Run the [**dhcp receive server-packet**](cmdqueryname=dhcp+receive+server-packet) **ack** command to enable the Router to receive and process the ACK packets proactively delivered by the DHCP server so that the bandwidth can be changed for online users.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the function to parse QoS profile names from Option 64 fields in the AAA domain view.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**aaa**](cmdqueryname=aaa) command to enter the AAA view.
  3. Run the [**domain**](cmdqueryname=domain) *domain-name* command to enter the AAA domain view.
  4. Run the [**dhcp option-64 qos-profile**](cmdqueryname=dhcp+option-64+qos-profile) [ **parse-mode** **separator** *separator* **segment** *segment* ] command in the domain view to configure an Option 64 parsing mode.
  5. Run the [**dhcp receive server-packet**](cmdqueryname=dhcp+receive+server-packet) **ack** command to enable the Router to receive and process the ACK packets proactively sent by the DHCP server so that the bandwidth can be changed for online users in the domain.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.