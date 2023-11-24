mod character;
mod character_manager;

use character_manager::*;
use std::io;

fn main() {
    loop {
        println!("DnD App CLI Menu");
        // Menu
        println!("Welcome to the D&D Character Manager!");
        println!("1. Create a new character");
        println!("2. View existing characters");
        println!("0. Exit");

        println!("Please enter your choice:");

        let mut choice = String::new();
        io::stdin()
            .read_line(&mut choice)
            .expect("Failed to read line");

        // Parse user input
        let choice: u32 = match choice.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid input. Please enter a number");
                continue;
            }
        };

        match choice {
            0 => {
                println!("Exiting the program...");
                break
            },
            1 => create_character(),
            2 => view_characters(),
            _ => {println!("Invalid choice. Please enter a valid option.");}
        }
    }
}
