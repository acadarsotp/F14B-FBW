use serde::Deserialize;
use std::io::Read;
use std::net::TcpStream;

#[allow(dead_code)]
#[derive(Deserialize, Debug)]
pub(crate) struct Input {
    time: u32,
    axis_0: f32,
    axis_1: f32,
    axis_2: f32,
    axis_3: f32,
    axis_4: f32,
    button_0: u8,
    button_1: u8,
    button_2: u8,
    button_3: u8,
    button_4: u8,
    button_5: u8,
    button_6: u8,
    button_7: u8,
    button_8: u8,
    button_9: u8,
    button_10: u8,
    button_11: u8,
    hat_0: (i8, i8),
}

pub(crate) fn handle_client(mut stream: TcpStream) -> std::io::Result<()> {
    // Create a new vector to store incoming data from the client
    let mut data = Vec::new();

    // Loop indefinitely to read data from the stream
    loop {
        // Create a buffer to read incoming data
        let mut buf = [0; 2048];

        // Read data from the stream and check if the read operation succeeded and if any data was read
        match stream.read(&mut buf) {
            Ok(size) if size > 0 => {
                // Extend the data vector with the read data
                data.extend_from_slice(&buf[..size]);

                // Try to deserialize the received data into an Input struct
                if let Ok(input) = serde_json::from_slice::<Input>(&data) {
                    // If deserialization was successful, print the Input struct
                    println!("{:?}", input);

                    // Clear the data vector for the next read operation
                    data.clear();
                }
            }
            // If the read operation succeeded but no data was read, continue reading
            Ok(_) => continue,
            // If the read operation failed, check if the stream was disconnected
            Err(e) if e.kind() == std::io::ErrorKind::ConnectionReset => {
                println!("Client disconnected");
                break;
            }
            // If the read operation failed and the stream was not disconnected, return an error
            Err(_) => return Err(std::io::ErrorKind::InvalidData.into()),
        }
    }

    Ok(())
}

