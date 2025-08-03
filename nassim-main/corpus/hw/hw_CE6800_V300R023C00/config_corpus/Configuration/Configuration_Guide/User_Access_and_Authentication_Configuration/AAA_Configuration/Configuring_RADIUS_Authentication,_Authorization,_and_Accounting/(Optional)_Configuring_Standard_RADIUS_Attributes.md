(Optional) Configuring Standard RADIUS Attributes
=================================================

(Optional) Configuring Standard RADIUS Attributes

#### Context

The content or format of some standard RADIUS attributes can be configured.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the RADIUS server template view.
   
   
   ```
   [radius-server template](cmdqueryname=radius-server+template) template-name
   ```
3. Configure standard RADIUS attributes as required.
   
   
   
   **Table 1** Configuring specific standard RADIUS attributes
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure RADIUS attribute 4 (NAS-IP-Address). | [**radius-attribute nas-ip**](cmdqueryname=radius-attribute+nas-ip) *ip-address* | By default, the source IP address is used as the value of the NAS-IP-Address attribute. |
   | Configure RADIUS attribute 5 (NAS-Port). | [**radius-server nas-port-format**](cmdqueryname=radius-server+nas-port-format) { **new** | **old** } | By default, the new NAS port format is used. |
   | [**radius-server format-attribute**](cmdqueryname=radius-server+format-attribute) **nas-port** *nas-port-sting* | By default, the default new NAS port format is used. |
   | Configure the encapsulation format of the MAC address in the Called-Station-Id (30) attribute. | * **called-station-id mac-format** { **dot-split** | **hyphen-split** } [ **mode1** | **mode2** ] [ **lowercase** | **uppercase** ] * **called-station-id mac-format** **unformatted** [ **lowercase** | **uppercase** ] | By default, the MAC address format in the Called-Station-Id (30) attribute is XX-XX-XX-XX-XX-XX, in uppercase. |
   | Configure RADIUS attribute 31 (Calling-Station-Id). | * **[**calling-station-id mac-format**](cmdqueryname=calling-station-id+mac-format)** { **dot-split** | **hyphen-split** | **colon-split** } [ **mode1** | **mode2** ] [ **lowercase** | **uppercase** ] * **[**calling-station-id mac-format**](cmdqueryname=calling-station-id+mac-format) unformatted** [ **lowercase** | **uppercase** ] * **[**calling-station-id mac-format**](cmdqueryname=calling-station-id+mac-format) bin** | By default, the MAC address format in the Calling-Station-Id attribute is xxxx-xxxx-xxxx, in lowercase. |
   | Configure RADIUS attribute 32 (NAS-Identifier). | [**radius-server nas-identifier-format**](cmdqueryname=radius-server+nas-identifier-format) { **hostname** | **vlan-id** } | By default, the encapsulation format of the NAS-Identifier attribute is the device name of a user. |
   | Configure RADIUS attribute 80 (Message-Authenticator). | [**radius-server attribute message-authenticator access-request**](cmdqueryname=radius-server+attribute+message-authenticator+access-request) | By default, authentication packets do not carry the RADIUS attribute 80 (Message-Authenticator). |
   | Configure RADIUS attribute 87 (NAS-Port-Id). | [**radius-server nas-port-id-format**](cmdqueryname=radius-server+nas-port-id-format) { **new** | **old** | **vendor** *vendor-id* } | By default, the new NAS port ID format is used. |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```