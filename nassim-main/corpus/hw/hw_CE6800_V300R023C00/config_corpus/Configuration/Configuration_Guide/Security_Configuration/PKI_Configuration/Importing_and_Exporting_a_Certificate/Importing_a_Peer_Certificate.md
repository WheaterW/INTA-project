Importing a Peer Certificate
============================

Importing a Peer Certificate

#### Context

Importing a peer certificate applies to large-scale networks.

If the imported peer certificate is no longer needed, release the certificate.


#### Procedure

* Import a peer certificate to the device memory.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [pki import-certificate peer](cmdqueryname=pki+import-certificate+peer) peer-name { der | pem | pkcs12 } filename filename [ cert-name cert-name ] [ no-check-same-name ]
  [commit](cmdqueryname=commit)
  ```
* Release a peer certificate.
  
  
  ```
  [system-view](cmdqueryname=system-view)
  [pki release-certificate peer](cmdqueryname=pki+release-certificate+peer) { name peer-name | all }
  [commit](cmdqueryname=commit)
  ```

#### Verifying the Configuration

Run the [**display pki peer-certificate**](cmdqueryname=display+pki+peer-certificate) { **name** *peer-name* | **all** } command to check the imported peer certificates.