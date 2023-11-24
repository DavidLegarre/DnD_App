use crate::character::Character;


pub fn create_character() {
    println!("Creating a new character...");
    // Add logic to create a new character
    let new_character = Character::new(); // Call the new() function from character.rs
    println!("New character created: {:?}", new_character);
}

pub fn view_characters() {
    println!("Viewing existing characters...");
    // Add logic to view existing characters
}