Configuring a Flexible Flow Statistics Template
===============================================

Configuring a Flexible Flow Statistics Template

#### Context

Before configuring flexible flow statistics collection, configure a flexible flow statistics template. To obtain more detailed flow statistics, you can configure whether the statistics include the number of packets and bytes and the indexes of the inbound and outbound interfaces.


#### Procedure

* Configure an IPv4 flexible flow statistics template.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an IPv4 flexible flow statistics template and enter its view.
     
     
     ```
     [netstream record](cmdqueryname=netstream+record) record-name ip
     ```
  3. (Optional) Configure a description for an IPv4 flexible flow.
     
     
     ```
     [description](cmdqueryname=description) description-information
     ```
  4. Configure aggregation keywords for the IPv4 flexible flow statistics template.
     
     
     ```
     [match ip](cmdqueryname=match+ip) { destination-address | destination-port | tos | protocol | source-address | source-port | source-mac | destination-mac | ethernet-type | vlan }
     ```
     
     By default, no aggregation keyword is configured for an IPv4 flexible flow statistics template. If you run this command multiple times, multiple keywords are configured to aggregate flows that match all these keywords.
  5. (Optional) Configure the flexible flow statistics to be sent to the NSC to include the number of packets and bytes.
     
     
     ```
     [collect counter](cmdqueryname=collect+counter) { bytes | packets }
     ```
     
     By default, the flexible flow statistics to be sent to the NSC do not include the number of packets or bytes.
  6. (Optional) Configure the flexible flow statistics to be sent to the NSC to include the indexes of the inbound and outbound interfaces, as well as sampling information.
     
     
     ```
     [collect interface](cmdqueryname=collect+interface) { input | output | sampler-info }
     ```
     
     By default, the flexible flow statistics to be sent to the NSC do not include the indexes of the inbound and outbound interfaces or sampling information.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an IPv6 flexible flow statistics template.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an IPv6 flexible flow statistics template and enter its view.
     
     
     ```
     [netstream record](cmdqueryname=netstream+record) record-name ipv6
     ```
  3. (Optional) Configure a description for an IPv6 flexible flow.
     
     
     ```
     [description](cmdqueryname=description) description-information
     ```
  4. Configure aggregation keywords for the IPv6 flexible flow statistics template.
     
     
     ```
     [match ipv6](cmdqueryname=match+ipv6) { destination-address | destination-port | tos | flow-label | protocol | source-address | source-port | source-mac | destination-mac | ethernet-type | vlan }
     ```
     
     By default, no aggregation keyword is configured for an IPv6 flexible flow statistics template. If you run this command multiple times, multiple keywords are configured to aggregate flows that match all these keywords.
  5. (Optional) Configure the flexible flow statistics to be sent to the NSC to include the number of packets and bytes.
     
     
     ```
     [collect counter](cmdqueryname=collect+counter) { bytes | packets }
     ```
     
     By default, the flexible flow statistics to be sent to the NSC do not include the number of packets or bytes.
  6. (Optional) Configure the flexible flow statistics to be sent to the NSC to include the indexes of the inbound and outbound interfaces, as well as sampling information.
     
     
     ```
     [collect interface](cmdqueryname=collect+interface) { input | output | sampler-info }
     ```
     
     By default, the flexible flow statistics to be sent to the NSC do not include the indexes of the inbound and outbound interfaces or sampling information.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a VXLAN flexible flow statistics template.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a VXLAN flexible flow statistics template and enter its view.
     
     
     ```
     [netstream record](cmdqueryname=netstream+record) record-name vxlan inner-ip
     ```
  3. (Optional) Configure a description for a VXLAN flexible flow.
     
     
     ```
     [description](cmdqueryname=description) description-information
     ```
  4. Configure aggregation keywords for the VXLAN flexible flow statistics template.
     
     
     ```
     [match inner-ip](cmdqueryname=match+inner-ip) { destination-address | destination-port | tos | protocol | source-address | source-port | source-mac | destination-mac | cvlan | ethernet-type }
     ```
     
     By default, no aggregation keyword is configured for a VXLAN flexible flow statistics template. If you run this command multiple times, multiple keywords are configured to aggregate flows that match all these keywords.
  5. (Optional) Configure the flexible flow statistics to be sent to the NSC to include the number of packets and bytes.
     
     
     ```
     [collect counter](cmdqueryname=collect+counter) { bytes | packets }
     ```
     
     By default, the flexible flow statistics to be sent to the NSC do not include the number of packets or bytes.
  6. (Optional) Configure the flexible flow statistics to be sent to the NSC to include the indexes of the inbound and outbound interfaces, as well as sampling information.
     
     
     ```
     [collect interface](cmdqueryname=collect+interface) { input | output | sampler-info }
     ```
     
     By default, the flexible flow statistics to be sent to the NSC do not include the indexes of the inbound and outbound interfaces or sampling information.
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```