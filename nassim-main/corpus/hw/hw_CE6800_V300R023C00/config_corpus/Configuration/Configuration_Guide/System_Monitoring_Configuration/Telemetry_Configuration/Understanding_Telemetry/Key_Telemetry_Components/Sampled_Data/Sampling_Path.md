Sampling Path
=============

A sampling path defines the data to be sampled. Data on the device has been described in the YANG model. The YANG model and its subtree paths can form sampling paths.

#### Sampling Path Format

* Basic format
  
  Example: huawei-ifm:ifm/interfaces/interface/mib-statistics
  
  **huawei-ifm** before the colon (:) indicates the YANG model name, and **ifm/interfaces/interface/mib-statistics** indicates the node names in the YANG model. The node names at different layers are separated by slashes (/).

* Model mounting format
  
  Example: huawei-twamp-controller:twamp-controller/client/sessions/session/huawei-twamp-statistics:statistics
  
  **huawei-twamp-controller** and **huawei-twamp-statistics** before the colons (:) indicate two YANG model names. The **statistics** node of **huawei-twamp-statistics** is mounted to the **session** node of **huawei-twamp-controller** using the augment parameter.

Based on the preceding two formats, nodes in YANG models can be converted into sampling paths.


#### Filter Criteria

Filter criteria can be configured for a sampling path only by specifying key fields in YANG models.

* Filtering based on a single criterion
  
  Example: huawei-ifm:ifm/interfaces/interface[name="interface\_name"]/mib-statistics
  
  Only data matching the [key-name="key-value"] condition is sampled.

* Filtering based on multiple criteria
  
  If a YANG model contains multiple key fields, you can configure multiple criteria and separate them using commas (,).
  
  Example: huawei-qos:qos/global-query/channel-queue-statisticss/channel-queue-statistics[name="interface\_name",service-class="be"]
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The **service-class** field is defined as an enumerated type in the YANG model. Therefore, an enumerated character string needs to be entered for this field.

* Filtering based on multiple layers of criteria
  
  If a sampling path in a YANG file is long and there are key fields at different layers, you must specify the key field of the parent node before specifying the key fields of child nodes in the filter criteria.
  
  Example: huawei-qos:qos/global-query/interface-traffic-policy-statisticss/interface-traffic-policy-statistics[interface-name="interface\_name",pe-vlan-id=19,vlan-id=10,direction="inbound",slot-id="1"]/classifier-based-staticss/classifier-based-statics[classifier-name="test",traffic-policy-name="traffic"]

* Filtering based on interface name prefixes
  
  If a YANG model defines the interface name as a key field, the interface name prefix can be used for filtering.
  
  For example, huawei-ifm:ifm/interfaces/interface[name="100GE\*"]/mib-statistics defines that the name of a sampling interface starts with 100GE and contains the main interface and sub-interface. The interface name consists of the interface type and interface number, with no space between them. The asterisk (\*) can be used only once and must be placed at the end.

Currently, only the filter criteria that are mentioned above are supported.