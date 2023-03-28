use std::io::{BufRead, BufReader};
use std::net::TcpListener;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct InputData {
    time: u64,
    axis_0: f32,
    axis_1: f32,
    axis_2: f32,
    axis_3: f32,
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
    hat_0: String,
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8000").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                let mut reader = BufReader::new(stream);
                let mut line = String::new();
                while reader.read_line(&mut line).unwrap() > 0 {
                    match serde_json::from_str::<InputData>(&line) {
                        Ok(input_data) => {
                            println!("{:?}", input_data);
                        }
                        Err(e) => {
                            eprintln!("Error parsing input data: {:?}", e);
                        }
                    }
                    line.clear();
                }
            }
            Err(e) => {
                eprintln!("Error connecting to client: {:?}", e);
            }
        }
    }
}

