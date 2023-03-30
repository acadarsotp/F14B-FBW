use std::net::TcpListener;
mod data_link;


fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("0.0.0.0:3333")?;
    println!("Server listening on port 3333");

    // accept connections and process them, spawning a new thread for each one
    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("New connection: {}", stream.peer_addr()?);
                std::thread::spawn(move || {
                    // connection succeeded
                    data_link::handle_client(stream).unwrap_or_else(|error| {
                        eprintln!("Error: {}", error);
                    });
                });
            }
            Err(e) => {
                // connection failed
                eprintln!("Error: {}", e);
            }
        }
    }
    Ok(())
}




