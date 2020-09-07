# Fibre Channels

- Fibre Channel Protocol is widely used in most SAN (Storage Area Networks).

- SAN is a common storage architecture. It uses a centralized shared storage. This allows for consistent methodologies and tools used.

- SAN is very secure because it is only used for reading and writing files and nothing else.

- Each server in SAN is connected to their logical disk units (LUNs).

- An LUN is a range of blocks from the shared storage and presented to the server as a logical disk.

- The client uses SCSI commands to request the storage device to do a service, like reading or writing data.

- The protocol is lossless, unlike TCP and UDP connections, the data sent using the FCP protocol will never be lost as we never lose any trafic that goes through it.

- A zoning can be installed between one of the servers (client) and the storage in order to prevent the servers from talking to each other and prevent unauthorized hosts to connect to the storage. Zoning can be done either with hardware or software.

- LUN masking is needed in order to prevent different servers from using the same LUN.

- Zoning is configured on the fibre switches and LUN masking is done on the storage system.
